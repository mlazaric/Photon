from .constants import *
from .turtle_helpers import *

from sympy import Rational, Point, Basic
from sympy.geometry import Point, Ray, Circle, intersection

from typing import Generator, Tuple, List, Any, Union

from math import floor, ceil


class Photon:
    position: Point
    imprecise_position: Point
    ray: Ray
    checked_circles: List[Circle]
    distance: Rational

    def __init__(self,
                 position: Point,
                 angle: float,
                 distance: Rational) -> None:
        """
        Creates a new photon with the given current position, angle and distance to cover.

        :param position: starting position of the photon
        :param angle: starting angle of the photon
        :param distance: distance to cover
        :rtype: None
        """

        # Current position which one changes when the src hits a circle.
        self.position = position

        # Imprecise current position used for ray tracing.
        self.imprecise_position = Point(position, evaluate=False)

        # Current heading of the src.
        self.ray = Ray(position, angle=angle)

        # Circles we have already checked before, after the last reflection, so we don't have to do it again.
        self.checked_circles = []

        # Distance left to cover.
        self.distance = distance

    def jump_to_position(self) -> None:
        """
        Draws a line from the current turtle position to self.position.
        Sets current turtle position to self.position.

        :rtype: None
        """

        set_position(float(self.position.x),
                     float(self.position.y))

    def invisible_jump_to_position(self) -> None:
        """
        Sets current turtle position to self.position without drawing a line.

        :rtype: None
        """

        inv_set_position(float(self.position.x),
                         float(self.position.y))

    def raytrace(self) -> None:
        """
        Moves imprecise_position STEP distance in the direction of the photon.

        :rtype: None
        """

        self.imprecise_position = self.imprecise_position.translate(
            (STEP * self.ray.direction.x).evalf(PRECISION),
            (STEP * self.ray.direction.y).evalf(PRECISION))

    def check_nearby_circles(self) -> None:
        """
        Checks the circles around the photon to see if it has collided with any of them.

        If it has, it sets the new position and calls self.reflect with the previous position and the collided circle.
        Otherwise, it adds the circle to checked_circles.

        :rtype: None
        """

        for (x, y) in self.possible_centers():
            center = Point(x, y)
            circle = Circle(center, RADIUS)

            # If we already checked that circle after the last reflection.
            if circle in self.checked_circles:
                continue

            intersect = intersection(self.ray,
                                     circle)

            prev_position = self.position

            # If intersection returns one Point, set position to it.
            if len(intersect) == 1:
                self.position = intersect[0]

                self.reflect(prev_position, circle)
                break

            # If intersection returns two Points, find the closer one and set position to it.
            elif len(intersect) == 2:
                if (self.position.distance(intersect[0]).evalf(PRECISION)) < \
                        (self.position.distance(intersect[1]).evalf(PRECISION)):
                    self.position = intersect[0]
                else:
                    self.position = intersect[1]

                self.reflect(prev_position, circle)
                break

            # Otherwise we have not collided with that circle, so we add it to the circles list.
            else:
                self.checked_circles.append(circle)

    def reflect(self,
                prev_position: Point,
                circle: Circle) -> None:
        """
        Reflects the photon on the given circle.

         - calculates distance covered and subtracts it from self.distance
         - calculates new direction vector
         - jumps to the new position and prints it

        :rtype: None
        """
        if prev_position.distance(self.position) > self.distance:
            self.position = prev_position.translate(self.ray.direction.x * self.distance,
                                                    self.ray.direction.y * self.distance)
            self.distance = 0
            return

        self.distance -= prev_position.distance(self.position).evalf(PRECISION)
        self.checked_circles = [circle]

        tangent = circle.tangent_lines(self.position)[0]
        self.position = Point(self.position.x.evalf(PRECISION),
                              self.position.y.evalf(PRECISION))
        self.imprecise_position = self.position

        direction = self.position + self.ray.reflect(tangent).direction
        direction = Point(direction.x.evalf(PRECISION),
                          direction.y.evalf(PRECISION))

        self.ray = Ray(self.position, direction)

        self.jump_to_position()
        dot()
        self.print_position()

    def possible_centers(self) -> Generator[Tuple[float, float], None, None]:
        """
        Returns the possible centers of the circles around the photon as a generator.

        :return: a generator for the possible circle centers
        :rtype: Generator[Tuple[float, float]]
        """

        # The only circles we have to check are the ones with these center coordinates.
        possible_center_x = [floor(self.imprecise_position.x),
                             ceil(self.imprecise_position.x)]

        possible_center_y = [floor(self.imprecise_position.y),
                             ceil(self.imprecise_position.y)]

        for center_x in possible_center_x:
            for center_y in possible_center_y:
                yield (center_x, center_y)

    def print_position(self) -> None:
        """
        Print coordinates of the current position.

        :rtype: None
        """

        x = self.position.x.evalf(PRECISION)
        y = self.position.y.evalf(PRECISION)

        print(f'{x: 1.15f} {y: 1.15f}')
