import turtle as t


def yi(width, height, color):
    t.pencolor(color)
    t.seth(0)

    t.pu()
    t.goto(-width / 4 - 1.5 * width, height / 20 + 0.5 * height)
    t.pd()
    t.fd(width / 3)


def qian(width, height, color):
    t.seth(0)
    t.pencolor(color)

    t.pu()
    t.goto(width / 12 + 0.5 * width, height / 4 + 0.5 * height)
    t.pd()
    t.left(-160)
    t.circle(-width / 3, 35)

    t.pu()
    t.goto(-width / 6 + 0.5 * width, height / 10 + 0.5 * height)
    t.pd()
    t.seth(0)
    t.fd(width / 3)

    t.pu()
    t.goto(0 + 0.5 * width, height / 5 + 0.5 * height)
    t.pd()
    t.seth(-90)
    t.fd(width / 3)


def nuo(width, height, x, y, color):
    t.pencolor(color)

    t.pu()
    t.goto(-width / 4 + x * width, height / 3 + y * height)
    t.pd()
    t.seth(-45)
    t.fd(width / 16)

    t.pu()
    t.goto(-width / 3.5 + x * width, height / 4.5 + y * height)
    t.pd()
    t.seth(0)
    t.fd(width / 12)
    t.seth(-90)
    t.fd(width / 3.5)
    t.seth(45)
    t.fd(width / 12)

    # 一横
    t.pu()
    t.goto(-width / 8 + x * width, height / 4 + y * height)
    t.pd()
    t.seth(0)
    t.fd(width / 4)

    t.pu()
    t.goto(-width / 19 + x * width, height / 3 + y * height)
    t.pd()
    t.seth(-80)
    t.fd(width / 10)

    t.pu()
    t.goto(width / 19 + x * width, height / 3 + y * height)
    t.pd()
    t.seth(-100)
    t.fd(width / 10)

    # 二横
    t.pu()
    t.goto(-width / 8 + x * width, height / 6.5 + y * height)
    t.pd()
    t.seth(0)
    t.fd(width / 4)

    # 撇
    t.pu()
    t.goto(+x * width, height / 5 + y * height)
    t.pd()
    t.seth(-120)
    t.fd(width / 4)
    kou(width, height, x, y)


def kou(width, height, x=1, y=1):
    # 口
    t.pu()
    t.goto(-width / 30 + x * width, height / 14 + y * height)
    t.pd()
    t.seth(-90)
    t.fd(width / 8)

    t.pu()
    t.goto(-width / 30 + x * width, height / 14 + y * height)
    t.pd()
    t.seth(0)
    t.fd(width / 7)

    t.pu()
    t.goto(-width / 30 + width / 7 + x * width, height / 14 + y * height)
    t.pd()
    t.seth(-90)
    t.fd(width / 8)

    t.pu()
    t.goto(-width / 30 + x * width, height / 14 - height / 8 + y * height)
    t.pd()
    t.seth(0)
    t.fd(width / 7)


def jin(width, height, color):
    t.pencolor(color)

    # 撇
    t.pu()
    t.goto(width / 100 + 1.5 * width, height / 3 + 0.5 * height)
    t.pd()
    t.seth(-115)
    t.circle(-width / 2, 40)

    # 捺
    t.pu()
    t.goto(0 + 1.5 * width, height / 3.8 + 0.5 * height)
    t.pd()
    t.left(105)
    t.circle(width / 2, 30)

    t.pu()
    t.goto(-width / 10 + 1.5 * width, height / 8 + 0.5 * height)
    t.pd()
    t.seth(0)
    t.fd(width / 5)

    t.pu()
    t.goto(-width / 8 + 1.5 * width, 0 + 0.5 * height)
    t.pd()
    t.seth(0)
    t.fd(width / 4)

    t.pu()
    t.goto(0 + 1.5 * width, height / 8 + 0.5 * height)
    t.pd()
    t.seth(-90)
    t.fd(width / 4)

    t.pu()
    t.goto(-width / 10 + 1.5 * width, -height / 30 + 0.5 * height)
    t.pd()
    t.seth(-45)
    t.fd(width / 16)

    t.pu()
    t.goto(width / 10 + 1.5 * width, -height / 30 + 0.5 * height)
    t.pd()
    t.seth(-135)
    t.fd(width / 16)

    t.pu()
    t.goto(-width / 6 + 1.5 * width, -height / 8 + 0.5 * height)
    t.pd()
    t.seth(0)
    t.fd(width / 3)


