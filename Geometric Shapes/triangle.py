import turtle
obj=turtle.Turtle()
scr=turtle.Screen()
scr.title('TRIANGLE SHAPE')
obj.pensize(6)
scr.bgcolor('black')
obj.shape('circle')
obj.color('red','yellow')
obj.begin_fill()
obj.fillcolor('yellow')
obj.circle(100,steps=3)
obj.end_fill()


