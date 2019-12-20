import matplotlib.pyplot as plt

def one_list():
    """plt.plot()当只有一个参数时，作为Y轴参数绘制，X轴以索引绘制"""
    plt.plot([3, 1, 4, 5, 2])
    plt.ylabel('grade')
    # plt.savefig()将输出图像存储为文件，默认为PNG格式，可以通过dpi修改输出质量
    plt.savefig('text', dpi=600)
    plt.show()

def two_list():
    """plt.plot(x,y)当有两个以上参数时，按照X轴和Y轴顺序绘制数据点"""
    plt.plot([0, 2, 4, 6, 8], [3, 1, 4, 5, 2])
    plt.ylabel('grade')
    # plt.axis()设置横纵坐标尺度，分别为X轴起始坐标，Y轴起始坐标
    plt.axis([-1, 10, 0, 6])
    plt.show()

if __name__ == '__main__':
    one_list()
    two_list()
