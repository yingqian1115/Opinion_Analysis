from selenium import webdriver
import requests
import bs4
import re

# 使用chrome的webdriver
# browser = webdriver.Chrome()
browser = webdriver.Chrome('./chromed=driver')
# 開啟google新聞頁面
browser.get('https://news.google.com/topstories?hl=zh-TW&gl=TW&ceid=TW:zh-Hant')
# 關閉瀏覽器
# browser.close()

element = browser.find_element_by_class_name('Ax4B8.ZAGvjd')
w = "氣象廳結局"
element.send_keys(w)
buttom = browser.find_element_by_class_name("gb_nf")
buttom.click()
res = requests.get("https://news.google.com/search?q="+w+"&hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")
data = bs4.BeautifulSoup(res.text, "html.parser")
titles = data.find_all("h3")
t1 = []
for title in titles:
    t1.append(title.text)
# print(t1)
titles1 = data.find_all("h4")
t2 = []
for title1 in titles1:
    t2.append(title1.text)
# print(t2)

total = t1 + t2
print(total)

sen = []
for t in total:
    source = t

    for i in range(len(source)):
        x = ""
        if "《" in source[i]:
            x = x + source[i]
            j = i + 1
            while source[j] not in "》":
                x = x + source[j]
                j = j + 1
            else:
                y = x + "》"
                sen.append(y)
if len(sen) == 0:
    pass
else:
    print(sen)

sens = []
for s in sen:
    if s in sens:
        continue
    else:
        sens.append(s)
removeword = ['《','》','span','class','f3','https','imgur','h1','_   blank','href','rel','nofollow',
              'target','cdn','cgi','b4','jpg','hl','b1','f5','f4','goo.gl','f2','email','map'
    ,'f1','f6','__cf___','data','bbs', 'html','cf','f0','b2','b3','b5','b6','原文內容','原文連結',
              '作者', '標題','時間','看板','<','>','，','。','？','—','閒聊','・','/', ' ','=','\"',
              '\n', '\r','」','「','！','[',']','：','‧','╦','╔','╗','║','╠','╬','╬',':','╰','╩',
              '╯','╭','╮','│','╪','─','《','》','_','.','、','（','）','','*','※','~','○','”','“',
              '～','@','＋','、','+','▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁','▁▁▁▁▁▁▁▁','▁▁','▁','〈','〉']
gsen = []
for g in sen:
    for word in removeword:
        if word in g:
            g = g.replace(word, '')
        else:
            continue
    gsen.append(g)
print(gsen)



sen2 = []
for gs in gsen:
    if gs in sen2:
        continue
    else:
        sen2.append(gs)
print(sen2)

for y in sen2:
    c = 0
    for yy in range(len((gsen))):
        if y == gsen[yy]:
            c += 1

    print(c)
# # 使用chrome的webdriver
# browser = webdriver.Chrome()
# # browser = webdriver.Chrome('./chromed=driver')
# # 開啟google新聞頁面
# browser.get('https://news.google.com/topstories?hl=zh-TW&gl=TW&ceid=TW:zh-Hant')
# # 關閉瀏覽器
# # browser.close()
#
# element = browser.find_element_by_class_name('Ax4B8.ZAGvjd')
# w = "2521"
# element.send_keys(w)
# buttom = browser.find_element_by_class_name("gb_nf")
# buttom.click()
# res = requests.get("https://news.google.com/search?q="+w+"&hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")
# data = bs4.BeautifulSoup(res.text, "html.parser")
# titles = data.find_all("h3")
# t1 = []
# for title in titles:
#     t1.append(title.text)
# # print(t1)
# titles1 = data.find_all("h4")
# t2 = []
# for title1 in titles1:
#     t2.append(title1.text)
# # print(t2)
#
# total = t1 + t2
# print(total)
#
# sen = []
# for t in total:
#     source = t
#
#     for i in range(len(source)):
#         x = ""
#         if "《" in source[i]:
#             x = x + source[i]
#             j = i + 1
#             while source[j] not in "》":
#                 x = x + source[j]
#                 j = j + 1
#             else:
#                 y = x + "》"
#                 sen.append(y)
# if len(sen) == 0:
#     pass
# else:
#     print(sen)
#
# sens = []
# for s in sen:
#     if s in sens:
#         continue
#     else:
#         sens.append(s)
#
#
