num = input()
if eval(num) == 1:
    print(True)
else:
    while len(num) > 1:
        res = 0
        for i in num:
            res += pow(int(i),2)
        if res != 1:
            num = str(res)
        else:
            print(True)
            break
    else:
        print(False)
