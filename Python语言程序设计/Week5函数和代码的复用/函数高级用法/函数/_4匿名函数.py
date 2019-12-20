l = [{'name': 'a1', 'age': 20}, {'name': 'a2', 'age': 19}, {'name': 'a3', 'age': 18}]
def get_key(d):
    return d['name']

# print('以name排序：', sorted(l, key=get_key))


print('以name排序：', sorted(l, key=lambda l: l['name']))

