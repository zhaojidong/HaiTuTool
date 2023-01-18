import os, openpyxl as op ,shutil
import threading, time
from datetime import datetime
import ScriptFailarmy.gloVal as glv_DS

path_come = r'D:\Tool_RAW\de'
path_from = r'D:\Tool_RAW\Here'

sof = '11111111111111000000000000000000000000000010101011000000'
sol = '11111111111111000000000000000000000000000010000000000000'
eol = '11111111111111000000000000000000000000000010011101000000'
eof = '11111111111111000000000000000000000000000010110110000000'


def Data2Shmoo_b(selected_file_list):
    ev = r'D:\Tool_RAW\ev.xlsx'
    training_code = '00011100001111'  # 070f
    dataBitW = 310 * 14
    invalid_data = 258 * 14
    Sync_width = 56
    rest_data_f2l = ''
    sum_index = 0
    index = 0
    lineBitW = len(sol) + dataBitW + len(eol)
    wb = op.Workbook()
    ws_all = wb.create_sheet('All_Error')
    ws_sol = wb.create_sheet('SOL_Error')
    ws_eol = wb.create_sheet('EOL_Error')
    ws_sof = wb.create_sheet('SOF_Error')
    for i in range(int(len(selected_file_list)/8)):
        Not_SOF = 0
        code_fail_cnt = 0
        sol_fail_cnt = 0
        eol_fail_cnt = 0
        for f8 in range(8):
            pi_string = ''
            if f8 == 0:
                file_name = os.path.basename(selected_file_list[f8 + i * 8])
                edge_num = int(os.path.splitext(file_name)[0][:-1].split('_')[1])
                vdd18l_num = int(os.path.splitext(file_name)[0][:-1].split('_')[3])
                edge_index = edge_num + 1 + 1
                vdd18l_index = vdd18l_num + 1 + 1
                edge_val = 5 + edge_num*0.2
                vdd18l_val = 1.7 + vdd18l_num * 0.03
                ws_all.cell(row=edge_index, column=1, value=edge_val)  # edge
                ws_all.cell(row=1, column=vdd18l_index, value=vdd18l_val)  # vdd18l
                ws_sol.cell(row=edge_index, column=1, value=edge_val)  # edge
                ws_sol.cell(row=1, column=vdd18l_index, value=vdd18l_val)  # vdd18l
                ws_eol.cell(row=edge_index, column=1, value=edge_val)  # edge
                ws_eol.cell(row=1, column=vdd18l_index, value=vdd18l_val)  # vdd18l
                ws_sof.cell(row=edge_index, column=1, value=edge_val)  # edge
                ws_sof.cell(row=1, column=vdd18l_index, value=vdd18l_val)  # vdd18l
            with open(selected_file_list[f8 + i * 8], 'r+') as r_fp:
                lines = r_fp.readlines()
            for line in lines:
                pi_string += line.rstrip()
            for V in range(2072):  # 0-2081  sum = 2082
                if V == 0:
                    if sof in pi_string:
                        index = pi_string.find(sof)
                        del_sof = pi_string[index + len(sof):]
                        for data_num in range(310):
                            data = del_sof[data_num * 14:14 * (data_num + 1)]
                            if data != training_code:
                                code_fail_cnt += 1
                        if del_sof[dataBitW:dataBitW + len(eol)] != eol:
                            eol_fail_cnt += 1
                        rest_data_f2l = del_sof[dataBitW + len(eol) + invalid_data:]
                        sum_index = index + len(sof) + dataBitW + len(eol)
                    else:
                        sol_fail_cnt += 2071
                        code_fail_cnt += 310*2072
                        eol_fail_cnt += 2071
                        Not_SOF += 1
                        break
                if 0 < V < 2072:
                    if sol == rest_data_f2l[0:Sync_width]:
                        index = rest_data_f2l.find(sol)
                        del_sol = rest_data_f2l[index + len(sol):]
                        for data_num in range(310):
                            data = del_sol[data_num * 14:14 * (data_num + 1)]
                            if data != training_code:
                                code_fail_cnt += 1
                        if del_sol[dataBitW:dataBitW + len(eol)] != eol:
                            eol_fail_cnt += 1
                        rest_data_f2l = del_sol[dataBitW + len(eol) + invalid_data:]
                        sum_index = sum_index + lineBitW + index
                    else:
                        index += 1
                        sol_fail_cnt += 1
                        del_sol = rest_data_f2l[index + len(sol):]
                        for data_num in range(310):
                            data = del_sol[data_num * 14:14 * (data_num + 1)]
                            if data != training_code:
                                code_fail_cnt += 1
                        if del_sol[dataBitW:dataBitW + len(eol)] != eol:
                            eol_fail_cnt += 1
                        rest_data_f2l = del_sol[dataBitW + len(eol) + invalid_data:]
                        sum_index = sum_index + lineBitW + index
        ws_all.cell(row=edge_index, column=vdd18l_index, value=sol_fail_cnt + code_fail_cnt + eol_fail_cnt)  # write data
        ws_sol.cell(row=edge_index, column=vdd18l_index, value=sol_fail_cnt)  # write data
        ws_eol.cell(row=edge_index, column=vdd18l_index, value=eol_fail_cnt)  # write data
        ws_sof.cell(row=edge_index, column=vdd18l_index, value=Not_SOF)  # write data
        print('Finished ' + str(i))
    wb.save(ev)
    print('All Finished')

