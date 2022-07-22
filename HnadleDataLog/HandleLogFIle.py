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
log_file_path = r'C:\007\PythonProject\DataAnalysis'
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

find_fail_str = '_FAIL_'
output_file_path = '.\Out'
title_append = ['CheckStatus', 'PASS_Count', 'Fail_Count', 'unit']
gs = glv.global_str()
gss = glv.global_status_str()
gp = glv.global_pattern()


# traverse all log files, generate pandas
def ParseLogFile_b():
    log_file_list = glv.selected_file_list
    merge_file = CreatFile.MergeFile(log_file_list)
    FileInfo = glv.extractFileName(log_file_list)
    files_num = len(glv.selected_file_list)
    glv.File_NO = glv.extractDataFromFileName(log_file_list)
    pd.set_option('display.width', None)
    # Follow Code: get all files name and file count
    file_name_list = os.listdir(log_file_path)
    file_total = len(file_name_list)
    TNCT = []
    dut_num = 0
    execute_once = True
    for f_num in range(files_num):
        fp = open(log_file_list[f_num], 'rb')
        # Follow Code: get line total sum
        count = -1
        for count, line in enumerate(open(log_file_list[f_num], 'r')):
            pass
        count += 1
        # Follow Code: read line information
        execute_once_2 = True
        pd_dict = {}
        title_len = 0
        title_list = []
        got_title = False
        execute_file = True
        finish_one_flag = False
        for line_data in range(count):
            text = linecache.getline(log_file_list[f_num], line_data)
            # Follow Code: Find the title's line
            if re.search(pat_Title, text) and execute_file:
                info_list = glv.extractNum2list(linecache.getline(log_file_list[f_num], line_data-1))
                TNCT.append(info_list[0])
                SITE = info_list[1]
                title_list = linecache.getline(log_file_list[f_num], line_data).split()
                title_list.extend(title_append)
                glv.title_pd_dict = title_list
                title_len = len(title_list)
                got_title = True
                continue
            if got_title:
                # split according to signal space
                line = re.split(r"[ ]+", text)
                # delete '\n':strip() used for \n and space defaulted
                line = [x.strip() for x in line]
                # merger the unit with before data
                for index, value in enumerate(line):
                    if value == 'nV' or value == 'uV' or value == 'mV' or value == 'V' \
                            or value == 'pA' or value == 'nA' or value == 'uA' or value == 'mA' or value == 'A' \
                            or value == 'M' or value == 'K':
                        line[index - 1] = line[index - 1] + line[index]
                        del line[index]
                # list max length, append 'None' to
                for add_none_count in range(title_len - len(line)):
                    line.append('None')
                # line_end[2] = file_name_info[1]  # DUT PASS or FAIL
                if re.search(pat_Over, text) is None:
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
                            elif re.search(pat_AnalysisData, text):
                                AnalysisData_item = text.split()[:]  # value copy to list, not list copy to list
                                AnalysisData_item[0] = 999
                                AnalysisData_item[1] = 0
                                AnalysisData_item[2] = text.split()[-1] == '1' and 'PASS' or 'FAIL'
                                AnalysisData_item[3] = str(text.split()[0])
                                AnalysisData_item.extend(['-']*(title_len-len(AnalysisData_item)))
                                pd_dict[key] = pd_dict.get(key, []) + [AnalysisData_item[line_count]]
                                line_count += 1
                # -----------------------------------------------------------------------------------#
                # End line information:
                # -End of line -, Site, Fail, Total, Cate, Bin, XCoord, YCoord, TestTime, DUT NO, -, -
                if re.search(log_End_Title, text):  # find the end line, and fill some information(test time)
                    TestTime = re.findall(r"[(](.*?)[)]", linecache.getline(log_file_list[f_num], line_data))  # get the string in the parentheses, it is test time
                    end_line_list = linecache.getline(log_file_list[f_num], line_data + 2).split()
                    end_line_list.insert(0, glv.end_label)  # '-EOL-'
                    end_line_list.append(TestTime[0])
                    end_line_list.append(glv.File_NO[f_num])  # add the DUT NO. to EOL
                    end_line_list.append(FileInfo[f_num])  # add the file name to EOL
                    # -----Add info before this line-----
                    end_line_list.extend(['-'] * (title_len - len(end_line_list)))
                    for each in zip(end_line_list, pd_dict):
                        ele, key = each
                        pd_dict[key].append(ele)
                    line_count += 1
                    dut_num += 1
                    finish_one_flag = True
            if finish_one_flag:
                logs_pd = pd.DataFrame(pd_dict)
                finish_one_flag = False
                if execute_once_2:
                    tree_pd = logs_pd
                    glv.log_row = tree_pd.shape[0]
                    execute_once_2 = False
        if f_num == 0:
            final_pd = logs_pd
        else:
            final_pd = final_pd.append(logs_pd, ignore_index=True)
        fp.close()
    final_pd.to_csv(glv.final_path)
    glv.final_df = final_pd
    glv.file_count = dut_num
    glv.log_col = title_len
    tree_pd = fill_Info4tree()
    glv.tree_df = tree_pd
    return tree_pd, final_pd, file_name_list, file_total

