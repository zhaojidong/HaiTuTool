"""
-EOL-,0,1,1,60,15,1,0,12982ms,-,-,-
-End of line-, Site, Fail, Total, Cate, Bin, XCoord, YCoord, TestTime, DUT NO, -, -
"""
import linecache, os, re
import HnadleDataLog.glovar as glv
import os
import pandas as pd
import HnadleDataLog.StatisticalAnalysis as SA
from HnadleDataLog import CreatFile
test_name_dict = {}
signal_list = []
# log_file_path = r'D:\Python\Project\Ref_Data\out\text'
log_file_path = glv.P_file
# pattern1 = re.compile(r'(TCNT#)\s*[0-9](\s*)(SITE#)(\s*)', re.I)  # the TCNT as the beginning
# pattern2 = re.compile(r'-------------------', re.I)
# pattern3 = re.compile(r'AnalysisData', re.I)
# pattern4 = re.compile(r'(_FAIL_)', re.I)

pat_Title = re.compile(r'(NO Site(\s+)Result(\s+)TestName)', re.I)
pat_TCNT = re.compile(r'(TCNT#(\s*)(\d{0,9})(\s*)SITE#)', re.I)
log_End_Title = re.compile(r'(Site(\s+)Fail(\s+)Total(\s+)Cate(\s+)Bin(\s+)XCoord(\s+)YCoord)', re.I)
pat_AnalysisData = re.compile(r'(AnalysisData_)', re.I)
pat_Over = re.compile(r'-------------------', re.I)
log_End_Info = re.compile(r'^(\s+)(\d{0,9})(\s+)(\d{0,9})(\s+)(\d{0,9})(\s+)(\d{0,9})(\s+)(\d{0,9})(\s+)(\d{0,9})(\s+)(\d{0,9})$')
pat_Pattern = re.compile(r'^(\d{0,9})(\s+)(\d{0,9})(\s+)FC\((\d{0,9})\)')
pat_Item_PASS = re.compile(r'^(\d{0,9})(\s+)(\d{0,9})(\s+)PASS(\s+)')
pat_Item_FAIL = re.compile(r'^(\d{0,9})(\s+)(\d{0,9})(\s+)FAIL(\s+)')
# pat_Excld1 = re.compile(r'data(\s+)(\d{0,9})(\s+)is(\s+)(\d{0,9})')
pat_FAIL = re.compile(r'(\s+)FAIL(\s+)')
pat_PASS = re.compile(r'(\s+)PASS(\s+)')

pat_Excld1 = re.compile(r'^(data)(\s+)')
find_fail_str = '_FAIL_'
output_file_path = '.\Out'
title_append = ['CheckStatus', 'PASS_Count', 'Fail_Count', 'unit']
gs = glv.global_str()
gss = glv.global_status_str()
gp = glv.global_pattern()

