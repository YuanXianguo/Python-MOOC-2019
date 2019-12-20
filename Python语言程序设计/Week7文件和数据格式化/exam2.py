list = eval(input())
def colum(n,count):
    count = 0
    if n ==0:
        count =0
    else:
        for i in range(len(list)):
            if list[i][0] >= list[n][0]:
                count +=1
    return list[n][count]

