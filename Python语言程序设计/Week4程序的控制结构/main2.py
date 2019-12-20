res = 0
for i in range(2,101):
    for n in range(2,i):
        if i % n == 0:
            break
    else:
        res += i
print(res)
