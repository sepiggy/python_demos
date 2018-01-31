#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.codewars.com/kata/552c028c030765286c00007d/train/python

def iq_test(numbers):
    l = [int(x) % 2 for x in numbers.split()]
    # 一个奇数, 其余都是偶数
    if sum(l) == 1:
        for i in range(len(numbers)):
            if l[i] == 1:
                return i + 1
    # 一个偶数, 其余都是奇数
    else:
        for i in range(len(numbers)):
            if l[i] == 0:
                return i + 1


if __name__ == '__main__':
    r = iq_test('2 4 7 8 10')
    print(r)
