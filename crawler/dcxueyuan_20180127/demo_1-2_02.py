# -*- coding:utf-8 -*-

import requests

r = requests.get('http://www.baidu.com')
print(r)

print(r.text)
r.encoding = 'utf-8'
print(r.text)
