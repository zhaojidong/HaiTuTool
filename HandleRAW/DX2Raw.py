# W = 5488;H = 4112
import numpy as np

def Try_Raw():
    gen_raw = r'D:\Try_Raw.raw'
    data = []
    low_8bit = '{:0>8}'.format(str(bin(123))[2:])
    int_data = int(low_8bit.strip('  '), 2)
    print(int_data)
    print(type(int_data))
    data.append(int_data)
    x = np.array(data, '>H')
    x.tofile(gen_raw)
    print('Finished')

def deal_dxRaw10():
    if 0:
        raw_file = r'D:\FrameID597_W5488_H4112Mipiraw10.raw'
        gen_raw = r'D:\Gen_Raw_DX.raw'
    else:
        raw_file = r'D:\Tool_RAW\DX_GrabFrame.txt'
        gen_raw = r'D:\Tool_RAW\Gen_Raw_HT.raw'
    read_raw = np.fromfile(raw_file, dtype=np.uint8)
    j = 3
    data = []
    print(len(read_raw))
    for i in range(len(read_raw)):
        if int((i + 1) % 5) != 0:
            cnt = int((i+1) / 5)
            low_2bit = '{:0>8}'.format(str(bin(read_raw[4 + 5 * cnt]))[2:])[j * 2:j * 2 + 2]
            if j != 0:
                j -= 1
            else:
                j = 3
            # j -= 1 if j != 0 else 3
            high_8bit = '{:0>8}'.format(str(bin(read_raw[i]))[2:])
            byte_2 = high_8bit + low_2bit + '000000'
            int_data = int(byte_2, 2)
            data.append(int_data)
    print(len(data))
    x = np.array(data, '>H')
    x.reshape(4112, 5488)
    x.tofile(gen_raw)
    print('Finished')

if __name__ == '__main__':
    deal_dxRaw10()
    # Try_Raw()