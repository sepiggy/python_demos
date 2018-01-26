# -*- coding:utf-8 -*-

class Programmer(object):
    hobby = 'Play Computer'

    def __init__(self, name, age, weight):
        self._name = name
        self._age = age
        self._weight = weight

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def weight(self):
        return self._weight

    @name.setter
    def name(self, value):
        self._name = value

    @age.setter
    def age(self, value):
        self._age = value

    @weight.setter
    def weight(self, value):
        self._weight = value

    def info(self):
        return self.name + " " + str(self.age) + " " + str(self.weight)


class BackendProgrammer(Programmer):
    def __init__(self, name, age, weight, language):
        super(BackendProgrammer, self).__init__(name, age, weight)
        self._language = language


if __name__ == '__main__':
    # programmer = Programmer('Jms', 28, 80)
    programmer = BackendProgrammer('Jms', 28, 80, 'Python')
    print(dir(programmer))
    print(programmer.__dict__)
    print(type(programmer))
    print(isinstance(programmer, Programmer))
