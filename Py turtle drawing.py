import turtle

colours = ["red","purple","blue","green","orange","yellow"]
t = turtle.Pen()
turtle.speed(1)
turtle.bgcolor("black")
a = 0
for x in range(150):
    t.pencolor(colours[x%6])
    t.width(x//100+1)
    t.forward(x)
    t.left(59)
    t.speed(10)
    a = x
t.pencolor(colours[0])
t.width(a//100+1)
t.forward(50)
turtle.done()