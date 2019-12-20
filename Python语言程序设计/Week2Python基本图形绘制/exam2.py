calorie = input()
if calorie[-3:] == 'cal':
   j = eval(calorie[:-3]) * 4.186
   print("{:.3f}j".format(j))
elif calorie[-1] == 'j':
    cal = eval(calorie[:-1]) / 4.186
    print("{:.3f}cal".format(cal))
else:
    print("格式错误！")
