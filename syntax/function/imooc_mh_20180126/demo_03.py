# -*- coding:utf-8 -*-

def func_150(val):
    passline = 90
    if val >= passline:
        print('pass')
    else:
        print('failed')


def func_100(val):
    passline = 60
    if val >= passline:
        print('pass')
    else:
        print('failed')


# 使用闭包统一 func_150 和 func_100
def set_passline(passline):
    def cmp(val):
        if val >= passline:
            print('pass')
        else:
            print('failed')
    return cmp


func_150(89)
func_100(89)

f_150 = set_passline(90)
f_150(89)
print(type(f_150))
print(f_150.__closure__)

f_100 = set_passline(60)
f_100(89)