def Data2Shmoo(selected_file_list):
    ev = r'D:\Tool_RAW\ev.xlsx'
    training_code = '00011100001111'  # 070f
    dataBitW = 310 * 14
    Sync_width = 56
    rest_data_f2l = ''
    H_width = 576*14
    sum_index = 0
    if selected_file_list:
        file_path = os.path.dirname(selected_file_list[0])
        time_label = datetime.now().strftime("%Y%m%d%H%M%S")
        SaveExcel = file_path + '\\' + 'Shmoo_' + str(time_label) + '.xlsx'
    else:
        return
    wb = op.Workbook()
    ws_all = wb.create_sheet('All_Error')
    ws_sol = wb.create_sheet('SOL_Error')
    ws_eol = wb.create_sheet('EOL_Error')
    ws_sof = wb.create_sheet('SOF_Error')
    for i in range(int(len(selected_file_list)/8)):
        Not_SOF = 0
        code_fail_cnt = 0
        sol_fail_cnt = 0
        eol_fail_cnt = 0
        for f8 in range(8):
            pi_string = ''
            if f8 == 0:
                file_name = os.path.basename(selected_file_list[f8 + i * 8])
                edge_num = int(os.path.splitext(file_name)[0][:-1].split('_')[1])
                vdd18l_num = int(os.path.splitext(file_name)[0][:-1].split('_')[3])
                edge_index = edge_num + 1 + 1
                vdd18l_index = vdd18l_num + 1 + 1
                edge_val = 5 + edge_num*0.2
                vdd18l_val = 1.7 + vdd18l_num * 0.03
                ws_all.cell(row=edge_index, column=1, value=edge_val)  # edge
                ws_all.cell(row=1, column=vdd18l_index, value=vdd18l_val)  # vdd18l
                ws_sol.cell(row=edge_index, column=1, value=edge_val)  # edge
                ws_sol.cell(row=1, column=vdd18l_index, value=vdd18l_val)  # vdd18l
                ws_eol.cell(row=edge_index, column=1, value=edge_val)  # edge
                ws_eol.cell(row=1, column=vdd18l_index, value=vdd18l_val)  # vdd18l
                ws_sof.cell(row=edge_index, column=1, value=edge_val)  # edge
                ws_sof.cell(row=1, column=vdd18l_index, value=vdd18l_val)  # vdd18l
            with open(selected_file_list[f8 + i * 8], 'r+') as r_fp:
                lines = r_fp.readlines()
            for line in lines:
                pi_string += line.rstrip()
            for V in range(2072):  # 0-2081  sum = 2082
                if V == 0:
                    if sof in pi_string:
                        index = pi_string.find(sof)
                        del_sof = pi_string[index + len(sof):]
                        for data_num in range(310):
                            data = del_sof[data_num * 14:14 * (data_num + 1)]
                            if data != training_code:
                                code_fail_cnt += 1
                        if del_sof[dataBitW:dataBitW + len(eol)] != eol:
                            eol_fail_cnt += 1
                        rest_data_f2l = del_sof[H_width - Sync_width:]
                        sum_index = index + H_width
                    else:
                        sol_fail_cnt += 2071
                        code_fail_cnt += 310*2072
                        eol_fail_cnt += 2071
                        Not_SOF += 1
                        break
                if 0 < V < 2072:
                    if sol == rest_data_f2l[0:Sync_width]:
                        del_sol = rest_data_f2l[len(sol):]
                        for data_num in range(310):
                            data = del_sol[data_num * 14:14 * (data_num + 1)]
                            if data != training_code:
                                code_fail_cnt += 1
                        if del_sol[dataBitW:dataBitW + len(eol)] != eol:
                            eol_fail_cnt += 1
                        rest_data_f2l = del_sol[H_width - Sync_width:]
                        sum_index = sum_index + H_width
                    else:
                        sol_fail_cnt += 1
                        del_sol = rest_data_f2l[len(sol):]
                        for data_num in range(310):
                            data = del_sol[data_num * 14:14 * (data_num + 1)]
                            if data != training_code:
                                code_fail_cnt += 1
                        if del_sol[dataBitW:dataBitW + len(eol)] != eol:
                            eol_fail_cnt += 1
                        rest_data_f2l = del_sol[H_width - Sync_width:]
                        sum_index = sum_index + H_width
        ws_all.cell(row=edge_index, column=vdd18l_index, value=sol_fail_cnt + code_fail_cnt + eol_fail_cnt)  # write data
        ws_sol.cell(row=edge_index, column=vdd18l_index, value=sol_fail_cnt)  # write data
        ws_eol.cell(row=edge_index, column=vdd18l_index, value=eol_fail_cnt)  # write data
        ws_sof.cell(row=edge_index, column=vdd18l_index, value=Not_SOF)  # write data
        print('Finished ' + str(i))
    wb.save(SaveExcel)
    print('All Finished')