def ParseLogFile_b():
    log_file_list = glv.selected_file_list
    merge_file = CreatFile.MergeFile(log_file_list)
    final_pd = pd.DataFrame()
    glv.File_NO, glv.File_Info = glv.extractDataFromFileName(log_file_list)
    pd.set_option('display.width', None)
    # Follow Code: get all files name and file count
    file_name_list = os.listdir(glv.P_file)
    file_total = len(file_name_list)
    TNCT = []
    EOL_Num_Is_Chips = 0
    execute_once = True
    # read the line count of the file
    line_count = 0
    thefile = open(merge_file)
    Chip_Name_list = []
    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        line_count += buffer.count('\n')
    thefile.close()
    # Follow Code: read line information
    pd_dict = {}
    title_len = 0
    title_list = []
    got_title = False
    execute_at_num = 0
    line_cnt = 0
    line_cnt2 = 0
    line_max = 0
    re_max = False
    with open(merge_file, 'r+') as mf_fp:
        ReadData = mf_fp.readlines()
        line_num = -1
        execute_num = 0
        for line_data in ReadData:
            line_num += 1
            # text = linecache.getline(merge_file, line_data)
            if re.search(pat_TCNT, line_data):
                info_list = glv.extractNum2list(line_data)
                TNCT.append(info_list[0])
                SITE = info_list[1]
            # Follow Code: Find the title's line
            if re.search(pat_Title, line_data) and not got_title:
                title_list = line_data.split()
                title_list.extend(title_append)
                glv.title_pd_dict = title_list
                title_len = len(title_list)
                got_title = True
                continue
            if gp.file_name in line_data:
                line_data = line_data.strip(gp.file_name)
                file_name, ChipID = glv.extractFileName(line_data)
                if '#' in str(ChipID):
                    Chip_Name = str(ChipID)
                else:
                    Chip_Name = '#' + str(ChipID)
                Chip_Name_list.append(Chip_Name)
            if got_title:
                # split according to signal space
                line = re.split(r"[ ]+", line_data)
                # delete '\n':strip() used for \n and space defaulted
                line = [x.strip() for x in line]
                # merger the unit with before data
                for index, value in enumerate(line):
                    if value == 'nV' or value == 'uV' or value == 'mV' or value == 'V' \
                            or value == 'pA' or value == 'nA' or value == 'uA' or value == 'mA' or value == 'A' \
                            or value == 'M' or value == 'K' or value == 'MHz':
                        line[index - 1] = line[index - 1] + line[index]
                        del line[index]
                # list max length, append 'None' to
                for add_none_count in range(title_len - len(line)):
                    line.append('None')
                # line_end[2] = file_name_info[1]  # DUT PASS or FAIL
                # if re.search(pat_Over, line_data) is None and re.search(pat_Excld1, line_data) is None:
                if re.search(pat_Item_PASS, line_data) or re.search(pat_Item_FAIL, line_data):
                    line_cnt += 1
                    line_cnt2 += 1
                    if execute_once:
                        execute_once = False
                        NewList = [[x] for x in line]
                        pd_dict = dict(zip(title_list, NewList))
                    else:
                        line_count = 0
                        for key in title_list:
                            if str(line[0]).isdigit():  # NO. is digit, and Result is alpha
                                pd_dict[key] = pd_dict.get(key, []) + [line[line_count]]
                                line_count += 1
                            elif re.search(pat_AnalysisData, line_data):
                                AnalysisData_item = line_data.split()[:]  # value copy to list, not list copy to list
                                AnalysisData_item[0] = 999
                                AnalysisData_item[1] = 0
                                AnalysisData_item[2] = line_data.split()[-1] == '1' and 'PASS' or 'FAIL'
                                AnalysisData_item[3] = str(line_data.split()[0])
                                AnalysisData_item.extend(['-']*(title_len-len(AnalysisData_item)))
                                pd_dict[key] = pd_dict.get(key, []) + [AnalysisData_item[line_count]]
                                line_count += 1
                                line_cnt += 1
                # -----------------------------------------------------------------------------------#
                # End line information:
                # -End of line -, Site, Fail, Total, Cate, Bin, XCoord, YCoord, TestTime, DUT NO, -, -
                if re.search(log_End_Title, line_data):  # find the end line, and fill some information(test time)
                    TestTime = re.findall(r"[(](.*?)[)]", line_data)  # get the string in the parentheses, it is test time
                    line_cnt2 += 1
                if re.search(log_End_Info, line_data):
                    line_cnt2 += 1
                    end_line_list = []
                    start_line_list = line_data.split()
                    end_line_list.insert(0, glv.end_label)  # '-EOL-'
                    start_line_list.insert(0, glv.start_label)  # '-SOL-'
                    # end_line_list.append(TestTime[0])
                    start_line_list.append(TestTime[0])
                    # end_line_list.append(Chip_Name)  # add the DUT NO. to EOL
                    start_line_list.append(Chip_Name)
                    # end_line_list.append(file_name)  # add the file name to EOL
                    start_line_list.append(file_name)
                    # -----Add info before this line-----
                    end_line_list.extend(['---'] * (title_len - len(end_line_list)))
                    start_line_list.extend(['-'] * (title_len - len(start_line_list)))
                    for each in zip(end_line_list, pd_dict):
                        ele, key = each
                        pd_dict[key].append(ele)
                    if execute_num == 0:
                        for each in zip(start_line_list, pd_dict):
                            ele, key = each
                            pd_dict[key].insert(0, ele)
                        cnt = len(pd_dict[key])
                    else:
                        for each in zip(start_line_list, pd_dict):
                            ele, key = each
                            pd_dict[key].insert(cnt, ele)
                        cnt = len(pd_dict[key])
                    if line_cnt > line_max:
                        line_max = line_cnt
                        tree_pd = pd.DataFrame(pd_dict).iloc[line_cnt2 - line_max - 2:line_cnt2]
                        glv.log_row = tree_pd.shape[0]
                    line_cnt = 0
                    execute_num += 1
                    line_count += 1
                    EOL_Num_Is_Chips += 1
                    logs_pd = pd.DataFrame(pd_dict)
                    final_pd = logs_pd
                    execute_at_num += 1
    final_pd.to_csv(glv.final_path)
    glv.final_df = final_pd
    Chip_List = list(dict.fromkeys(Chip_Name_list))
    glv.Chip_List = Chip_List
    glv.file_count = len(Chip_List)
    glv.test_count = EOL_Num_Is_Chips
    glv.log_col = title_len
    glv.tree_df = tree_pd
    # tree_pd = fill_Info4tree()
    return tree_pd, final_pd  # , file_name_list, file_total

