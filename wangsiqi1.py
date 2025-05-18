import xlrd 
import matplotlib
from matplotlib import rcParams
import matplotlib.pyplot as plt

wb = xlrd.open_workbook('marks.xlsx')         #打开文件
sheetNames = wb.sheet_names()     
sh = wb.sheet_by_index(0)   
sh = wb.sheet_by_name('Sheet1')   
courseList = sh.row_values(0)                # 第一行的值，课程名
print(courseList[2:])                        #打印出所有课程名
course=input("请输入需要展示的课程名:")
m=courseList.index(course)
columnValueList = sh.col_values(m)  
print(columnValueList)                        #打印出所有课程名

scoreList = columnValueList[1:]
print('最高分:',max(columnValueList[1:]))      #输出指定科目最高分、最低分、平均分
print('最低分:',min(columnValueList[1:]))
print('平均分:',sum(columnValueList[1:])/(len(columnValueList)-1))

plt.rcParams['font.family']=['SimHei']          #用来显示中文标签
a=b=c=d=e=0
for x in columnValueList[1:]:                   #循环筛选分数段
    if x>=90:
        a=a+1
    elif x>=80:
        b=b+1
    elif x>=70:
        c=c+1
    elif x>=60:
        d=d+1
    else:
        e=e+1
x=['90~100','80~89','70~79','60~69','0~60']
y=[a,b,c,d,e]
fig,ax=plt.subplots()
ax.set_ylabel('人数')
plt.title('成绩分布图')
plt.bar(x,y,width=0.43,facecolor='orange')
for i,j in zip(x,y):
    plt.text(i,j,j)
plt.show()                                   #输出柱状图

labels='90~100','80~89','70~79','60~69','0~60'
sizes=[a,b,c,d,e]
explode=(0.15,0.05,0.05,0.05,0.05)
fig,ax=plt.subplots()
ax.pie(sizes,explode=explode,labels=labels,autopct='%.1f%%',shadow=False,startangle=90,colors=['gray','orange','blue','green','red','yellow'])
ax.axis('equal')
plt.title('成绩分布图')
plt.show()                                   #输出饼状图
