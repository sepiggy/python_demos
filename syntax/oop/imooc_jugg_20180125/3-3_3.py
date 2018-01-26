# -*- coding:utf-8 -*-

# 关于方法的两个装饰器
# 1. @classmethod: 表示类方法, 调用的时候用类名, 而不是某个对象
# 2. @property: 像访问属性一样调用方法


class Programmer(object):
    hobby = 'Play Computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight


if __name__ == '__main__':
    programmer = Programmer('Albert', 25, 80)
    print(dir(programmer))
    print(Programmer.get_hobby())
    print(programmer.get_hobby())
    print(Programmer.get_weight)
    print(programmer.get_weight)
