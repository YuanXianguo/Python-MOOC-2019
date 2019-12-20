def rightK(n):
    list = []
    if n == 1:
        list.append('()')
        print(list)
    else:
        list = rightK(n-1)
        for char in list:
            for i in char:
                char.insert(char.index(i),'(')
                for m in char[i:]:
                    char.insert(m,')')
def main():
    n = eval(input())
    rightK(n)

main()
