import os, openpyxl as op

sof = '11111111111111000000000000000000000000000010101011000000'
sol = '11111111111111000000000000000000000000000010000000000000'
eol = '11111111111111000000000000000000000000000010011101000000'
eof = '11111111111111000000000000000000000000000010110110000000'
sof_a='11111111111111000000000000000000000000000010101011000000'

def ToRaw_b(selected_file_list):
    for i in range(len(selected_file_list)):
        with open(selected_file_list[i], 'r+') as r_fp:
            lines = r_fp.readlines()
            # print(lines)
        pi_string = ''
        for line in lines:
            pi_string +=line.rstrip()
        if eof in pi_string:
            index_eof = pi_string.find(eof)
            print('index_eol:' + str(index_eof))

def ToRaw_b2(selected_file_list):
    file = r'D:\HaiTu\HT50A\CP\Datalog\raw.txt'
    file_ch1 = r'D:\HaiTu\HT50A\CP\Datalog\ch1.txt'
    w_fp = open(file, 'w+')
    ch1_fp = open(file_ch1, 'w+')
    final_singel = ''
    for i in range(len(selected_file_list)):
        with open(selected_file_list[i], 'r+') as r_fp:
            lines = r_fp.readlines()
            # print(lines)
        pi_string = ''
        for line in lines:
            pi_string +=line.rstrip()
        if i == 0:
            if sof in pi_string:
                index = pi_string.find(sof)
                # print(index)
                # print(pi_string[index+len(sof):])
                del_sof = pi_string[index+len(sof):]
                if eol in del_sof:
                    index_eol = del_sof.find(eol)
                    final_singel = del_sof[:index_eol]
                else:
                    print('Not find EOL')
            else:
                print('Not find SOF')
            ch1_fp.write(final_singel)
            ch1_fp.close()
        elif 1 <= i <= 6:
            if sol in pi_string:
                index = pi_string.find(sol)
                # print(index)
                # print(pi_string[index+len(sof):])
                del_sol = pi_string[index+len(sol):]
                if eol in del_sol:
                    index_eol = del_sol.find(eol)
                    final_singel = del_sol[:index_eol]
                else:
                    print('Not find EOL')
            else:
                print('Not find SOL')
        elif i == 7:
            if sol in pi_string:
                index = pi_string.find(sol)
                # print(index)
                # print(pi_string[index+len(sof):])
                del_sol = pi_string[index+len(sol):]
                if eof in del_sol:
                    index_eof = del_sol.find(eof)
                    final_singel = del_sol[:index_eof]
                else:
                    print('Not find EOF')
            else:
                print('Not find SOL')
        r_fp.close()
        w_fp.write(final_singel)
        print('Finished ' + selected_file_list[i])
    w_fp.close()
    print('All Finished')

