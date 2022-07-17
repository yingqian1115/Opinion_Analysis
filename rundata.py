# 最終資料(已存成csv檔，已寫入資料庫)
import pymysql
import drama
import requests
from bs4 import BeautifulSoup
import bs4
import time
import pandas as pd
start = 2680 #設定網頁啟始頁

number = 60 #設定要開始頁往後爬多少頁
end = start - number #2620
author,board,title,date,content = [],[],[],[],[]
for i in range(start,end,-1):
    # 組成正確url
    url = "https://www.ptt.cc/bbs/KoreaDrama/index"+str(i)+".html"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    soup1 = soup.select(".title")
    for i in soup1:
        try:
            res = requests.get("https://www.ptt.cc" + i('a')[0]['href'])
            soup2 = BeautifulSoup(res.text, "html.parser")
            title.append(soup2.select(".article-meta-value")[2].text)
            date.append(soup2.select(".article-meta-value")[3].text)
            content.append(soup2.select("#main-content")[0].text.split("※")[0].split(date[-1])[1])
        except:
            pass

    time.sleep(1)
# print(len(title))
# print(len(date))
# print(len(content))



data = {
    "Title":title,
    "Date":date,
    "Content":content
}

# print(data)
# 把資料放到csv檔
# ptt_drama = list(zip(title,date,content))
# df = pd.DataFrame(ptt_drama,columns=["Title","Time","Content"])
# df.to_csv("koreadrama.csv")
# print(df)
# print(data)
#
removeword = ['\n','span','class','f3','https','imgur','h1','_   blank','href','rel','nofollow',
              'target','cdn','cgi','b4','jpg','hl','b1','f5','f4','goo.gl','f2','email','map'
    ,'f1','f6','__cf___','data','bbs', 'html','cf','f0','b2','b3','b5','b6','原文內容','原文連結',
              '作者', '標題','時間','看板','<','>','，','。','？','—','閒聊','・','/', ' ','=','\"'
              , '\r','」','「','！','[',']','：','‧','╦','╔','╗','║','╠','╬','╬',':','╰','╩',
              '╯','╭','╮','│','╪','─','《','》','_','.','、','（','）','','*','※','~','○','”','“',
              '～','@','＋','、','+','▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁','▁▁▁▁▁▁▁▁','▁▁','▁','〈','〉','\'',' ',',','-','|']
article = []
for i in range(len(content)):
    for word in removeword:
        content[i] = content[i].replace(word, '')

    article.append(content[i])


title1 = []
for i in range(len(title)):
    for word in removeword:
        title[i] = title[i].replace(word, '')

    title1.append(title[i])

# 連線資料庫


con = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       passwd = '111586',
                       db = 'pttdrama',
                       charset='utf8')
print('連線上資料庫了!')


#建立操作游標
cursor = con.cursor()
#SQL語法 (for迴圈)

for i in range(len(title)):
        id = i+1
        t = title1[i]
        # d = date[i]
        c = article[i]
        a = "INSERT INTO drama(id, title, content) VALUES  ('" + str(id) + "','" + t + "','" + c + "')"
        try:
            cursor.execute(a)
            # 提交修改
            con.commit()
            print('success')
        except Exception as e:
            # 發生錯誤時停止執行SQL
            con.rollback()
            print('error')
            print(e)


#關閉連線
con.close()
print(len(title1))
print(len(article))