#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/python

def gimme(input_array):
    return input_array.index(sorted(input_array)[1])


if __name__ == '__main__':
    r = gimme([5, 10, 14])
    print(r)
