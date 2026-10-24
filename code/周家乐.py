import turtle
t= turtle.Turtle()

for i in range(12): 
    for i in range(6):     
        t.forward(100)
        t.right(60)
    for i in range(6):       
        t.forward(100)
        t.left(60) 
    t.right(30)                 
turtle.done()