import numpy as np
print("Welcome to numpy")
var = np.array([1,2,3,4,5])
print(var)
#2d array
var2 = np.array([[2,3,4,5,6,7],[8,9,10,11,12,13]])
print(var2)
#arrays with only 0
ar = np.zeros((4,8))
print(ar)
#arrays with only 1
ar2 = np.ones((5,4))
print(ar2)
#arrays with a specific number
user=int(input("Enter the number to be filled: "))
one = np.full((4,9),user)
print(one)
#range of numbers and reshaping them
test = np.arange(0,55)
print(test)
#reshaping
reshape = test.reshape(6,7)
print(reshape)