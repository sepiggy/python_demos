#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/make-a-function-that-does-arithmetic/train/python

def arithmetic(a, b, operator):
    d = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y,
    }
    return d[operator](a, b)


if __name__ == '__main__':
    r = arithmetic(24, 6, 'add')
    print(r)
