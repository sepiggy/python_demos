#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# http://www.codewars.com/kata/586f6741c66d18c22800010a/train/python

def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    nums = []
    while (begin_number <= end_number):
        nums.append(begin_number)
        begin_number += step
    return sum(nums)


if __name__ == '__main__':
    r = sequence_sum(2, 6, 2)
    print(r)
