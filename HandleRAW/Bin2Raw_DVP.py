import os
import numpy as np
import time
from multiprocessing import Process
from multiprocessing.pool import Pool
# import taichi as ti
# import cython

BinFiles_FVAL = r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_FVAL.bin'
BinFiles_LVAL = r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_LVAL.bin'
BinFiles_Ch = [ r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch0.bin',  r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch1.bin',
                r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch2.bin',  r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch3.bin',
                r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch4.bin',  r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch5.bin',
                r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch6.bin',  r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch7.bin',
                r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch8.bin',  r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch9.bin',
                r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch10.bin', r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch11.bin']
# BinFiles_LVAL = r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_LVAL.bin'
# BinFiles_FVAL = r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_FVAL.bin'
# BinFiles_Ch = [ r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch0.bin',  r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch1.bin',
#                 r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch2.bin',  r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch3.bin',
#                 r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch4.bin',  r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch5.bin',
#                 r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch6.bin',  r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch7.bin',
#                 r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch8.bin',  r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch9.bin',
#                 r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch10.bin', r'D:\Tool_RAW\Light_CI_1\0-0_TrainingCode_Ch11.bin']


# BinFiles_LVAL = r'D:\Tool_RAW\BlockGray_12_1\0-0_BlockGray_LVAL.bin'
# BinFiles_FVAL = r'D:\Tool_RAW\BlockGray_12_1\0-0_BlockGray_FVAL.bin'
# BinFiles_Ch = [ r'D:\Tool_RAW\BlockGray_12_1\0-0_BlockGray_Ch0.bin',  r'D:\Tool_RAW\BlockGray_12_1\0-0_BlockGray_Ch1.bin',
#                 r'D:\Tool_RAW\BlockGray_12_1\0-0_BlockGray_Ch2.bin',  r'D:\Tool_RAW\BlockGray_12_1\0-0_BlockGray_Ch3.bin',
#                 r'D:\Tool_RAW\BlockGray_12_1\0-0_BlockGray_Ch4.bin',  r'D:\Tool_RAW\BlockGray_12_1\0-0_BlockGray_Ch5.bin',
#                 r'D:\Tool_RAW\BlockGray_12_1\0-0_BlockGray_Ch6.bin',  r'D:\Tool_RAW\BlockGray_12_1\0-0_BlockGray_Ch7.bin',
#                 r'D:\Tool_RAW\BlockGray_12_1\0-0_BlockGray_Ch8.bin',  r'D:\Tool_RAW\BlockGray_12_1\0-0_BlockGray_Ch9.bin',
#                 r'D:\Tool_RAW\BlockGray_12_1\0-0_BlockGray_Ch10.bin', r'D:\Tool_RAW\BlockGray_12_1\0-0_BlockGray_Ch11.bin']
def DVP_12bit():
    #read FVAL
    print('Start...')
    gen_raw = r'D:\Tool_RAW\GenRaw_DVP.raw'
    binfile_FVAL = open(BinFiles_FVAL, 'rb')
    binfile_LVAL = open(BinFiles_LVAL, 'rb')
    size_fval = os.path.getsize(BinFiles_FVAL)  # 获得文件大小
    size_lval = os.path.getsize(BinFiles_LVAL)  # 获得文件大小
    lines_fval = ''
    # data = binfile_FVAL.read(size_fval)
    # lines_fval = bin(int(data, 16))[2:].zfill(size_fval * 2)
    T1 = time.time()
    for loop in range(size_fval):
        data = binfile_FVAL.read(1)  # 每次输出一个字节
        a = [hex(x) for x in data]
        s10 = int(a[0], 16)
        s2 = '{:08b}'.format(s10)
        lines_fval += s2
    fval_loc = lines_fval.find('10')
    print('fval_loc = ', fval_loc)
    lval_loc = 0
    lines_lval = ''
    # data = binfile_LVAL.read(size_fval)
    # lines_lval = bin(int(data, 16))[2:].zfill(size_fval * 2)
    for loop in range(size_lval):
        data = binfile_LVAL.read(1)  # 每次输出一个字节
        a = [hex(x) for x in data]
        s10 = int(a[0], 16)
        s2 = '{:08b}'.format(s10)
        lines_lval += s2
    lines_chs = []
    for ch in range(12):
        lines_ch = ''
        for loop in range(size_lval):
            f = open(BinFiles_Ch[ch], 'rb')
            data = f.read(1)
            a = [hex(x) for x in data]
            s10 = int(a[0], 16)
            s2 = '{:08b}'.format(s10)
            lines_ch += s2
        lines_chs.append(lines_ch)
        print('Finished ch' + str(ch))
    frame = []
    pixel = 0
    lines_lval_re = lines_lval[fval_loc + lval_loc:]
    lval_loc = lines_lval_re.find('01')
    print('lval_loc =', lval_loc)
    ch_loc = fval_loc + lval_loc + 1
    for high in range(1096):
        ch_loc_new = ch_loc + 2200 * high
        for i in range(1936):
            for ch in range(12):
                pixel |= (int(lines_chs[ch][ch_loc_new+i:ch_loc_new+i+1]) << ch)
            frame.append(pixel)
            pixel = 0
    x = np.array(frame, '>H')
    x.reshape(1936, 1096)
    x.tofile(gen_raw)
    T2 = time.time()
    print('程序运行时间:%smin' % ((T2 - T1)/60))
    print('Finished!')


