# -*- coding:gbk -*-
'''ʾ��2: ʹ����Ƕ��װ������ȷ��ÿ���º����������ã�
��Ƕ��װ�������βκͷ���ֵ��ԭ������ͬ��װ�κ���������Ƕ��װ��������'''


def deco(func):
    def _deco():
        print("before myfunc() called.")
        func()
        print("  after myfunc() called.")
        # ����Ҫ����func��ʵ����Ӧ����ԭ�����ķ���ֵ

    return _deco


@deco
def myfunc():
    print(" myfunc() called.")
    return 'ok'


myfunc()
myfunc()
