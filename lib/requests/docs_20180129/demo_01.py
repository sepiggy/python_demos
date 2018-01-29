# -*- coding:utf-8 -*-

import requests

# 发送请求
r = requests.get('https://github.com/timeline.json')
# print(r)
# print(r.text)
# print(r.encoding)

r = requests.post('http://httpbin.org/post')
# print(r.text)

r = requests.put('http://httpbin.org/put')
# print(r.text)

r = requests.options('http://httpbin.org/delete')
# print(r.text)

# 传递 URL 参数
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('http://httpbin.org/get', params=payload)
# print(r.url)

# 响应内容
r = requests.get('http://www.baidu.com')
# print(r.encoding)
# print(r.text)
# r.encoding = 'utf-8'
# print(r.encoding)
# print(r.text)
# print(r.content)

# JSON 响应内容
r = requests.get('https://github.com/timeline.json')
# print(r.content)
# print(r.text)
# print(r.json())

# 原始响应内容
r = requests.get('https://github.com/timeline.json', stream=True)
# print(r.raw)
# print(r.raw.read(10))

# 定制请求头
# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
# r = requests.get(url, headers=headers)
# print(r)

# 更加复杂的 POST 请求
payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)

# 响应状态码
r = requests.get('http://httpbin.org/get')
# print(r.status_code)
# print(r.status_code == requests.codes.ok)

# bad_r = requests.get('http://httpbin.org/status/404')
# print(bad_r.status_code)

# 响应头
r = requests.get('http://douban.com')
print(r.headers)
