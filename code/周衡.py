import turtle
import random
t=turtle.Turtle()

t.speed(0)

screen=turtle.Screen()      #sky
screen.bgcolor("lightblue")

t.color("white")
t.hideturtle()
t.penup()
for i in range(60):             #star
    x=random.randint(-500,500)
    y=random.randint(0,500)
    t.goto(x,y)
    t.dot(random.randint(3,9))

t.penup()
t.goto(-500,-50)
t.pendown()
t.color("green","limegreen")
t.begin_fill()
for i in range(2):   #草地
    t.forward(1000)
    t.right(90)
    t.forward(800)
    t.right(90)
t.end_fill()

t.penup()
for i in range(150):            #grass
    x=random.randint(-500,500)
    y=random.randint(-500,-50)
    t.goto(x,y)
    t.setheading(90)
    if(i%2==0):
        t.color("dark green")
    else:
        t.color("green")
    t.pendown()
    t.forward(random.randint(6,14))
    t.penup()

t.setheading(0)     #复原

for i in range(20):               #flower
    x=random.randint(-500,500)
    y=random.randint(-400,-70)  
    t.goto(x,y)
    t.color(random.choice(["red","blue","yellow","orange","pink"]))
    t.dot(random.randint(8,9))         

t.goto(-50,-50)
t.pendown()
t.color("black","firebrick")
t.begin_fill()
for i in range(4):   #房子
    t.forward(100)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-50,50)
t.pendown()
t.color("black","wheat")
t.begin_fill()
for i in range(3):   #房顶
    t.forward(100)
    t.left(120)
t.end_fill()

t.penup()
t.goto(-15,-50)
t.pendown()
t.color("sienna","sienna")
t.begin_fill()
for i in range(2):   #门
    t.forward(30)
    t.left(90)
    t.forward(50)
    t.left(90)
t.end_fill()

t.penup()
t.goto(90,-50)
t.pendown()
t.color("brown","brown")
t.begin_fill()
for i in range(2):    #树干
    t.forward(10)
    t.left(90)
    t.forward(70)
    t.left(90)
t.end_fill()  

t.penup()
t.goto(60,20)
t.pendown()
t.color("green","green")
t.begin_fill()
for i in range(3):    #树叶
    t.forward(70)
    t.left(120)    
t.end_fill()

t.penup()
t.goto(250,300)
t.color("yellow","yellow")  #sun
t.begin_fill()
t.circle(30)
t.end_fill()

color=("red","orange","yellow")    #旋转
t.penup()
t.goto(-200,250)
t.pendown()
for i in range(36):
    for i in range(4):
        t.pencolor(color[i%3])
        t.forward(100)
        t.right(90)
    t.right(10)    

t.penup()
t.goto(-200,220)    #word
t.pendown()
t.write("快乐天巡",move=True,align="center",font=("SimHei",30,"bold"))

turtle.done()    



