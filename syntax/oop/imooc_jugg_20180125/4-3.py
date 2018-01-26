# -*- coding:utf-8 -*-

# 魔术方法之类与运算符 :
# 1) 比较运算符: cmp, eq, lt, gt
# 2) 数字运算符: add, sub, mul, div
# 3) 逻辑运算符: or, and

class Programmer(object):
    def __init__(self, name, age):
        self._name = name
        if isinstance(age, int):
            self._age = age
        else:
            raise Exception('age must be int')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self._age = value
        else:
            raise Exception('age must be int')

    def __eq__(self, other):
        # 先判断类型
        if isinstance(other, Programmer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('The type of object must be Programmer')

    def __gt__(self, other):
        # 先判断类型
        if isinstance(other, Programmer):
            if self.age > other.age:
                return True
            else:
                return False
        else:
            raise Exception('The type of object must be Programmer')

    def __add__(self, other):
        # 先判断类型
        if isinstance(other, Programmer):
            return self.age + other.age
        else:
            raise Exception('The type of object must be Programmer')


if __name__ == '__main__':
    Maria = Programmer('Maria', 22)
    Tom = Programmer('Tom', 21)
    print(Maria == Tom)
    print(Maria < Tom)
    print(Maria + Tom)
