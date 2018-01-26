# -*- coding:utf-8 -*-

# 多态的两大要素 :
# 1. 继承
# 2. 方法重写

class Programmer(object):

    def info(self):
        print(self.name + " " + self.age)

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
        self._value = value


class BackendProgrammer(Programmer):

    def info(self):
        print(self.name + " " + self.age + " " + self.language)

    def __init__(self, name, age, language):
        super(BackendProgrammer, self).__init__(name, age)
        self._language = language

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value


def introduce(programmer):
    if isinstance(programmer, BackendProgrammer):
        programmer.info()
    else:
        print('type error...')


if __name__ == '__main__':
    coder = Programmer('Maria', '5', )
    introduce(coder)
