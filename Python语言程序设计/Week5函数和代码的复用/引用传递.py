def change(num):
    """不可变数据类型的参数"""
    print(id(num))  # 打印num的地址
    num = 20  # 函数内改变参数会重新开辟地址
    print(id(num))   # 不能改变原件

b = 10
print(id(b))  # 打印b的地址
change(b)
print(b)

def changec(num):
    """可变数据类型的参数"""
    print(id(num))  # 打印num的地址
    num.append(66)
    print(id(num))

c = [1, 2, 3]
print(id(c))  # 打印b的地址
changec(c)
print(c)   # 可以改变原件

