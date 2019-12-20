def test():
    for i in range(10):
        yield i

g = test()  # 生成一个生成器
print(g)
print(next(g))
print(next(g))
print(g.__next__())
