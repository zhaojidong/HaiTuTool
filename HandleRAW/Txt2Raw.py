import os, time
import numpy as np


sof = '11111111111111000000000000000000000000000010101011000000'
sol = '11111111111111000000000000000000000000000010000000000000'
eol = '11111111111111000000000000000000000000000010011101000000'
eof = '11111111111111000000000000000000000000000010110110000000'

Pixel_File = []

def Txt2Raw(selected_file_list):
    print('TXT to RAW')
    # file = r'D:\HaiTu\HT50A\CP\Datalog\0_data.txt'
    # one_line = r'D:\HaiTu\HT50A\CP\Datalog\one_line.txt'
    # w_fp = open(file, 'w')
    # w_ol = open(one_line, 'w')
    training_code = '00011100001111'  # 070f
    # training_code = '11111111111111'  # 3fff
    gen_raw = r'D:\Python\Project\Ref_Data\gen2raw.raw'
    r_fp = open(gen_raw, 'w+')
    pixel_np = np.zeros(shape=(2480, 2072))
    data_ana = '_ana'
    dataBitW = 310*14
    lineBitW = len(sol) + dataBitW + len(eol)
    bin_file = ''
    new_file = ''
    for i in range(len(selected_file_list)):
        with open(selected_file_list[i], 'r+') as r_fp:
            lines = r_fp.readlines()
        file_name = os.path.basename(selected_file_list[i])
        file_path = os.path.dirname(selected_file_list[i])
        print(file_path)
        file_info = file_name.split('.')
        print(file_info)
        new_file = file_path + '\\' + file_info[0] + data_ana + '.' + file_info[1]
        Pixel_File.append(new_file)
        bin_file = file_path + '\\' + file_info[0] + data_ana + '.bin'
        raw_file = file_path + '\\' + 'Raw' + '.raw'
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
                    #w_fp.write(pi_string[index:index+len(sof)])
                    #w_fp.write('\r')
                    del_sof = pi_string[index + len(sof):]
                    for data_num in range(310):
                        data = del_sof[data_num*14:14*(data_num+1)]
                        w_fp.write(data)
                        w_fp.write('\r')
                    #w_fp.write(del_sof[dataBitW:dataBitW+len(eol)])
                    #w_fp.write('\r')
                    rest_data_f2l = del_sof[dataBitW+len(eol):]
                    sum_index = index + len(sof) + dataBitW + len(eol)
            if 0 < V < 2072:
                if sol in rest_data_f2l:
                    index = rest_data_f2l.find(sol)
                    #w_fp.write(rest_data_f2l[index:index+len(sol)])
                    #w_fp.write('\r')
                    del_sol = rest_data_f2l[index + len(sol):]
                    for data_num in range(310):
                        data = del_sol[data_num * 14:14 * (data_num + 1)]
                        w_fp.write(data)
                        w_fp.write('\r')
                    #w_fp.write(del_sol[dataBitW:dataBitW + len(eol)])
                    #w_fp.write('\r')
                    rest_data_f2l = del_sol[dataBitW + len(eol):]
                    sum_index = sum_index + lineBitW + index
        w_fp.close()
        print('Finished Transfer to Txt of 14bit.')

        # b_fp = open(bin_file, 'ab+')
        # with open(new_file, 'r+') as sec_txt:
        #     lines = sec_txt.readlines()
        #     for line in lines:
        #         for bitNum in range(len(line)-1):
        #             str2int = int(line[bitNum])
        #             bin_data = str2int.to_bytes(1, 'big')
        #             b_fp.write(bin_data)
        #     b_fp.close()

    for f_cnt in range(len(Pixel_File)):
        with open(Pixel_File[f_cnt], 'r+') as PF:
            lines = PF.readlines()
    #         for y in 2071:
    #             for x in 309:
    #                 pixel_np[8*x+f_cnt, y] = lines[310*y+x]
    # #r_fp.write(pixel_np)
    # pixel_np.tofile(raw_file)
    # print('All Finished')
    print('Finished')
def Pixel2Raw():
    T1 = time.time()
    Pixel_File = [r'D:\Python\Project\Ref_Data\toraw\00_ana.txt', r'D:\Python\Project\Ref_Data\toraw\10_ana.txt',
                  r'D:\Python\Project\Ref_Data\toraw\20_ana.txt', r'D:\Python\Project\Ref_Data\toraw\30_ana.txt',
                  r'D:\Python\Project\Ref_Data\toraw\40_ana.txt', r'D:\Python\Project\Ref_Data\toraw\50_ana.txt',
                  r'D:\Python\Project\Ref_Data\toraw\60_ana.txt', r'D:\Python\Project\Ref_Data\toraw\70_ana.txt']
    print(Pixel_File)
    gen_raw = r'D:\Python\Project\Ref_Data\toraw\gen2raw.raw'
    rawtxt = r'D:\Python\Project\Ref_Data\toraw\rawtxt.txt'
    r_fp = open(gen_raw, 'w+')
    t_fp = open(rawtxt, 'w+')
    pixel_np = np.zeros(shape=(2480, 2072))
    for f_cnt in range(len(Pixel_File)):
        with open(Pixel_File[f_cnt], 'r+') as PF:
            lines = PF.readlines()
            for y in range(2071):
                for x in range(309):
                    print(lines[310*y+x])
                    pixel_np[8*x+f_cnt, y] = lines[310*y+x]
                    print(pixel_np[8*x+f_cnt, y])

    print(str(pixel_np[0, 0]))
    pixel_np.astype(np.uint16)
    pixel_np.tofile(gen_raw)
    pixel_np.tofile(rawtxt)
    # t_fp.write(str(pixel_np))
    print('Finished')
    T2 = time.time()
    print('Take time = ' + str((T2-T1).__round__(3)) + 's')

def Pixel2Raw2():
    T1 = time.time()
    Pixel_File = [r'D:\Python\Project\Ref_Data\toraw\00_ana.txt', r'D:\Python\Project\Ref_Data\toraw\10_ana.txt',
                  r'D:\Python\Project\Ref_Data\toraw\20_ana.txt', r'D:\Python\Project\Ref_Data\toraw\30_ana.txt',
                  r'D:\Python\Project\Ref_Data\toraw\40_ana.txt', r'D:\Python\Project\Ref_Data\toraw\50_ana.txt',
                  r'D:\Python\Project\Ref_Data\toraw\60_ana.txt', r'D:\Python\Project\Ref_Data\toraw\70_ana.txt']
    print(Pixel_File)
    gen_raw = r'D:\Python\Project\Ref_Data\toraw\gen2raw.raw'
    rawtxt = r'D:\Python\Project\Ref_Data\toraw\rawtxt.txt'
    r_fp = open(gen_raw, 'w+')
    t_fp = open(rawtxt, 'w+')
    pixel_np = np.zeros(shape=(2480, 2072))

    for y in range(2071):
        for x in range(309):
            for f_cnt in range(len(Pixel_File)):
                with open(Pixel_File[f_cnt], 'r+') as PF:
                    lines = PF.readlines()
                    r_fp.write(lines[8*x+310*y])
                    #pixel_np[8*x+f_cnt, y] = lines[310*y+x]
        r_fp.write('\n')
    r_fp.close()
    # pixel_np.tofile(gen_raw)
    # print(pixel_np)
    # pixel_np.tofile(rawtxt)
    # t_fp.write(str(pixel_np))
    print('Finished')
    T2 = time.time()
    print('Take time = ' + str((T2-T1).__round__(3)) + 's')





# if __name__ == '__main__':
    # Bin2Raw()




