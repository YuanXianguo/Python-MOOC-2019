try:
    n = input('输入：')
    if n.isdigit():
        print('输入为整数')
    elif n.isalpha():
        print('输入为字母串')
    elif n.isalnum():
        print('输入为数字字母混合')
    elif '.' in n:
        s = n.index('.')
        n = n[:s] + n[s+1:]
        if n.isdigit():
            print('输入为浮点数')
        else:
            print('输入为混合')
    else:
        print('输入为混合')
except:
    print('输入为混合')

