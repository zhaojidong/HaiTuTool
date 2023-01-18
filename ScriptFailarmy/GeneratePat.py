
def GenPat_Write_Read():
    file_r = r'D:\Python\Project\Ref_Data\sjz.txt'
    file_w = r'D:\Python\Project\Ref_Data\ejz.txt'
    w_fp = open(file_w, 'w+')
    add_start = -1
    space_1 = " "
    space_n = space_1*10
    with open(file_r, 'r+') as r_fp:
        lines = r_fp.readlines()
        for line in lines:
            if line != " ":
                if 'h' in line:
                    Dh_line = line.replace('h', '')
                elif 'H' in line:
                    Dh_line = line.replace('H', '')
                else:
                    Dh_line = line
                if '\n' in Dh_line:
                    Dh_line = Dh_line.replace('\n', '')
                print(Dh_line)
                state_10 = int(Dh_line, 16)
                state_2 = '{:08b}'.format(state_10)
                otp = 0
                add_start += 1
                for i in range(len(state_2)):
                    if "0" in state_2[i]:
                        w_fp.write(str(space_n))
                        w_fp.write("> 1 ")
                        w_fp.write("L")
                        w_fp.write(";")
                    elif "1" in state_2[i]:
                        w_fp.write(str(space_n))
                        w_fp.write("> 1 ")
                        w_fp.write("H")
                        w_fp.write(";")
                    if otp == 0:
                        w_fp.write("	//Reg Add=")
                        w_fp.write(str(add_start))
                        w_fp.write("; Data=")
                        w_fp.write(str(line.strip("\n")))
                    w_fp.write("\n")
                    otp += 1
                w_fp.write(str(space_n))
                w_fp.write("> 1 L;	//Ack bit(Low)")
                w_fp.write("\n")

# ./rw_cmos.exe -bk 0 -ra 106 -w 0x04,0x00,0x80,0x00,0x80,0x00,0x00,0x01,0x00,0x01,0x80,0x01,0x80,0x01,0x00,0x02,0x00,0x02,0x80,0x02,0x80,0x02,0x00,0x03,0x00,0x03,0x80,0x03,0x80,0x03,0x0e,0x04
# ./rw_cmos.exe -bk 0 -ra 141 -w 0xfa
Sample_W = '> 0 1 W XX	X X	X X	X X	X X X X	X X	X X	X X X X	X X	X X	X X	X X	X X	X X	X X	X X	X0;'        # used to write add or reg
Sample_A = '> 1 1 0 XX	X X	X X	X X	X X X X	X X	X X	X X X X	X X	X X	X X	X X	X X	X X	X X	X X	X0;    //'  # used to append
Sample_R = ''
def GenPat_Write():
    file_r = r'D:\Python\Project\Ref_Data\sjz.txt'
    file_w = r'D:\Python\Project\Ref_Data\ejz.txt'
    w_fp = open(file_w, 'w+')
    valid_line = './rw_cmos.exe'
    w1 = Sample_W.split('W')[0]
    w3 = Sample_W.split('W')[1]
    with open(file_r, 'r+') as r_fp:
        lines = r_fp.readlines()
        for line in lines:
            if valid_line in line:
                exec_once_add = True
                emu = line.split(' ')
                reg_add = emu[4]
                reg_val = emu[6].split(',')
                print(reg_val)
                bin_data_reg = '{:08b}'.format(int(reg_add))
                for i in range(len(bin_data_reg)):  # write reg add to pattern
                    w_fp.write(w1)
                    w_fp.write(bin_data_reg[i])
                    w_fp.write(w3)
                    if exec_once_add:
                        w_fp.write('    // Reg Add=' + str(reg_add))
                        exec_once_add = False
                    w_fp.write('\r')
                for i in range(len(reg_val)):
                    exec_once_val = True
                    bin_data_val0 = '{:04b}'.format(int(reg_val[i].split('x')[1][0], 16))
                    bin_data_val1 = '{:04b}'.format(int(reg_val[i].split('x')[1][1], 16))
                    bin_data_val = bin_data_val0 + bin_data_val1
                    print(bin_data_val)
                    for j in range(len(bin_data_val)):
                        w_fp.write(w1)
                        w_fp.write(bin_data_val[j])
                        w_fp.write(w3)
                        if exec_once_val:
                            w_fp.write('    // Reg Val=' + str(reg_val[i].strip()))
                            exec_once_val = False
                        w_fp.write('\r')
            w_fp.write('\r' + Sample_A)
            w_fp.write('\r' + Sample_A + '\r\n')
        w_fp.close()









if __name__ == '__main__':
    GenPat_Write()
