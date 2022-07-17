import jieba.analyse
import pandas as pd
jieba.set_dictionary('dict.txt.big')
KoreaDrama=pd.read_csv('midterm.csv', encoding='utf-8-sig')
KoreaDrama.head()
movie = ['社內相親','二十五、二十一','明天/還有明天','單戀原聲帶','氣象廳的人們','少年法庭','']