# -*- coding:utf-8 -*-

# Python 中类的方法也可以看作是类的属性, 其属性类型是 class 'method'

class Test(object):
    def test(self):
        print('this is test attr')


if __name__ == '__main__':
    a = Test()
    a.test()
    print(type(a.test))  # class 'method'
    print('-----下面更改方法属性-----')
    a.test = '123'
    print(a.test)
    print(type(a.test))  # class 'str'
