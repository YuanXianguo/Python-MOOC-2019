def test():
    a = 10
    def test2():
        print(a)
    a = 20

    return test2

# print(test())
test()()


def test():
    funcs = []
    for i in range(3):
        def test2():
            print(i)
        funcs.append(test2)
    return funcs

for i in range(3):
    test()[i]()

def test():
    funcs = []
    for i in range(3):
        def test2(num):
            def inner():
                """inner函数和所引用的变量num整体又构成一个闭包"""
                print(num)
            return inner
        funcs.append(test2(i))
    return funcs

for i in range(3):
    test()[i]()
