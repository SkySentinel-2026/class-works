import turtle
t=turtle.Turtle()
t.color('red')
t.pensize(1)
t.speed(0)
for n in range(360):
    for i in range(5):
        t.forward(150)
        t.right(72)
    t.right(1)
turtle.done()
    