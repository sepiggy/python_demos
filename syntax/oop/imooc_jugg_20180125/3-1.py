# -*- coding:utf-8 -*-

# Python3 中都是新式类

class NewStyle(object):

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc


if __name__ == '__main__':
    new = NewStyle('new', 'new style class')
    print(new)
    print(type(new))
    print(dir(new))
