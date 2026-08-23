import numpy as np

def OD_array():
    arr = np.array(48)  # Only one element
    print(arr)

def one_D_array():
    arr = np.array([1,2,3,4])   # 1 dimension that contains multiple elements
    print(arr)  # the first number in a dimension is zero, therefore in this array arr[0] = 1

def two_D_array():
    arr = np.array([[1,2,3,4], [5,6,7,8]]) # 2 dimension arrays are composed of 2x 1 dimensional arrays
    # This displays how each dimension is composed of two of the previous dimensional arrays. As an example a 3D array is constructed as 
    # x = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
    print(arr)

def display_type(): # type() gives the array type.
    arr1 = np.array(48)
    arr2 = np.array([1,2,3,4])
    arr3 = np.array([[1,2,3,4], [5,6,7,8]])
    print(type(arr1))   # <Class 'numpy.ndarray'>
    print(type(arr2))   # <Class 'numpy.ndarray'>
    print(type(arr3))   # <Class 'numpy.ndarray'>

def check_dimensions(): # ndim gives the number of dimensions used within the array.
    arr1 = np.array(48)
    arr2 = np.array([1,2,3,4])
    arr3 = np.array([[1,2,3,4], [5,6,7,8]])
    print(arr1.ndim)    # 0
    print(arr2.ndim)    # 1
    print(arr3.ndim)    # 2

def higher_dimensional_arrays():    # ndmin can be used to set the number of dimensions.
    arr = np.array([1,2,3,4],ndmin=5)   # This creates a 5th dimensional array.
    print(arr.ndim)

def Indexing():
    arr1 = np.array([1,2,3,4])  # Using arr[x] gives the x element in the array
    arr2 = np.array([[1,2,3,4], [5,6,7,8]]) ## Using arr[x,y] gives the y element in the x dimension.
    arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])   # Using arr[x,y,z] gives x as the first dimension, y as the second dimension, and z as the element
    # x splits the 3D array into [[1,2,3],[4,5,6]] & [[7,8,9],[10,11,12]]
    # normal indexing
    print(arr1[0])  # 1
    print(arr2[1,0])    # 5
    print(arr3[1,1,0])  # 10
    # negative indexing
    print(arr1[-1]) # 4
    print(arr2[-1,-1])  # 8
    print(arr3[-1,-1,-1])   # 12

def slicing():
    # Slicing is the process of taking one element from one given index to another, it passes through as [start:end:step] where step is optional.
    # if start is not passed it is assumed to be 0, if you don't pass end it is considered the length of the array in that dimension.
    arr = np.array([1,2,3,4,5,6,7,8,9])
    # Normal slicing
    print(arr[1:5]) # [2 3 4 5]
    print(arr[:5])  # [1 2 3 4 5]
    print(arr[:6:2])    # [1 3 5]
    # Negative slicing is nearly identical except the (-) operator is used to refer to the end of the index

def two_D_slicing():
    arr = np.array([[1,2,3,4],[5,6,7,8]])
    print(arr[0,:4]) # [1 2 3 4]
    print(arr[1,1:3])   # [6 7]

def data_types():   # Using dtype states the data type of the array
# python:                       | #NumPy:
    # str(), string             |   # 'i', integer            # 'm', time delta
    # int(), integer            |   # 'b', boolean            # 'M', datetime
    # float(), float            |   # 'u', unasigned integer  # 'S', string
    # bool(), True or False     |   # 'f', float              # 'U', unicode
    # complex()                 |   # 'c', complex float      # 'O', object
#                               |   # 'V', fixed chunk of memory for other type(void)
    arr1 = np.array([1,2,3,4])
    arr2 = np.array(False)
    arr3 = np.array([0.1,0.2,0.3,0.4])
    print(arr1.dtype)   # int64
    print(arr2.dtype)   # bool
    print(arr3.dtype)   # float64
    # dtype can also be used to define data types
    arr4 = np.array([1,2,3,4], dtype='S')
    print(arr4) # [b'1' b'2' b'3' b'4']
    print(arr4.dtype)   # |S1
    # For 'i','u','f','s' and 'U' we can define the size
    arr5 = np.array([1,2,3,4], dtype='i4')  # this creates a 4 byte integer
    print(arr5.dtype)   # int32, 4 bytes = 32 bits
    # If a value cannot be converted it returns a ValueError

def converting_array():
    # You can convert data types of existing arrays using astype(). You can use both the short and long hand
    arr1 = np.array([1.1,2.1,3.1,4.1])
    newarr1 = arr1.astype('i')
    arr2 = np.array([1,0,3])
    newarr2 = arr2.astype(bool)
    print(newarr1)  # [1 2 3 4]
    print(newarr1.dtype)    # int32
    print(newarr2)  # [True False True]
    print(newarr2.dtype)    # bool

def VIEW_vs_COPY():
    # COPY:
        # The copy owns the data and any changes made to copy the affect the original and any changes made to the original dont affect the copy
    arr1 = np.array([1,2,3,4])
    x = arr1.copy()
    arr1[0] = 45
    print(arr1) # [45 2 3 4]
    print(x)    # [1 2 3 4]
    # VIEW:
        # The view does not own the data, any changes made to the original affects the view and any changes to the view affect the original 
    arr2 = np.array([1,2,3,4])
    y = arr2.view()
    arr2[0] = 47
    print(arr2) # [47 2 3 4]
    print(y)    # [47 2 3 4]
    arr3 = np.array([1,2,3,4])
    z = arr3.view()
    z[0] = 43
    print(arr3) # [43 2 3 4]
    print(z)    # [43 2 3 4]

