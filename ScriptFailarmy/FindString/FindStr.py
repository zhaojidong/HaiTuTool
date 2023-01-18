

if __name__ == '__main__':
    file = r'D:\HaiTu\HT50A\CP\Datalog\123.txt'
    loop_cnt = 0
    append_name = ''
    finder = False
    with open(file, 'r+') as r_fp:
        lines = r_fp.readlines()
        print(lines)

    pi_string = ''
    for line in lines:
        pi_string +=line.rstrip()

    print(pi_string)
    print(len(pi_string))
    r_fp.close()
    with open(file, 'w+') as r_fp:
        r_fp.write(pi_string)
