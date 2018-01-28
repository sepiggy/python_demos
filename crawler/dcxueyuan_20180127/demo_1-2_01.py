# -*- coding:utf-8 -*-

import urllib.request

f = urllib.request.urlopen('http://www.baidu.com/')

# 获取前 500 个字符并修改编码为 utf-8
r = f.read(500).decode('utf-8')

print(r)
