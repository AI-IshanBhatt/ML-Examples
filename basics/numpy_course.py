import numpy as np
import pandas as pd

print("Hello Machine Learning")
x = np.array([4,5,6])
y = np.array([1,2,3])
print(y)

z = np.array([[1,2,3],[4,5,6]]) #Mismatch in dimensions works.
print(z)

print(z.shape) #(2,3)2 rows 3 cols

n = np.arange(0, 30, 2) #The size of the steps in array
print(n)

n = n.reshape(3,5) #Reshape into 3,5 array,Have to assign to something.
                    #ravel is inverse of reshape,it flattens the 2 diminsonal array
                    #reshape may return a view or a copy,so be careful on doing operations on reshaped array
print(n)

o = np.linspace(0,10,8) #Here we specify range and how many points we want.include end-point
print(o)

one = np.ones((3,4))
print(one) #Similarly youhave zeros too. eye creates identity matrix. (Has to be square)

rep = np.repeat([1,2] ,4)
print(rep)

p = np.ones((2,3), int)
vstack = np.vstack([p , 2*p]) #Stack the original array vertically,number of rows increases.
print(vstack)#Horizontally also there. We stack p with 2*p. You can pass any tupple

print ("="*100)
print("OPERATIONS")
print("Element wise operations")
print(x+y)
print(x-y)
print(x*y)
print(x.dot(y))

z = np.array([y, y**2])
print(z)
print(z.T) #Transpose of an array.This also creates view not copy so elemtns may get fucked up
"""
The transposition is a view
As a results, the following code is wrong and will not make a matrix symmetric:
>>> a += a.T
It will work for small arrays (because of buffering) but fail for large one, in unpredictable ways.
"""
print(z.dtype) #The type of data array has.
complex = np.array([1+2j, 3+4j, 5+6*1j])
print(complex.dtype)

a = np.array([-4,-2,1,3,5])
print(a.sum())
print(a.max())
print(a.mean())
print(a.std()) #standard deviation
print(a.argmax()) #Inde of maximum

print("="*100)
print("INDEX AND SLICE")

s = np.arange(13)**2
print(s)
print(s[0], s[0:3])

r = np.arange(36)
r = r.reshape((6,6))
print(r)
print(r[2,3]) #In normal array it is r[2][3]
print(r[3,4:]) #3rd row, 4 to6 columns
print(r[:2,:-1]) #First two rows all columns

print("="*100)
print("Copying arrays")
r2 = r[:3,:3]
print(r2)

r2[:] = 0
# A slicing operation creates a view on the original array, which is just a way of accessing array data. Thus the
# original array is not copied in memory. You can use np.may_share_memory() to check if two arrays share the
# samememory block.
print(r2)
print(np.may_share_memory(r,r2))
print(r) #The slice which r2 was assigned to also becomes 0, be careful , they have same reference

r_copy = r.copy() #Forcing a copy
r_copy[:] = 10
print(r) #See this time not all elements of r changes

print("="*100)
print("Iterate over arrays")

test = np.random.randint(0, 10, (4,3)) #Last arg is dimension
print(test)

for row in test:
    print(row)

test2 = test**2
for row1, row2 in zip(test,test2):
    print(row1)
    print(row2)