def ToRaw(selected_file_list):
    file = r'D:\HaiTu\HT50A\CP\Datalog\raw.txt'
    w_fp = open(file, 'w+')
    final_singel = ''
    error_data = False
    for i in range(len(selected_file_list)):
        with open(selected_file_list[i], 'r+') as r_fp:
            lines = r_fp.readlines()
            # print(lines)
        r_fp.close()
        pi_string = ''
        for line in lines:
            pi_string +=line.rstrip()
        for V in range(2082):  # 0-2081  sum = 2082
            # print(V)
            if V == 0:
                if sof in pi_string:
                    index = pi_string.find(sof)
                    del_sof = pi_string[index + len(sof):]
                    if eol in del_sof:
                        index_eol = del_sof.find(eol)
                        del_sof_eol = del_sof[:index_eol]
                        if len(del_sof_eol) != 310 * 14:
                            print('len(del_sof_eol) = ' + str(len(del_sof_eol)))
                        rest_data_f2l = del_sof[index_eol + len(eol):]
                        w_fp.write(del_sof_eol)
                    else:
                        error_data = True
                        print('V=' + str(V))
                        print('Not find EOL')
                else:
                    error_data = True
                    print('V=' + str(V))
                    print('Not find SOF')
            if error_data:
                break
            if 0 < V < 2071:
                if V == 1:
                    if sol in rest_data_f2l:
                        index = rest_data_f2l.find(sol)
                        del_sol = rest_data_f2l[index + len(sol):]
                        if eol in del_sol:
                            index_eol = del_sol.find(eol)
                            del_sol_eol = del_sol[:index_eol]
                            if len(del_sol_eol) != 310 * 14:
                                print('V=' + str(V))
                                print('len(del_sol_eol) = ' + str(len(del_sol_eol)))
                            rest_data_l2l = del_sol[index_eol + len(eol):]
                            w_fp.write(del_sol_eol)
                        else:
                            error_data = True
                            print('V=' + str(V))
                            print('Not find EOL')
                    else:
                        error_data = True
                        print('V=' + str(V))
                        print('Not find SOL')
                else:
                    if sol in rest_data_l2l:
                        index = rest_data_l2l.find(sol)
                        del_sol = rest_data_l2l[index + len(sol):]
                        if eol in del_sol:
                            index_eol = del_sol.find(eol)
                            del_sol_eol = del_sol[:index_eol]
                            if len(del_sol_eol) != 310 * 14:
                                print('V=' + str(V))
                                print('len(del_sol_eol) = ' + str(len(del_sol_eol)))
                            rest_data_l2l = del_sol[index_eol + len(eol):]
                            w_fp.write(del_sol_eol)
                        else:
                            error_data = True
                            print('V=' + str(V))
                            print('Not find EOL')
                    else:
                        error_data = True
                        print('V=' + str(V))
                        print('Not find SOL')
            if V == 2071:
                if sol in rest_data_l2l:
                    index = rest_data_l2l.find(sol)
                    del_sol_eof = rest_data_l2l[index + len(sol):index + len(sol) + 310*14]
                    if len(del_sol_eof) != 310 * 14:
                        print('V=' + str(V))
                        print('len(del_sol_eof) = ' + str(len(del_sol_eof)))
                    w_fp.write(del_sol_eof)
                    break
                    # if eof in del_eof:
                    #     index_eol = del_eof.find(eof)
                    #     del_sol_eof = del_eof[:index_eol]
                    #     if len(del_sol_eof) != 310 * 14:
                    #         print('V=' + str(V))
                    #         print('len(del_sol_eof) = ' + str(len(del_sol_eof)))
                    #     w_fp.write(del_sol_eof)
                    # else:
                    #     error_data = True
                    #     print('V=' + str(V))
                    #     print('Not find EOF')
                else:
                    error_data = True
                    print('V=' + str(V))
                    print('Not find SOL')
        if error_data:
            print('Error Data at V=' + str(V))
            print('At---' + selected_file_list[i])
            break
        print('Finished ' + selected_file_list[i])
    w_fp.close()
    print('All Finished')

def splic_data():
    file = r'D:\HaiTu\HT50A\CP\Datalog\raw.txt'
    raw = r'D:\HaiTu\HT50A\CP\Datalog\34rawdata-1.raw'
    rf = r'D:\HaiTu\HT50A\CP\Datalog\rawdata.txt'
    # file = r'D:\Python\Project\Ref_Data\tt_data.txt'
    # raw = r'D:\Python\Project\Ref_Data\tt_raw.txt'
    w_fp = open(raw, 'w')
    w_rf = open(rf, 'w')
    with open(file, 'r') as r_fp:
        lines = r_fp.readlines()
    line_str = ''
    line_str = line_str.join(lines)
    for v in range(2072):
        for data in range(310):
            for ch in range(8):
                w_fp.write(line_str[310*ch*v+14*data:310*ch*v+14*(data+1)])
                w_rf.write(line_str[310 * ch * v + 14 * data:310 * ch * v + 14 * (data + 1)])
        w_fp.write('\r')
        w_rf.write('\r')
    print('Convert finished')

