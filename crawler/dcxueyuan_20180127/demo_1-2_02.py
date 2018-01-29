# -*- coding:utf-8 -*-

import requests

r = requests.get('http://www.baidu.com')
print(r)
print(type(r))

print(r.encoding)
# print(r.text)
r.encoding = 'utf-8'
print(r.text)
