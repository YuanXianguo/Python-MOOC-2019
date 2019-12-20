from functools import wraps

"""装饰器实际上就是一个函数，有两个特别之处：
1.参数是一个函数名（指针），即要执行的函数
2.返回值是一个函数名（指针），即经过包装后的函数，里面包括原要执行的函数和添加的功能"""

def decorator(func):
    @wraps(func)  # 保护原函数的属性
    def _decorator(*args, **kwargs):
        # *args表示任意多个位置参数（无名参数），它是一个tuple类型
        # **kwargs表示任意多个关系参数（关键字参数），它是一个dict类型
        print('装饰器开始：')
        res = func(*args, **kwargs)
        print('装饰器结束：')
        return res
    return _decorator


@decorator  # 等价于：demo=decorator(demo)
def demo(a, b, c=3):
    print('这是原要执行的函数')
    return (a + b) / c

demo(1 , 2)
print(demo.__name__)
print(demo(1, 2))
