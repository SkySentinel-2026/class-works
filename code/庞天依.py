import turtle
t=turtle.Turtle()
t.color("yellow");
t.goto(0,0);
t.pensize(4)
for i in range(4):
    t.forward(200)
    t.right(90)
t.penup()
t.goto(0,0);
t.pendown()
t.color("yellow");
for i in range(3):
    t.forward(200)
    t.left(120)#房子
t.penup()
t.goto(40,-40);
t.pendown()
t.color("pink");
for i in range(4):
    t.forward(30)
    t.right(90)
t.penup()
t.goto(130,-40);
t.pendown()
t.color("pink");
for i in range(4):
    t.forward(30)
    t.right(90)#窗户
t.penup()
t.goto(80,-110);
t.pendown()
t.color("brown");
for i in range(1):
    t.forward(50)
t.penup()
t.goto(80,-110);
t.pendown()
t.color("brown");
for i in range(1):
    t.right(90);
    t.forward(90)
t.penup()
t.goto(130,-110);
t.pendown()
t.color("brown");
for i in range(1):
    
    t.forward(90)#门
    