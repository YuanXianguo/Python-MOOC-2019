import turtle

datas = [['blue',(-110,-25)], ['black',(0,-25)], ['red',(110,-25)],
             ['yellow',(-55,-75)], ['green',(55,-75)]]
for data in datas:
    turtle.pensize(5)
    turtle.color(data[0])
    turtle.penup()
    turtle.goto(data[1])
    turtle.pendown()
    turtle.circle(45)

turtle.done()
