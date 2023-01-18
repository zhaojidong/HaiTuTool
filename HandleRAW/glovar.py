import os

x = 1
display_file = ''
rows = 2064  # image row is V:2064     2064*2672 = 5515008
cols = 2672  # image column is H:2672
image_path = ''
P_image = ''
P_file = ''
P_html = ''
P_excel = ''
rememberPath = ''
Width = ''
Height = ''
HeadBit = ''
PixBit = ''

AREA = [500, 500, 1500, 1500]
Ver_pixel = AREA[2] - AREA[0]
Hoz_pixel = AREA[3] - AREA[1]
x_axis = list(range(Ver_pixel))
y_axis = list(range(Hoz_pixel))
x_axis_half = list(range(Ver_pixel // 2))
y_axis_half = list(range(Hoz_pixel // 2))
RGB_Count_SUM = (Ver_pixel * Hoz_pixel)//4

class row_info:
    def __init__(self):
        self.Width = str()
        self.Height = str()
        self.Pixel_Bit = str()
        self.Head_Bit = str()

        self.setValue('Width', 'Height', 'Pixel_Bit', 'Head_Bit')

    def setValue(self, Width, Height, Pixel_Bit, Head_Bit):
        self.Width = Width
        self.Height = Height
        self.Pixel_Bit = Pixel_Bit
        self.Head_Bit = Head_Bit



def creatFolder(path,f_folder1,s_folder1,s_folder2,s_folder3,s_folder4):
    f_pf1 = path + '\\' + f_folder1
    s_pf1 = f_pf1 + '\\' + s_folder1
    s_pf2 = f_pf1 + '\\' + s_folder2
    s_pf3 = f_pf1 + '\\' + s_folder3
    s_pf4 = f_pf1 + '\\' + s_folder4
    if os.path.exists(f_pf1):
        if os.path.exists(s_pf1):
            print(s_folder1+' has existed')
        else:
            os.makedirs(s_pf1)
        if os.path.exists(s_pf2):
            print(s_folder2+' has existed')
        else:
            os.makedirs(s_pf2)
        if os.path.exists(s_pf3):
            print(s_folder3+' has existed')
        else:
            os.makedirs(s_pf3)
        if os.path.exists(s_pf4):
            print(s_folder4+' has existed')
        else:
            os.makedirs(s_pf4)
    else:
        os.makedirs(f_pf1)
        os.makedirs(s_pf1)
        os.makedirs(s_pf2)
        os.makedirs(s_pf3)
        os.makedirs(s_pf4)
    return s_pf1, s_pf2, s_pf3, s_pf4