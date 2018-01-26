# -*- coding:utf-8 -*-

# Python 中的访问控制
# 1. Python 没有提供访问控制机制，没有提供私有属性的功能，全靠程序员自觉
# 2. Python 中定义属性的约定 (见下):
# 2-1. 属性名前不加下划线, 表示可以公开, 类似 public
# 2-2. 属性名前加一个下划线, 表示名义上的私有属性, 类似 private
# 2-3. 属性名前加两个下划线, 通过改名的方式变相实现私有属性的功能, 类似 private

class Programmer(object):
    hobby = 'Play Computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return self.__weight


if __name__ == '__main__':
    programmer = Programmer('Albert', 25, 80)
    print(dir(programmer))
    print(programmer.__dict__)
    print(programmer.get_weight())
    print(programmer._Programmer__weight)
