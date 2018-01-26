# -*- coding:utf-8 -*-

a_var = 1


def a_func():
    # global a_var
    # a_var = 1234
    a_var = a_var + 1
    print(a_var, '[ a_var inside a_func() ]')


print(a_var, '[ a_var outside a_func() ]')
a_func()
