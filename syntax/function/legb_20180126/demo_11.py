# -*- coding:utf-8 -*-

a_var = 2


def a_func(some_var):
    return 2 ** 3


# 通过函数返回值改变全局变量, 而不是在函数内部修改
a_var = a_func(a_var)
print(a_var)
