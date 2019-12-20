ch = input()
for i in ch:
    if i == ' ':
        reschr = ' '
    elif ord(i) > ord('w'):
        resnum = ord(i) - 23
        reschr = chr(resnum)
    else:
        resnum = ord(i) + 3
        reschr = chr(resnum)
    print(reschr, end='')
