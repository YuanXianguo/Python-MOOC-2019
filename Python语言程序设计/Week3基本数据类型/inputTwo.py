temp_1 = input()
temp_2 = input()
if 'm' in temp_1:
    if 'm' in temp_2:
        print('mm')
    elif 'n' in temp_2:
        print('mn')
    else:
        print('输入二格式错误！')
elif 'n' in temp_1:
    if 'm' in temp_2:
        print('nm')
    elif 'n' in temp_2:
        print('nn')
    else:
        print("输入二格式错误！")
else:
    print("输入一格式错误！")
