# 爬單頁 標題及內容
import requests
from bs4 import BeautifulSoup
import pandas as  pd
res = requests.get("https://www.ptt.cc/bbs/KoreaDrama/index2679.html")
soup = BeautifulSoup(res.text, "html.parser")
# print(soup)
soup1 = soup.select(".title")
# print(soup1)
# for i in soup1: #把list中的文章標題抓下來
#     print("https://www.ptt.cc"+i('a')[0]['href']) #a標籤裡的內容，只要前半段，且在href裡的內容
#要讓網址完整所以要加上http
author,board,title,time,content = [],[],[],[],[]
for i in soup1:
    try:
        res = requests.get("https://www.ptt.cc"+i('a')[0]['href'])
        soup = BeautifulSoup(res.text,"html.parser")
        author.append(soup.select(".article-meta-value")[0].text)
        board.append(soup.select(".article-meta-value")[1].text)
        title.append(soup.select(".article-meta-value")[2].text)
        time.append(soup.select(".article-meta-value")[3].text)
        content.append(soup.select("#main-content")[0].text.split("*")[0].split(time[-1])[1])
    except:
        pass
print(content)

# 資料彙整
# drama = {
#     "Author":author,
#     "Board":board,
#     "Title":title,
#     "Time":time,
#     "Content":content
# }
# ptt_drama = list(zip(author,board,title,time,content))
# df = pd.DataFrame(ptt_drama,columns=["Author","Board","Title","Time","Content"])
# print(df)
# df.to_csv("koreamovie.csv")
# drama_df = pd.DataFrame(drama)
# drama_df.to_csv("koreadrama.csv")

