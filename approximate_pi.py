#! /usr/bin/env python3
"""pi approximation module"""
from random import random
from sys import argv
from multiprocessing import Process, cpu_count, Queue


def random_point():
    """
    Generates and returns a point (x,y) with -1<=x,y<=1
    x and y are floating numbers.
    """
    return (2*random()-1, 2*random()-1)


def in_circle(point):
    """
    Returns True if the point is in the disc of radius 1 and False otherwise.
    """
    return (point[0]**2+point[1]**2) <= 1


def pi_approximate(point_nb, queue):
    """
    Returns an approximation of pi using the Monte-Carlo method with n points.
    """
    points_in_circle = 0
    for _ in range(point_nb):
        points_in_circle += in_circle(random_point())
    # points_in_circle/n corresponds to an approximation of
    # the area of the disc divided by the area of the square,
    # which is pi/4
    queue.put(4*points_in_circle/point_nb)


def multiprocessing(point_nb):
    """
    uses multiprocessing to estimate pi faster
    """
    processes = []
    queue = Queue()
    cpu_nb = cpu_count()
    for _ in range(cpu_nb):
        processes.append(Process(target=pi_approximate,
                         args=(point_nb//cpu_nb+1, queue)))
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    return sum([queue.get() for _ in range(cpu_nb)])/cpu_nb


def main():
    """Returns an approximation of pi using the Monte-Carlo method
    using the number passed in as an argument.
    """
    if len(argv) != 2:
        print(
            "use: ./approximate_pi.py n "
        )
    else:
        if not argv[1].isdigit():
            raise ValueError("Argument must be a positive integer")
        else:
            print(multiprocessing(int(argv[1])))


if __name__ == "__main__":
    main()
