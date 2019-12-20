try:
    num = 0
    n = eval(input())
    if n > 0:
        def fact(n):
            if n == 1:
                res = 1
            else:
                res = n * fact(n-1)
            return res
        for i in range(1,n+1):
            num += fact(i)
        print(num)
    else:
        print("输入有误，请输入正整数")
except:
    print("输入有误，请输入正整数")
