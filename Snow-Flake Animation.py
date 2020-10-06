from turtle import Screen, Turtle

def vshape():
    turtle.right(25)
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(50)
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(25)

def snowflakeArm():
    for _ in range(4):
        turtle.forward(30)
        vshape()

    turtle.backward(120)

def snowflake(angle, position):

    turtle.setheading(angle)
    turtle.penup()
    turtle.setposition(position)

    turtle.pendown()
    for _ in range(6):
        snowflakeArm()
        turtle.right(60)

angle = 0

def snowflakes():
    global angle

    turtle.clear()

    snowflake(angle, (0, 0))
    snowflake(angle, (350, 0))
    snowflake(angle, (-350, 0))
    snowflake(angle, (0, 350))
    snowflake(angle, (0, -350))

    screen.update()

    angle = (angle + 10) % 360

    screen.ontimer(snowflakes, 25)  # repeat 25 milliseconds from now

screen = Screen()
screen.tracer(False)

turtle = Turtle()
turtle.hideturtle()
turtle.pencolor('blue')
turtle.pensize(5)

snowflakes()

screen.exitonclick()