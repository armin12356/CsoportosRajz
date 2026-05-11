import turtle

turtle.bgcolor("lightblue")
turtle.speed(0)
turtle.color("brown")
turtle.begin_fill()
i=0
while i<2:
    turtle.forward(100)
    turtle.left(-90)
    turtle.forward(300)
    turtle.left(-90)
    i+=1
turtle.fillcolor("brown")
turtle.end_fill()

turtle.done()