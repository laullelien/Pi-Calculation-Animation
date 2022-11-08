#! /usr/bin/env python3
"""pi approximation module"""
from random import uniform
from sys import argv


def random_point():
    """
    Generates and returns a point (x,y) with -1<=x,y<=1
    x and y are floating numbers
    """
    return (uniform(-1, 1), uniform(-1, 1))


def in_circle(point):
    """
    Returns True if the point is in the disc of radius 1 and False otherwise
    """
    return (point[0]**2+point[1]**2) <= 1


def pi_approximate(point_number):
    """
    Returns an approximation of pi using the Monte-Carlo method with n points
    """
    points_in_circle = 0
    for _ in range(point_number):
        points_in_circle += int(in_circle(random_point()))
    # points_in_circle/n corresponds to an approximation of
    # the area of the disc divided by the area of the square,
    # which is pi/4
    return 4*points_in_circle/point_number


def main():
    """Returns an approximation of pi using the Monte-Carlo method
    using the number passed in as an argument
    """
    if len(argv) != 2:
        print(
            "use: ./approximate_pi.py n "
        )
        exit(1)
    else:
        if not argv[1].isdigit():
            raise TypeError("Argument must be a positive integer")
        else:
            print(pi_approximate(int(argv[1])))


if __name__ == "__main__":
    main()
