import requests # 网络请求
import urllib.request as urlopen
import re
url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
wb_data = urlopen.urlopen(url)
res = str(wb_data.read())
print(res)
mes = re.findall(r'<!--.*-->', res)

mes1 = mes[0].replace('find rare characters in the mess below:', '')
mes2 = mes1.replace(r'\n', '')
pasw = re.findall(r'[a-z]|[A-Z]|[0-9]', mes2)
url = ''
for i in pasw:
    url += i

print(url)


