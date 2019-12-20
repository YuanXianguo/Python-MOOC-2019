day = 1.0
dayup = 1.0
daydown = 1.0
n = eval(input())
if n < 0 or n > 100:
    print("输出错误！")
else:
    dayfac = n / 1000
    for i in range(365):
        dayup  *= (day + dayfac)
        daydown  *= (day - dayfac)
daydif = round(dayup / daydown)
print("{:.2f},{:.2f},{}".format(dayup, daydown, daydif))
