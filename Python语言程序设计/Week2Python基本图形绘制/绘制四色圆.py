import turtle

turtle.bgcolor('black')
colors = ['red', 'yellow', 'blue', 'green']
for x in range(100):
    turtle.color(colors[x % 4])
    turtle.circle(x)
    turtle.left(91)
turtle.done()
