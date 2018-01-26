# -*- coding:utf-8 -*-

# print(globals()) # prints global namespace
# print(locals()) # prints local namespace

glob = 1


def foo():
    loc = 5
    print('loc in foo():', 'loc' in locals())


foo()
print('loc in global:', 'loc' in globals())
print('glob in global:', 'foo' in globals())