def DVP_12bit_M2():
    #read FVAL
    print('Start...')
    gen_raw = r'D:\Tool_RAW\GenRaw_DVP_Light_CI_2.raw'
    binfile_FVAL = open(BinFiles_FVAL, 'rb')
    binfile_LVAL = open(BinFiles_LVAL, 'rb')
    size_fval = os.path.getsize(BinFiles_FVAL)  # 获得文件大小
    lines_fval = ''
    data = binfile_FVAL.read(size_fval)  # 每次输出一个字节
    a = [hex(x) for x in data]
    for i in range(len(a)):
        s10 = int(a[i], 16)
        s2 = '{:08b}'.format(s10)
        lines_fval += s2
    fval_loc = lines_fval.find('10')
    # fval_loc = 2274570
    print('fval_loc =', fval_loc)
    lines_lval = ''
    data = binfile_LVAL.read(size_fval)  # 每次输出一个字节
    a = [hex(x) for x in data]
    for i in range(len(a)):
        s10 = int(a[i], 16)
        s2 = '{:08b}'.format(s10)
        lines_lval += s2
    lval_loc_1st = lines_lval[fval_loc:].find('01')
    print('lval_loc_1st =', lval_loc_1st)
    lines_chs = []
    for ch in range(12):
        lines_ch = ''
        f = open(BinFiles_Ch[ch], 'rb')
        data = f.read(size_fval)
        a = [hex(x) for x in data]
        for i in range(len(a)):
            s10 = int(a[i], 16)
            s2 = '{:08b}'.format(s10)
            lines_ch += s2
        lines_chs.append(lines_ch)
        print('Finished ch' + str(ch))
    frame = []
    pixel = 0
    # ch_loc = 2274570+6800  # tc
    ch_loc = fval_loc + lval_loc_1st
    lval_loc_cnt = 0
    for high in range(1096):
        lines_lval_re = lines_lval[ch_loc + 1936*high + lval_loc_cnt:]
        lval_loc = lines_lval_re.find('011')+1
        lval_loc_cnt = lval_loc + lval_loc_cnt
        ch_loc_new = ch_loc + 1936*high + lval_loc_cnt
        for i in range(1936):
            for ch in range(12):
                pixel |= (int(lines_chs[ch][ch_loc_new+i:ch_loc_new+i+1]) << ch)
                # print(lines_chs[ch][ch_loc_new + i:ch_loc_new + i + 1], ch, ch_loc_new + i, 'pixel=', pixel)
            frame.append(pixel)
            pixel = 0
    x = np.array(frame, '>H')
    x.reshape(1936, 1096)
    x.tofile(gen_raw)
    print('Finished!')


