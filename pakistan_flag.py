from turtle import *

#set page size in pixals
setup(800, 500)
bgcolor("#01411C")
speed(5)

#white Rectangle
penup()
goto(-400, 250)
pendown()
color("white")
begin_fill()

#loop
for i in range(2):
    forward(200)
    right(90)
    forward(500)
    right(90)
end_fill()

#Moon Shape
penup()
goto(50, -135)
pendown()
begin_fill()
circle(150)
end_fill()

penup()
goto(90, -80)
pendown()
color("#01411C")
begin_fill()
circle(135)
end_fill()

#Star Shape
penup()
goto(110, 90)
pendown()
color("white")
begin_fill()

for i in range(5):
    forward(90)
    left(144)
end_fill()

I'll post source code link also with this tutorial
that's it I hope you guyz like this video and follow for more
Thanks

