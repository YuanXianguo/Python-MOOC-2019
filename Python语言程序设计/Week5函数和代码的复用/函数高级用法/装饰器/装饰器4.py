def decorator(char):
    def _decorator(func):
        def inner(*args):
            print(char * 30)
            res = func(*args)
            return res
        return inner
    return _decorator

@decorator('*')
def sum(a, b):
    return a + b

print(sum(1, 2))
