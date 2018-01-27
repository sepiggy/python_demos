# -*- coding:utf-8 -*-

passline = 60


def func(val):
    print('%x' % id(val))
    if val >= passline:
        print('pass')
    else:
        print('failed')

    # 闭包
    def in_func():
        print(val)

    return in_func


f = func(89)
f()
print(f.__closure__)