def check_base():
    # Using .base lets you view the base of the array, if it owns it .base returns None, otherwise the base attribute refers to the original object.
    arr = np.array([1,2,3,4])
    x = arr.copy()
    y = arr.view()
    print(x.base)   # None
    print(y.base)   # [1 2 3 4]

def get_shape():
    # Using .shape returns the tuple with each index having the number of corresponding elements, starts from the n-1 dimensions held within the array, then each element held within such element until the 0D arrays to each dimension above it.
    arr1 = np.array([[1,2,3,4],[5,6,7,8]])
    arr2 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
    print('shape of array: ', arr1.shape)   # shape = (2,4), this shape shows that this array has two 1D arrays each with four 0D arrays
    print('shape of array: ', arr2.shape)   # shape = (2,2,3), this shape shows that this array has two 2D arrays, each with two 1D arrays, which each have three corresponding 0D arrays
    # If we were to use ndmin to create an an array with 5 dimensions we would get a shape that shows all but the 0D elements as 1
    arr3 = np.array([1,2,3,4], ndmin=5)
    print('shape of array: ',arr3.shape)    # shape = (1,1,1,1,4)
    # As seen with all these they are always n dimensional arrays, and each one prints n-1 array elements

def Reshaping_arrays():
    # As the shape of an array is the number of elements in each dimension by reshaping we can add or remove dimensionsm or change the number of elements in each dimension.
    arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
    newarr1 = arr.reshape(4,3)   #   this reshapes it into a 2 dimensional array made of four 1D arrays, each consisting of three 0D arrays
    print(newarr1)   # [[1 2 3] [4 5 6] [7 8 9] [10 11 12]]
    print('# of dimensions: ',newarr1.ndim)  # No. dimensions = 2 
    newarr2 = arr.reshape(2,3,2)
    print(newarr2)  # [[[1 2] [3 4] [5 6]] [[7 8] [9 10] [11 12]]]
    print('# of dimensions: ',newarr2.ndim) # No. dimensions = 3
    # Any shape can be reshaped as long as the elements required for reshaping are equal in both shapes.
    # For example if you were to try reshape [1,2,3,4,5,6,7,8] using arr.reshape(3,3) an error is raised.
    # if .base was used the original array would be returned, thus the reshapes are views.
    # If a dimension is unkown you can pass the value as -1, example:
    newarr3 = arr.reshape(2,2,-1)
    print(newarr3)  # [[[1 2 3] [4 5 6]] [[7 8 9] [10 11 12]]]
    print('# of dimensions: ',newarr3.ndim)  # No.dimensions = 3

def flattening_array():
    # Flattening an array means converting a multidimensional array into a 1D array
    # This is done by using reshape(-1)
    arr1 = np.array([[1,2,3],[4,5,6]])  # 2D arrary
    arr2 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])   # 3D array
    newarr1 = arr1.reshape(-1)
    newarr2 = arr2.reshape(-1)
    print(newarr1)
    print(newarr2)

def iterating_array():
    # iterating means going through elements one by one as we deal with multi-dimensional arrays in numpy we can do this using a basic [for] loop
    arr1 = np.array([1,2,3])    # if we iterate on a 1D array it will go through each element one by one
    arr2 = np.array([[1,2,3],[4,5,6]])    # Iterating a 2D array will go through all the rows
    arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    # Each Nth dimensional array iterated will go though the N-1th dimension one by one
    for x in arr1:  
        print(x)    # Prints each element out one by one
    
    for x in arr2:
        print(x)    # Prints each dimension out one by one
        for y in x:
            print(y)    # Prints the actual values, the scalars, we have to iterate the arrays in each dimension 
    
    for x in arr3:
        print(x)    # prints each 2D array
        for y in x:
            print(y)    # prints each 1D array in each 2D array
            for z in y:
                print(z)    # prints each 0D array in each 1D array
                
def iterating_using_nditer():
    # The function nditer()is a function that can be used from very basic to very advanced iterrations. it solves some basic issueswhich we face in iteration
    
# iterating on each scalar element
    # in basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality
    arr1 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
    for x in np.nditer(arr1):
        print(x)    # This gives the scalar for the array without having to iterate every dimension seperately

# iterating array with different data types
    # We can use the op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating
    # NumPy does not change the data type of the element in-place so it needs some other space to perform this action, that extra space is called buffer, and in order toenable it in nditer() we pass flags=['buffered']
    arr2 = np.array([1,2,3])
    for x in np.nditer(arr2, flags=['buffered'], op_dtypes=['S']):
        print(x)    # Prints each element as a string, ie b' '

# Iterating with different step size
    arr3 = np.array([[1,2,3,4],[5,6,7,8]])
    for x in np.nditer(arr3[:, ::2]):
        print(x)    # prints out every other scalar starting from the 0th element 

def enumerated_iteration():
    # enumeration means mentioning sequence number of something one by one
    # sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those use cases
    arr = ([1,2,3,4])
    for idx, x in np.ndenumerate(arr):
        print(idx, x)   # this prints the position of the element and the value that it holds, 
        print(idx)  # ie. position 0 has a value of one. this would be written as (0, ) 1
        # with the value inside the brackets being th position
        
    arr2 = ([[1,2,3],[4,5,6]])
    for idx,x in np.ndenumerate(arr2):
        print(idx, x) # This does the same as the previous one except that it gives 2 positionals,
        print(idx)  # Since this is a two dimension array the first value is for array 0 or 1, the seconf is for the position with the previous array, as an example (0,1) 2, or (1,2) 6

def joining_arrays():
    