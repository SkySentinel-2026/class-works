import turtle
t = turtle.Turtle()
t.color("purple")
t.pensize(6)
for i in range(4):
    t.forward(150)
    t.right(90)

t.left(60)
t.forward(150)
t.right(120)
t.forward(150)
t.right(120)
t.forward(150)

t.penup()
t.goto(100, -150)
t.pendown()
for i in range(4):
    t.forward(50)
    t.right(90)

t.penup()
t.goto(115, -60)
t.pendown()
for i in range(4):
    t.forward(20)
    t.right(90)

turtle.done()
