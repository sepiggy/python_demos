#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# http://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python

def tower_builder(n_floors):
    if n_floors == 1:
        return ['*']
    return [' ' * ((2 * n_floors - 1 - x) // 2) + '*' * x + ' ' * ((2 * n_floors - 1 - x) // 2) for x in
            range(1, 2 * n_floors, 2)]


if __name__ == '__main__':
    r = tower_builder(2)
    print(r)
