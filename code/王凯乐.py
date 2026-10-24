import turtle
t =turtle.Turtle()
t.speed(0)
t.penup()
t.goto(0,-25)
t.pendown()
t.pencolor("purple")
t.pensize(5)
t.circle(25)
t.pensize(5)
t.penup()
t.goto(0,0)
t.setheading(0)
t.pendown()
for angle in range(10):
    t.pencolor("red")
    for i in range(5):
        t.forward(80)
        t.right(72)
    t.right(36)
t.penup()
for i in range(12):
    t.goto(0,0)
    t.setheading(i*30)
    t.pendown()
    t.pencolor("gold")
    for i in range(3):
        t.forward(20)
        t.right(120)
    t.penup    
t.hideturtle()
turtle.done()
    
