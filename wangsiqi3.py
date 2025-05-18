import matplotlib
from matplotlib import rcParams
import pandas as pd
import matplotlib.pyplot as plt

xlsx=pd.ExcelFile('gdp.xlsx')                        #打开文件
sh=pd.read_excel(xlsx,'Sheet1')     


data=sh.iloc[0]                                        #某省份从2014年以来的GDP变化图
data2=list(data)
print(data2)
y=data2[-1:-len(data2):-1]
x='2014年','2015年','2016年','2017年','2018年','2019年','2020年','2021年','2022年','2023年'
plt.rcParams['font.family']=['SimHei']                  #用来显示中文标签
plt.title('北京市从2014年以来的GDP变化折线图')
plt.xlabel('年份')
plt.ylabel('G D P 总 值')
plt.xticks(rotation=75)                               #x轴坐标倾斜
plt.plot(x, y, marker='*', linewidth=1, linestyle='--', color='orange')
for a,b in zip(x,y):
    plt.text(a,b,b)
plt.plot(x, y)
plt.show()  

fig,ax=plt.subplots()                             #某一年各省GDP变化表
a=['北京市', '天津市', '河北省', '山西省', '内蒙古自治区', '辽宁省', '吉林省', '黑龙江省', '上海市', '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省', '河南省', '湖北省', '湖南省', '广东省', '广西壮族自治区', '海南省', '重庆市', '四川省', '贵州省', '云南省', '西藏自治区', '陕西省', '甘肃省', '青海省', '宁夏回族自治区', '新疆维吾尔自治区']
b=list(sh['2022年'])

plt.title('2022年各省份GDP折线图')
plt.xlabel('省份')
plt.ylabel('G D P总值')
plt.xticks(rotation=75)                               #x轴坐标倾斜
for i,j in zip(a,b):
    plt.text(i,j,j)
plt.plot(a, b, marker='*', linewidth=1, linestyle='--', color='orange')
plt.plot(a, b)
plt.show()  

fig,ax=plt.subplots()                                 #绘制柱状图     
plt.rcParams['axes.unicode_minus']=False  #用来正常显示负号
plt.title('2022年各省份GDP柱状图')  
plt.xticks(rotation=75)
plt.xlabel('省份')
plt.ylabel('G D P总值')
for i,j in zip(a,b):
    plt.text(i,j,j)
plt.bar(a,b,width=0.35,facecolor='lightskyblue',edgecolor='white')

plt.show()