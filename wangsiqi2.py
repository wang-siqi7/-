import pandas as pd

xlsx=pd.ExcelFile('学生成绩表.xlsx')            #打开文件
sh=pd.read_excel(xlsx,'Sheet1')

a=sh.dropna()                                    #删除空值
b=a.drop_duplicates()                            #删除重复值

score1=b.sort_values(by='成绩',ascending=False)     #按成绩进行降序排列
print(score1)

x=b['成绩']
score=list(x)                                      #获取所有有效成绩

print('最高分:',max(score))                         #输出最高分、最低分、平均分
print('最低分:',min(score[1:]))
print('平均分:',round(sum(score[1:])/(len(score)-1),0))
