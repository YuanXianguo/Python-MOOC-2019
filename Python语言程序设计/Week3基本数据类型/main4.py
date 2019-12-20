n = eval(input())
if n % 2 != 0:
    for i in range(int((n + 1) / 2)):
        ch = int(2 * i + 1)
        print(('*'*ch).center(n,' '))
else:
    print("格式错误！")
