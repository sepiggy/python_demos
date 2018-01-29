# -*- coding:utf-8 -*-

import requests

r = requests.get('http://www.baidu.com/')
print(r)
print(r.status_code)
print(r.text)
print(r.content)
print(r.encoding)
print(r.apparent_encoding)