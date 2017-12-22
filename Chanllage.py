# -*- coding: utf-8 -*-

# 字符表替换 1关
# intab = 'abcdefghijklmnopqrstuvwxyz'
# outab = 'cdefghijklmnopqrstuvwxyzab'
#
# transtab = str.maketrans(intab,outab)
#
# text = 'map'
#
# out = text.translate(transtab)
#
# print(out)


# 字符查找 2关
# import requests # 网络请求
# import urllib.request as urlopen
# import re
# url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
# wb_data = urlopen.urlopen(url)
# res = str(wb_data.read())
# print(res)
# mes = re.findall(r'<!--.*-->', res)
#
# mes1 = mes[0].replace('find rare characters in the mess below:', '')
# mes2 = mes1.replace(r'\n', '')
# pasw = re.findall(r'[a-z]|[A-Z]|[0-9]', mes2)
# url = ''
# for i in pasw:
#     url += i
#
# print(url)


# 字符查找 3关
# import requests # 网络请求
# import urllib.request as urlopen
# import re
# url = 'http://www.pythonchallenge.com/pc/def/equality.html'
# wb_data = urlopen.urlopen(url)
# res = str(wb_data.read())
#
# mes = re.findall(r'<!--.*-->', res)
# mes1 = mes[0].replace(r'\n', '')
# pasw = re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', mes1)
#
# pasw1 = ''.join(pasw)
#
#
# pasw2 = re.findall(r'[A-Z]{3}[a-z][A-Z]{3}', pasw1)
# pasw3 = ''.join(pasw2)
#
# pasw4 = re.findall(r'[a-z]', pasw3)
# pasw5 = ''.join(pasw4)
# print(pasw5)

# 网址链 4关
# import requests  # 网络请求
# import urllib.request as urlopen
# import re
# import time
#
#
# n = 0
# index = '63579'
#
# while n < 400:
#     url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'% index
#     wb_data = urlopen.urlopen(url)
#     res = str(wb_data.read())
#     nexturl = re.findall(r'[0-9]', res)
#     index = str(int(int(''.join(nexturl))))
#     print(res + 'next index is:' + index)
#     n += 1
#     print('%d--------------' % n)
#     time.sleep(0.7)


# peak hell 5关
# import requests  # 网络请求
# import urllib.request as urlopen
# import re
# import time
# import pickle

# pick_file = open('banner.p', 'rb')
# data = pickle.load(pick_file)
# pick_file.close()
# print(data)
# for i in data:
#     first = ''
#     for j in i:
#         first += j[0] * j[1]
#     print(first)





