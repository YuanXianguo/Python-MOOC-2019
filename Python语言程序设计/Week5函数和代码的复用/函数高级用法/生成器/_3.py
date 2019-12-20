def test():
    for i in range(10):
        res = yield i
        print(res)

g = test()  # 生成一个生成器
print(g.send(None))  # 在调用生成器第一个值时，send()只能传递None
print(g.send('666'))
print(g.send('777'))

