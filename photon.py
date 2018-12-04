#! /bin/python
import math, turtle

position = 0.5 + 0.26j
vector = 1 + 0j
time = 0

START_TIME = 0
END_TIME = 20
TIME_STEP = 1e-4
RADIUS = 1/3
RADIUS2 = RADIUS**2
TURTLE_MAGNIFICATION = 100
LINE_SIZE = TURTLE_MAGNIFICATION / 10

def setPosition(position):
    turtle.setpos(TURTLE_MAGNIFICATION * position.real, TURTLE_MAGNIFICATION * position.imag)

def invSetPosition(position):
    turtle.penup()
    setPosition(position)
    turtle.pendown()

def circle(position):
    invSetPosition(position - RADIUS * 1j)
    turtle.circle(TURTLE_MAGNIFICATION * RADIUS)

def dot():
    turtle.dot()

def line(length, angle):
    turtle.setheading(angle)
    turtle.forward(length)
    turtle.backward(length)

turtle.radians()
turtle.speed(0)
turtle.delay(0)

for centerX in range(-5, 5):
    for centerY in range(-5, 5):
        invSetPosition(centerX + 1j * centerY)
        dot()
        circle(centerX + 1j * centerY)

invSetPosition(position)

for timeOffset in range((int) ((END_TIME - START_TIME) / TIME_STEP)):

    time = START_TIME + TIME_STEP * timeOffset
    position += TIME_STEP * vector

    possibleCenterX = [math.floor(position.real), math.ceil(position.real)]
    possibleCenterY = [math.floor(position.imag), math.ceil(position.imag)]

    for x in possibleCenterX:
        reflected = False

        for y in possibleCenterY:
            center = x + y*1j

            if abs(position - center) <= RADIUS:
                setPosition(position)
                dot()

                # Backtrack to the beginning of the circle
                k = vector.imag / vector.real
                l = position.imag - k * position.real

                a = 1 + k**2
                b = -2 * center.real + 2 * k * l - 2 * k * center.imag
                c = center.real**2 + l**2 - 2 * center.imag * l + center.imag**2 - RADIUS**2

                x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
                x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)

                point1 = x1 + 1j * (k * x1 + l)
                point2 = x2 + 1j * (k * x2 + l)

                delta = min(abs(point1 - position), abs(point2 - position))

                if abs(point1 - position) > abs(point2 - position):
                    position = point2
                else:
                    position = point1

                # Calculate normal and tangent
                normal = position - center
                tangent = normal / 1j

                normal /= abs(normal)
                tangent /= abs(tangent)

                # Debug
                line(LINE_SIZE, math.atan2(normal.imag, normal.real))
                line(LINE_SIZE, math.atan2(normal.imag, normal.real) + math.pi)
                line(LINE_SIZE, math.atan2(tangent.imag, tangent.real))
                line(LINE_SIZE, math.atan2(tangent.imag, tangent.real) + math.pi)

                alpha = math.acos((vector.real * tangent.real + vector.imag * tangent.imag) / (abs(vector) * abs(tangent)))

                if alpha > math.pi / 2:
                    alpha -= math.pi / 2

                vector = math.sin(alpha) * normal + math.cos(alpha) * tangent
                position += vector * delta;

                reflected = True
                break

            if reflected:
                break

        if reflected:
            break

input()
