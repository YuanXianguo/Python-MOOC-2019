dict = {}
dict['中国'] = '北京'
dict['美国'] = '华盛顿'
dict['美国'] = '纽约'
if 'c' in dict:
    print(True)
print(len(dict))
print(dict.keys())
dict.clear()
print(dict)