def ParseLogFile():
    log_file_list = glv.selected_file_list
    merge_file = CreatFile.MergeFile(log_file_list)
    final_pd = pd.DataFrame()
    glv.File_NO, glv.File_Info = glv.extractDataFromFileName(log_file_list)
    pd.set_option('display.width', None)
    # Follow Code: get all files name and file count
    file_name_list = os.listdir(glv.P_file)
    file_total = len(file_name_list)
    TNCT = []
    EOL_Num_Is_Chips = 0
    execute_once = True
    # read the line count of the file
    line_count = 0
    thefile = open(merge_file)
    Chip_Name_list = []
    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        line_count += buffer.count('\n')
    thefile.close()
    # Follow Code: read line information
    pd_dict = {}
    title_len = 0
    title_list = []
    got_title = False
    execute_at_num = 0
    line_cnt = 0
    line_cnt2 = 0
    line_max = 0
    fail_cnt = 0
    pass_cnt = 0
    t_dict = {}
    t_dict_first = True
    with open(merge_file, 'r+') as mf_fp:
        ReadData = mf_fp.readlines()
        line_num = -1
        execute_num = 0
        for line_data in ReadData:
            line_num += 1
            # text = linecache.getline(merge_file, line_data)
            if re.search(pat_TCNT, line_data):
                info_list = glv.extractNum2list(line_data)
                TNCT.append(info_list[0])
                SITE = info_list[1]
            # Follow Code: Find the title's line
            if re.search(pat_Title, line_data) and not got_title:
                title_list = line_data.split()
                title_list.extend(title_append)
                glv.title_pd_dict = title_list
                title_len = len(title_list)
                got_title = True
                continue
            if gp.file_name in line_data:
                line_data = line_data.strip(gp.file_name)
                file_name, ChipID = glv.extractFileName(line_data)
                if '#' in str(ChipID):
                    Chip_Name = str(ChipID)
                else:
                    Chip_Name = '#' + str(ChipID)
                if glv.Log_Debug:
                    Chip_Name_list.append(Chip_Name)
            if got_title:
                # split according to signal space
                line = re.split(r"[ ]+", line_data)
                # delete '\n':strip() used for \n and space defaulted
                line = [x.strip() for x in line]
                # merger the unit with before data
                for index, value in enumerate(line):
                    if value == 'nV' or value == 'uV' or value == 'mV' or value == 'V' \
                            or value == 'pA' or value == 'nA' or value == 'uA' or value == 'mA' or value == 'A' \
                            or value == 'M' or value == 'K' or value == 'MHz':
                        line[index - 1] = line[index - 1] + line[index]
                        del line[index]
                # list max length, append 'None' to
                for add_none_count in range(title_len - len(line)):
                    line.append('None')
                # line_end[2] = file_name_info[1]  # DUT PASS or FAIL
                # if re.search(pat_Over, line_data) is None and re.search(pat_Excld1, line_data) is None:
                if re.search(pat_Item_PASS, line_data) or re.search(pat_Item_FAIL, line_data):
                    # print(line_data.split('.'))
                    finder = False
                    t_value = []
                    line_cnt += 1
                    line_cnt2 += 1
                    tree_list = line_data.split()[2:5]
                    # if 'IDD_LvdsOff' in line_data:
                    #     loop_cnt = 0
                    #     append_name = str(line_data.split()[4].split('.'))
                    #     t_key = tree_list[1] + '@' + tree_list[2]
                    # if 0 < loop_cnt < 9:
                    #     t_key = tree_list[1] + '_' + append_name + '@' + tree_list[2]
                    t_key = tree_list[1] + '@' + tree_list[2]
                    if t_dict_first:
                        t_value.append(tree_list[0])
                        t_dict.update({t_key: t_value})
                    else:
                        for key, value in t_dict.items():
                            if key == t_key:
                                value.append(tree_list[0])
                                finder = True
                                break
                        if not finder:
                            t_value.append(tree_list[0])
                            t_dict.update({t_key: t_value})
                    t_dict_first = False
                    if execute_once:
                        execute_once = False
                        NewList = [[x] for x in line]
                        pd_dict = dict(zip(title_list, NewList))
                    else:
                        line_count = 0
                        for key in title_list:
                            if str(line[0]).isdigit():  # NO. is digit, and Result is alpha
                                pd_dict[key] = pd_dict.get(key, []) + [line[line_count]]
                                line_count += 1
                            elif re.search(pat_AnalysisData, line_data):
                                AnalysisData_item = line_data.split()[:]  # value copy to list, not list copy to list
                                AnalysisData_item[0] = 999
                                AnalysisData_item[1] = 0
                                AnalysisData_item[2] = line_data.split()[-1] == '1' and 'PASS' or 'FAIL'
                                AnalysisData_item[3] = str(line_data.split()[0])
                                AnalysisData_item.extend(['-']*(title_len-len(AnalysisData_item)))
                                pd_dict[key] = pd_dict.get(key, []) + [AnalysisData_item[line_count]]
                                line_count += 1
                                line_cnt += 1
                # -----------------------------------------------------------------------------------#
                # End line information:
                # -End of line -, Site, Fail, Total, Cate, Bin, XCoord, YCoord, TestTime, DUT NO, -, -
                if re.search(log_End_Title, line_data):  # find the end line, and fill some information(test time)
                    TestTime = re.findall(r"[(](.*?)[)]", line_data)  # get the string in the parentheses, it is test time
                    line_cnt2 += 1
                if re.search(log_End_Info, line_data):
                    line_cnt2 += 1
                    end_line_list = []
                    start_line_list = line_data.split()
                    die_location_wafer = start_line_list[5] + '_' + start_line_list[6]
                    end_line_list.insert(0, glv.end_label)  # '-EOL-'
                    start_line_list.insert(0, glv.start_label)  # '-SOL-'
                    # end_line_list.append(TestTime[0])
                    start_line_list.append(TestTime[0])
                    # end_line_list.append(Chip_Name)  # add the DUT NO. to EOL
                    if glv.Log_Wafer:
                        start_line_list.append(die_location_wafer)
                        Chip_Name_list.append(die_location_wafer)
                    if glv.Log_Debug:
                        start_line_list.append(Chip_Name)
                    # end_line_list.append(file_name)  # add the file name to EOL
                    start_line_list.append(file_name)
                    # -----Add info before this line-----
                    end_line_list.extend(['---'] * (title_len - len(end_line_list)))
                    start_line_list.extend(['-'] * (title_len - len(start_line_list)))
                    for each in zip(end_line_list, pd_dict):
                        ele, key = each
                        pd_dict[key].append(ele)
                    if execute_num == 0:
                        for each in zip(start_line_list, pd_dict):
                            ele, key = each
                            pd_dict[key].insert(0, ele)
                        cnt = len(pd_dict[key])
                    else:
                        for each in zip(start_line_list, pd_dict):
                            ele, key = each
                            pd_dict[key].insert(cnt, ele)
                        cnt = len(pd_dict[key])
                    if line_cnt > line_max:
                        line_max = line_cnt
                        tree_pd = pd.DataFrame(pd_dict).iloc[line_cnt2 - line_max - 2:line_cnt2]
                        glv.log_row = tree_pd.shape[0]
                    line_cnt = 0
                    execute_num += 1
                    line_count += 1
                    EOL_Num_Is_Chips += 1
                    logs_pd = pd.DataFrame(pd_dict)
                    final_pd = logs_pd
                    execute_at_num += 1
    t_list = []
    tree_title = [gs.TestName, gs.Signal, gs.PASS_Count, gs.Fail_Count]
    for key, value in t_dict.items():
        t_list_son = []
        p_cnt = 0
        f_cnt = 0
        t_list_son = str(key).split('@')
        for i in value:
            if i == 'PASS':
                p_cnt += 1
            if i == 'FAIL':
                f_cnt += 1
        t_list_son.append(p_cnt)
        t_list_son.append(f_cnt)
        t_list.append(t_list_son)
    new_tree = pd.DataFrame(t_list)
    new_tree.columns = tree_title
    final_pd.to_csv(glv.final_path)
    glv.final_df = final_pd
    Chip_List = list(dict.fromkeys(Chip_Name_list))
    glv.Chip_List = Chip_List
    glv.file_count = len(Chip_List)
    glv.test_count = EOL_Num_Is_Chips
    glv.log_col = title_len
    glv.tree_df = tree_pd
    # tree_pd = fill_Info4tree()
    return new_tree, final_pd  # , file_name_list, file_total

