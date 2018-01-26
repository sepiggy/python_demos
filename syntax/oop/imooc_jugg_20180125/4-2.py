# -*- coding:utf-8 -*-

# Python 的魔术方法之对象实例的创建

class Person(object):

    def __new__(cls, *args, **kwargs):
        print('call new method...')
        return object.__new__(cls, *args, **kwargs)

    def __init__(self, name, age):
        print('call init method...')
        self._name = name
        self._age = age


if __name__ == '__main__':
    person = Person('Albert', 25)
    print(person.__dict__)
