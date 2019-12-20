dayA = 1.0
dayB = 1.0
dayfactor1 = 0.01
for i in range(365):
    dayA *= (1 + dayfactor1)
for dayfactor2 in range(1000):
    for i in range(365):
        if i % 7 in [6, 0]:
            dayB *= 1 - dayfactor1
        else:
            dayB *= 1 + dayfactor2/1000
    if dayB > dayA:
        break
print(dayfactor2)
