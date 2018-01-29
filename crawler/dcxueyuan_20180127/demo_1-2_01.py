# -*- coding:utf-8 -*-

import urllib.request

with urllib.request.urlopen('http://www.baidu.com/') as f:
    # print(type(f))
    print(f.read(500))
    # print(f.read(500).decode('utf-8'))

