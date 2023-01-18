
import os
filePath = r'D:\Tool_RAW\pat\pat'
file_w = r'D:\Tool_RAW\pat\write.txt'
fp = open(file_w, 'w+')
for i,j,k in os.walk(filePath):
    print(k)
for i in range(len(k)):
    fp.write(str(k[i]))
    fp.write('\r')