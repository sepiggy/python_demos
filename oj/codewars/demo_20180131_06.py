#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python


# def binary_array_to_number(arr):
#     sum = 0
#     for i in range(len(arr)):
#         sum += arr[i] * (2 ** (len(arr) - 1 - i))
#     return sum


def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)


if __name__ == '__main__':
    r = binary_array_to_number([0, 0, 0, 1])
    print(r)
