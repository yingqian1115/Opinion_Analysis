# 計算韓劇名出現次數與長條圖
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
              '～','@','＋','、','+','▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁','▁▁▁▁▁▁▁▁','▁▁','▁','〈','〉']

movie = ['二十五二十一','還有明天','社內相親','三十九','氣象廳的人們','那年我們的夏天','機智醫生','單戀原聲帶',
         '少年法庭','殭屍校園']
koreadrama = pd.read_csv('koreadrama.csv', encoding="utf-8", engine="python")
koreadrama['Title and Content'] = koreadrama['Title'] + koreadrama['Content']
print(koreadrama['Title and Content'])

# 移除無意義自元列
for word in removeword:
    koreadrama['Title and Content'] = koreadrama['Title and Content'] .str.replace(word,'',regex=True)
# print(koreadrama.head()['Title and Content'])
theSTR = koreadrama['Title and Content'].tolist()
print(theSTR)
theSTR = ''.join(theSTR)
# print(type(theSTR))
jieba.load_userdict('./userdict.txt')
words = ([t for t in jieba.cut(theSTR,cut_all=False)])
# print(words) # 前20個切詞成果
# x = words.count("二十五二十一")
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

plt.bar(movie,total_movie,color = colorgroup)
plt.xlabel('dramaname',fontsize=15)
plt.ylabel('trending',fontsize=15)
plt.title('Korea drama analyze', fontsize=20)
plt.xticks(fontsize=10,rotation = 35)

pylab.show()