#! /bin/python
import math, turtle

currentX = 0.5
currentY = 0.26
angle = 0
time = 0

START_TIME = 0
END_TIME = 20
TIME_STEP = 1e-4
SPEED = 1
RADIUS = 1/3
RADIUS2 = RADIUS**2

turtle.radians()
turtle.speed(0)

for centerX in range(-5, 5):
    for centerY in range(-5, 5):
        turtle.penup()
        turtle.setpos(100*centerX, 100*centerY)
        turtle.pendown()
        turtle.dot()
        turtle.penup()
        turtle.setpos(100*centerX, 100*centerY - 100*RADIUS)
        turtle.pendown()
        turtle.circle(100*RADIUS)

turtle.penup()
turtle.setpos(100*currentX, 100*currentY)
turtle.pendown()

for timeOffset in range((int) ((END_TIME - START_TIME) / TIME_STEP)):

    time = START_TIME + TIME_STEP * timeOffset
    currentX = currentX + SPEED * TIME_STEP * math.cos(angle)
    currentY = currentY + SPEED * TIME_STEP * math.sin(angle)

    possibleXForCircles = [math.floor(currentX), math.ceil(currentX)]
    possibleYForCircles = [math.floor(currentY), math.ceil(currentY)]
    
    for centerX in possibleXForCircles:
        for centerY in possibleYForCircles:
            if ((centerX - currentX)**2 + (centerY - currentY)**2) <= RADIUS2:
                print("We're inside a circle " + str(centerX) + " " + str(centerY) + " " + str(currentX) + " " + str(currentY))
                beta = abs(math.atan((centerX - currentX) / (currentY - centerY)))

                if angle <= math.pi:
                    if currentX > centerX:
                        if currentY > centerY:
                            angle = 2 * math.pi - angle - 2 * beta
                        else:
                            angle = -angle + 2 * beta
                    else:
                        if currentY > centerY:
                            angle = -angle + 2 * beta
                        else:
                            angle = 2 * math.pi - angle - 2 * beta
                else:
                    if currentX > centerX:
                        if currentY > centerY:
                            angle = 4 * math.pi - angle - 2 * beta
                        else:
                            angle = 2 * math.pi - angle + 2 * beta
                    else:
                        if currentY > centerY:
                            angle = 2 * math.pi - angle + 2 * beta
                        else:
                            angle = 4 * math.pi - angle - 2 * beta
                
                turtle.setpos(100*currentX, 100*currentY)
                turtle.setheading(angle)
    
    while angle > 2 * math.pi:
        angle -= 2 * math.pi

    while angle < 0:
        angle += 2 * math.pi

input()
