#! /usr/bin/env python3
"""Graphical module"""
from sys import argv
import subprocess
import approximate_pi
import time


def generate_pixel_list(window_size):
    """
    Returns a list of dimension window_size²representing pixels.
    At fist, it only stores (1,1,1), white pixels
    """
    return [(1, 1, 1)]*window_size**2


def coordinate_conversion(point, window_size):
    """
    Transforms a point of coordinate (x,y)
    in an other point of coordinate (u,v) and returns it
    -1<x,y<1
    0<=u,v<=window_size-1
    x and y are floating numbers
    u and v are integers
    """
    u_coord = int((point[0]+1)*window_size/2)
    v_coord = int((point[1]+1)*window_size/2)
    if u_coord == window_size:
        u_coord -= 1
    if v_coord == window_size:
        v_coord -= 1
    return (u_coord, v_coord)


def next_step(pixel_list, window_size, point_number):
    """
    Generates ⌈point_number/10⌉ points, stores them as pixels in
    pixel_list. They are stored as (1,0,0) (red) if they are
    in the disc and (0,0,1) (blue) otherwise. Also returns the
    approximation of pi calculated with these points
    """
    in_circle_points = 0
    for _ in range(int(point_number/10 + 1)):
        point = approximate_pi.random_point()
        in_circle = approximate_pi.in_circle(point)
        point = coordinate_conversion(point, window_size)
        if in_circle:
            in_circle_points += 1
            pixel_list[point[1]*window_size+point[0]] = (1, 0, 0)
        else:
            pixel_list[point[1]*window_size+point[0]] = (0, 0, 1)
    return 4*in_circle_points/int(point_number/10 + 1)


def create_pi_dict(window_size, displayed_pi, digit_number):
    """
    Returns a dictionnary with black pixels (0,0,0). Its keys
    are the pixel numbers of the pixels that allow to display pi
    """
    maximum_text_size = window_size/3
    maximum_letter_size = int(maximum_text_size/(digit_number+2))
    # letter sizes must be a multiple of 5
    size_factor = maximum_letter_size//5
    pixels_to_top = int((window_size-5*size_factor)/2)
    pixels_to_left = int((window_size-(digit_number+2)*5*size_factor)/2)
    pi_dict = {}
    for number in enumerate(str(displayed_pi)+"0"*(2+digit_number-len(str(displayed_pi)))):
        add_number(pi_dict, pixels_to_top+1, pixels_to_left +
                   1+number[0]*5*size_factor, number[1], size_factor, window_size)
    return pi_dict


def color_black(pi_dict, left_corner_pos, size_factor, window_size):
    """
    Adds the pixel numbers of a black square of dimension size_factor**2 in pi_dict.
    The square's left corner coordinates is left_corner_pos
    """
    for i in range(size_factor):
        for j in range(size_factor):
            pi_dict[left_corner_pos+i+j*window_size] = (0, 0, 0)


def add_number(pi_dict, pixels_to_top, pixels_to_left, number, size_factor, window_size):
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
                    pi_dict, pixels_to_left+size_factor*i +
                    (pixels_to_top+j*size_factor)*window_size, size_factor, window_size)


def generate_ppm_file(i, window_size, displayed_pi, pixel_list, digit_number):
    """
    Generates a ppm file of dimension window_size*window_size,
    maximum color value of 1, color informations are in binary.
    The pixels are stored in pixel_list.
    Returns the file's name which contains the number of the step, i as well as
    the current value of the approximation of pi with the right number of digit digit_number.
    """
    pi_string = displayed_pi.replace(".", "-")
    img_name = f"img{i}_{pi_string}.ppm"
    pi_dict = create_pi_dict(window_size, displayed_pi, digit_number)
    t0 = time.time()
    pixel_to_bytes = {(0, 0, 0): b"\x00\x00\x00", (0, 0, 1): b"\x00\x00\x01", (0, 1, 0): b"\x00\x01\x00", (0, 1, 1): b"\x00\x01\x01",
                      (1, 0, 0): b"\x01\x00\x00", (1, 0, 1): b"\x01\x00\x01", (1, 1, 0): b"\x01\x01\x00", (1, 1, 1): b"\x01\x01\x01"}
    with open(img_name, "w", encoding="utf-8") as img:
        img.write(f"P6\n{window_size} {window_size}\n1\n")
    with open(img_name, "ab") as img:
        for i in range(window_size**2):
            if i in pi_dict:
                img.write(pixel_to_bytes[pi_dict[i]])
            else:
                img.write(pixel_to_bytes[pixel_list[i]])
    print("write", time.time()-t0)
    return img_name


def average(number_list):
    """Returns the average of the numbers in the list"""
    return sum(number_list)/len(number_list)


def modify_digit_number(number, digit_number):
    """
        Returns a new number which is the number
        passed in with only digit_number digits
        after its comma
    """
    return f"{number:{digit_number}f}"


def convert(file_names):
    """The images name contained in file_name
    are used to generate a gif of name approximate_pi.gif"""
    cmd = ['convert'] + file_names + ['approximate_pi.gif']
    subprocess.call(cmd)


def main():
    """
    Generates the 10 ppm files and the gif
    window_size,point_number>=100
    1<=digit_number<=5
    window_size, point_number and digit_number are integers
    """
    t0 = time.time()
    if len(argv) != 4:
        print("use: ./draw.pi window_size point_number digit_number")
    for element in (argv[1], argv[2], argv[3]):
        if not element.isdigit():
            raise TypeError(f"{element} is not an interger")
    if int(argv[1]) < 100 or int(argv[2]) < 100 or int(argv[3]) < 1 or int(argv[3]) > 5:
        raise ValueError(
            "Argument values must respect window_size >= 100, point_number >= 100, 1 <= digit_number <= 5")
    window_size, point_number, digit_number = [int(arg) for arg in argv[1:]]
    pi_list = []  # contains the 10 approximations of pi
    file_names = []
    pixel_list = generate_pixel_list(window_size)
    for i in range(10):
        pi_approx = next_step(pixel_list, window_size, point_number)
        pi_list.append(pi_approx)
        displayed_pi = average(pi_list)
        displayed_pi = modify_digit_number(displayed_pi, digit_number)
        file_names.append(generate_ppm_file(
            i, window_size, displayed_pi, pixel_list, digit_number))
    convert(file_names)
    print("main", time.time()-t0)


if __name__ == "__main__":
    main()
