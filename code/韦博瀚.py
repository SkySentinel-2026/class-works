import turtle
t = turtle.Turtle()
t.color("red")
t.pensize(10)
t.penup()
t.goto(-100,-100)
t.pendown()
for i in range(4):
    t.forward(300)
    t.right(90)

t.color("blue")
t.penup()
t.goto(-120,-100)
t.pendown()
for i in range(3):
    t.forward(340)
    t.right(240)

t.color("red")
t.penup()
t.goto(0,-200)
t.pendown()
t.forward(75)   
t.right(90)
t.forward(200)   
t.right(90)
t.forward(75)
t.right(90)
t.forward(200)
t.right(90)

t.color("red")
t.begin_fill()
t.penup()
t.goto(500,250)
t.pendown()
t.circle(60)
t.end_fill()
    

   

turtle.done()