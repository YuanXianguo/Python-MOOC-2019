def get_fun(flag):
    def sum(a, b):
        return a + b

    def sub(a, b):
        return a - b

    if flag == '+':
        return sum
    elif flag == '-':
        return sub

res = get_fun('+')
print(res, type(res))
print(res(1, 2))
