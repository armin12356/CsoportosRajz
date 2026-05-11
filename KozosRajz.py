import turtle
turtle.speed(0)
turtle.color("green")
turtle.begin_fill()
i=60
while i<120:

    turtle.circle(60)
    turtle.left(i)
    turtle.circle(60)
    turtle.right(i+60)
    turtle.circle(60)
    i+=60
turtle.fillcolor("green")
turtle.end_fill()
turtle.done()


#fa lombja