def Data2Shmoo_Driver7Edge(selected_folder):
    DeleteFolder()
    SortFile(selected_folder)
    training_code = '00011100001111'  # 070f
    dataBitW = 310 * 14
    Sync_width = 56
    rest_data_f2l = ''
    H_width = 576*14
    sum_index = 0
    if path_from:
        time_label = datetime.now().strftime("%Y%m%d%H%M%S")
        SaveExcel = path_from + '\\' + 'Shmoo_' + str(time_label) + '.xlsx'
    else:
        return
    wb = op.Workbook()
    ws_all = wb.create_sheet('All_Error')
    ws_sol = wb.create_sheet('SOL_Error')
    ws_eol = wb.create_sheet('EOL_Error')
    ws_sof = wb.create_sheet('SOF_Error')
    path = os.listdir(path_from)
    for k in range(len(path)):
        selected_file_list = []
        for root, dirs, files in os.walk(path_from + "\\" + path[k]):
            for file in files:
                # 使用join函数将文件名称和文件所在根目录连接起来
                print(os.path.join(root, file))
                selected_file_list.append(os.path.join(root, file))
        driverC_num = int(path[k].split('_')[0])
        edge_num = int(path[k].split('_')[1])
        Not_SOF = 0
        code_fail_cnt = 0
        sol_fail_cnt = 0
        eol_fail_cnt = 0
        for i in range(int(len(selected_file_list))):
            pi_string = ''
            if i == 0:
                edge_index = edge_num + 1 + 1
                driverC_index = driverC_num + 1 + 1
                edge_val = 5 + edge_num * 0.2
                vdd18l_val = 150 + driverC_num * 25
                ws_all.cell(row=edge_index, column=1, value=edge_val)  # edge
                ws_all.cell(row=1, column=driverC_index, value=vdd18l_val)  # vdd18l
                ws_sol.cell(row=edge_index, column=1, value=edge_val)  # edge
                ws_sol.cell(row=1, column=driverC_index, value=vdd18l_val)  # vdd18l
                ws_eol.cell(row=edge_index, column=1, value=edge_val)  # edge
                ws_eol.cell(row=1, column=driverC_index, value=vdd18l_val)  # vdd18l
                ws_sof.cell(row=edge_index, column=1, value=edge_val)  # edge
                ws_sof.cell(row=1, column=driverC_index, value=vdd18l_val)  # vdd18l
            with open(selected_file_list[i], 'r+') as r_fp:
                lines = r_fp.readlines()
            for line in lines:
                pi_string += line.rstrip()
            for V in range(2072):  # 0-2081  sum = 2082
                if V == 0:
                    if sof in pi_string:
                        index = pi_string.find(sof)
                        del_sof = pi_string[index + len(sof):]
                        for data_num in range(310):
                            data = del_sof[data_num * 14:14 * (data_num + 1)]
                            if data != training_code:
                                code_fail_cnt += 1
                        if del_sof[dataBitW:dataBitW + len(eol)] != eol:
                            eol_fail_cnt += 1
                        rest_data_f2l = del_sof[H_width - Sync_width:]
                        sum_index = index + H_width
                    else:
                        sol_fail_cnt += 2071
                        code_fail_cnt += 310 * 2072
                        eol_fail_cnt += 2071
                        Not_SOF += 1
                        break
                if 0 < V < 2072:
                    if sol == rest_data_f2l[0:Sync_width]:
                        del_sol = rest_data_f2l[len(sol):]
                        for data_num in range(310):
                            data = del_sol[data_num * 14:14 * (data_num + 1)]
                            if data != training_code:
                                code_fail_cnt += 1
                        if del_sol[dataBitW:dataBitW + len(eol)] != eol:
                            eol_fail_cnt += 1
                        rest_data_f2l = del_sol[H_width - Sync_width:]
                        sum_index = sum_index + H_width
                    else:
                        sol_fail_cnt += 1
                        del_sol = rest_data_f2l[len(sol):]
                        for data_num in range(310):
                            data = del_sol[data_num * 14:14 * (data_num + 1)]
                            if data != training_code:
                                code_fail_cnt += 1
                        if del_sol[dataBitW:dataBitW + len(eol)] != eol:
                            eol_fail_cnt += 1
                        rest_data_f2l = del_sol[H_width - Sync_width:]
                        sum_index = sum_index + H_width
            ws_all.cell(row=edge_index, column=driverC_index,
                        value=sol_fail_cnt + code_fail_cnt + eol_fail_cnt)  # write data
            ws_sol.cell(row=edge_index, column=driverC_index, value=sol_fail_cnt)  # write data
            ws_eol.cell(row=edge_index, column=driverC_index, value=eol_fail_cnt)  # write data
            ws_sof.cell(row=edge_index, column=driverC_index, value=Not_SOF)  # write data
        print('Finished ' + str(path_from + "\\" + path[k]))
    wb.save(SaveExcel)
    print('All Finished')