def ParseLogFile():
    log_file_list = glv.selected_file_list
    merge_file = CreatFile.MergeFile(log_file_list)
    final_pd = pd.DataFrame()
    glv.File_NO = glv.extractDataFromFileName(log_file_list)
    pd.set_option('display.width', None)
    # Follow Code: get all files name and file count
    file_name_list = os.listdir(log_file_path)
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
                if re.search(pat_Over, line_data) is None:
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
                # print(pd_dict)
                # -----------------------------------------------------------------------------------#
                # End line information:
                # -End of line -, Site, Fail, Total, Cate, Bin, XCoord, YCoord, TestTime, DUT NO, -, -
                if re.search(log_End_Title, line_data):  # find the end line, and fill some information(test time)
                    TestTime = re.findall(r"[(](.*?)[)]", line_data)  # get the string in the parentheses, it is test time
                if re.search(log_End_Info, line_data):
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
                    execute_num += 1
                    line_count += 1
                    EOL_Num_Is_Chips += 1
                    logs_pd = pd.DataFrame(pd_dict)
                    final_pd = logs_pd
                    execute_at_num += 1
            if execute_at_num == 1:
                tree_pd = logs_pd
                glv.log_row = tree_pd.shape[0]
    # if execute_at_num == 2:
    #     final_pd = final_pd.append(logs_pd, ignore_index=True)
    final_pd.to_csv(glv.final_path)
    glv.final_df = final_pd
    Chip_List = list(dict.fromkeys(Chip_Name_list))
    glv.Chip_List = Chip_List
    glv.file_count = len(Chip_List)
    glv.test_count = EOL_Num_Is_Chips
    glv.log_col = title_len
    tree_pd = fill_Info4tree()
    glv.tree_df = tree_pd
    return tree_pd, final_pd  # , file_name_list, file_total



def fill_Info4tree():
    final_df = glv.final_df.copy()  # deep copy
    tree_fd = final_df.iloc[0:glv.log_row]  # slice
    shift_count = glv.log_row
    for index, row in tree_fd.iterrows():
        DUT_F = [1] * glv.test_count
        for dut in range(glv.test_count):
            if final_df.at[index + dut * shift_count, str(gs.Result)] == str(gss.FAIL):
                DUT_F[dut] = 0
        tree_fd.at[index, str(gs.PASS_Count)] = sum(DUT_F)
        tree_fd.at[index, str(gs.Fail_Count)] = len(DUT_F)-sum(DUT_F)
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



# if __name__ == '__main__':
#     ParseLogFile()
#     handle_FinalPd4tree()
#     CreatFile.CreatExcel_VP_log()
#     pass

