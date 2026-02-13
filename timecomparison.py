import time
import numpy as np
list1 = list(range(10000))
starttime = time.time()
list2 = []
for i in list1:
    list2.append(i + 5)
#print(list2)
print(time.time()-starttime)
#endtime = time.time()
#total = endtime - starttime
#print(total)

#arrays
var = np.array(range(10000))
starttime = time.time()
var2 = np.array(var + 5)
print(time.time()-starttime)
#endtime = time.time()
#total = endtime - starttime
#print(total)