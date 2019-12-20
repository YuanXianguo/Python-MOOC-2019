l = [{'name': 'a1', 'age': 20}, {'name': 'a2', 'age': 19}, {'name': 'a3', 'age': 18}]
def get_key(d):
    return d['name']

def get_key1(d):
    return d['age']

print('以name排序：', sorted(l, key=get_key))
print('以age排序：', sorted(l, key=get_key1))

def test(a, b, my_test):
    print(my_test(a, b))

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

test(4, 5, sum)
test(4, 5, sub)
