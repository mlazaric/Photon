#! /bin/python

import turtle
from PIL import Image
import io
from src.photon import Photon
from src.turtle_helpers import *

"""
Simple python script for simulating a src reflecting off circular mirrors located at points with
    integer x and y coordinates and with radius of 1/3.
"""

if __name__ == '__main__':
    # Set turtle window to fullscreen
    window = turtle.Screen()
    window.setup(width=1.0,
                 height=1.0,
                 startx=None,
                 starty=None)

    photon = Photon(START_POSITION, START_ANGLE, DISTANCE)

    # Pause refreshing while we draw the circles to speed up drawing
    init_turtle()
    pause_refreshing()

    draw_visible_circles()
    photon.invisible_jump_to_position()
    dot()
    photon.print_position()

    # Resume refreshing
    resume_refreshing()

    # While we still have distance to cover...
    while photon.distance > 0:
        # Move imprecisely using imprecise_position
        photon.raytrace()
        # Check nearby circles for collisions and reflect if it has collided
        photon.check_nearby_circles()

    # Jump and print the last position
    photon.jump_to_position()
    dot()
    photon.print_position()

    # Save the turtle window as a png image in images/result.png
    ps = turtle.getscreen().getcanvas().postscript(colormode='color')
    image = Image.open(io.BytesIO(ps.encode('utf-8')))
    image.save('images/result.png')

    turtle.done()

    #
    # Important information: you have to close the turtle window for it to save the image.
    #
