import turtle
ws=turtle.Screen()
gT=turtle.Turtle()
gT.fillcolor('red')
gT.begin_fill()
for i in range(6):
    gT.forward(100)
    gT.right(60)
gT.end_fill()
turtle.exitonclick()