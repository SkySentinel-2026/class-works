import turtle

t = turtle.Turtle()
t.color("green","green")

t.begin_fill()
for i in range(4):
    t.pensize(9)
    t.forward(100)
    t.right(90)
t.end_fill()

turtle.done()