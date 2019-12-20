lenth, weight = eval(input("请输入身高（m）和体重（公斤）[逗号隔开]："))
BMI = weight / (lenth ** 2)
print("BMI数值为：{:.2f}".format(BMI))
who, nat = "", ""
if BMI < 18.5:
    who, nat = "偏瘦",  "偏瘦"
elif BMI <= 24:
    who, nat = "正常",  "正常"
elif BMI <= 25:
    who, nat = "偏胖",  "正常"
elif BMI <= 28:
    who, nat = "偏胖",  "偏胖"
elif BMI < 30:
    who, nat = "偏胖",  '肥胖'
else:
    who, nat = "肥胖",  "肥胖"
print("根据国际BMI数值您{}；根据国内BMI数值您{}".format(who, nat))
