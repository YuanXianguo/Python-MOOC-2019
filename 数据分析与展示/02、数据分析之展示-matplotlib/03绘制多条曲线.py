import matplotlib.pyplot as plt
import numpy as np

def no_format():
    a = np.arange(10)
    plt.plot(a, a*1.5, a, a*2.5, a, a*3.5, a, a*4.5)
    plt.show()

def format_string():
    a = np.arange(10)
    plt.plot(a, a * 1.5, 'go-', a, a * 2.5, 'rx',  a, a * 3.5, 'b*', a, a * 4.5, '-.')
    plt.show()

format_string()
