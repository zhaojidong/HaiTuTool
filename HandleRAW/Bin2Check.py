import os

sof = '11111111111111000000000000000000000000000010101011000000'
sol = '11111111111111000000000000000000000000000010000000000000'
eol = '11111111111111000000000000000000000000000010011101000000'
eof = '11111111111111000000000000000000000000000010110110000000'
sof_160 = '11111111111111000000000000000000000000000010101011000000'
def Bin2Raw():
    BinFiles = r'D:\Python\Project\Ref_Data\340.bin'
    binfile = open(BinFiles, 'rb')
    size = os.path.getsize(BinFiles) #获得文件大小
    s0 = ''
    for loop in range(size):
        data = binfile.read(1) #每次输出一个字节
        a = [hex(x) for x in data]
        s10 = int(a[0], 16)
        s2 = '{:08b}'.format(s10)
        s0 += s2

def CheckBinData_14bit_b(selected_file_list):
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
        binfile = open(selected_file_list[i], 'rb')
        size = os.path.getsize(selected_file_list[i])  # 获得文件大小
        lines = ''
        for loop in range(size):
            data = binfile.read(1)  # 每次输出一个字节
            a = [hex(x) for x in data]
            s10 = int(a[0], 16)
            s2 = '{:08b}'.format(s10)
            lines += s2
        file_name = os.path.basename(selected_file_list[i])
        file_path = os.path.dirname(selected_file_list[i])
        print(file_path)
        file_info = file_name.split('.')
        print(file_info)
        new_file = file_path + '\\' + file_info[0] + data_ana + '.txt'
        print(new_file)
        w_fp = open(new_file, 'w+')
        # w_ol.write(str(lines))
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
                    sum_index = index + len(sof) + dataBitW + len(eol)
                else:
                    print('Not Found SOF')
                    w_fp.write('Not Found SOF\r')
                    break
            if 0 < V < 2072:
                if sol == rest_data_f2l[0:Sync_width]:
                    #print(rest_data_f2l[0:Sync_width])
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
                        eol_fail_cnt += 1
                        w_fp.write('\r')
                    w_fp.write(del_sol[dataBitW:dataBitW + len(eol)])
                    w_fp.write('\r')
                    rest_data_f2l = del_sol[dataBitW + len(eol) + invalid_data:]
                    sum_index = sum_index + lineBitW + index
                else:
                    #print(rest_data_f2l[0:Sync_width])
                    index += 1
                    sol_fail_cnt += 1
                    w_fp.write('Err SOL:')
                    w_fp.write('V=' + str(V))
                    w_fp.write(' SOL Add:' + str(sum_index + index + 1))
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
                        eol_fail_cnt += 1
                        w_fp.write('\r')
                    w_fp.write(del_sol[dataBitW:dataBitW + len(eol)])
                    w_fp.write('\r')
                    rest_data_f2l = del_sol[dataBitW + len(eol) + invalid_data:]
                    sum_index = sum_index + lineBitW + index
        w_fp.close()

