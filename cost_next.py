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

drama_cost = pd.read_csv('cost.csv', encoding = 'utf-8-sig')
# print(drama_cost)

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
dcost = statistics.median(drama_cost['cost'])
print(dcost)


voice_list =[] # 用以儲存聲量
cost_list = [] # 用以儲存成本
axe_list = [] # 用以儲存象限
for i in range(len(drama_cost['cost'])):
    if drama_cost['cost'][i]>dcost and total_movie[i] >med:#1_第一象限
        axe = '1_第一象限'
    elif drama_cost['cost'][i]>dcost and total_movie[i] <= med:
        axe = '4_第四象限'
    elif drama_cost['cost'][i]<=dcost and total_movie[i] > med:
        axe = '2_第二象限'
    else:
        axe = '3_第三象限'
    voice_list.append(total_movie[i])
    cost_list.append(drama_cost['cost'][i])
    axe_list.append(axe)



final2 = pd.DataFrame(zip(voice_list, cost_list, axe_list, movie), columns=['聲量', '成本', '象限', '劇名'])
final2 = final2.sort_values('象限')
final2.to_csv('cost_and_value.csv', encoding = 'utf-8-sig')


fig = px.scatter(final2, x = '成本', y = '聲量', size = '成本', color = '象限',  hover_data=['劇名'])
fig.update_layout(
title = '成本效益評估分析',
shapes=[
# 設定X軸
dict({
'type': 'line',
'x0': dcost,
'y0': -100,
'x1': dcost,
'y1': final2['聲量'].max()*1.2,
'line': {
'color': '#FF00FF',
'width': 2}}),
# 設定Y軸
dict({
'type': 'line',
'x0': 0,
'y0': med,
'x1': final2['成本'].max()*1.1,
'y1': med,
'line': {
'color': '#FF00FF',
'width': 2}})])
fig.show()