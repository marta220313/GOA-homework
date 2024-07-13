from turtle import *

#we want to paint a house

#step 1: draw a square
speed (30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door


forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)          #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#little square above the house
penup()
goto(50, 150)
pendown()



color("pink")
begin_fill()
right(50)
forward(20)
right(10)
forward(15)
right(90)
forward(30)
left(50)
forward(0)
right(130)
forward(35)
right(100)
forward(35)
end_fill()


exitonclick()