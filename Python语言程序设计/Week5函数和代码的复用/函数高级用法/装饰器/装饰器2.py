# -*- coding:gbk -*-
'''示例2: 使用内嵌包装函数来确保每次新函数都被调用，
内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''


def deco(func):
    def _deco():
        print("before myfunc() called.")
        func()
        print("  after myfunc() called.")
        # 不需要返回func，实际上应返回原函数的返回值

    return _deco


@deco
def myfunc():
    print(" myfunc() called.")
    return 'ok'


myfunc()
myfunc()
