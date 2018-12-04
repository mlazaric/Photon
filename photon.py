#! /bin/python
import math, turtle

currentX = 0.5
currentY = 0.25
angle = 0
time = 0

START_TIME = 0
END_TIME = 20
TIME_STEP = 1e-4
SPEED = 1
RADIUS = 1/3
RADIUS2 = RADIUS**2
TURTLE_MAGNIFICATION = 100

turtle.radians()
turtle.speed(0)
turtle.delay(0)

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
                
                k = (currentY - centerY) / (currentX - centerX)
                l = currentY - currentX * k

                a = 1 + k**2
                b = -2 * centerX + 2 * k * l - 2 * k * centerY
                c = centerX**2 + l**2 - 2 * centerY * l + centerY**2 - RADIUS**2

                x1 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
                x2 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)

                y1 = k * x1 + l
                y2 = k * x2 + l

                if ((x1 - currentX)**2 + (y1 - currentY)**2) < ((x2 - currentX)**2 + (y2 - currentY)**2):
                    delta = math.sqrt((x1 - currentX)**2 + (y1 - currentY)**2)
                    currentX = x1
                    currentY = y1
                else:
                    delta = math.sqrt((x2 - currentX)**2 + (y2 - currentY)**2)
                    currentX = x2
                    currentY = y2

                turtle.setpos(100*currentX, 100*currentY)
                turtle.setheading(angle)

                currentX = currentX + delta * math.cos(angle)
                currentY = currentY + delta * math.sin(angle)

    
    while angle > 2 * math.pi:
        angle -= 2 * math.pi

    while angle < 0:
        angle += 2 * math.pi

input()
