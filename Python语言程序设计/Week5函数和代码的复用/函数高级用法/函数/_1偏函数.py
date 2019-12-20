from functools import partial

def test(a, b, c):
    print(a + b + c)

new_test = partial(test, c=5)

new_test(1, 4)
