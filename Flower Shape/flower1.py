import turtle
obj=turtle.Turtle()
scr=turtle.Screen()
scr.title('FLOWER SHAPE USING PYTHON GRAPHICS')
scr.bgcolor('black')
l=['yellow','red','green','orange','purple']
for i in range(30):
    obj.color(l[i%5])
    obj.pensize(i/10+1)
    obj.forward(i)
    obj.left(59)