def splic_data7shfit():
    print('Running splic_data7shfit')
    file = r'D:\HaiTu\HT50A\CP\Datalog\raw.txt'
    raw = r'D:\HaiTu\HT50A\CP\Datalog\34rawdata-1.raw'
    rf = r'D:\HaiTu\HT50A\CP\Datalog\rawdata.txt'
    f_NoDeal = r'D:\HaiTu\HT50A\CP\Datalog\rawdata.txt'
    # file = r'D:\Python\Project\Ref_Data\tt_data.txt'
    # raw = r'D:\Python\Project\Ref_Data\tt_raw.txt'
    w_fp = open(raw, 'w')
    w_rf = open(rf, 'w')
    w_f_NoDeal = open(f_NoDeal, 'w')
    line_str = ''
    binary_label = '0b'
    extern_data = '00'
    with open(file, 'r') as r_fp:
        lines = r_fp.readlines()
    line_str = line_str.join(lines)
    for v in range(2072):
        for data in range(310):
            for ch in range(8):
                # num_shift=0
                # num = int(line_str[310*ch*v+14*data:310*ch*v+14*(data+1)] + binary_label, 2)
                # num_shift |= num << 14
                # w_fp.write(line_str[310*ch*v+14*data:310*ch*v+14*(data+1)])
                # w_rf.write(line_str[310 * ch * v + 14 * data:310 * ch * v + 14 * (data + 1)])
                # w_fp.write(str(int(extern_data+line_str[310*ch*v+14*data:310*ch*v+14*(data+1)], 2)))
                # w_rf.write(str(int(extern_data+line_str[310*ch*v+14*data:310*ch*v+14*(data+1)], 2)))
                w_fp.write(line_str[310*ch*v+14*data:310*ch*v+14*(data+1)])
                w_rf.write(line_str[310*ch*v+14*data:310*ch*v+14*(data+1)])
        w_fp.write('\r')
        w_rf.write('\r')
    w_fp.close()
    w_rf.close()
    print('Convert finished')

# 采集的原始数据，包含无效数据，sync code，有效数据
# 下面的函数用于提取有效数据，从sof或sol提取，并比对有效数据是否是070f
def CompareDataWith70F(selected_file_list):
    # file = r'D:\HaiTu\HT50A\CP\Datalog\0_data.txt'
    # one_line = r'D:\HaiTu\HT50A\CP\Datalog\one_line.txt'
    # w_fp = open(file, 'w')
    # w_ol = open(one_line, 'w')
    training_code = '00011100001111'  # 070f
    # training_code = '11111111111111'  # 3fff
    data_ana = '_ana'
    dataBitW = 310*14
    code_fail_cnt = 0
    sol_fail_cnt = 0
    eol_fail_cnt = 0
    lineBitW = len(sol) + dataBitW + len(eol)
    for i in range(len(selected_file_list)):
        with open(selected_file_list[i], 'r+') as r_fp:
            lines = r_fp.readlines()
        file_name = os.path.basename(selected_file_list[i])
        file_path = os.path.dirname(selected_file_list[i])
        print(file_path)
        file_info = file_name.split('.')
        print(file_info)
        new_file = file_path + '\\' + file_info[0] + data_ana + '.' + file_info[1]
        print(new_file)
        w_fp = open(new_file, 'w+')
        # w_ol.write(str(lines))
        r_fp.close()
        pi_string = ''
        for line in lines:
            pi_string += line.rstrip()
        for V in range(2072):  # 0-2081  sum = 2082
            if V == 0:
                if sof in pi_string:
                    index = pi_string.find(sof)
                    w_fp.write('V=' + str(V))
                    w_fp.write(' SOF Add:' + str(index+1))
                    w_fp.write('\r')
                    w_fp.write(pi_string[index:index+len(sof)])
                    w_fp.write('\r')
                    del_sof = pi_string[index + len(sof):]
                    for data_num in range(310):
                        data = del_sof[data_num*14:14*(data_num+1)]
                        if data != training_code:
                            w_fp.write(data + ' Err at ')
                            code_fail_cnt += 1
                            w_fp.write(str(index+len(sof)+(data_num)*14+1))
                        else:
                            w_fp.write(data)
                        w_fp.write('\r')
                    if del_sof[dataBitW:dataBitW+len(eol)] != eol:
                        code_fail_cnt += 1
                        eol_fail_cnt += 1
                        w_fp.write('Err EOL:')
                        w_fp.write('\r')
                    w_fp.write(del_sof[dataBitW:dataBitW+len(eol)])
                    w_fp.write('\r')
                    rest_data_f2l = del_sof[dataBitW+len(eol):]
                    sum_index = index + len(sof) + dataBitW + len(eol)
                else:
                    print('Not Found SOF')
                    w_fp.write('Not Found SOF\r')
                    break
            if 0 < V < 2072:
                if sol in rest_data_f2l:
                    w_fp.write('V=' + str(V))
                    index = rest_data_f2l.find(sol)
                    w_fp.write(' SOL Add:' + str(sum_index+index+1))
                    w_fp.write('\r')
                    w_fp.write(rest_data_f2l[index:index+len(sol)])
                    w_fp.write('\r')
                    del_sol = rest_data_f2l[index + len(sol):]
                    for data_num in range(310):
                        data = del_sol[data_num * 14:14 * (data_num + 1)]
                        if data != training_code:
                            w_fp.write(data + ' Err at ')
                            code_fail_cnt += 1
                            w_fp.write(str(sum_index + index + len(sol) + (data_num) * 14 + 1))
                        else:
                            w_fp.write(data)
                        w_fp.write('\r')
                    if del_sol[dataBitW:dataBitW+len(eol)] != eol:
                        w_fp.write('Err EOL:')
                        code_fail_cnt += 1
                        eol_fail_cnt += 1
                        w_fp.write('\r')
                    w_fp.write(del_sol[dataBitW:dataBitW + len(eol)])
                    w_fp.write('\r')
                    rest_data_f2l = del_sol[dataBitW + len(eol):]
                    sum_index = sum_index + lineBitW + index
                else:
                    w_fp.write('Err SOL:')


        w_fp.close()
    print('All Finished')
    print('Error Code Count=' + str(code_fail_cnt))
    print('Error EOL Count=' + str(code_fail_cnt))

