import turtle
import math
import random

t=turtle.Turtle()
turtle.bgcolor("black")
t.hideturtle()

for i in range(100):
    t.speed(0)
    t.color("white")
    t.penup()
    t.goto(random.randint(-500,500),random.randint(-300,300))
    t.dot(random.randint(1,4))

t.pensize(40)
t.speed(10)
t.color("#FFD700")
t.goto(0,-100)
t.pendown()
t.circle(100,360)


#t.pensize(15)
#t.color("yellow")
#t.penup()
#t.goto(0,0)
#t.pendown()
#t.goto(300,0)
#t.goto(-300,0)

def draw_ellipse(x, y, a, b, color, pensize):
    t.color(color)
    t.pensize(pensize)
    t.penup()
    t.goto(x + a, y) 
    t.pendown()
    for i in range(0, 180, 4):
        rad = math.radians(i)
        t.goto(x + a * math.cos(rad), y + b * math.sin(rad))
draw_ellipse(0, 0, 330, 35, "#8B0000", 16) 
draw_ellipse(0, 0, 300, 25, "#FF4500", 10) 
draw_ellipse(0, 0, 280, 15, "#FFD700", 4) 
draw_ellipse(0, 0, 270, 12, "#FFFFFF", 1)  

t.color("black")
t.penup()
t.goto(0,-90)
t.pendown()
t.begin_fill()
t.circle(80)
t.end_fill()


def draw_ellipse(x, y, a, b, color, pensize):
    t.color(color)
    t.pensize(pensize)
    t.penup()
    t.goto(x-a, y) 
    t.pendown()
    for i in range(180, 360, 4):
        rad = math.radians(i)
        t.goto(x + a * math.cos(rad), y + b * math.sin(rad))
draw_ellipse(0, 0, 330, 35, "#8B0000", 16) 
draw_ellipse(0, 0, 300, 25, "#FF4500", 10) 
draw_ellipse(0, 0, 280, 15, "#FFD700", 4) 
draw_ellipse(0, 0, 270, 12, "#FFFFFF", 1)  

t.penup()
t.goto(-500,0)
t.pendown()
t.showturtle()
def draw_ellipse(x, y, a, b, color, pensize):
    t.color(color)
    t.pensize(pensize)
    t.penup()
    t.goto(x -a, y) 
    t.pendown()
    for i in range(180,360,1):
        rad = math.radians(i)
        t.goto(x + a * math.cos(rad), y + b * math.sin(rad))
draw_ellipse(-500,0,1000,200,"white",1)

t.penup()
t.goto(200,-200)
t.pendown()
t.write("天巡",font=("微软雅黑",30,"bold"))


turtle.exitonclick()