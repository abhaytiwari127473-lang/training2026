from numpy import *
arr=array([
    [1,2,3],
    [2,3,4],
    [4,5,6]
])
print(arr)
print(arr.shape)
print(arr.size)
print(arr.ndim)
arr2=array([
    [1,2,3],
    [2,3,4],
    [4,5,6],
    [4,5,6]
])
print("max=",arr2.max())
'''
print(arr+arr2)
print(arr-arr2)'''
#print(arr*arr2) # this is not matrix multiplication
#print(arr@arr2)
print(dot(arr2,arr))