"""
Constants for the project, includes various starting conditions and other information.
"""

from sympy import Rational, Point

# Step used for ray tracing to find the circle which the src hits.
STEP = 0.1

# Radius of the circles.
RADIUS = Rational('1/3')

# Multiplication factor for the turtle.
TURTLE_MAGNIFICATION = 100

# Precision of the position.
PRECISION = 50

"""
Starting conditions
"""
# Starting position of the src.
START_POSITION = Point('0.5', '0.26')

# Starting angle of the src.
START_ANGLE = 0

# The distance which the simulation covers.
DISTANCE = Rational(20)

"""
Start and end position of circular mirrors to draw at the start.
"""
START_CENTER_X = -11
END_CENTER_X = 11

START_CENTER_Y = -6
END_CENTER_Y = 6