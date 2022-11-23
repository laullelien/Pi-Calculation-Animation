#! /usr/bin/env python3
"""Graphical module"""
from sys import argv
import subprocess
import approximate_pi


def generate_pixel_list(window_size):
    """
    Returns a list of dimension window_size² representing pixels.
    At first, it only stores 1s, white pixels
    """
    return [1]*window_size**2


def coordinate_conversion(point, window_size):
    """
    Transforms a point of coordinates (x,y)
    in another point of coordinates (u,v) and returns it
    -1<x,y<1
    0<=u,v<=window_size-1
    x and y are floating numbers
    u and v are integers
    """
    u_coord = int((point[0]+1)*window_size/2)
    v_coord = int((point[1]+1)*window_size/2)
    return (u_coord, v_coord)


def next_step(pixel_list, window_size, point_number):
    """
    Generates ⌈point_number/10⌉ points, stores them as pixels in
    pixel_list. They are stored as 2s (red) if they are
    in the disc and 3s (blue) otherwise. Also returns the
    approximation of pi calculated with these points.
    """
    in_circle_points = 0
    for _ in range(int(point_number/10 + 1)):
        point = approximate_pi.random_point()
        in_circle = approximate_pi.in_circle(point)
        point = coordinate_conversion(point, window_size)
        if in_circle:
            in_circle_points += 1
            pixel_list[point[1]*window_size+point[0]] = 2
        else:
            pixel_list[point[1]*window_size+point[0]] = 3
    return 4*in_circle_points/int(point_number/10 + 1)


def create_pi_dict(window_size, displayed_pi, digit_nb):
    """
    Returns a dictionary with black pixels. Its keys
    are the pixel numbers allowing to display pi.
    """
    maximum_text_size = window_size/3
    maximum_letter_size = int(maximum_text_size/(digit_nb+2))
    # letter sizes must be a multiple of 5
    size_factor = maximum_letter_size//5
    pixels_to_top = int((window_size-5*size_factor)/2)
    pixels_to_left = int((window_size-(digit_nb+2)*5*size_factor)/2)
    pi_dict = {}
    for number in enumerate(str(displayed_pi)+"0"*(2+digit_nb-len(str(displayed_pi)))):
        add_number(pi_dict, pixels_to_top+1, pixels_to_left +
                   1+number[0]*5*size_factor, number[1], size_factor, window_size)
    return pi_dict


def add_number(pi_dict, pixels_to_top, pixels_to_left, number, size_factor, window_size):
    """
    Adds the pixels numbers of the pixel that are required to display the number passed in as a parametre
    to pi_dict thanks to the coordinates of the number's left corner.
    """
    zero = {1, 2, 5, 8, 10,
            13, 15, 18, 21, 22}
    one = {1, 2, 7, 12, 17, 22}
    two = {1, 2, 5, 8, 12, 16, 20, 21, 22, 23}
    three = {0, 1, 2, 3, 8, 11, 12, 13, 18, 20, 21, 22, 23}
    four = {0, 3, 5, 8, 10,
            11, 12, 13, 18, 23}
    five = {1, 2, 3, 5, 10, 11, 12, 13, 18, 20, 21, 22, 23}
    six = {0, 1, 2, 3, 5, 10, 11, 12, 13, 15, 18, 20, 21, 22, 23}
    seven = {0, 1, 2, 3, 8, 12, 16, 20}
    eight = {0, 1, 2, 3, 5, 8, 11, 12, 15, 18, 20, 21, 22, 23}
    nine = {0, 1, 2, 3, 5, 8, 10, 11, 12, 13, 18, 20, 21, 22, 23}
    dot = {22}

    number_to_dict = {"0": zero, "1": one, "2": two, "3": three, "4": four,
                      "5": five, "6": six, "7": seven, "8": eight, "9": nine, ".": dot}
    for i in range(5):
        for j in range(5):
            if i+5*j in number_to_dict[number]:
                color_black(
                    pi_dict, pixels_to_left+size_factor*i +
                    (pixels_to_top+j*size_factor)*window_size, size_factor, window_size)


def color_black(pi_dict, left_corner_pos, size_factor, window_size):
    """
    Adds the pixel numbers of a black square of dimension size_factor**2 in pi_dict.
    The square's left corner coordinates are left_corner_pos.
    """
    for i in range(size_factor):
        for j in range(size_factor):
            pi_dict[left_corner_pos+i+j*window_size] = 0


def generate_ppm_file(i, window_size, displayed_pi, pixel_list, digit_nb):
    """
    Generates a ppm file of dimension window_size*window_size,
    maximum color value of 1, color informations are in binary.
    The pixels are stored in pixel_list.
    Returns the file's name which contains the number of the step, as well as
    the current value of the approximation of pi with the right number of digits digit_nb.
    """
    pi_string = displayed_pi.replace(".", "-")
    img_name = f"img{i}_{pi_string}.ppm"
    pi_dict = create_pi_dict(window_size, displayed_pi, digit_nb)
    pixel_to_bites = {0: b"\x00\x00\x00", 3: b"\x00\x00\x01",
                      2: b"\x01\x00\x00", 1: b"\x01\x01\x01"}
    with open(img_name, "w", encoding="utf-8") as img:
        img.write(f"P6\n{window_size} {window_size}\n1\n")
    with open(img_name, "ab") as img:
        for i in range(window_size**2):
            if i in pi_dict:
                img.write(pixel_to_bites[pi_dict[i]])
            else:
                img.write(pixel_to_bites[pixel_list[i]])
    return img_name


def average(number_list):
    """
    Returns the average of the numbers in the list.
    """
    return sum(number_list)/len(number_list)


def modify_digit_nb(number, digit_nb):
    """
        Returns a new number which is the number
        passed in with only digit_nb digits
        after its comma.
    """
    return f"{number:.{digit_nb}f}"


def convert(file_names):
    """
    The image names contained in file_name
    are used to generate a gif of name approximate_pi.gif.
    """
    cmd = ["convert", "-delay", "25"] + file_names + ["approximate_pi.gif"]
    subprocess.call(cmd)


def main():
    """   
    Generates the 10 ppm files and the gif
    window_size, point_number >= 100
    1 <= digit_nb <= 5
    window_size, point_number and digit_nb are integers.
    """
    if len(argv) != 4:
        print("use: ./draw.pi window_size point_number digit_nb")
    for element in (argv[1], argv[2], argv[3]):
        if not element.isdigit():
            raise ValueError(f"{element} is not an interger")
    if int(argv[1]) < 100 or int(argv[2]) < 100 or int(argv[3]) < 1 or int(argv[3]) > 5:
        raise ValueError(
            "Argument values must respect window_size >= 100, point_number >= 100, 1 <= digit_nb <= 5")
    window_size, point_number, digit_nb = [int(arg) for arg in argv[1:]]
    pi_list = []  # contains the 10 approximations of pi
    file_names = []
    pixel_list = generate_pixel_list(window_size)
    for i in range(10):
        pi_approx = next_step(pixel_list, window_size, point_number)
        pi_list.append(pi_approx)
        displayed_pi = average(pi_list)
        displayed_pi = modify_digit_nb(displayed_pi, digit_nb)
        file_names.append(generate_ppm_file(
            i, window_size, displayed_pi, pixel_list, digit_nb))
    convert(file_names)


if __name__ == "__main__":
    main()