def fill_Info4tree():
    tree_fd = glv.tree_df.copy()  # deep copy
    final_df = glv.final_df.copy()  # slice
    shift_count = glv.log_row
    fail_cnt = 0
    pass_cnt = 0
    for index, row in final_df.iterrows():
        for index_t, row_t in tree_fd.iterrows():
            if final_df.at[index, str(gs.TestName)] == tree_fd.at[index_t, str(gs.TestName)]:
                if final_df.at[index, str(gs.Signal)] == tree_fd.at[index_t, str(gs.Signal)]:
                    if final_df.at[index, str(gs.Result)] == str(gss.FAIL):
                        fail_cnt += 1
                        tree_fd.at[index, str(gs.Fail_Count)] = fail_cnt
                    elif final_df.at[index, str(gs.Result)] == str(gss.PASS):
                        pass_cnt += 1
                        tree_fd.at[index, str(gs.PASS_Count)] = pass_cnt
        # DUT_F = [1] * glv.test_count
        # for dut in range(glv.test_count):
        #     if final_df.at[index + dut * shift_count, str(gs.Result)] == str(gss.FAIL):
        #         DUT_F[dut] = 0
        # tree_fd.at[index, str(gs.PASS_Count)] = sum(DUT_F)
        # tree_fd.at[index, str(gs.Fail_Count)] = len(DUT_F)-sum(DUT_F)
    return tree_fd


