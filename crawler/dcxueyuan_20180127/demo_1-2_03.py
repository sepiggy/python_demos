# -*- coding:utf-8 -*-

# 爬虫第一步: 使用 requests 获取数据
# 爬虫第二步: 使用 BeautifulSoup4 解析数据
# 爬虫第三步: 使用 pandas 保存数据

import pandas
import requests
from bs4 import BeautifulSoup

r = requests.get('https://book.douban.com/subject/1084336/comments').text
soup = BeautifulSoup(r, 'lxml')
pattern = soup.find_all('p', 'comment-content')
comments = []
for item in pattern:
    comments.append(item.string)
df = pandas.DataFrame(comments)
df.to_csv('comments.csv')
