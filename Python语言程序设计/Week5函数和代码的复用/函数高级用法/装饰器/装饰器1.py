# -*- coding:gbk -*-
'''ʾ��1: ʹ���﷨��@��װ�κ������൱�ڡ�myfunc = deco(myfunc)��
�������º���ֻ�ڵ�һ�α����ã���ԭ�����������һ��'''


def deco(func):
    print("before myfunc() called.")
    func()
    print("  after myfunc() called.")
    return func


@deco
def myfunc():
    print(" myfunc() called.")


myfunc()
myfunc()
