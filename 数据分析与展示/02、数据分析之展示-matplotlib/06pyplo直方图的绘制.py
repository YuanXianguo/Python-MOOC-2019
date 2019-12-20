import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
loc, scale = 100, 20  # 均值和标准差
a = np.random.normal(loc, scale, size=100)

# 数组，直方的个数，概率/个数，类型，颜色，比例
plt.hist(a, 20, normed=1, histtype='stepfilled', facecolor='b', alpha=0.75)
plt.title('Histogram')
plt.show()
