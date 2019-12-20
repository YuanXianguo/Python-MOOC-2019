list1 = ['()']
list2 = []
for char in list1:
    for i in char:
        list2.append(i)
        for n in range(len(list2)+1):
            list2.insert(int(n),'(')
            for m in range(n+1,len(list2)+1):
                list.insert(int(m),')')
print(list2)
