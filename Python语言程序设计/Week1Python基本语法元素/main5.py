Money = input()
if Money[:3] == 'RMB':
    USD = eval(Money[3:]) / 6.78
    print("USD{:.2f}".format(USD))
elif Money[:3] == 'USD':
    RMB = eval(Money[3:]) * 6.78
    print("RMB{:.2f}".format(RMB))
