def args(*args):
    """*args任意多个位置参数，元组类型"""
    print(args, type(args))  # 装包
    print(*args)  # 拆包

def kwargs(**kwargs):
    """任意多个关系参数，字典类型"""
    print(kwargs, type(kwargs))  # 装包
    my_sum(**kwargs)  # 拆包

def my_sum(a, b):
    print(a, b)

args(1, 2)
kwargs(a=1, b=2)

