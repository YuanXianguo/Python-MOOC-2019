i = 0
j = 0
yes = int(input())
num = input()
while num.lower() != 'stop':
    i += 1
    right = int(num)
    if right >= yes:
        j += 1
    num = input()
if i == 0:
    print("合格率为100.00%")
else:
    print("合格率为{:.2f}%".format(j/i*100))
