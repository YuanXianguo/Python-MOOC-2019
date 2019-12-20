try:
    num = eval(input())
    if 90 <= num <= 100:
        res = 'A'
    elif 80 <= num < 90:
        res = 'B'
    elif 70 <= num < 80:
        res = 'C'
    elif 60 <= num < 70:
        res = 'D'
    elif 0 <= num < 60:
        res = 'E'
    print("输入成绩属于{}级别".format(res))
    if res != 'E':
        print("祝贺你通过考试！")
except:
    print("输入数据有误！")
finally:
    print("好好学习，天天向上！")
