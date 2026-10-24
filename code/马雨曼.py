import turtle
t = turtle.Turtle()
t.speed(2)

# 正方形房体，循环4次
t.color("lightblue")
t.begin_fill()
for _ in range(4):
    t.forward(150)
    t.left(90)
t.end_fill()

# 移到屋顶
t.penup()
t.goto(0,150)
t.pendown()

# 三角形屋顶，循环3次
t.color("coral")
t.begin_fill()
for _ in range(3):
    t.forward(150)
    t.left(120)
t.end_fill()

# 小窗户，循环4次
t.penup()
t.goto(50,50)
t.pendown()
t.color("white")
t.begin_fill()
for _ in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()

# ========== 左上角 小太阳 ==========
t.penup()
t.goto(-220, 200)   # 左上角位置
t.pendown()
t.color("gold")
t.begin_fill()
# 太阳圆形（正12边形近似圆）
for _ in range(12):
    t.forward(18)
    t.left(30)
t.end_fill()

# 小草小花（放在房子下方）
# 第一棵小草
t.penup()
t.goto(-120, -30)
t.pendown()
t.color("green")
for i in range(3):
    t.forward(25)
    t.left(120)

# 第二棵小草
t.penup()
t.goto(-60, -30)
t.pendown()
for i in range(3):
    t.forward(25)
    t.left(120)

# 第一朵小花
t.penup()
t.goto(20, -40)
t.pendown()
t.color("pink")
for i in range(5):
    t.forward(15)
    t.left(72)

# 第二朵小花
t.penup()
t.goto(90, -40)
t.pendown()
t.color("hotpink")
for i in range(5):
    t.forward(15)
    t.left(72)

t.hideturtle()
turtle.done()