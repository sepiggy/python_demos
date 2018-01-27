# -*- coding:utf-8 -*-

# for-loops will use the 01_scope they exist in and leave their defined loop-variable behind

for a in range(5):
    if a == 4:
        print(a, '-> a in for-loop')

print(a, '-> a in global')
