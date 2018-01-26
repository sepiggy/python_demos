# -*- coding:utf-8 -*-

# 因为方法可以看作 Python 的属性, 因此方法的访问控制和之前提到的属性的访问控制是相同的 :
# 分为零个, 一个, 两个下划线三种情况, eg:

class Example(object):
    # 公用方法
    def add(self):
        print('add...')

    # 私有方法 (不被语法限制)
    def _minus(self):
        print('minus...')

    # 私有方法 (被语法限制)
    def __multiply(self):
        print('multiply...')


if __name__ == '__main__':
    example = Example()
    print(example.__dict__)
    example.add()
    example._minus()
    example._Example__multiply()  # 通过这个名称依然可以访问 multiply 方法