def DVP_12bit_M3():
    #read FVAL
    print('Start...')
    gen_raw = r'D:\Tool_RAW\GenRaw_DVP_HighSpeed.raw'
    binfile_FVAL = open(BinFiles_FVAL, 'rb')
    binfile_LVAL = open(BinFiles_LVAL, 'rb')
    size_fval = os.path.getsize(BinFiles_FVAL)  # 获得文件大小
    lines_fval = ''
    T1 = time.time()
    data = binfile_FVAL.read(size_fval)  # 每次输出一个字节
    a = [hex(x) for x in data]
    for i in range(len(a)):
        s10 = int(a[i], 16)
        s2 = '{:08b}'.format(s10)
        lines_fval += s2
    fval_loc = lines_fval.find('10')
    print('fval_loc =', fval_loc)
    lines_lval = ''
    data = binfile_LVAL.read(size_fval)  # 每次输出一个字节
    a = [hex(x) for x in data]
    for i in range(len(a)):
        s10 = int(a[i], 16)
        s2 = '{:08b}'.format(s10)
        lines_lval += s2
    lval_loc_1st = lines_lval[fval_loc:].find('01')
    print('lval_loc_1st =', lval_loc_1st)
    lines_chs = []
    for ch in range(12):
        lines_ch = ''
        f = open(BinFiles_Ch[ch], 'rb')
        data = f.read(size_fval)
        a = [hex(x) for x in data]
        for i in range(len(a)):
            s10 = int(a[i], 16)
            s2 = '{:08b}'.format(s10)
            lines_ch += s2
        lines_chs.append(lines_ch)
        print('Finished ch' + str(ch))
    frame = []
    pixel = 0
    # ch_loc = 2274570+6800  # tc
    ch_loc = fval_loc + lval_loc_1st
    lval_loc_cnt = 0
    for high in range(1096):
        lines_lval_re = lines_lval[ch_loc + 1936*high + lval_loc_cnt:]
        lval_loc = lines_lval_re.find('011')+1
        lval_loc_cnt = lval_loc + lval_loc_cnt
        ch_loc_new = ch_loc + 1936*high + lval_loc_cnt
        for i in range(1936):
            for ch in range(12):
                pixel |= (int(lines_chs[ch][ch_loc_new+i:ch_loc_new+i+1]) << ch)
                # print(lines_chs[ch][ch_loc_new + i:ch_loc_new + i + 1], ch, ch_loc_new + i, 'pixel=', pixel)
            frame.append(pixel)
            pixel = 0
    x = np.array(frame, '>H')
    x.reshape(1936, 1096)
    x.tofile(gen_raw)
    T2 = time.time()
    print('程序运行时间:%smin' % ((T2 - T1)/60))
    print('Finished!')


def FVAL_LVAL():
    binfile_FVAL = open(BinFiles_FVAL, 'rb')
    binfile_LVAL = open(BinFiles_LVAL, 'rb')
    size_fval = os.path.getsize(BinFiles_FVAL)  # 获得文件大小
    lines_fval = ''
    T1 = time.time()
    data = binfile_FVAL.read(size_fval)  # 每次输出一个字节
    a = [hex(x) for x in data]
    for i in range(len(a)):
        s10 = int(a[i], 16)
        s2 = '{:08b}'.format(s10)
        lines_fval += s2
    fval_loc = lines_fval.find('10')
    print('fval_loc =', fval_loc)
    lines_lval = ''
    data = binfile_LVAL.read(size_fval)  # 每次输出一个字节
    a = [hex(x) for x in data]
    for i in range(len(a)):
        s10 = int(a[i], 16)
        s2 = '{:08b}'.format(s10)
        lines_lval += s2
    lval_loc_1st = lines_lval[fval_loc:].find('01')
    print('lval_loc_1st =', lval_loc_1st)
    return fval_loc, lval_loc_1st, lines_lval

