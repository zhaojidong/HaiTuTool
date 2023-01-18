import os, shutil, math

path_come = r'D:\Tool_RAW\de'
path_from = r'D:\Tool_RAW\Here'

DataSource = r'D:\Tool_RAW\SortFile\SourceFile\FT'
DataGo = r'D:\Tool_RAW\SortFile\FT\50A'

folderName_data = '20221103'
lotID_label = 'lot_id:'
waferID_label = 'sublot_id:'
DataGo_Path = DataGo + '\\' + folderName_data

efw_ft1 = ['L_0', 'L_5', 'L_50', 'L_80', 'L_400', 'L_5']
wafer_no = ['11', '12', '13']
lot_no = 'HS0156700A'
dieCntOnWafer = 82
waferStartNO = 11
def SortFile4Nes():
    lotID = ''
    waferID = ''
    label_cnt = 0
    Datalog_Folder_C = DataSource + '\\' + 'Datalog'
    Rawdata_Folder_C = DataSource + '\\' + 'Rawdata'
    files = os.listdir(Datalog_Folder_C)
    if not os.path.exists(DataGo_Path):
        os.mkdir(DataGo_Path)
    for file in range(len(files)):
        deviceID = files[file].split('_')[0]
        file_path = Datalog_Folder_C + '\\' + files[file]
        with open(file_path, 'r') as fp:
            lines = fp.readline()
            while lines:
                if lotID_label == lines.split(' ')[0]:
                    lotID = lines.split(' ')[1]
                    label_cnt += 1
                if waferID_label == lines.split(' ')[0]:
                    # waferID = lines.split(' ')[1]
                    waferID = waferStartNO + math.floor(int(deviceID) / dieCntOnWafer)
                    label_cnt += 1
                if label_cnt == 2:
                    # ChipFolderName = lotID.strip() + '_' + waferID.strip() + '_' + deviceID.strip()
                    ChipFolderName = lot_no + '_#' + str(waferID) + '_' + deviceID.strip()
                    label_cnt = 0
                    new_folder = DataGo_Path + '\\' + ChipFolderName
                    if not os.path.exists(new_folder):
                        os.mkdir(new_folder)
                        new_folder_raw = new_folder + '\\' + 'RawData'
                        if not os.path.exists(new_folder_raw):
                            os.mkdir(new_folder_raw)
                    # copy datalog to new folder
                    shutil.copy(file_path, new_folder)
                    # copy Raw to new folder
                    s_RFC = Rawdata_Folder_C + '\\' + deviceID
                    if os.path.exists(s_RFC):
                        s_folder_name = os.listdir(s_RFC)
                        for go_path in range(len(s_folder_name)):
                            raw_c = Rawdata_Folder_C + '\\' + deviceID
                            All_Efws = os.listdir(raw_c)
                            for efw in range(len(All_Efws)):
                                raw_go_s = new_folder_raw + '\\' + efw_ft1[efw]
                                if not os.path.exists(raw_go_s):
                                    os.mkdir(raw_go_s)
                                raw_c_s = raw_c + '\\' + All_Efws[efw]
                                for root, _, fnames in os.walk(raw_c_s):
                                    for fname in fnames:  # sorted函数把遍历的文件按文件名排序
                                        src_file = os.path.join(root, fname)
                                        shutil.copy(src_file, raw_go_s)  # 完成文件拷贝
                lines = fp.readline()
        print('Finished ' + str(deviceID))

def SortFile():
    path = os.listdir(path_come)
    for path_loop in range(len(path)):
        all_t_file = []
        new_f_name = []
        son_folder = path_come + '\\' + path[path_loop]
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


def DeleteFolder(path_from):
    shutil.rmtree(path_from)
    os.mkdir(path_from)


def ftp2Nes():
    pass






if __name__ == '__main__':
    DeleteFolder(DataGo)
    SortFile4Nes()