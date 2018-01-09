# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time

def get_itme_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, "lxml")
    # title_list = soup.select("#wrapper > div.book.reader > div.content > h1")
    # title = title_list[0].text
    # read_list = soup.select('#content')
    read_list = soup.select('#wrapper > div.book.reader > div.content')
    textAll = ''
    for text in read_list:
        textAll = textAll + text.text + '\n'
    text_newline = textAll.replace('        ', '\n')
    text_newline = text_newline.replace('笔趣阁小说推荐阅读：一念永恒、圣墟、不朽凡人、天道图书馆、人皇纪、巫神纪、武道宗师、绝世战魂、超凡传、\n盖世帝尊、纨绔邪皇、侠行天下、恐怖广播', '')
    text_newline = text_newline.replace('天才壹秒記住『愛♂去÷小?說→網』，為您提供精彩小說閱讀。', '')
    text_newline = text_newline.replace('上一章\n返回目录\n下一章\n加入书签', '')
    text_newline = text_newline.replace('请记住本书首发域名：www.biqukan.com。笔趣阁手机版阅读网址：m.biqukan.com', '')
    text_newline = text_newline.replace('手机用户请访问http://m.ysxiaoshuo', '')
    text_newline = text_newline.replace(url, '')
    text_newline = text_newline.replace('read1()', '')
    text_newline = text_newline.replace('read2()', '')
    text_newline = text_newline.replace('read3()', '')
    text_newline = text_newline.replace('read4()', '')
    text_newline = text_newline.replace('（本章完）', '')
    text_newline = text_newline.replace('（本章未完，请翻页）', '')
    text_newline = text_newline.replace('天才壹秒記住愛♂去÷小說→網，為您提供精彩小說閱讀。最新章节全文阅读', '')
    return text_newline + '--------------------------------------\n'


url = "http://www.biqukan.com/11_11098/"
header ={
    'Cookie': 'UM_distinctid = 1608262d398aa - 0b006d09a466cd - 454f032b - 1fa400 - 1608262d3992b7',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36'
}
wb_data = requests.get(url)
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
    time.sleep(0.3)
    if txtCount % 10 == 0 and txtCount != 0:
        with open(filePath, 'w', encoding='gbk', errors='ignore') as f:
            f.write(txtOut)
            print('前%s章生成结束' % txtCount)
    txtCount += 1




