"""
Helper turtle functions so we do not have to duplicate code and can easily change behaviour.
"""

import turtle
from .constants import *


def set_position(x: float, y: float) -> None:
    """
    Set the position of the turtle to (TURTLE_MAGNIFICATION * x, TURTLE_MAGNIFICATION * y).

    :param x: x coordinate of the point
    :param y: y coordinate of the point
    :rtype: None
    """

    turtle.setpos(TURTLE_MAGNIFICATION * x, TURTLE_MAGNIFICATION * y)


def inv_set_position(x: float, y: float) -> None:
    """
    Set the position of the turtle to (TURTLE_MAGNIFICATION * x, TURTLE_MAGNIFICATION * y) without drawing a line.

    :param x: x coordinate of the point
    :param y: y coordinate of the point
    :rtype: None
    """

    turtle.penup()
    set_position(x, y)
    turtle.pendown()


def circle(x: float, y: float) -> None:
    """
    Draw a circle with center (TURTLE_MAGNIFICATION * x, TURTLE_MAGNIFICATION * y) and radius RADIUS.

    :param x: x coordinate of the center of the circle
    :param y: y coordinate of the center of the circle
    :rtype: None
    """

    inv_set_position(x, y - RADIUS)
    turtle.circle(TURTLE_MAGNIFICATION * RADIUS)


def dot() -> None:
    """
    Draw a dot at the current position.

    :rtype: None
    """

    turtle.dot()


def init_turtle() -> None:
    """
    Initialise turtle to maximum speed and minimum delay for turtle drawing.

    :rtype: None
    """

    turtle.speed(0)
    turtle.delay(0)


def pause_refreshing() -> None:
    """
    Pauses refreshing to speed up drawing.

    :rtype: None
    """

    turtle.tracer(0, 0)


def resume_refreshing() -> None:
    """
    Resumes refreshing on every turtle jump.

    :rtype: None
    """

    turtle.tracer(1, 0)

def draw_visible_circles() -> None:
    """
    Draws all the visible circular mirrors.

    :rtype: None
    """

    for center_x in range(START_CENTER_X, END_CENTER_X):
        for center_y in range(START_CENTER_Y, END_CENTER_Y):
            inv_set_position(center_x, center_y)
            circle(center_x, center_y)
