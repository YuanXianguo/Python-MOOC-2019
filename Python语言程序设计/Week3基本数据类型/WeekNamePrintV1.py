weekStr = "星期一星期二星期三星期四星期五星期六星期日"
weekID = eval(input("请输入数字（1-7）："))
pos = (weekID - 1) * 3
weekDay = weekStr[pos : pos+3]
print(weekDay)
