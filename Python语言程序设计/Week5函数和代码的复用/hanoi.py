count = 0
def hanoi(n, aa, ca, ba):
    global count
    if n == 1:
        print("{}:{}->{}".format(1, aa, ca))
        count += 1
    else:
        hanoi(n-1, aa, ba, ca)
        print("{}:{}->{}".format(n, aa, ca))
        count += 1
        hanoi(n-1, ba, ca, aa)

def main(n):
    hanoi(n,'A', 'C', 'B')
    print('count:{}'.format(count))

main(2)
