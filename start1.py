# 從mysql取回資料並算出韓劇出現的次數製作成長條圖
import pymysql
import drama
import jieba
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.express as px
import plotly.offline as py
import matplotlib.pyplot as plt
import pylab
import statistics
import numpy
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
jieba.set_dictionary("dict.txt.big") # 讀取結巴字典
colorgroup = ['#c6a300','#fff8d7','#AE8F00','#ffd306','#ffed97','#ffe66F','#FFED97','#FFF0AC','#FFE153','#EAC100']
colorgroup2 = ['#cd0003','#e60003','#ff0004','#ff1a1d','#ff3436','#ff4d4f','#ff6768','#ff8181','#ff9a9b','#ffb4b4']
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
        kkresult = cursor.fetchall()
        print('complete')

except Exception as e:
    print(e)

movie = ['二十五二十一','還有明天','社內相親','三十九','氣象廳的人們','那年我們的夏天','機智醫生','單戀原聲帶',
         '少年法庭','殭屍校園']
print(type(kkresult))
kkresult = list(kkresult)
print(type(kkresult))
kk = numpy.array(kkresult)
print(type(kk))
theSTR = kk.tolist()
print(type(theSTR))
strr = []
for i in range(len(theSTR)):
    for j in theSTR[i]:
       strr.append(j)
# print(strr)
strr = "".join(strr)
jieba.load_userdict('./userdict.txt')
words = ([t for t in jieba.cut(strr,cut_all=False)])
# x = words.count('二十五二十一') # 測試劇名計算結果
# print(x)

for j in movie:
    x = words.count(j)
    print(x) # 計算每部影集出現次數
total_movie = []
for mov in movie:
    count = 0
    for art in words:
        if mov in art:
            count += 1
    total_movie.append(count)
print(total_movie)
med = statistics.median(total_movie)
print(med)


movie1 = ['二十五\n二十一','還有明天','社內相親','三十九','氣象廳\n的人們','那年我們\n的夏天','機智醫生','單戀\n原聲帶',
         '少年法庭','殭屍校園']
plt.figure(figsize=(10,6))
plt.bar(movie1,total_movie,color = colorgroup)
plt.xlabel('dramaname',fontsize=10)
plt.ylabel('trending',fontsize=10)
plt.title('Korea drama analyze', fontsize=16)
plt.xticks(fontsize=8)
pylab.show()