lines_chs_mul = []
def Channel_Data(ch):
    size_fval = os.path.getsize(BinFiles_FVAL)  # 获得文件大小
    lines_ch = ''
    f = open(BinFiles_Ch[ch], 'rb')
    data = f.read(size_fval)
    a = [hex(x) for x in data]
    for i in range(len(a)):
        s10 = int(a[i], 16)
        s2 = '{:08b}'.format(s10)
        lines_ch += s2
    # lines_chs_mul.append(lines_ch)
    print('Finished ch' + str(ch))
    return lines_ch


def Fun_last():
    print('Start...')
    gen_raw = r'D:\Tool_RAW\GenRaw_DVP_HighSpeed.raw'
    fval_loc, lval_loc_1st, lines_lval = FVAL_LVAL()
    process_list = []
    for ch in range(12):  #开启12个子进程执行fun1函数
        p = Process(target=Channel_Data, args=(ch,)) #实例化进程对象
        p.start()
        process_list.append(p)
    for ch in process_list:
        p.join()
    frame = []
    pixel = 0
    # ch_loc = 2274570+6800  # tc
    ch_loc = fval_loc + lval_loc_1st
    lval_loc_cnt = 0
    print(len(lines_chs_mul))
    for high in range(1096):
        lines_lval_re = lines_lval[ch_loc + 1936*high + lval_loc_cnt:]
        lval_loc = lines_lval_re.find('011')+1
        lval_loc_cnt = lval_loc + lval_loc_cnt
        ch_loc_new = ch_loc + 1936*high + lval_loc_cnt
        for i in range(1936):
            for ch in range(12):
                pixel |= (int(lines_chs_mul[ch][ch_loc_new+i:ch_loc_new+i+1]) << ch)
                # print(lines_chs[ch][ch_loc_new + i:ch_loc_new + i + 1], ch, ch_loc_new + i, 'pixel=', pixel)
            frame.append(pixel)
            pixel = 0
    x = np.array(frame, '>H')
    x.reshape(1936, 1096)
    x.tofile(gen_raw)
    print('Finished!')

def fun_mulP():
    print('Start...')
    gen_raw = r'D:\Tool_RAW\GenRaw_DVP_HighSpeed.raw'
    BinFiles_Ch_mul = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    fval_loc, lval_loc_1st, lines_lval = FVAL_LVAL()
    pool = Pool(processes=12)
    lines_chs_mul.append(pool.map(Channel_Data, BinFiles_Ch_mul))
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
    frame = []
    pixel = 0
    # ch_loc = 2274570+6800  # tc
    ch_loc = fval_loc + lval_loc_1st
    lval_loc_cnt = 0
    print(len(lines_chs_mul))
    for high in range(1096):
        lines_lval_re = lines_lval[ch_loc + 1936*high + lval_loc_cnt:]
        lval_loc = lines_lval_re.find('011')+1
        lval_loc_cnt = lval_loc + lval_loc_cnt
        ch_loc_new = ch_loc + 1936*high + lval_loc_cnt
        for i in range(1936):
            for ch in range(12):
                pixel |= (int(lines_chs_mul[ch][ch_loc_new+i:ch_loc_new+i+1]) << ch)
                # print(lines_chs[ch][ch_loc_new + i:ch_loc_new + i + 1], ch, ch_loc_new + i, 'pixel=', pixel)
            frame.append(pixel)
            pixel = 0
    x = np.array(frame, '>H')
    x.reshape(1936, 1096)
    x.tofile(gen_raw)
    print('Finished!')

def lab():
    t = 0
    t1 = ['123', '456']
    print(t1[1][1:2])
    t |= int(t1[0][1:2]) << 12
    print(t)

if __name__ == "__main__":
    T1 = time.time()
    # lab()
    # DVP_12bit()
    DVP_12bit_M2()
    # DVP_12bit_M3()
    # Fun_last()
    # fun_mulP()
    T2 = time.time()
    print('程序运行时间:%smin' % ((T2 - T1)/60))


