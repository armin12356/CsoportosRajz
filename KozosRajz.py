import turtle


turtle.bgcolor("lightblue")

turtle.color("brown")
turtle.begin_fill()
i = 0
while i < 2:
    turtle.forward(100)
    turtle.left(-90)
    turtle.forward(300)
    turtle.left(-90)
    i += 1
turtle.fillcolor("brown")
turtle.end_fill()




turtle.color("green")
turtle.begin_fill()
turtle.penup()
turtle.forward(50)
turtle.pendown()
a=60
while a<120:

    turtle.circle(60)
    turtle.left(a)
    turtle.circle(60)
    turtle.right(a+60)
    turtle.circle(60)
    a+=60
turtle.fillcolor("green")
turtle.end_fill()
turtle.done()
