import matplotlib
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt


# 将字符串转换成数字列表
def convert(str_data):
    # s = str_data.replace('[', '').replace(']', '').replace('\n', '').split(' ')
    s = re.findall('(-?[0-9]\d*\.?\d*e?[+-]?\d*)', str_data)
    ls = []
    for i in s:
        if i == '':
            pass
        else:
            i = float(i)
            ls.append(i)
    return ls


# 生成最终的字典列表以用于数据分析
def gen_ls(path):
    dic_ls = []
    data = pd.read_csv(path, header=None)
    num = data.count()[0]
    # 7表示7元素一循环
    for m in np.arange(0, num, 7):
        sub_dic = {}
        sub_dic['start_frame'] = int(data.iloc[m][1])
        sub_dic['end_frame'] = int(data.iloc[m + 1][1])
        sub_dic['label'] = data.iloc[m + 2][1]
        sub_dic['world_x'] = convert(data.iloc[m + 3][1])
        sub_dic['world_y'] = convert(data.iloc[m + 4][1])
        sub_dic['velocity'] = convert(data.iloc[m + 5][1])
        sub_dic['yaw'] = convert(data.iloc[m + 6][1])
        dic_ls.append(sub_dic)
    return dic_ls


def main():
    path = 'C5-trajectories.csv'
    dic_ls = gen_ls(path)
    fig = plt.figure()
    for i in dic_ls:
        fps = 30
        t = np.arange(i['start_frame'], i['end_frame'] + 2) / fps
        t = t / 60
        s = np.sqrt(np.square(i['world_x']), np.square(i['world_y']))
        v = i['velocity']
        norm = matplotlib.colors.Normalize(vmin=0, vmax=29)
        plt.scatter(t, s, marker='.', s=2, c=v, cmap='jet_r', norm=norm)
    plt.clim(0, 29)
    plt.colorbar()
    # plt.axis('equal')
    plt.xlim((0, 30))
    plt.show()


if __name__ == '__main__':
    main()
