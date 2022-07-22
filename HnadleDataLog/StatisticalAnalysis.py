"""
This py uesd to statistical and analysis the log data which were selected on tree widget
1.Yeild
"""
import numpy as np
import pandas as pd
from numpy import mean
from matplotlib import pyplot as plt
import matplotlib
import HnadleDataLog.glovar as glv
from itertools import chain
gs = glv.global_str()
gss = glv.global_status_str()
gm = glv.global_math()


class SA:
    def __init__(self, marked_df, parent=None):  # parent=None,so the HaiTu_UI is the topmost window
        # super(self).__init__(None)  # the super().__init__() excutes the constructor fo father, then we can use the property of father
        self.sa_mk_df = marked_df
        self.init()

    def init(self):
        self.R_Yield()
        self.handle_EverySignalData()

    # calculate the yield
    def R_Yield(self):
        fail_counts = 0
        DUT_PF = [1]*glv.file_count
        shift_count = glv.log_row
        for index, row in self.sa_mk_df.iterrows():
            if index == glv.log_row:  # only loop the first dut's log, because it was marked
                break
            if self.sa_mk_df.at[index, str(gs.CheckStatus)] == str(gss.Checked) and sum(DUT_PF) != 0:
                for dut in range(glv.file_count):
                    if self.sa_mk_df.at[index + dut * shift_count, str(gs.Result)] == str(gss.FAIL):
                        fail_counts += 1
                        DUT_PF[dut] = 0
                    if sum(DUT_PF) == 0:
                        break
        glv.R_yield = round((sum(DUT_PF)/len(DUT_PF)) * 100, 2)


    # plto the waveform of checked value, include ave value, min, max, median, stdev
    def plot_single_itme(self):
        DUT_Val = [0]*glv.file_count
        DUT_PF = [1]*glv.file_count
        shift_count = glv.log_row
        for index, row in self.sa_mk_df.iterrows():
            if index == glv.log_row:  # only loop the first dut's log, because it was marked
                break
            if self.sa_mk_df.at[index, str(gs.CheckStatus)] == str(gss.Checked) and sum(DUT_PF) != 0:
                for dut in range(glv.file_count):
                    DUT_Val[dut] = self.sa_mk_df.at[index + dut * shift_count, str(gs.Measure)]
                break
        DUT_Val, _, _ = glv.extractUnit7UnifyValue(DUT_Val)
        glv.DUT_Val = DUT_Val
        # Average
        glv.DUT_math[gm.Average] = np.mean(DUT_Val).round(3)
        # Median
        glv.DUT_math[gm.Median] = np.median(DUT_Val).round(3)
        # Variance
        glv.DUT_math[gm.Variance] = np.var(DUT_Val).round(3)
        # Standard deviation
        glv.DUT_math[gm.St_dev] = np.std(DUT_Val).round(3)
        # Max
        glv.DUT_math[gm.Max] = round(max(DUT_Val), 3)
        # Min
        glv.DUT_math[gm.Min] = round(min(DUT_Val), 3)


    def handle_EverySignalData(self):
        global unit
        SA_df_copy = glv.marked_df.copy()
        SA_df_index_dict = {}
        SA_df_data_dict = {}
        new_col = glv.SA_pd_col
        for chip in glv.Chip_List:
            SA_df_index_dict[chip] = []
            SA_df_data_dict[chip] = []
            if chip not in new_col:
                new_col.append(chip)
        SA_df = pd.DataFrame(columns=new_col)
        Chip_ID = ''
        ChipID_List = []
        Chip_Cnt = 0
        SA_df_index = 0
        SA_df_index_list = []
        Pass_cnt = 0
        for index, row in SA_df_copy.iterrows():
            if SA_df_copy.at[index, str(gs.NO)] == glv.start_label:
                Chip_ID = SA_df_copy.at[index, str(gs.CheckStatus)]
                SA_df_index = 0
            if SA_df_copy.at[index, str(gs.CheckStatus)] == gss.Checked:
                SA_df.at[SA_df_index, str(gs.TestName)] = SA_df_copy.at[index, str(gs.TestName)]
                SA_df.at[SA_df_index, str(gs.Signal)] = SA_df_copy.at[index, str(gs.Signal)]
                SA_df.at[SA_df_index, str(gs.LowLimit)] = SA_df_copy.at[index, str(gs.LowLimit)]
                SA_df.at[SA_df_index, str(gs.HighLimit)] = SA_df_copy.at[index, str(gs.HighLimit)]
                SA_df.at[SA_df_index, str(gs.CheckStatus)] = SA_df_copy.at[index, str(gs.CheckStatus)]
                for k, v in SA_df_index_dict.items():
                    if k == Chip_ID:
                        if SA_df_index not in v:
                            SA_df.at[SA_df_index, Chip_ID] = []
                SA_df_index_dict[Chip_ID].append(SA_df_index)
                ChipID_List.append(Chip_ID)
                SA_df_index_list.append(SA_df_index)
                Chip_Cnt += 1
                SA_df.at[SA_df_index, Chip_ID].append(SA_df_copy.at[index, str(gs.Measure)])
                if SA_df_copy.at[index, str(gs.Result)] == str(gss.PASS):
                    if SA_df.at[SA_df_index, str(gs.PASS_Count)] != SA_df.at[SA_df_index, str(gs.PASS_Count)]:
                        # Pass_cnt = 0
                        SA_df.at[SA_df_index, str(gs.PASS_Count)] = str(1)
                    else:
                        SA_df.at[SA_df_index, str(gs.PASS_Count)] = str(int(SA_df.at[SA_df_index, str(gs.PASS_Count)]) + 1)
                        # Pass_cnt = int(SA_df.at[SA_df_index, str(gs.PASS_Count)])
                    # Pass_cnt += 1
                    # SA_df.at[SA_df_index, str(gs.PASS_Count)] = str(Pass_cnt)
                SA_df_index += 1
        for index, row in SA_df.iterrows():
            value_cnt = []
            all_val_index = []
            for chip in glv.Chip_List:
                value_cnt.append(len(SA_df.at[index, chip]))
                all_val_index.append(SA_df.at[index, chip])
            all_data = list(chain.from_iterable(all_val_index))
            all_data.append(SA_df.at[index, str(gs.LowLimit)])
            all_data.append(SA_df.at[index, str(gs.HighLimit)])
            DUT_Val, error_flag, unit = glv.extractUnit7UnifyValue(all_data)
            SA_df.at[index, str(gs.LowLimit)] = DUT_Val[-2]
            SA_df.at[index, str(gs.HighLimit)] = DUT_Val[-1]
            SA_df.at[index, str(gs.Unit)] = unit
            del DUT_Val[-2:]
            cnt_loop = 0
            for chip in glv.Chip_List:
                SA_df.at[index, chip] = DUT_Val[sum(value_cnt[0:cnt_loop]):sum(value_cnt[0:cnt_loop+1])]
                cnt_loop += 1
        SA_df.to_csv(glv.final_path)
        glv.WaveForm_pd = SA_df.copy()
        self.CalData(SA_df)


    def CalData(self, data):
        index_cnt = 0
        data_list = []
        TName_list = []
        glv.Math_dict = {}
        if glv.test_count > 100:
            sigma = 3
        else:
            sigma = 4
        for index, row in data.iterrows():
            Math_list = []
            data_list.append([])
            self.unit = data.at[index, str(gs.Unit)]
            usl = data.at[index, str(gs.HighLimit)]
            lsl = data.at[index, str(gs.LowLimit)]
            TName_list.append(data.at[index, str(gs.TestName)] + '@' + data.at[index, str(gs.Signal)])
            TName = data.at[index, str(gs.TestName)] + '@' + data.at[index, str(gs.Signal)]
            Pass_cnt = data.at[index, str(gs.PASS_Count)]
            for dut in range(glv.file_count):
                data_list[index_cnt].extend(data.at[index, str(glv.File_NO[dut])])
            index_cnt += 1
            u = (usl + lsl) / 2
            X = np.mean(data_list).round(3)
            Math_list.append(X)
            Math_list.append(np.median(data_list).round(3))
            # Math_list.append(np.var(data_lit).round(3))
            stdev = np.std(data_list).round(3)  # stdev is σ
            Math_list.append(stdev)
            # Cp = (USL - LSL) / 6σ
            Cp = round((usl - lsl) / (2*sigma*stdev), 3)
            Math_list.append(Cp)
            # Cpk = T/6σ- |M-μ|/3σ
            Cpk = round(min(usl-u, u-lsl)/(sigma*stdev), 3)
            Math_list.append(Cpk)
            # Yeild = Pass_cnt / glv.test_cnt
            Yeild = round(100*(int(Pass_cnt)/int(glv.test_count)), 3)
            Math_list.append(Yeild)
            glv.Math_dict[TName] = Math_list






