import pandas as pd
import matplotlib
from matplotlib import rcParams
import matplotlib.pyplot as plt

xlsx=pd.ExcelFile('人口数据.xlsx')            #打开文件
sh=pd.read_excel(xlsx,'Sheet1')

a=sh.dropna()                               #删除空值
b=a.sort_values(by='人          口          数',ascending=False)        #按人口降序排列
num=b['人          口          数']
number=list(num)
its=number[0]-number[1]-number[2]-number[3]-number[4]-number[5]         #求出其他人口值
x=[number[1],number[2],number[3],number[4],number[5],its]

plt.rcParams['font.family']=['SimHei']    
plt.figure(figsize=(6,6))
ax=plt.axes([0.1,0.1,0.8,0.8])
city=list(b['地    区'])
labels=city[1],city[2],city[3],city[4],city[5],'其    他'
explode=(0.05,0.05,0.05,0.05,0.05,0.05)
plt.pie(x,labels=labels,explode=explode,startangle=60,autopct='%1.1f%%')
plt.title('中国人口普查各省人口占全国情况')
plt.show()
