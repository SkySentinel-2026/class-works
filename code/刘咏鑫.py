import turtle

t=turtle.Turtle()
t.pensize(4)
t.speed(4)
t.pencolor("green")

for i in range(3):
    t.forward(180)
    t.left(120)

t.penup()
t.goto(70,0)
t.pendown()
t.pencolor("brown")
for i in range(2):
    t.forward(40)
    t.right(90)
    t.forward(180)
    t.right(90)
    
turtle.done()
