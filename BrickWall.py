import turtle

#Inmediately
wn = turtle.Screen()
wn.tracer(0)

#Rectangle Brick
def rectangleBrick(width, height):
    turtle.pendown()
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
 
#Square Brick
def squareBrick(size):
    turtle.pendown()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

#Row of Bricks
def rowBricks(numberbricks, width, height):
  x = turtle.xcor()
  for i in range(numberbricks):
    rectangleBrick(width, height)
    turtle.setx(turtle.xcor() + width)
  turtle.penup()

#Offset
def offsetBricks(rownum, width, height):
  x = turtle.xcor()
  squareBrick(height)
  turtle.setx(turtle.xcor()+ height)
  for i in range(1, rownum):
    rectangleBrick(width, height)
    turtle.setx(turtle.xcor()+ width)
  squareBrick(height)

#Columns in the Wall
def wallColms(ncolms, numberbricks, width, height):
    x = turtle.xcor()
    y = turtle.ycor()
    for i in range(ncolms):
        if i % 2 == 0:
            rowBricks(numberbricks, width, height)
            turtle.penup()
            turtle.sety(turtle.ycor()+height)
            turtle.setx(0)
            turtle.pendown()
        else:
            offsetBricks(numberbricks, width, height)
            turtle.penup()
            turtle.sety(turtle.ycor()+ height)
            turtle.setx(0)
            turtle.pendown()
    turtle.penup()

#Brick Sizes + Colums
def main():
    ncolms = 15
    numberbricks = 6
    width = 20
    height = 10
    
    wallColms(ncolms, numberbricks, width, height)
    turtle.speed()

main()

#Draw inmediately >:) + Don't close window
wn.update()
wn.mainloop()
 