def CheckBinData_14bit(selected_file_list):
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
        binfile = open(selected_file_list[i], 'rb')
        size = os.path.getsize(selected_file_list[i])  # 获得文件大小
        lines = ''
        for loop in range(size):
            data = binfile.read(1)  # 每次输出一个字节
            a = [hex(x) for x in data]
            s10 = int(a[0], 16)
            s2 = '{:08b}'.format(s10)
            lines += s2
        file_name = os.path.basename(selected_file_list[i])
        file_path = os.path.dirname(selected_file_list[i])
        print(file_path)
        file_info = file_name.split('.')
        print(file_info)
        new_file = file_path + '\\' + file_info[0] + data_ana + '.txt'
        print(new_file)
        w_fp = open(new_file, 'w+')
        # w_ol.write(str(lines))
        pi_string = ''
        for line in lines:
            pi_string += line.rstrip()
        for V in range(2072):  # 0-2081  sum = 2082
            if V == 0:
                if sof in pi_string:
                    index = pi_string.find(sof)
                    w_fp.write('V=' + str(V))
                    w_fp.write(' SOF Add:' + str(index + 1))
                    w_fp.write('\r')
                    w_fp.write(pi_string[index:index + len(sof)])
                    w_fp.write('\r')
                    del_sof = pi_string[index + len(sof):]
                    for data_num in range(310):
                        data = del_sof[data_num * 14:14 * (data_num + 1)]
                        if data != training_code:
                            w_fp.write(data + ' Err at ')
                            code_fail_cnt += 1
                            w_fp.write(str(index + len(sof) + (data_num) * 14 + 1))
                        else:
                            w_fp.write(data)
                        w_fp.write('\r')
                    if del_sof[dataBitW:dataBitW + len(eol)] != eol:
                        eol_fail_cnt += 1
                        w_fp.write('Err EOL:')
                        w_fp.write('\r')
                    w_fp.write(del_sof[dataBitW:dataBitW + len(eol)])
                    w_fp.write('\r')
                    rest_data_f2l = del_sof[dataBitW + len(eol) + invalid_data:]
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
                    if del_sol[dataBitW:dataBitW + len(eol)] != eol:
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
                    if del_sol[dataBitW:dataBitW + len(eol)] != eol:
                        w_fp.write('Err EOL:')
                        eol_fail_cnt += 1
                        w_fp.write('\r')
                    w_fp.write(del_sol[dataBitW:dataBitW + len(eol)])
                    w_fp.write('\r')
                    rest_data_f2l = del_sol[dataBitW + len(eol) + invalid_data:]
                    sum_index = sum_index + lineBitW + invalid_data
        w_fp.close()

def CheckBinData_14bit_new(selected_file_list):
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
        binfile = open(selected_file_list[i], 'rb')
        size = os.path.getsize(selected_file_list[i])  # 获得文件大小
        lines = ''
        for loop in range(size):
            data = binfile.read(1)  # 每次输出一个字节
            a = [hex(x) for x in data]
            s10 = int(a[0], 16)
            s2 = '{:08b}'.format(s10)
            lines += s2
        file_name = os.path.basename(selected_file_list[i])
        file_path = os.path.dirname(selected_file_list[i])
        print(file_path)
        file_info = file_name.split('.')
        print(file_info)
        new_file = file_path + '\\' + file_info[0] + data_ana + '.txt'
        print(new_file)
        w_fp = open(new_file, 'w+')
        # w_ol.write(str(lines))
        pi_string = ''
        for line in lines:
            pi_string += line.rstrip()
        for V in range(2072):  # 0-2081  sum = 2082
            if V == 0:
                if sof in pi_string:
                    index = pi_string.find(sof)
                    w_fp.write('V=' + str(V))
                    w_fp.write(' SOF Add:' + str(index + 1))
                    w_fp.write('\r')
                    w_fp.write(pi_string[index:index + len(sof)])
                    w_fp.write('\r')
                    del_sof = pi_string[index + len(sof):]
                    for data_num in range(310):
                        data = del_sof[data_num * 14:14 * (data_num + 1)]
                        if data != training_code:
                            w_fp.write(data + ' Err at ')
                            code_fail_cnt += 1
                            w_fp.write(str(index + len(sof) + (data_num) * 14 + 1))
                        else:
                            w_fp.write(data)
                        w_fp.write('\r')
                    if del_sof[dataBitW:dataBitW + len(eol)] != eol:
                        eol_fail_cnt += 1
                        w_fp.write('Err EOL:')
                        w_fp.write('\r')
                    w_fp.write(del_sof[dataBitW:dataBitW + len(eol)])
                    w_fp.write('\r')
                    rest_data_f2l = del_sof[dataBitW + len(eol) + invalid_data:]
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
                    if del_sol[dataBitW:dataBitW + len(eol)] != eol:
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
                    if del_sol[dataBitW:dataBitW + len(eol)] != eol:
                        w_fp.write('Err EOL:')
                        eol_fail_cnt += 1
                        w_fp.write('\r')
                    w_fp.write(del_sol[dataBitW:dataBitW + len(eol)])
                    w_fp.write('\r')
                    rest_data_f2l = del_sol[dataBitW + len(eol) + invalid_data:]
                    sum_index = sum_index + lineBitW + invalid_data
        w_fp.close()


