import turtle
t=turtle.Turtle()
scr=turtle.Screen()
scr.title("FLOWER SHAPE")
scr.bgcolor('black')
t.color('ivory')
t.speed(20)
t.pensize(2)
for i in range(0,360,5):
    t.left(i)
    t.circle(80)
