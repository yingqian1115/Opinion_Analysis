import jieba
import pymysql
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.express as px
import plotly.offline as py
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
jieba.set_dictionary("dict.txt.big") # 讀取結巴字典
colorgroup = ['#427f8f','#4a8fa1','#559db0','#66a7b8','#77b1c0','#89bbc8','#9ac5d0','#bdd9e0','#cee3e8','#e0edf0']
colorgroup2 = ['#cd0003','#e60003','#ff0004','#ff1a1d','#ff3436','ff4d4f','#ff6768','#ff8181','#ff9a9b','#ffb4b4']

removeword = ['span','class','f3','https','imgur','h1','_   blank','href','rel','nofollow',
              'target','cdn','cgi','b4','jpg','hl','b1','f5','f4','goo.gl','f2','email','map'
    ,'f1','f6','__cf___','data','bbs', 'html','cf','f0','b2','b3','b5','b6','原文內容','原文連結',
              '作者', '標題','時間','看板','<','>','，','。','？','—','閒聊','・','/', ' ','=','\"',
              '\n', '\r','」','「','！','[',']','：','‧','╦','╔','╗','║','╠','╬','╬',':','╰','╩',
              '╯','╭','╮','│','╪','─','《','》','_','.','、','（','）','','*','※','~','○','”','“',
              '～','@','＋','、','+','▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁','▁▁▁▁▁▁▁▁','▁▁','▁','〈','〉',')','(','!','%','-']

movie = ['二十五二十一','還有明天','社內相親','三十九','氣象廳的人們','那年我們的夏天','機智醫生','單戀原聲帶',
         '少年法庭','殭屍校園']
# koreadrama = pd.read_csv('koreadrama.csv', encoding="utf-8", engine="python")
# koreadrama['Title and Content'] = koreadrama['Title'] + koreadrama['Content']
# 資料庫設定
db_setting = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "111586",
    "db": "pttdrama",
    "charset": "utf8"
}
print('連線上資料庫了!')

try:
    # 建立connection物件
    conn = pymysql.connect(**db_setting)
    # 建立cursor物件
    with conn.cursor() as cursor:
        # 新增資料指令
        command = "SELECT title,content FROM drama"
        cursor.execute(command)
        # 取得資料，kkresult已經移除無意義字元
        kkresult = cursor.fetchmany(2)
        print('complete')

except Exception as e:
    print(e)
kkresult = list(kkresult)
for i in range(len(kkresult)):
    kkresult[i] = list(kkresult[i])
    kkresult[i]=kkresult[i][0]+kkresult[i][1]

# print(kkresult)
#移除無意義自元列
for word in removeword:
    for l in range(len(kkresult)):
        kkresult[l] = kkresult[l].str.replace(word,'',regex=True)
# print(koreadrama['Title and Content'])
# print(koreadrama['Title and Content'][0])
# theSTR = koreadrama['Title and Content'].tolist()
# print(theSTR)
# theSTR = ''.join(theSTR)
# print(theSTR)
# jieba.load_userdict('./userdict.txt')
# koreadrama1 =[]
# for k in kkresult:
#     words = ([t for t in jieba.cut(k,cut_all=False)])
#     koreadrama1.append(words)
# print(koreadrama1)
# #統計每個語詞的次數
# words_count = []
# for ws in koreadrama1:
#     count = {}
#     for w in ws:
#         if w in count:
#             count[w]+=1
#         else:
#             count[w]=1
#         words_count.append(count)
# print(words_count)
#
# # 統計每個語詞的頻率(次數/全部單語詞次數)
# words_frequency = []
# for word_count in words_count:
#     all_count = sum(word_count.values()) #單篇文章的所有單詞數量
#     fre = {}
#     for word,count in word_count.items():
#         fre[word] = round(count/all_count,4)
#     words_frequency.append(fre)
# print(words_frequency[5])