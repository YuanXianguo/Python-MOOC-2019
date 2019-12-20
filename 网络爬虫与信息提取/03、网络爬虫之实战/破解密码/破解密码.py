import itertools
import time

ls = list(map(str, list(range(10))))
n = 4
# 排列：n!/(n-m)!；列表，选取个数
my_list = list(itertools.permutations(ls, n))
# 组合：n!/(n-m)!/m!；列表，选取个数
my_list2 = list(itertools.combinations(ls, n))
# 重复组合；列表，选取个数（可重复）
my_list3 = list(itertools.product(ls, repeat=n))
print(len(my_list), '\n', len(my_list2), '\n', len(my_list3))
passwd = (''.join(i) for i in my_list3)  # 迭代器
while True:
    try:
        print(next(passwd))
        time.sleep(0.2)
    except:
        break
