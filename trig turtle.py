import turtle
import random
import math
turtle.hideturtle()
turtle.speed(0)
wn = turtle.Screen()
wn.bgcolor("#222222")
turtle.colormode(255)


def circleMaths(radius, angle):
    x = math.cos(math.radians(angle)) * radius
    y = math.sin(math.radians(angle)) * radius
    return [x,y]

def connectionPairs(vec1, vec2):
    table = []
    table.append(vec1)
    table.append(vec2)
    return table

def dothecircle(tableOfPoints):
    for i in tableOfPoints:
        colour = 255
        turtle.pencolor((colour,colour,colour))
        turtle.setpos(0,0)
        turtle.setpos(i[0][0] / 0.3, i[0][1] / 2)
        turtle.setpos(i[1][0] / 0.76, i[1][1] /0.76)


print("150 looks good")
radius = int(input("Radius = "))

returnedVecs = []
for i in range(0, 360, 1):
    thing = circleMaths(radius,i)
    returnedVecs.append(thing)

finals = []
for i in range(len(returnedVecs)):
    newPosSets = connectionPairs(returnedVecs[i], returnedVecs[((len(returnedVecs) -1) -i) or i])
    finals.append(newPosSets)

dothecircle(finals)

