import turtle
t = turtle.Turtle()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.penup()
t.goto(0,100)
t.pendown()
t.goto(50,150)
t.goto(100,100)
t.goto(0,100)
turtle.done()