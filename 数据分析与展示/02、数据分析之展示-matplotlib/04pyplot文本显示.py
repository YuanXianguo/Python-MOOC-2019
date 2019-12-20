import numpy as np
import matplotlib.pyplot as plt

def text_show():
    a = np.arange(0.0, 5.0, 0.02)
    plt.plot(a, np.cos(2*np.pi*a), 'r--')

    plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=15, color='green')
    plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=15)
    plt.title(r'正弦波实例 $y=cos(2\pi x)$', fontproperties='SimHei', fontsize=25)
    plt.text(2, 1, r'$\mu=100$', fontsize=15)  # 在(2,1)处增加文本
    # 设置带箭头的注解：字符串，箭头位置，文本位置，箭头属性；shrink,箭头两端空隙
    plt.annotate(r'$\mu=100$', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict
                                        (facecolor='black', shrink=0.1, width=2))

    plt.axis([-1, 6, -2, 2])  # 设置每个坐标轴的取值范围
    plt.tick_params(axis='both', labelsize=14)  # 设置刻度的样式
    plt.grid(True)  # 设置显示表格
    plt.show()

text_show()
