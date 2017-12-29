# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time

def get_itme_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, "lxml")
    title_list = soup.select("div.tc.txt > h1 > em")
    title = title_list[0].text
    read_list = soup.select('#readerFs > p')
    textAll = ''
    for text in read_list:
        textAll = textAll + text.text + '\n'
    return title + '\n' + textAll + '-----------------------------------\n'


url = 'http://book.zongheng.com/showchapter/625442.html'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, "lxml")
href_list = soup.select("td.chapterBean > a")
print(href_list)
txtNames = soup.select('div.tc.txt > h1')
txtName = txtNames[0].text
print(txtName)

txtOut = ''
txtCount = 0
filePath = 'D:/python/study/%s.txt' % txtName
for href in href_list:
    link =(href.get("href"))
    txtOut = txtOut + get_itme_info(link)
    print("Done:%s" % href)
    time.sleep(0.5)
    if txtCount % 10 == 0:
        with open(filePath, 'w', encoding='gbk', errors='ignore') as f:
            f.write(txtOut)
            print('前%s章生成结束' % txtCount)
    txtCount += 1

print('全文生成结束')




# filePath = 'D:/python/study/%s.txt' % txtName
# with open(filePath, 'w', encoding='gbk', errors='ignore') as f:
#     f.write(txtOut)
#


