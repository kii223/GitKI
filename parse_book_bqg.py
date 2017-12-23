# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time

def get_itme_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, "lxml")
    title_list = soup.select("#wrapper > div.book.reader > div.content > h1")
    title = title_list[0].text
    read_list = soup.select('#content')
    textAll = ''
    for text in read_list:
        textAll = textAll + text.text + '\n'
    text_newline = textAll.replace('        ', '\n')
    return title + '\n' + text_newline + '--------------------------------------\n'


url = "http://www.biqukan.com/1_1094/"

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, "lxml")
href_list = soup.select("div.listmain > dl > dd > a")
print(href_list)
txtNames = soup.select('body > div.book > div.info > h2')
txtName = txtNames[0].text
print(txtName)

txtOut = ''
for href in href_list:
    link = ('http://www.biqukan.com' + href.get("href"))
    txtOut = txtOut + get_itme_info(link)
    print("Done:%s" % href)
    time.sleep(0.3)

filePath = 'D:/python/study/%s.txt' % txtName
print(filePath)
with open(filePath, 'w', encoding='gbk', errors='ignore') as f:
    f.write(txtOut)
    print('生成结束')


