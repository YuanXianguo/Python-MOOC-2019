try:
    n = input('输入：')
    if n.isalpha():
        print('字母')
    elif isinstance(eval(n), int):
        print('int')
    elif isinstance(eval(n), float):
        print('float')
except:
    print('输入为混合')
