import turtle
t=turtle.Turtle()
t.pensize(2)

t.color("orange")
for i in range(4):
    t.forward(150)
    t.right(90)
    
t.color("red")
for i in range(3):
    t.forward(150)
    t.left(120)
    
t.penup()
t.goto(30,-20)
t.pendown()
t.color("brown")
for i in range(4):
    t.forward(40)
    t.right(90)

t.penup()
t.goto(30,-40)
t.pendown()
t.forward(40)
t.right(90)
t.forward(20)
t.right(90)
t.forward(20)
t.right(90)
t.forward(40)

t.penup()
t.goto(60,-150)
t.pendown()
t.setheading(90)
t.forward(60)
t.right(90)
t.forward(30)
t.right(90)
t.forward(60)
    
    
    
    
    
turtle.down()
