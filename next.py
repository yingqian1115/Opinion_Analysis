# 聲量與評分象限圖
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
# print(movie)
koreadrama = pd.read_csv('koreadrama.csv', encoding="utf-8", engine="python")
koreadrama['Title and Content'] = koreadrama['Title'] + koreadrama['Content']

# 移除無意義自元列
for word in removeword:
    koreadrama['Title and Content'] = koreadrama['Title and Content'] .str.replace(word,'',regex=True)
koreadrama.head()['Title and Content']
theSTR = koreadrama['Title and Content'].tolist()
theSTR = ''.join(theSTR)
# print(theSTR)
jieba.load_userdict('./userdict.txt')
words = ([t for t in jieba.cut(theSTR,cut_all=False)])
# print(words) # 前20個切詞成果
# x = words.count("二十五二十一")
# print(x)

# for j in movie:
#     x = words.count(j)
#     print(x) # 計算每部影集出現次數
total_movie = []
for mov in movie:
    count = 0
    for art in words:
        if mov in art:
            count += 1
    total_movie.append(count)
# print(total_movie)
med = statistics.median(total_movie)
print(med)
bean = [8.2, 6.7, 8.1, 6.8, 6.5, 8.7, 9.5, 7.5, 8.7, 6.3 ]
# print(bean)
score_avg = statistics.median(bean)
print(score_avg)

voice_list = [] #儲存聲量
bean_list = [] #儲存評分
axe_list = [] #儲存象線
print(len(bean))
for i in range(len(bean)):
    if bean[i]>score_avg and total_movie[i] > med:
        axe = '1_第一象限'
    elif bean[i] > score_avg and total_movie[i] <= med:
        axe = '4_第四象限'
    elif bean[i] <= score_avg and total_movie[i] > med:
        axe = '2_第二象限'
    else:
        axe = '3_第三象限'
    voice_list.append(total_movie[i])
    bean_list.append(bean[i])
    axe_list.append(axe)

final1 = pd.DataFrame(zip(voice_list, bean_list, axe_list, movie), columns=['聲量', '評分', '象限', '劇名'])
final1 = final1.sort_values('象限')
final1.to_csv('score.csv', encoding = 'utf-8-sig')
print(final1.head(10))

fig = px.scatter(final1, x="評分", y="聲量", color= "象限", hover_data= ["劇名"])
fig.update_layout(
title = '成本效益評估分析',
shapes=[
# 設定X軸
dict({
'type': 'line',
'x0': score_avg,
'y0': -100,
'x1': score_avg,
'y1': final1['聲量'].max()*1.1,
'line': {
'color': '#5CADAD',
'width': 2}}),
# 設定Y軸
dict({
'type': 'line',
'x0': 0,
'y0': med,
'x1': final1['評分'].max()*1.1,
'y1': med,
'line': {
'color': '#5CADAD',
'width': 2}})])
fig.show()

