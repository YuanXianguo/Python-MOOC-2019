n = input()
num = 0
fact = 1
if n.isdigit():
    n = eval(n)
    if isinstance(n,int) and n > 0:
        for i in range(1, n + 1):
            for m in (1, i):
                fact *= m
            num += fact
        print(num)
    else:
        print("输入有误，请输入正整数")
else:
    print("输入有误，请输入正整数")