def CompareDataWith70F_14bit(selected_file_list):
    # file = r'D:\HaiTu\HT50A\CP\Datalog\0_data.txt'
    # one_line = r'D:\HaiTu\HT50A\CP\Datalog\one_line.txt'
    # w_fp = open(file, 'w')
    # w_ol = open(one_line, 'w')
    training_code = '00011100001111'  # 070f
    data_ana = '_Ana'
    dataBitW = 310*14
    code_fail_cnt = 0
    sol_fail_cnt = 0
    eol_fail_cnt = 0
    invalid_data = 258*14
    Sync_width = 56
    rest_data_f2l = ''
    lineBitW = len(sol) + dataBitW + len(eol)
    for i in range(len(selected_file_list)):
        with open(selected_file_list[i], 'r+') as r_fp:
            lines = r_fp.readlines()
        file_name = os.path.basename(selected_file_list[i])
        file_path = os.path.dirname(selected_file_list[i])
        print(file_path)
        file_info = file_name.split('.')
        print(file_info)
        new_file = file_path + '\\' + file_info[0] + data_ana + '.' + file_info[1]
        print(new_file)
        w_fp = open(new_file, 'w+')
        # w_ol.write(str(lines))
        r_fp.close()
        pi_string = ''
        for line in lines:
            pi_string += line.rstrip()
        for V in range(2072):  # 0-2081  sum = 2082
            if V == 0:
                if sof in pi_string:
                    index = pi_string.find(sof)
                    w_fp.write('V=' + str(V))
                    w_fp.write(' SOF Add:' + str(index+1))
                    w_fp.write('\r')
                    w_fp.write(pi_string[index:index+len(sof)])
                    w_fp.write('\r')
                    del_sof = pi_string[index + len(sof):]
                    for data_num in range(310):
                        data = del_sof[data_num*14:14*(data_num+1)]
                        if data != training_code:
                            w_fp.write(data + ' Err at ')
                            code_fail_cnt += 1
                            w_fp.write(str(index+len(sof)+(data_num)*14+1))
                        else:
                            w_fp.write(data)
                        w_fp.write('\r')
                    if del_sof[dataBitW:dataBitW+len(eol)] != eol:
                        eol_fail_cnt += 1
                        w_fp.write('Err EOL:')
                        w_fp.write('\r')
                    w_fp.write(del_sof[dataBitW:dataBitW+len(eol)])
                    w_fp.write('\r')
                    rest_data_f2l = del_sof[dataBitW+len(eol)+invalid_data:]
                    sum_index = index + len(sof) + dataBitW + len(eol) + invalid_data  # + invalid_data
                else:
                    print('Not Found SOF')
                    w_fp.write('Not Found SOF\r')
                    break
            if 0 < V < 2072:
                if sol == rest_data_f2l[0:Sync_width]:
                    w_fp.write('V=' + str(V))
                    w_fp.write(' SOL Add:' + str(sum_index + 1))
                    w_fp.write('\r')
                    w_fp.write(rest_data_f2l[0:len(sol)])
                    w_fp.write('\r')
                    del_sol = rest_data_f2l[len(sol):]
                    for data_num in range(310):
                        data = del_sol[data_num * 14:14 * (data_num + 1)]
                        if data != training_code:
                            w_fp.write(data + ' Err at ')
                            code_fail_cnt += 1
                            w_fp.write(str(sum_index + len(sol) + (data_num) * 14 + 1))
                        else:
                            w_fp.write(data)
                        w_fp.write('\r')
                    if del_sol[dataBitW:dataBitW+len(eol)] != eol:
                        w_fp.write('Err EOL:')
                        eol_fail_cnt += 1
                        w_fp.write('\r')
                    w_fp.write(del_sol[dataBitW:dataBitW + len(eol)])
                    w_fp.write('\r')
                    rest_data_f2l = del_sol[dataBitW + len(eol) + invalid_data:]
                    sum_index = sum_index + lineBitW + invalid_data
                else:
                    sol_fail_cnt += 1
                    w_fp.write('Err SOL:')
                    w_fp.write('V=' + str(V))
                    w_fp.write(' SOL Add:' + str(sum_index + 1))
                    w_fp.write('\r')
                    w_fp.write(rest_data_f2l[0:len(sol)])
                    w_fp.write('\r')
                    del_sol = rest_data_f2l[len(sol):]
                    for data_num in range(310):
                        data = del_sol[data_num * 14:14 * (data_num + 1)]
                        if data != training_code:
                            w_fp.write(data + ' Err at ')
                            code_fail_cnt += 1
                            w_fp.write(str(sum_index + len(sol) + (data_num) * 14 + 1))
                        else:
                            w_fp.write(data)
                        w_fp.write('\r')
                    if del_sol[dataBitW:dataBitW+len(eol)] != eol:
                        w_fp.write('Err EOL:')
                        eol_fail_cnt += 1
                        w_fp.write('\r')
                    w_fp.write(del_sol[dataBitW:dataBitW + len(eol)])
                    w_fp.write('\r')
                    rest_data_f2l = del_sol[dataBitW + len(eol) + invalid_data:]
                    sum_index = sum_index + lineBitW + invalid_data
        w_fp.close()
    print('All Finished')
    print('Error SOL Count=' + str(sol_fail_cnt))
    print('Error Code Count=' + str(code_fail_cnt))
    print('Error EOL Count=' + str(eol_fail_cnt))
    print('All Error=' + str(sol_fail_cnt+code_fail_cnt+eol_fail_cnt))

