from turtle import *
from time import *
# Apparently you're not supposed to use an import splat bc it might
# hide one of your classes (since you have no idea what you're importing)

# turtle.forward(150)
# sleep(1)
# turtle.right(250)
# sleep(1)
# turtle.forward(150)
# turtle.done()

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    print(pos())
    if abs(pos()) < 1:
        break
end_fill()
done()
