# 爬很多頁但只爬標題
import requests #導入模組
import bs4 # 導入beautifulSoup 模組:解析HTML工具
import time
import pandas as pd
def get_one_page(URL,a,b):
    # URL = "https://www.ptt.cc/bbs/KoreaDrama/index.html"
    # 設定header與cookie
    my_headers = {'cookie':'over18=1;'}
    # 發送get請求到ptt八卦版
    response = requests.get(URL,headers=my_headers)

    # 把網頁程式碼(html)丟入bs4模組分析
    soup = bs4.BeautifulSoup(response.text,"html.parser")

    ## ptt上方二個欄位 標題和日期
    titles= soup.find_all("div","title")
    date = soup.find_all("div","date")

    # a = []
    # b = []
    for t in titles:
        a.append(t.text.strip())
        # print(t.text.strip())
    for d in date:
        b.append(d.text.strip()) #strip把空白去掉
        # print(d.text.strip())


a = []
b = []

start = 2680 #設定網頁啟始頁
number = 5 #設定要開始頁往後爬多少個
end = start - number #2675
for i in range(start,end,-1):
    # 組成正確url
    link = "https://www.ptt.cc/bbs/KoreaDrama/index"+str(i)+".html"
    # 執行單頁面網頁爬蟲
    get_one_page(link,a,b)
    time.sleep(2)
print(len(a))
print(len(b))

mid_term_marks = {"title": a,
                  "time": b}
mid_term_marks_df = pd.DataFrame(mid_term_marks)

mid_term_marks_df.to_csv("midterm.csv")

KoreaDrama=pd.read_csv('midterm.csv', encoding='utf-8-sig')
print(KoreaDrama)

# ## 查出所有html元素抓出內容
# main_container = soup.find(id='main-container')
# # 把所有文字都抓出來
# all_text = main_container.text
# # 把整個內容切割透過 "--" 切割成兩個陣列
# pre_text = all_text.split("--")[0]  # 若在後面加上[0] 取切割後的第一段，代表只取內容不取留言
# # 把每段文字依據\n切開
# texts = pre_text.split("\n")
# contents = texts[2:]
#
# print(titles)
# print(date)
