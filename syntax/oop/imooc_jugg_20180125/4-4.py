# -*- coding:utf-8 -*-

# 魔术方法之类的展现

# 1) 对象转换为字符串的三个魔术方法 :
# 1.1) __str__  : 适合人看
# 1.2) __repr__ : 适合机器看
# 1.3) __unicode__

# 2) 展现对象属性:
# __dir__ 供 dir() 调用

class Programmer(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

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
        self._age = value

    def __str__(self):
        return '%s is %s years old' % (self.name, self.age)

    def __dir__(self):
        return self.__dict__.keys()


if __name__ == '__main__':
    p = Programmer('albert', 25)

    # print() 调用 __str__ 魔术方法
    print(p)

    # dir() 调用 __dir__ 魔术方法
    print(dir(p))
