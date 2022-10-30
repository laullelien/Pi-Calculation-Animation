#! /usr/bin/env python3
"""Module graphique du projet BPI"""
import subprocess
import approximate_pi


def generate_pixel_dict(size):
    """
    Returns a dictionnary with keys from 0 to size²-1
    representing pixels. Each key is associated with
    (1,1,1), a white pixel
    """
    pixel_dict = {}
    for i in range(size**2):
        pixel_dict[i] = (1, 1, 1)
    return pixel_dict


def coordinate_conversion(point, size):
    """
    Transforms a point of coordinate (x,y)
    in an other point of coordinate (u,v) and returns it
    -1<x,y<1
    0<=u,v<=size-1
    x and y are floating numbers
    u and v are integers
    """
    u = int((point[0]+1)*size/2)
    v = int((point[1]+1)*size/2)
    if u == size:
        u -= 1
    if v == size:
        v -= 1
    return (u, v)


def next_step(pixel_dict, size, n):
    """
    Generates ⌈n/10⌉ points, stores them as pixels in
    pixel_dict. They are stored as (1,0,0) (red) if they are
    in the disc and (0,0,1) (blue) otherwise. Also returns the
    approximation of pi calculated with these points
    """
    in_circle_points = 0
    for _ in range(int(n/10 + 1)):
        point = approximate_pi.random_point()
        in_circle = approximate_pi.in_circle(point)
        point = coordinate_conversion(point, size)
        if in_circle:
            in_circle_points += 1
            pixel_dict[point[1]*size+point[0]] = (1, 0, 0)
        else:
            pixel_dict[point[1]*size+point[0]] = (0, 0, 1)
    return 4*in_circle_points/int(n/10 + 1)


def generate_ppm_file(i, size, displayed_pi, pixel_dict):
    """
    Generates a ppm file of dimension size*size,
    maximum color value of 1, color informations are in binary.
    The pixels are stored in pixel_dict.
    Returns the file's name which contains the number of the step as well as
    the current value of the approximation of pi.
    """
    img_name = f"img{i}_"+str(displayed_pi).replace(".", "-")+".ppm"
    with open(img_name, "w", encoding="UTF-8") as img:
        img.write(f"P6\n{size} {size}\n1\n")
    with open(img_name, "ab") as img:
        for i in range(size**2):
            pixel_string = "%c%c%c" % (
                pixel_dict[i][0], pixel_dict[i][1], pixel_dict[i][2])
            img.write(pixel_string.encode("utf-8"))
    return img_name


def average(number_list):
    """Return the average of the numbers in the list"""
    return sum(number_list)/len(number_list)


def modify_digit_number(number, digit_number):
    """
        Return a new number which is the number
        passed in with only digit_number digits
        after its comma
    """
    return int(number*10**digit_number)/10**digit_number


def main(size, n, digit_number):
    """
    Generates the 10 ppm files and the gif
    size,n>10
    1<=digit_number<=5
    size, n and digit_number are integers
    """
    pi_list = []  # contains the 10 approximations of pi
    file_names = []
    pixel_dict = generate_pixel_dict(size)
    for i in range(10):
        pi_approx = next_step(pixel_dict, size, n)
        pi_list.append(pi_approx)
        displayed_pi = average(pi_list)
        displayed_pi = modify_digit_number(displayed_pi, digit_number)
        file_names.append(generate_ppm_file(i, size, displayed_pi, pixel_dict))
        convert(file_names)


def convert(file_names):
    """The images name contained in file_name
    are used to generate a gif of name pi_approximate.gif"""
    cmd = ['convert'] + file_names + ['pi_approximate.gif']
    subprocess.call(cmd)


main(1000, 100000, 5)
