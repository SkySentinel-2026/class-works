import turtle as t

t.pu()

t.pd()
t.color("green")
t.left(180)
t.begin_fill()
for i in range(4):
    for j in range(1):
        t.right(60)
        t.fd(80)
        t.right(30)
        t.circle(-20,180)
        t.left(180)
        t.circle(-20,180)
        t.right(30)
        t.fd(80)
    t.left(30)   
t.end_fill()    
t.update()
t.done()
    