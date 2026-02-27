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
test = np.arange(0,56)
print(test)
#reshaping
reshape = test.reshape(7,8)
print(reshape)
#maths with arrays
print("Math with arrays")
test1 = np.array([2,4,6,8,10])
test2 = np.array([1,2,3,4,5])
print("addition: ",test1 + test2)
print("subtraction: ",test1 - test2)
print("division: ",test1 * test2)
print("addition: ",test1 / test2)
#numpy maths functions
test3 = np.array([1,4,25,64,1243])
print("Finding sqaure root")
square = np.sqrt(test3)
print(square)
mean1 = np.mean(test3)
print(mean1)
max1 = np.max(test3)
min1 = np.min(test3)
print(max1)
print(min1)
sum1 = np.sum(test3)
print(sum1)
