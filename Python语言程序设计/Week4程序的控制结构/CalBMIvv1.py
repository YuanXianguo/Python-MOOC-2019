lenth, weight = eval(input("请输入身高（m）和体重（公斤）[逗号隔开]："))
BMI = weight / (lenth ** 2)
print("BMI数值为：{:.2f}".format(BMI))
ch1 = '根据国际BMI您'
ch2 = '根据国内BMI您'
if BMI < 18.5:
    print(ch1 + "偏瘦；" + ch2 + "偏瘦。")
elif BMI <= 24:
    print(ch1 + "正常；" + ch2 + "正常。")
elif BMI <= 25:
    print(ch1 + "偏胖；" + ch2 + "正常。")
elif BMI <= 28:
    print(ch1 + "偏胖；" + ch2 + "偏胖。")
elif BMI < 30:
    print(ch1 + "偏胖；" + ch2 + '肥胖。')
else:
    print(ch1 + "肥胖；" + ch2 + "肥胖。")