def yu(width, height, color):
    t.pencolor(color)
    t.seth(0)

    # 横
    t.pu()
    t.goto(-width / 6 - 1.5 * width, height / 4 - 0.5 * height)
    t.pd()
    t.fd(width / 4)

    t.pu()
    t.seth(-100)
    t.goto(-width / 6 - 1.5 * width, height / 3 - 0.5 * height)
    t.pd()
    t.fd(width / 5)
    t.left(100)
    t.fd(width / 4)
    t.right(90)
    t.circle(-width, 15)
    t.seth(135)
    t.fd(width / 12)

    t.pu()
    t.goto(-width / 4 - 1.5 * width, height / 40 - 0.5 * height)
    t.seth(0)
    t.pd()
    t.fd(width / 4)


def tong(width, height, color):
    t.pencolor(color)
    t.seth(-90)
    t.pu()
    t.goto(-width / 6 + 0.5 * width, height / 3 - 0.5 * height)
    t.pd()
    t.fd(width / 2.5)

    # 横
    t.seth(0)
    t.pu()
    t.goto(-width / 6 + 0.5 * width, height / 3 - 0.5 * height)
    t.pd()
    t.fd(width / 3)
    t.right(90)
    t.fd(width / 2.4)
    t.seth(135)
    t.fd(width / 12)

    # 小横
    t.seth(0)
    t.pu()
    t.goto(-width / 8 + 0.5 * width, height / 3.8 - 0.5 * height)
    t.pd()
    t.fd(width / 4.5)

    # 口
    kou(1.1*width, height, 0.41, -0.4)


def xing(width, height, color):
    t.pencolor(color)
    # 撇
    t.pu()
    t.goto(-width / 20 + 1.5 * width, height / 2.4 - 0.5 * height)
    t.pd()
    t.seth(-115)
    t.circle(-width / 2, 28)

    # 撇
    t.pu()
    t.goto(-width / 20 + 1.5 * width, height / 3.5 - 0.5 * height)
    t.pd()
    t.seth(-115)
    t.circle(-width / 2, 28)

    # 竖
    t.pu()
    t.goto(-width / 10 + 1.5 * width, height / 5 - 0.5 * height)
    t.pd()
    t.seth(-90)
    t.fd(width/4)

    # 横
    t.pu()
    t.goto(width / 100 + 1.5 * width, height / 3 - 0.5 * height)
    t.pd()
    t.seth(0)
    t.fd(width/5)


    # 二横
    t.pu()
    t.goto(-width / 100 + 1.5 * width, height / 4.4 - 0.5 * height)
    t.pd()
    t.fd(width/4)

    # 竖钩
    t.pu()
    t.goto(width / 6 + 1.5 * width, height / 4.4 - 0.5 * height)
    t.seth(-90)
    t.pd()
    t.fd(width/3.5)
    t.seth(135)
    t.fd(width/12)


def heart(width, n):
    t.color('red', 'pink')
    t.seth(0)

    t.pu()
    t.goto(-2.5 * width, 0)
    t.pd()
    t.begin_fill()
    t.left(140)
    t.forward(112 / n)
    draw_circle(n)
    t.left(120)
    draw_circle(n)
    t.forward(112 / n)
    t.end_fill()


def draw_circle(n):
    t.speed(1000)
    for i in range(200):
        t.right(1)
        t.forward(1 / n)
    t.speed(2)


def main(width, height, x, y):
    t.setup(width, height, x, y)
    t.speed(2)
    t.pensize(4)

    width, height = 100, 100
    n = 3.5
    yi(width, height, "red")
    nuo(width, height, -0.5, 0.4, "red")
    qian(width, height, "red")
    jin(width, height, "red")
    yu(width, height, "red")
    nuo(width, height, -0.5, -0.5, "red")
    tong(width, height, "red")
    xing(width, height, "red")

    heart(width, n)
    heart(-width, n)

    t.hideturtle()
    t.done()


if __name__ == '__main__':
    width, height, x, y = 650, 200, 630, 400
    main(width, height, x, y)
