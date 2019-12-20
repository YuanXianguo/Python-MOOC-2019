import turtle
# 设置窗体大小及位置，后两个参数可选
turtle.setup(650, 350, 200, 200)
turtle.penup() #抬起画笔
turtle.fd(-250) #fd海龟正方向
turtle.pendown() #落下画笔
turtle.pensize(25) #海龟腰围
turtle.pencolor("purple") #画笔颜色或（0.63，0.13，0.94）
turtle.seth(-40) #改变海龟行进方向但不行进（绝对角度），right、left相对角度
for i in range(4):
    turtle.circle(40, 80) #根据半径40绘制80角度的弧形
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()
