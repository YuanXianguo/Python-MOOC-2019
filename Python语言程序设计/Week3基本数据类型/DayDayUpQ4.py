dayupA = 1.0
for i in range(365):
    dayupA *= 1 + 0.01
def DayUp(df):
    dayup = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup *= 1 - 0.01
        else:
            dayup *= 1 + df
    return dayup
dayfactor = 0.01
while DayUp(dayfactor) < dayupA:
    dayfactor += 0.001
print("{:.3f}".format(dayfactor))

