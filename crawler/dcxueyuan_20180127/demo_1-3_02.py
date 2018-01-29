# -*- coding:utf-8 -*-

import requests

r = requests.get('https://www.zhihu.com/')
print(r)
print(r.status_code)
print(r.text)
print(r.encoding)
print(r.apparent_encoding)
