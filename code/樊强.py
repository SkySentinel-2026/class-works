import turtle

t = turtle.Turtle()
m = turtle.Screen()
m.setup(width=500, height=500)
m.title("雷霆小房子")
m.bgcolor("lightblue")

for i in range(4):
    t.forward(100)
    t.right(90)
    t.color("red")
    t.pensize(4)

for i in range(3):
    t.forward(100)
    t.left(120)
    t.color("green")
    t.pensize(3)

t.penup()
t.goto(180,120)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(40,-50)
t.pendown()
for i in range(5):
  t.forward(50)
  t.right(90)
  t.color("orange")
  t.pensize(3)




turtle.done()