def CompareDataWith70F_14bit_160A(selected_file_list):
    # file = r'D:\HaiTu\HT50A\CP\Datalog\0_data.txt'
    # one_line = r'D:\HaiTu\HT50A\CP\Datalog\one_line.txt'
    # w_fp = open(file, 'w')
    # w_ol = open(one_line, 'w')
    training_code = '00011100001111'  # 070f
    data_ana = '_Ana'
    dataBitW = 310*14
    code_fail_cnt = 0
    sol_fail_cnt = 0
    eol_fail_cnt = 0
    invalid_data = 258*14
    Sync_width = 56
    rest_data_f2l = ''
    lineBitW = len(sol) + dataBitW + len(eol)
    for i in range(len(selected_file_list)):
        with open(selected_file_list[i], 'r+') as r_fp:
            lines = r_fp.readlines()
        file_name = os.path.basename(selected_file_list[i])
        file_path = os.path.dirname(selected_file_list[i])
        print(file_path)
        file_info = file_name.split('.')
        print(file_info)
        new_file = file_path + '\\' + file_info[0] + data_ana + '.' + file_info[1]
        print(new_file)
        w_fp = open(new_file, 'w+')
        # w_ol.write(str(lines))
        r_fp.close()
        pi_string = ''
        for line in lines:
            pi_string += line.rstrip()
        for V in range(4120):  # 0-2081  sum = 2082
            if V == 0:
                if sof_a in pi_string:
                    index = pi_string.find(sof_a)
                    w_fp.write('V=' + str(V))
                    w_fp.write(' SOF Add:' + str(index+1))
                    w_fp.write('\r')
                    w_fp.write(pi_string[index:index+len(sof)])
                    w_fp.write('\r')
                    del_sof = pi_string[index + len(sof):]
                    for data_num in range(310):
                        data = del_sof[data_num*14:14*(data_num+1)]
                        if data != training_code:
                            w_fp.write(data + ' Err at ')
                            code_fail_cnt += 1
                            w_fp.write(str(index+len(sof)+(data_num)*14+1))
                        else:
                            w_fp.write(data)
                        w_fp.write('\r')
                    if del_sof[dataBitW:dataBitW+len(eol)] != eol:
                        eol_fail_cnt += 1
                        w_fp.write('Err EOL:')
                        w_fp.write('\r')
                    w_fp.write(del_sof[dataBitW:dataBitW+len(eol)])
                    w_fp.write('\r')
                    rest_data_f2l = del_sof[dataBitW+len(eol)+invalid_data:]
                    sum_index = index + len(sof) + dataBitW + len(eol) + invalid_data  # + invalid_data
                else:
                    print('Not Found SOF')
                    w_fp.write('Not Found SOF\r')
                    break
            if 0 < V < 4120:
                if sol == rest_data_f2l[0:Sync_width]:
                    w_fp.write('V=' + str(V))
                    w_fp.write(' SOL Add:' + str(sum_index + 1))
                    w_fp.write('\r')
                    w_fp.write(rest_data_f2l[0:len(sol)])
                    w_fp.write('\r')
                    del_sol = rest_data_f2l[len(sol):]
                    for data_num in range(257):
                        data = del_sol[data_num * 14:14 * (data_num + 1)]
                        if data != training_code:
                            w_fp.write(data + ' Err at ')
                            code_fail_cnt += 1
                            w_fp.write(str(sum_index + len(sol) + (data_num) * 14 + 1))
                        else:
                            w_fp.write(data)
                        w_fp.write('\r')
                    if del_sol[dataBitW:dataBitW+len(eol)] != eol:
                        w_fp.write('Err EOL:')
                        eol_fail_cnt += 1
                        w_fp.write('\r')
                    w_fp.write(del_sol[dataBitW:dataBitW + len(eol)])
                    w_fp.write('\r')
                    rest_data_f2l = del_sol[dataBitW + len(eol) + invalid_data:]
                    sum_index = sum_index + lineBitW + invalid_data
                else:
                    sol_fail_cnt += 1
                    w_fp.write('Err SOL:')
                    w_fp.write('V=' + str(V))
                    w_fp.write(' SOL Add:' + str(sum_index + 1))
                    w_fp.write('\r')
                    w_fp.write(rest_data_f2l[0:len(sol)])
                    w_fp.write('\r')
                    del_sol = rest_data_f2l[len(sol):]
                    for data_num in range(257):
                        data = del_sol[data_num * 14:14 * (data_num + 1)]
                        if data != training_code:
                            w_fp.write(data + ' Err at ')
                            code_fail_cnt += 1
                            w_fp.write(str(sum_index + len(sol) + (data_num) * 14 + 1))
                        else:
                            w_fp.write(data)
                        w_fp.write('\r')
                    if del_sol[dataBitW:dataBitW+len(eol)] != eol:
                        w_fp.write('Err EOL:')
                        eol_fail_cnt += 1
                        w_fp.write('\r')
                    w_fp.write(del_sol[dataBitW:dataBitW + len(eol)])
                    w_fp.write('\r')
                    rest_data_f2l = del_sol[dataBitW + len(eol) + invalid_data:]
                    sum_index = sum_index + lineBitW + invalid_data
        w_fp.close()
    print('All Finished')
    print('Error SOL Count=' + str(sol_fail_cnt))
    print('Error Code Count=' + str(code_fail_cnt))
    print('Error EOL Count=' + str(eol_fail_cnt))
    print('All Error=' + str(sol_fail_cnt+code_fail_cnt+eol_fail_cnt))