# find the itme was checked on the tree widget, and mark label on DataFrame
def handle_FinalPd4tree():
    target_df = glv.final_df.copy()  # deep copy
    # target_tree = {'OS_NEG': ['CH_VCOMS_B1', 'CH_VCOMS_T1', 'CH_VREFN_B1', 'CH_VREFN_T1', 'CH_VREFP_B1', 'CH_VREFP_T1', 'CH_VRPGA_B1', 'CH_VRPGA_T1', 'CH_VDDCL1', 'CH_RSH1', 'CH_GRSTH1', 'CH_TX2H1', 'CH_TX1H1', 'SA', 'SYSSTBN', 'SYSRSTN', 'VCP2', 'VIREF', 'SDO', 'CSN', 'SCK', 'SDI', 'HSYNC', 'VSYNC', 'DTSTR0', 'DTSTR1', 'DTSTR3', 'DTSTR4', 'TOUT0', 'TOUT1', 'TOUT2', 'ATST0', 'ATST1', 'ATST2', 'RCK2', 'TRGEXP', 'MSTSLV', 'TSG2_config.TSG2_config', 'TSG2.TSG2', 'compare', 'TSG2.TSG2', 'compare'], 'TSG2_TEST': ['CH_VCOMS_B1', 'CH_VCOMS_T1', 'CH_VREFN_B1', 'CH_VREFN_T1', 'CH_VREFP_B1', 'CH_VREFP_T1', 'CH_VRPGA_B1', 'CH_VRPGA_T1', 'CH_VDDCL1', 'CH_RSH1', 'CH_GRSTH1', 'CH_TX2H1', 'CH_TX1H1', 'SA', 'SYSSTBN', 'SYSRSTN', 'VCP2', 'VIREF', 'SDO', 'CSN', 'SCK', 'SDI', 'HSYNC', 'VSYNC', 'DTSTR0', 'DTSTR1', 'DTSTR3', 'DTSTR4', 'TOUT0', 'TOUT1', 'TOUT2', 'ATST0', 'ATST1', 'ATST2', 'RCK2', 'TRGEXP', 'MSTSLV', 'TSG2_config.TSG2_config', 'TSG2.TSG2', 'compare', 'TSG2.TSG2', 'compare']}
    target_tree = glv.tree_checked
    finish_once = False
    for index, row in target_df.iterrows():
        for key, values in target_tree.items():
            if isinstance(values, list):
                for value in values:
                    if key == target_df.at[index, str(gs.TestName)] and value == target_df.at[index, str(gs.Signal)]:
                        target_df.at[index, str(gs.CheckStatus)] = str(gss.Checked)
    glv.marked_df = target_df
    sa1 = SA.SA(target_df)


# unify the unit and value of measure and limit
def unify_value7unit():
    unified_df = glv.final_df.copy()
    for index, row in unified_df.iterrows():
        if re.search(glv.pat_unit, unified_df.at[index, str(gs.Result)]):
            pass

def find_special_str():
    pass


# if __name__ == '__main__':
#     ParseLogFile()
#     handle_FinalPd4tree()
#     CreatFile.CreatExcel_VP_log()
#     pass

