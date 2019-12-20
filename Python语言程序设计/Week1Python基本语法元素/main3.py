value = eval(input())

list= []
for i in range(6):
    num = value ** i
    list.append(str(num))

print(' '.join(tuple(list)))
