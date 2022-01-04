import pandas as pd
import numpy as np
import matplotlib.pylab as plt 
plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


def occuptin_analysis():   
    user_information = 'u.user'

    occuption_count = {}
    for line in open(user_information):
        occuption = line.split('|')[3]
        occuption_count[occuption] = occuption_count.get(occuption,0) + 1


    sort_occuption_counts = sorted(occuption_count.items(),key=lambda k: k[1])
    # print(sort_occuption_counts)

    sort_occuption = {}
    for i in sort_occuption_counts: #将排序结果存回字典
        sort_occuption[i[0]] = i[1]
    print(sort_occuption)

    x4 = sort_occuption.keys()
    y4 = sort_occuption.values()

    plt.bar(x4,y4,color = 'blue',width = 0.8)
    plt.xticks(rotation = -60) #将x轴坐标旋转60度
    # plt.title("用户职业统计情况",fontsize=14)
    plt.xlabel("职业",fontsize=14)
    plt.ylabel("人数",fontsize=14)
    plt.show()

if __name__ == "__main__":
    occuptin_analysis()