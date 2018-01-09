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


url = "http://www.biqukan.com/11_11098/"
header ={
    'Cookie': 'UM_distinctid = 1608262d398aa - 0b006d09a466cd - 454f032b - 1fa400 - 1608262d3992b7',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36'
}
wb_data = requests.get(url, headers=header)
soup = BeautifulSoup(wb_data.text, "lxml")
href_list = soup.select("div.listmain > dl > dd > a")
print(href_list)
txtNames = soup.select('body > div.book > div.info > h2')
txtName = txtNames[0].text
print(txtName)

txtOut = ''
txtCount = 0
filePath = 'D:/python/study/%s.txt' % txtName
for href in href_list:
    link = ('http://www.biqukan.com' + href.get("href"))
    txtOut = txtOut + get_itme_info(link)
    print("Done:%s" % href.text)
    time.sleep(0.5)
    if txtCount % 10 == 0 and txtCount != 0:
        with open(filePath, 'w', encoding='gbk', errors='ignore') as f:
            f.write(txtOut)
            print('前%s章生成结束' % txtCount)
    txtCount += 1




