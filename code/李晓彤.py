import turtle

t=turtle.Turtle()
t.pensize(6)


for i in range(4):
  t.forward(200)
  t.right(90)
t.penup()
t.goto(0,0)
t.pendown()
t.left(60)

for i in range(3):
  t.forward(200)
  t.right(120)
t.penup()
t.goto(20,-200)
t.pendown()
t.left(30)
  
for i in range(2):
    t.forward(100)
    t.right(90)
    t.forward(70)
    t.right(90)
t.penup()
t.goto(35,-155)
t.pendown()

t.circle(5)
t.penup()
t.goto(-300,300)
t.pendown()

t.pencolor("orange")
t.circle(60)
t.penup()
t.goto(-200,-300)
t.pendown()
t.left(90)

t.pencolor("brown")
for i in range(2):
    t.forward(100)
    t.right(90)
    t.forward(250)
    t.right(90)
t.penup()
t.goto(-323,-50)
t.pendown()
t.right(180)

t.pencolor("green")
for i in range(3):
  t.forward(150)
  t.left(120)




  
         
    

