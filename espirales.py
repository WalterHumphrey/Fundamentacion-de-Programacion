import turtle

t = turtle.Turtle()
t.left(30)

for i in range(1,21):
    n = i*10
    t.forward(300-n)
    t.left(120)
turtle.done()