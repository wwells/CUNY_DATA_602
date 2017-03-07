import numpy as np
import numpy.random as rand 

arr = np.arange(1e2)
larr = arr.tolist()

#create arrays

alist = [1,2,3]
arr = np.array(alist)

arr = np.zeros(5)
arr = np.linspace(0,1,100)

image = np.zeros((5,5))

cube = np.zeros((5,5,5)).astype(int) + 1
#or
cube = np.ones((5,5,5)).astype(np.float16)

arr1d = np.arange(1000)
arr3d = np.reshape(arr1d, (10, 10, 10))

### col as diff data types
recarr = np.zeros((2,), dtype=('i4,f4,a10'))
col1 = np.arange(2) + 1
col2 = np.arange(2, dtype=np.float32)
col3 = ['Hello', 'World']
toadd = zip(col1, col2, col3)
# Assigning values to recarr
recarr[:] = toadd
recarr.dtype.names = ('Integers' , 'Floats', 'Strings')

## indexing and slicing
alist=[[1,2],[3,4]]
arr = np.array(alist)
print arr[1,:]

## create image
img1 = np.zeros((20, 20)) + 3
img1[4:-4, 4:-4] = 6
img1[7:-7, 7:-7] = 9

index1 = img1 > 2
index2 = img1 < 6
compound_index = index1 & index2

index3 = img1 == 9
index4 = (index1 & index2) | index3
img3 = np.copy(img1)
img3[index4] = 0

a = rand.randn(100)

index = a > 0.2
b = a[index]
b = b ** 2 - 2
a[index] = b

## lin algebra
A = np.matrix([[3, 6, -5],
	[1, -3, 2],
	[5, -1, 4]])
B = np.matrix([[12],
	[-2],[10]])

X = A ** (-1)  * B
print(X)

