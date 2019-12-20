import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def rc_params():
    matplotlib.rcParams['font.family'] = 'SimHei'
    matplotlib.rcParams['font.size'] = 20
    a = np.arange(0.0, 5.0, 0.02)
    plt.xlabel('横轴：时间')
    plt.ylabel('纵轴：振幅')
    plt.plot(a, np.cos(2*np.pi*a), 'r--')
    plt.show()

def font_properties():
    a = np.arange(0.0, 5.0, 0.02)
    plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=20)
    plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=20)
    plt.plot(a, np.cos(2*np.pi*a), 'r--')
    plt.show()

# rc_params()
font_properties()
