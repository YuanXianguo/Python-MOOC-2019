TempStr = input("请输入带单位的温度，我将帮你转换：")
if TempStr[-1] in ['f', 'F']:
    C = (eval(TempStr[:-1]) - 32) / 1.8
    print("转换后的温度为{:.2f}C".format(C))
elif TempStr[-1] in ['c', 'C']:
    F = eval(TempStr[:-1]) * 1.8 + 32
    print("转换后的温度为{:.2f}F".format(F))
else:
    print("输入格式错误！")


list =[1,3,4]
list[0]
list[1]
for i in list:
    print(i)
dict = {"beijing":"中国", "huashengdun":'美国'}
dict['beijing']
