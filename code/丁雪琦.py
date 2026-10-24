import turtle
t=turtle.Turtle()
t.pensize(3)
t.color("blue")
for j in range(10):
    for i in range(4):
        t.forward(80)
        t.left(90)
    t.left(36)
turtle.done()