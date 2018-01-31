#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

def printer_error(s):
    total, bad = len(s), 0
    for ch in s:
        if ch in 'nopqrstuvwxyz':
            bad += 1
    return str(bad) + '/' + str(total)


if __name__ == '__main__':
    r = printer_error('aaaxbbbbyyhwawiwjjjwwm')
    print(r)
