import numpy as np

arr=np.random.randint(0, 101, size = 60)        #生成60个整数

print('创建的数组：\n',arr)
print('数组的和：',np.sum(arr))
print('数组的平均值：',np.mean(arr))
print('数组的最大值：',np.max(arr))
print('数组的最小值：',np.min(arr))
print('数组的加权平均值：',np.average(arr))
print('数组的方差：',np.var(arr))
print('数组的标准差：',np.std(arr))

a=np.sort(arr,kind='quicksort')                #快速排序
print("快速排序",a)


b=np.sort(arr,kind='heapsort')                 #堆排序
print("堆排序",b)

c=a[::-1]                                       #降序输出
print("降序输出",c)