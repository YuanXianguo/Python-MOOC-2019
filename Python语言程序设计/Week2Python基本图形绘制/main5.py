TempStr = input()
if TempStr[-1] == 'm':
    In = eval(TempStr[:-1]) * 39.37
    print("{:.3f}in".format(In))

elif TempStr[-2:] == 'in':
    m = eval(TempStr[:-2]) / 39.37
    print("{:.3f}m".format(m))

else:
    print("输入格式错误！")