def CheckBinData_14bit_160A(selected_file_list):
    training_code = '00011100001111'  # 070f
    data_ana = '_Ana'
    dataBitW = 257*14
    code_fail_cnt = 0
    sol_fail_cnt = 0
    eol_fail_cnt = 0
    invalid_data = 23*14
    Sync_width = 56
    rest_data_f2l = ''
    lineBitW = len(sol) + dataBitW + len(eol)
    for i in range(len(selected_file_list)):
        binfile = open(selected_file_list[i], 'rb')
        size = os.path.getsize(selected_file_list[i])  # 获得文件大小
        lines = ''
        for loop in range(size):
            data = binfile.read(1)  # 每次输出一个字节
            a = [hex(x) for x in data]
            s10 = int(a[0], 16)
            s2 = '{:08b}'.format(s10)
            lines += s2
        file_name = os.path.basename(selected_file_list[i])
        file_path = os.path.dirname(selected_file_list[i])
        print(file_path)
        file_info = file_name.split('.')
        print(file_info)
        new_file = file_path + '\\' + file_info[0] + data_ana + '.txt'
        print(new_file)
        w_fp = open(new_file, 'w+')
        # w_ol.write(str(lines))
        pi_string = ''
        for line in lines:
            pi_string += line.rstrip()
        for V in range(4120):  # 0-2081  sum = 2082
            if V == 0:
                if sof_160 in pi_string:
                    index = pi_string.find(sof_160)
                    w_fp.write('V=' + str(V))
                    w_fp.write(' SOF Add:' + str(index + 1))
                    w_fp.write('\r')
                    w_fp.write(pi_string[index:index + len(sof)])
                    w_fp.write('\r')
                    del_sof = pi_string[index + len(sof):]
                    for data_num in range(310):
                        data = del_sof[data_num * 14:14 * (data_num + 1)]
                        if data != training_code:
                            w_fp.write(data + ' Err at ')
                            code_fail_cnt += 1
                            w_fp.write(str(index + len(sof) + (data_num) * 14 + 1))
                        else:
                            w_fp.write(data)
                        w_fp.write('\r')
                    if del_sof[dataBitW:dataBitW + len(eol)] != eol:
                        eol_fail_cnt += 1
                        w_fp.write('Err EOL:')
                        w_fp.write('\r')
                    w_fp.write(del_sof[dataBitW:dataBitW + len(eol)])
                    w_fp.write('\r')
                    rest_data_f2l = del_sof[dataBitW + len(eol) + invalid_data:]
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
                    if del_sol[dataBitW:dataBitW + len(eol)] != eol:
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
                    if del_sol[dataBitW:dataBitW + len(eol)] != eol:
                        w_fp.write('Err EOL:')
                        eol_fail_cnt += 1
                        w_fp.write('\r')
                    w_fp.write(del_sol[dataBitW:dataBitW + len(eol)])
                    w_fp.write('\r')
                    rest_data_f2l = del_sol[dataBitW + len(eol) + invalid_data:]
                    sum_index = sum_index + lineBitW + invalid_data
        w_fp.close()



if __name__ == '__main__':
    selected_file_list = [r'D:\Tool_RAW\160\340.bin', r'D:\Tool_RAW\160\341.bin',
                          r'D:\Tool_RAW\160\342.bin', r'D:\Tool_RAW\160\343.bin',
                          r'D:\Tool_RAW\160\344.bin', r'D:\Tool_RAW\160\345.bin',
                          r'D:\Tool_RAW\160\346.bin', r'D:\Tool_RAW\160\347.bin']
    CheckBinData_14bit_160A(selected_file_list)

