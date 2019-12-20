TempStr = input()
if TempStr[0] == 'C':
    F = eval(TempStr[1:]) * 1.8 + 32
    print("F{:.2f}".format(F))
elif TempStr[0] == 'F':
    C = (eval(TempStr[1:]) - 32) / 1.8
    print("C{:.2f}".format(C))