def shmoo_data(selected_file_list):
    # selected_file_list = [r'D:\Tool_RAW\E_0_V_00.txt']
    ev = r'D:\Tool_RAW\ev.xlsx'
    training_code = '00011100001111'  # 070f
    dataBitW = 310 * 14
    code_fail_cnt = 0
    sol_fail_cnt = 0
    eol_fail_cnt = 0
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
    pi_string = ''
    edge_num = vdd18l_num = 0
    for i in range(int(len(selected_file_list)/8)):
        for f8 in range(8):
            if not f8:
                file_name = os.path.basename(selected_file_list[f8 + i*8])
                edge_num = int(os.path.splitext(file_name)[0][:-1].split('_')[1])
                edge_val = 5 + edge_num*0.2
                vdd18l_num = int(os.path.splitext(file_name)[0][:-1].split('_')[3])
                vdd18l_val = 1.7 + vdd18l_num * 0.3
                ws_all.cell(row=edge_num+1, column=1, value=edge_val)  # edge
                ws_all.cell(row=1, column=vdd18l_num+1, value=vdd18l_val)  # vdd18l
                ws_sol.cell(row=edge_num+1, column=1, value=edge_val)  # edge
                ws_sol.cell(row=1, column=vdd18l_num+1, value=vdd18l_val)  # vdd18l
                ws_eol.cell(row=edge_num+1, column=1, value=edge_val)  # edge
                ws_eol.cell(row=1, column=vdd18l_num+1, value=vdd18l_val)  # vdd18l
            with open(selected_file_list[f8 + i*8], 'r+') as r_fp:
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
                        ws_all.cell(row=edge_num + 1, column=vdd18l_num + 1, value=str('No_SOF'))  # write data
                        ws_sol.cell(row=edge_num + 1, column=vdd18l_num + 1, value=str('No_SOF'))  # write data
                        ws_eol.cell(row=edge_num + 1, column=vdd18l_num + 1, value=str('No_SOF'))  # write data
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
        ws_all.cell(row=edge_num + 1, column=vdd18l_num + 1, value=sol_fail_cnt + code_fail_cnt + eol_fail_cnt)  # write data
        ws_sol.cell(row=edge_num + 1, column=vdd18l_num + 1, value=sol_fail_cnt)  # write data
        ws_eol.cell(row=edge_num + 1, column=vdd18l_num + 1, value=eol_fail_cnt)  # write data
        wb.save(ev)
    print('All Finished')
    print('Error SOL Count=' + str(sol_fail_cnt))
    print('Error Code Count=' + str(code_fail_cnt))
    print('Error EOL Count=' + str(eol_fail_cnt))
    print('All Error=' + str(sol_fail_cnt + code_fail_cnt + eol_fail_cnt))

def Cal_SOF_Count():
    selected_file_list = [r'D:\Tool_RAW\0.txt']
    for i in range(len(selected_file_list)):
        with open(selected_file_list[i], 'r+') as r_fp:
            lines = r_fp.readlines()
        pi_string = ''
        for line in lines:
            pi_string += line.rstrip()
        print("SOF Count = " + str(pi_string.count(sof)))



if __name__ == '__main__':
    selected_file_list = [r'D:\Tool_RAW\160\0.txt']
    CompareDataWith70F_14bit_160A(selected_file_list)