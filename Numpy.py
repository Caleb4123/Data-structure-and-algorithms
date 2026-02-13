import time
starttime = time.time()
list1 = [1,2,3,4,5]
list2 = []
for i in list1:
    list2.append(i + 5)
print(list2)
endtime = time.time()
totaltime = endtime - starttime
print(totaltime)
list3 = [5,10,15]
list4 = [6,12,18]
print(list3+list4)
#finding average
total = 0
average = 0
count = 0
for i in list1:
    total = total + i
    count = count+1
average = total / count
print(average)
#using numpy

import numpy as np
starttime = time.time()
var = np.array([3,2,1,5,6,7,4])
print(var)
print(var + 10)
endtime = time.time()
totaltime = endtime - starttime
print(totaltime)
#joining 2 arrays
var2 = np.array([3,6,9])
var3 = np.array([4,8,12])


print(var2+var3)
#built in functions of numpy arrays
print(np.max(var))
print(np.min(var))
print(np.mean(var))
print(np.sort(var))
table = np.array([[4,3,2,1,5,7,6],[8,10,9,14,12,11,15],[17,16,19,18,21,22,20]])
print(table)
