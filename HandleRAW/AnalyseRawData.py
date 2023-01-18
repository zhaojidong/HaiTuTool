import numpy as np
import HandleRAW.glovar as glv
import itertools


def handle_raw(file_path, raw_file_list):
    np.set_printoptions(precision=3)
    rows = 2064  # image row is V:2064     2064*2672 = 5515008
    cols = 2672  # image column is H:2672
    channels = 1  # image channel, the gray is 1
    slice_start = 32
    rows = int(glv.Height)
    cols = int(glv.Width)
    HeadBit = int(glv.HeadBit)
    PixBit = int(glv.PixBit)
    slice_end = rows * cols
    Frame_count = len(raw_file_list)  # frame count is the count of .raw files
    RGB_Result_list = []
    raw_sum = np.zeros((glv.Ver_pixel, glv.Hoz_pixel), dtype=np.uint64)  # be careful the data overflow
    frame_list = []
    raw_median_list = [[0 for col in range(len(raw_file_list))] for row in range(glv.Ver_pixel * glv.Hoz_pixel)]
    for file_loop in range(len(raw_file_list)):
        raw_file = file_path + '\\' + raw_file_list[file_loop]
        single_frame = np.fromfile(raw_file, dtype='>u2')  # big endian, u2(uint16, 2byte)
        # the ADC is 14 bits, but the raw data has been dealt, so it is not need to right shift(divide 4)
        single_frame = np.reshape(single_frame[HeadBit:],
                                  [rows, cols])  # do not need to shift the bin data, it is high zero padding
        # choose the partial area
        choose_pixels = single_frame[(glv.AREA[0]):(glv.AREA[2]), (glv.AREA[1]):(glv.AREA[3])]
        # raw_sum is the sum of 32 frame
        raw_sum = raw_sum + choose_pixels
        frame_list.append(np.mean(choose_pixels))
        if file_loop == 0:
            first_raw = choose_pixels
        ###################################################################
        # use two dimensional list([[32 data, because 32 frame]every pixel for single frame ]) to note the every pixel value
        ###################################################################
        xy_axis = 0
        for x, y in itertools.product(glv.x_axis, glv.y_axis):
            raw_median_list[xy_axis][file_loop] = choose_pixels[x, y]
            xy_axis += 1
    frame_list = frame_list
    # self.RGB_RAW_AVE = raw_sum / Frame_count
    # self.raw_median_list2 = raw_median_list
    # print(self.raw_median_list2)
    # print(self.RGB_RAW_AVE)
    ###################################################################
    # loop again calculation numpy -- raw median value  -- time
    ###################################################################
    allFrame_singlePixel_median = []
    for xy_axis in range(glv.Ver_pixel * glv.Hoz_pixel):
        allFrame_singlePixel_median.append(np.median(raw_median_list[xy_axis]))
    raw_median = np.reshape(allFrame_singlePixel_median, [glv.Ver_pixel, glv.Hoz_pixel])

    ###-------------------------------------------------------------------###
    # CALCULATE: <<<<<<<<<<DIV R G B>>>>>>>>>>
    # base on raw_median(the median of all frames) calculate R G B median
    ###-------------------------------------------------------------------###
    GB_median_list_single = []
    B_median_list_single = []
    R_median_list_single = []
    GR_median_list_single = []
    for x, y in itertools.product(glv.x_axis_half, glv.y_axis_half):
        GB_median_list_single.append(raw_median[2 * x + 0, 2 * y + 0])
        B_median_list_single.append(raw_median[2 * x + 0, 2 * y + 1])
        R_median_list_single.append(raw_median[2 * x + 1, 2 * y + 0])
        GR_median_list_single.append(raw_median[2 * x + 1, 2 * y + 1])
    GB_median = np.median(GB_median_list_single)
    B_median = np.median(B_median_list_single)
    R_median = np.median(R_median_list_single)
    GR_median = np.median(GR_median_list_single)
    RGB_Result_list.extend([GB_median, B_median, R_median, GR_median])
    ###################################################################
    # calculation numpy -- raw average -- time
    ###################################################################
    RGB_RAW_AVE = raw_sum / Frame_count
    ###-------------------------------------------------------------------###
    # CALCULATE: <<<<<<<<<<DIV R G B>>>>>>>>>>
    # calculation numpy -- raw average for every pixel()
    # GB  B
    # R   GR
    ###-------------------------------------------------------------------###
    GB_sum = 0
    B_sum = 0
    R_sum = 0
    GR_sum = 0
    # **_sum is the sum value of every color(GR GB R B)
    for x, y in itertools.product(glv.x_axis_half, glv.y_axis_half):
        GB_sum = GB_sum + RGB_RAW_AVE[2 * x + 0, 2 * y + 0]
        B_sum = B_sum + RGB_RAW_AVE[2 * x + 0, 2 * y + 1]
        R_sum = R_sum + RGB_RAW_AVE[2 * x + 1, 2 * y + 0]
        GR_sum = GR_sum + RGB_RAW_AVE[2 * x + 1, 2 * y + 1]
    GB_ave = GB_sum / glv.RGB_Count_SUM
    B_ave = B_sum / glv.RGB_Count_SUM
    R_ave = R_sum / glv.RGB_Count_SUM
    GR_ave = GR_sum / glv.RGB_Count_SUM
    RGB_Result_list.extend([GB_ave, B_ave, R_ave, GR_ave])
    ###################################################################
    # calculation numpy -- raw stdev -- time
    ###################################################################
    GB_stdev_list_single = []
    B_stdev_list_single = []
    R_stdev_list_single = []
    GR_stdev_list_single = []
    for x, y in itertools.product(glv.x_axis_half, glv.y_axis_half):
        GB_stdev_list_single.append(RGB_RAW_AVE[2 * x + 0, 2 * y + 0])
        B_stdev_list_single.append(RGB_RAW_AVE[2 * x + 0, 2 * y + 1])
        R_stdev_list_single.append(RGB_RAW_AVE[2 * x + 1, 2 * y + 0])
        GR_stdev_list_single.append(RGB_RAW_AVE[2 * x + 1, 2 * y + 1])
    GB_stdev = np.std(GB_stdev_list_single)
    B_stdev = np.std(B_stdev_list_single)
    R_stdev = np.std(R_stdev_list_single)
    GR_stdev = np.std(GR_stdev_list_single)
    RGB_Result_list.extend([GB_stdev, B_stdev, R_stdev, GR_stdev])

    display_ave_flag = True
    display_stdev_flag = True
    plot_wave_flag = True
    return RGB_Result_list