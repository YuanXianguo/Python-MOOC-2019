def getNum():
    nums = []
    iNumstr = input("请输入数字（回车退出）：")
    while iNumstr != '':
        nums.append(eval(iNumstr))
        iNumstr = input("请输入数字（回车退出）：")
    return nums

def mean(numbers):
    s = 0.0
    for num in numbers:
        s += num
    return s / len(numbers)

def dev(numbers, mean):
    sdev = 0.0
    for num in numbers:
        sdev += (num - mean) ** 2
    return pow(sdev / (len(numbers) -1), 0.5)

def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size / 2 == 0:
        med = (numbers[size // 2] + numbers[size //2 - 1])/ 2
    else:
        med = numbers[size // 2]
    return med

def main():
    n = getNum()
    m = mean(n)
    print("平均值：{}，方差：{}，中位数：{}。"
          .format(m, dev(n, m), median(n)))

main()
