#!/usr/bin/env python3

import math


def print_addition(z_1, z_2):
    print("{} + {} = {}".format(z_1, z_2, z_1 + z_2))


def print_subtraction(z_1, z_2):
    print("{} - {} = {}".format(z_1, z_2, z_1 - z_2))


def print_multiplication(z_1, z_2):
    print("{} * {} = {}".format(z_1, z_2, z_1 * z_2))


def print_division(z_1, z_2):
    print("{} / {} = {}".format(z_1, z_2, z_1 / z_2))


def complex_conjugate(z):
    return z.real + z.imag * -1j


def print_conjugated_multiplication(z_1, z_2):
    z_1_star = complex_conjugate(z_1)
    print("{}* * {} = {}".format(z_1_star, z_2, z_1_star * z_2))


def print_conjugated_division(z_1, z_2):
    z_2_star = complex_conjugate(z_2)
    print("{} / {}* = {}".format(z_1, z_2_star, z_1 / z_2_star))


def main():
    print("1 a)")
    z_1 = complex(1, math.sqrt(3))
    z_2 = complex(1, -1)
    print_addition(z_1, z_2)
    print_subtraction(z_1, z_2)
    print_multiplication(z_1, z_2)
    print_division(z_1, z_2)
    print_conjugated_multiplication(z_1, z_2)
    print_conjugated_division(z_1, z_2)
    print()

    print("1 b)")
    z_1 = complex(2, 3)
    z_2 = complex(3, -5)
    print_addition(z_1, z_2)
    print_subtraction(z_1, z_2)
    print_multiplication(z_1, z_2)
    print_division(z_1, z_2)
    print_conjugated_multiplication(z_1, z_2)
    print_conjugated_division(z_1, z_2)
    print()

    print("1 c)")
    z_1 = complex(4, -5)
    z_2 = complex(4, 5)
    print_addition(z_1, z_2)
    print_subtraction(z_1, z_2)
    print_multiplication(z_1, z_2)
    print_division(z_1, z_2)
    print_conjugated_multiplication(z_1, z_2)
    print_conjugated_division(z_1, z_2)
    print()

    print("1 d)")
    z_1 = complex(0, 1)
    z_2 = complex(-2, -4)
    print_addition(z_1, z_2)
    print_subtraction(z_1, z_2)
    print_multiplication(z_1, z_2)
    print_division(z_1, z_2)
    print_conjugated_multiplication(z_1, z_2)
    print_conjugated_division(z_1, z_2)


if __name__ == "__main__":
    main()
