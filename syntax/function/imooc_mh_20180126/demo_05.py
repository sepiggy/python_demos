# -*- coding:utf-8 -*-

def dec(func):
    print('call dec')

    def in_dec(*args):
        print('in dec args =', args)
        if len(args) == 0:
            return 0
        for val in args:
            if not isinstance(val, int):
                return 0
        return func(*args)

    print('return in_dec')
    return in_dec


@dec
def my_sum(*args):
    print('in my_sum')
    return sum(args)


my_sum = my_sum(1, 2, 3, 4, 5)
print(my_sum)
