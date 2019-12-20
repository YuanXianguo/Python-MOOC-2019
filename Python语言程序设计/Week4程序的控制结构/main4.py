for num in range(1000,10000):
    res = 0
    a = 3
    for i in str(num):
        res += pow(int(i),4)
        a -= 1
    if res == num:
        print(num)
