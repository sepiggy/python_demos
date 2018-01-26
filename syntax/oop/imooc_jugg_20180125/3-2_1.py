# -*- coding:utf-8 -*-

# 在类里直接定义属性，这个属性值被所有对象共享
class Programer(object):
    sex = 'male'

    def _get_sex_(self):
        return '1234'


if __name__ == '__main__':
    p1, p2 = Programer(), Programer()
    p2.sex = 'female'
    print(p1.sex, p2.sex)
    print(p1._get_sex_())