def SortFile(selected_folder):
    path = os.listdir(selected_folder)
    for path_loop in range(len(path)):
        all_t_file = []
        new_f_name = []
        son_folder = selected_folder + '\\' + path[path_loop]
        for root, dirs, files in os.walk(son_folder):
            for f in range(len(files)):
                new_f_name.append(files[f].split('_')[1].split('.')[0][4:])  # edge num
        new_f_name = list(set(new_f_name))
        for i in range(len(new_f_name)):
            new_p = path_from + '\\' + path[path_loop] + "_" + new_f_name[i]
            if not os.path.exists(new_p):
                os.mkdir(new_p)
        for root, dirs, files in os.walk(son_folder):
            for f in range(len(files)):
                target_file = son_folder + '\\' + files[f]
                target_folder = path_from + '\\' + path[path_loop] + "_" + files[f].split('_')[1].split('.')[0][4:]
                if target_file not in all_t_file:
                    all_t_file.append(target_file)
                    shutil.copy(target_file, target_folder)


def DeleteFolder():
    shutil.rmtree(path_from)
    os.mkdir(path_from)

def IsMe(selected_file_list):
    Data2Shmoo_Pro = threading.Thread(target=Data2Shmoo(selected_file_list), args=("Data2Shmoo_Pro",))
    Data2Shmoo_Pro.start()



if __name__ == '__main__':
    Data2Shmoo_Driver7Edge(path_from)

