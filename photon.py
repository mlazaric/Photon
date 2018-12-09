#! /bin/python
import turtle
from sympy import Rational
from sympy.geometry import Point, Segment2D, Circle, Ray, intersection, Line
from math import floor, ceil, sqrt, pi

position = Point('0.5', '0.26')
imprecise_position = Point('0.5', '0.26', evaluate=False)
ray = Ray(position, angle=0.0)
time = 0

STEP = 0.1
RADIUS = Rational('1/3')
TURTLE_MAGNIFICATION = 100
LINE_SIZE = TURTLE_MAGNIFICATION / 10
e = Line((0, 0), (1, 0))
PRECISION = 50
PRINT_PRECISION = 8
circles = []
prev_circle = None
distance = Rational(20)

def setPosition(x, y):
    turtle.setpos(TURTLE_MAGNIFICATION * x, TURTLE_MAGNIFICATION * y)

def invSetPosition(x, y):
    turtle.penup()
    setPosition(x, y)
    turtle.pendown()

def circle(x, y):
    invSetPosition(x, y - RADIUS)
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

for centerX in range(-10, 10):
    for centerY in range(-5, 5):
        invSetPosition(centerX, centerY)
        dot()
        circle(centerX, centerY)

invSetPosition(position.x, position.y)

print(position.x.evalf(PRINT_PRECISION), position.y.evalf(PRINT_PRECISION))

while distance > 0:
    imprecise_position = imprecise_position.translate((STEP * ray.direction.x).evalf(PRECISION), (STEP * ray.direction.y).evalf(PRECISION)) 

    possibleCenterX = [floor(imprecise_position.x), ceil(imprecise_position.x)]
    possibleCenterY = [floor(imprecise_position.y), ceil(imprecise_position.y)]

    for x in possibleCenterX:
        reflected = False

        for y in possibleCenterY:
            center = Point(x, y)
            circle = Circle(center, RADIUS)

            if prev_circle == circle:
                continue

            if circle in circles:
                continue

            intersect = intersection(ray, circle)
            prev_position = position

            if len(intersect) == 1:
                position = intersect[0]
            elif len(intersect) == 2:
                if (position.distance(intersect[0]).evalf(PRECISION)) < (position.distance(intersect[1]).evalf(PRECISION)):
                    position = intersect[0]
                else:
                    position = intersect[1]
            else:
                circles.append(circle)

            if len(intersect) >= 1:
                if prev_position.distance(position) > distance:
                    position = prev_position.translate(ray.direction.x * distance, ray.direction.y * distance)
                    distance = 0
                    break

                distance -= prev_position.distance(position).evalf(PRECISION)
                circles = []
                prev_circle = circle
                tangent = circle.tangent_lines(position)[0]
                position = Point(position.x.evalf(PRECISION), position.y.evalf(PRECISION))
                imprecise_position = position

                direction = position + ray.reflect(tangent).direction
                direction = Point(direction.x.evalf(PRECISION), direction.y.evalf(PRECISION))

                ray = Ray(position, direction)

                setPosition(position.x, position.y)
                dot()
                print(position.x.evalf(PRINT_PRECISION), position.y.evalf(PRINT_PRECISION))

                reflected = True

            if reflected:
                break

            if distance <= 0:
                break

        if reflected:
            break

        if distance <= 0:
            break

setPosition(position.x, position.y)
dot()
print(position.x.evalf(PRINT_PRECISION), position.y.evalf(PRINT_PRECISION))
input()
