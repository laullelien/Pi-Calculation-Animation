#! /usr/bin/env python3
"""Graphical module"""
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


def add_pi_display(pixel_dict, size, displayed_pi, digit_number):
    """
    Changes some pixel in pixel_dict to black pixels (0,0,0)
    in order to add pie approximation in the middle of the ppm file
    """
    maximum_text_size = size/3
    maximum_letter_size = int(maximum_text_size/(digit_number+2))
    # letter sizes must be a multiple of 5
    size_factor = maximum_letter_size//5
    displayed_dict = pixel_dict.copy()
    pixels_to_top = int((size-5*size_factor)/2)
    pixels_to_left = int((size-(digit_number+2)*5*size_factor)/2)
    for number in enumerate(str(displayed_pi)):
        add_number(displayed_dict, pixels_to_top+1, pixels_to_left +
                   1+number[0]*5*size_factor, number[1], size_factor, size)
    return displayed_dict


def color_black(displayed_dict, left_corner_pos, size_factor, size):
    """
    Adds a black square of dimension size_factor**2 in displayed_dict.
    The square's left corner coordinates is left_corner_pos/
    """
    for i in range(size_factor):
        for j in range(size_factor):
            displayed_dict[left_corner_pos+i+j*size] = (0, 0, 0)


def add_number(displayed_dict, pixels_to_top, pixels_to_left, number, size_factor, size):
    """efeaz"""
    zero = {0: False, 1: True, 2: True, 3: False, 4: False, 5: True, 6: False, 7: False, 8: True,
            9: False, 10: True, 11: False, 12: False, 13: True, 14: False, 15: True, 16: False,
            17: False, 18: True, 19: False, 20: False, 21: True, 22: True, 23: False, 24: False}
    one = {0: False, 1: True, 2: True, 3: False, 4: False, 5: False, 6: False, 7: True, 8: False,
           9: False, 10: False, 11: False, 12: True, 13: False, 14: False, 15: False, 16: False,
           17: True, 18: False, 19: False, 20: False, 21: False, 22: True, 23: False, 24: False}
    two = {0: False, 1: True, 2: True, 3: False, 4: False, 5: True, 6: False, 7: False, 8: True,
           9: False, 10: False, 11: False, 12: True, 13: False, 14: False, 15: False, 16: True,
           17: False, 18: False, 19: False, 20: True, 21: True, 22: True, 23: True, 24: False}
    three = {0: True, 1: True, 2: True, 3: True, 4: False, 5: False, 6: False, 7: False, 8: True,
             9: False, 10: False, 11: True, 12: True, 13: True, 14: False, 15: False, 16: False,
             17: False, 18: True, 19: False, 20: True, 21: True, 22: True, 23: True, 24: False}
    four = {0: True, 1: False, 2: False, 3: True, 4: False, 5: True, 6: False, 7: False, 8: True,
            9: False, 10: True, 11: True, 12: True, 13: True, 14: False, 15: False, 16: False,
            17: False, 18: True, 19: False, 20: False, 21: False, 22: False, 23: True, 24: False}
    five = {0: False, 1: True, 2: True, 3: True, 4: False, 5: True, 6: False, 7: False, 8: False,
            9: False, 10: True, 11: True, 12: True, 13: True, 14: False, 15: False, 16: False,
            17: False, 18: True, 19: False, 20: True, 21: True, 22: True, 23: True, 24: False}
    six = {0: True, 1: True, 2: True, 3: True, 4: False, 5: True, 6: False, 7: False, 8: False,
           9: False, 10: True, 11: True, 12: True, 13: True, 14: False, 15: True, 16: False,
           17: False, 18: True, 19: False, 20: True, 21: True, 22: True, 23: True, 24: False}
    seven = {0: True, 1: True, 2: True, 3: True, 4: False, 5: False, 6: False, 7: False, 8: True,
             9: False, 10: False, 11: False, 12: True, 13: False, 14: False, 15: False, 16: True,
             17: False, 18: False, 19: False, 20: True, 21: False, 22: False, 23: False, 24: False}
    eight = {0: True, 1: True, 2: True, 3: True, 4: False, 5: True, 6: False, 7: False, 8: True,
             9: False, 10: False, 11: True, 12: True, 13: False, 14: False, 15: True, 16: False,
             17: False, 18: True, 19: False, 20: True, 21: True, 22: True, 23: True, 24: False}
    nine = {0: True, 1: True, 2: True, 3: True, 4: False, 5: True, 6: False, 7: False, 8: True,
            9: False, 10: True, 11: True, 12: True, 13: True, 14: False, 15: False, 16: False,
            17: False, 18: True, 19: False, 20: True, 21: True, 22: True, 23: True, 24: False}
    dot = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False,
           9: False, 10: False, 11: False, 12: False, 13: False, 14: False, 15: False, 16: False,
           17: False, 18: False, 19: False, 20: False, 21: False, 22: True, 23: False, 24: False}

    number_to_dict = {"0": zero, "1": one, "2": two, "3": three, "4": four,
                      "5": five, "6": six, "7": seven, "8": eight, "9": nine, ".": dot}
    for i in range(5):
        for j in range(5):
            if number_to_dict[number][i+5*j]:
                color_black(
                    displayed_dict, pixels_to_left+size_factor*i +
                    (pixels_to_top+j*size_factor)*size, size_factor, size)


def generate_ppm_file(i, size, displayed_pi, pixel_dict, digit_number):
    """
    Generates a ppm file of dimension size*size,
    maximum color value of 1, color informations are in binary.
    The pixels are stored in pixel_dict.
    Returns the file's name which contains the number of the step as well as
    the current value of the approximation of pi.
    """
    img_name = f"img{i}_"+str(displayed_pi).replace(".", "-")+".ppm"
    displayed_dict = add_pi_display(
        pixel_dict, size, displayed_pi, digit_number)
    with open(img_name, "w", encoding="UTF-8") as img:
        img.write(f"P6\n{size} {size}\n1\n")
    with open(img_name, "ab") as img:
        for i in range(size**2):
            pixel_string = "%c%c%c" % (
                displayed_dict[i][0], displayed_dict[i][1], displayed_dict[i][2])
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


def convert(file_names):
    """The images name contained in file_name
    are used to generate a gif of name pi_approximate.gif"""
    cmd = ['convert'] + file_names + ['pi_approximate.gif']
    subprocess.call(cmd)


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
        file_names.append(generate_ppm_file(
            i, size, displayed_pi, pixel_dict, digit_number))
        convert(file_names)


main(1000, 1000000, 5)
