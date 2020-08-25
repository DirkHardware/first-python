# Pixel Art - http://www.101computing.net/pixel-art-in-python/

import turtle
import random

myPen = turtle.Turtle()
# myPen.tracer(0)
myPen.speed(0)
myPen.color("#000000")

minX = 16
minY = 16

grid = [[]]
for columns in range(0, minX):
    grid[0].append(0)

for rows in range(0, minY):
    row = []
    for columns in range(0, minX):
        row.append(0)
    grid.append(row)

entrance_dir = random.randint(0, 4)
# entrance_dir = 3
# 0 = North, 1 = East, 2 = South, 3 = West


def setEntrance(entrance_dir = entrance_dir, grid = grid):
    if entrance_dir == 0:
        entrance_side0 = [0, (minX // 2) - 1]
        entrance_side1 = [0, (minX // 2)]
        entrance_side2 = [0, (minX // 2) + 1]
        grid[0][minX // 2] = 1
        grid[0][(minX // 2) - 1] = 1
        grid[0][(minX // 2) + 1] = 1
        return [entrance_side0, entrance_side1, entrance_side2]
    elif entrance_dir == 1:
        entrance_side0 = [(minY // 2) - 1, -1]
        entrance_side1 = [(minY // 2), -1]
        entrance_side2 = [(minY // 2) + 1, -1]
        grid[minY // 2][-1] = 1
        grid[(minY // 2) - 1][-1]
        grid[(minY // 2) + 1][-1]
        return [entrance_side0, entrance_side1, entrance_side2]
    elif entrance_dir == 2:
        entrance_side0 = [-1, (minX // 2) - 1]
        entrance_side1 = [-1, (minX // 2)]
        entrance_side2 = [-1, (minX // 2) + 1]
        grid[-1][minX // 2] = 1
        grid[-1][(minX // 2) - 1] = 1
        grid[-1][(minX // 2) + 1] = 1
        return [entrance_side0, entrance_side1, entrance_side2]
    else:
        entrance_side0 = [(minY // 2) - 1, 0]
        entrance_side1 = [(minY // 2), 0]
        entrance_side2 = [(minY // 2) + 1, 0]
        grid[minY // 2][0] = 1
        grid[(minY // 2) - 1][0] = 1
        grid[(minY // 2) + 1][0] = 1
        return [entrance_side0, entrance_side1, entrance_side2]



entrance_bounds = setEntrance()
print(entrance_bounds)

# This function draws a box by drawing each side of the square and using the fill function
def emptyGrid(intDim):
    # myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    # myPen.end_fill()
    myPen.setheading(0)


def fillGrid(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)

boxSize = 10
# Position myPen in top left area of the screen
myPen.penup()
# Below var was originally -100 I think.
myPen.forward(-(len(grid)*3.5))
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0)

##Here is an example of how to draw a box
# box(boxSize)

##Here are some instructions on how to move "myPen" around before drawing a box.
# myPen.setheading(0) #point to the right, 90 to go up, 180 to go to the left 270 to go down
# myPen.penup()
# myPen.forward(boxSize)
# myPen.pendown()

# Here is how your PixelArt is stored (using a "list of lists")

# pixels = [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]]
# pixels.append([0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0])
# pixels.append([0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0])
# pixels.append([0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0])
# pixels.append([0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0])
# pixels.append([1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1])
# pixels.append([1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1])
# pixels.append([1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1])
# pixels.append([1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1])
# pixels.append([1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1])
# pixels.append([1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1])
# pixels.append([1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1])
# pixels.append([0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0])
# pixels.append([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
# pixels.append([0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0])
# pixels.append([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0])


#

# print(pixels)
# print(len(pixels[0]))
# print(pixels[2])

# setEntrance(entrance_dir, grid)

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] == 0:
            emptyGrid(boxSize)
            # print("Printing grid row {0}".format(i))
        else:
            fillGrid(boxSize)
        myPen.penup()
        myPen.forward(boxSize)
        myPen.pendown()
    myPen.setheading(270)
    myPen.penup()
    myPen.forward(boxSize)
    myPen.setheading(180)
    myPen.forward(boxSize * len(grid[i]))
    myPen.setheading(0)
    myPen.pendown()

myPen.getscreen().update()
turtle.done()