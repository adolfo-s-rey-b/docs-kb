[Skip to main content](https://numpy.org/doc/stable/user/basics.creation.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/user/basics.creation.html)
[2.5 (stable)](https://numpy.org/doc/stable/user/basics.creation.html)
[2.4](https://numpy.org/doc/2.4/user/basics.creation.html)
[2.3](https://numpy.org/doc/2.3/user/basics.creation.html)
[2.2](https://numpy.org/doc/2.2/user/basics.creation.html)
[2.1](https://numpy.org/doc/2.1/user/basics.creation.html)
[2.0](https://numpy.org/doc/2.0/user/basics.creation.html)
[1.26](https://numpy.org/doc/1.26/user/basics.creation.html)
[1.25](https://numpy.org/doc/1.25/user/basics.creation.html)
[1.24](https://numpy.org/doc/1.24/user/basics.creation.html)
[1.23](https://numpy.org/doc/1.23/user/basics.creation.html)
[1.22](https://numpy.org/doc/1.22/user/basics.creation.html)
[1.21](https://numpy.org/doc/1.21/user/basics.creation.html)
[1.20](https://numpy.org/doc/1.20/user/basics.creation.html)
[1.19](https://numpy.org/doc/1.19/user/basics.creation.html)
[1.18](https://numpy.org/doc/1.18/user/basics.creation.html)
[1.17](https://numpy.org/doc/1.17/user/basics.creation.html)
[1.16](https://numpy.org/doc/1.16/user/basics.creation.html)
[1.15](https://numpy.org/doc/1.15/user/basics.creation.html)
[1.14](https://numpy.org/doc/1.14/user/basics.creation.html)
[1.13](https://numpy.org/doc/1.13/user/basics.creation.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Array creation[#](https://numpy.org/doc/stable/user/basics.creation.html#array-creation "Link to this heading")

================================================================================================================

See also

[Array creation routines](https://numpy.org/doc/stable/reference/routines.array-creation.html#routines-array-creation)

Introduction[#](https://numpy.org/doc/stable/user/basics.creation.html#introduction "Link to this heading")

------------------------------------------------------------------------------------------------------------

There are 6 general mechanisms for creating arrays:

1.  Conversion from other Python structures (i.e. lists and tuples)
    
2.  Intrinsic NumPy array creation functions (e.g. arange, ones, zeros, etc.)
    
3.  Replicating, joining, or mutating existing arrays
    
4.  Reading arrays from disk, either from standard or custom formats
    
5.  Creating arrays from raw bytes through the use of strings or buffers
    
6.  Use of special library functions (e.g., random)
    

You can use these methods to create ndarrays or [Structured arrays](https://numpy.org/doc/stable/user/basics.rec.html#structured-arrays)
. This document will cover general methods for ndarray creation.

1) Converting Python sequences to NumPy arrays[#](https://numpy.org/doc/stable/user/basics.creation.html#converting-python-sequences-to-numpy-arrays "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NumPy arrays can be defined using Python sequences such as lists and tuples. Lists and tuples are defined using `[...]` and `(...)`, respectively. Lists and tuples can define ndarray creation:

*   a list of numbers will create a 1D array,
    
*   a list of lists will create a 2D array,
    
*   further nested lists will create higher-dimensional arrays. In general, any array object is called an **ndarray** in NumPy.
    

\>>> import numpy as np
\>>> a1D \= np.array(\[1, 2, 3, 4\])
\>>> a2D \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> a3D \= np.array(\[\[\[1, 2\], \[3, 4\]\], \[\[5, 6\], \[7, 8\]\]\])

Copy to clipboard

When you use [`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
 to define a new array, you should consider the [dtype](https://numpy.org/doc/stable/user/basics.types.html)
 of the elements in the array, which can be specified explicitly. This feature gives you more control over the underlying data structures and how the elements are handled in C/C++ functions. When values do not fit and you are using a `dtype`, NumPy may raise an error:

\>>> import numpy as np
\>>> np.array(\[127, 128, 129\], dtype\=np.int8)
Traceback (most recent call last):
...
OverflowError: Python integer 128 out of bounds for int8

Copy to clipboard

An 8-bit signed integer represents integers from -128 to 127. Assigning the `int8` array to integers outside of this range results in overflow. This feature can often be misunderstood. If you perform calculations with mismatching `dtypes`, you can get unwanted results, for example:

\>>> import numpy as np
\>>> a \= np.array(\[2, 3, 4\], dtype\=np.uint32)
\>>> b \= np.array(\[5, 6, 7\], dtype\=np.uint32)
\>>> c\_unsigned32 \= a \- b
\>>> print('unsigned c:', c\_unsigned32, c\_unsigned32.dtype)
unsigned c: \[4294967293 4294967293 4294967293\] uint32
\>>> c\_signed32 \= a \- b.astype(np.int32)
\>>> print('signed c:', c\_signed32, c\_signed32.dtype)
signed c: \[-3 -3 -3\] int64

Copy to clipboard

Notice when you perform operations with two arrays of the same `dtype`: `uint32`, the resulting array is the same type. When you perform operations with different `dtype`, NumPy will assign a new type that satisfies all of the array elements involved in the computation, here `uint32` and `int32` can both be represented in as `int64`.

The default NumPy behavior is to create arrays in either 32 or 64-bit signed integers (platform dependent and matches C `long` size) or double precision floating point numbers. If you expect your integer arrays to be a specific type, then you need to specify the dtype while you create the array.

2) Intrinsic NumPy array creation functions[#](https://numpy.org/doc/stable/user/basics.creation.html#intrinsic-numpy-array-creation-functions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

NumPy has over 40 built-in functions for creating arrays as laid out in the [Array creation routines](https://numpy.org/doc/stable/reference/routines.array-creation.html#routines-array-creation)
. These functions can be split into roughly three categories, based on the dimension of the array they create:

1.  1D arrays
    
2.  2D arrays
    
3.  ndarrays
    

### 1 - 1D array creation functions[#](https://numpy.org/doc/stable/user/basics.creation.html#d-array-creation-functions "Link to this heading")

The 1D array creation functions e.g. [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
 and [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
 generally need at least two inputs, `start` and `stop`.

[`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
 creates arrays with regularly incrementing values. Check the documentation for complete information and examples. A few examples are shown:

\>>> import numpy as np
\>>> np.arange(10)
array(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\])
\>>> np.arange(2, 10, dtype\=np.float64)
array(\[2., 3., 4., 5., 6., 7., 8., 9.\])
\>>> np.arange(2, 3, 0.1)
array(\[2. , 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9\])

Copy to clipboard

Note: best practice for [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
 is to use integer start, end, and step values. There are some subtleties regarding `dtype`. In the second example, the `dtype` is defined. In the third example, the array is `dtype=np.float64` to accommodate the step size of `0.1`. Due to roundoff error, the `stop` value is sometimes included.

[`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
 will create arrays with a specified number of elements, and spaced equally between the specified beginning and end values. For example:

\>>> import numpy as np
\>>> np.linspace(1., 4., 6)
array(\[1. ,  1.6,  2.2,  2.8,  3.4,  4. \])

Copy to clipboard

The advantage of this creation function is that you guarantee the number of elements and the starting and end point. The previous `arange(start, stop, step)` will not include the value `stop`.

### 2 - 2D array creation functions[#](https://numpy.org/doc/stable/user/basics.creation.html#id1 "Link to this heading")

The 2D array creation functions e.g. [`numpy.eye`](https://numpy.org/doc/stable/reference/generated/numpy.eye.html#numpy.eye "numpy.eye")
, [`numpy.diag`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")
, and [`numpy.vander`](https://numpy.org/doc/stable/reference/generated/numpy.vander.html#numpy.vander "numpy.vander")
 define properties of special matrices represented as 2D arrays.

`np.eye(n, m)` defines a 2D identity matrix. The elements where i=j (row index and column index are equal) are 1 and the rest are 0, as such:

\>>> import numpy as np
\>>> np.eye(3)
array(\[\[1., 0., 0.\],\
       \[0., 1., 0.\],\
       \[0., 0., 1.\]\])
\>>> np.eye(3, 5)
array(\[\[1., 0., 0., 0., 0.\],\
       \[0., 1., 0., 0., 0.\],\
       \[0., 0., 1., 0., 0.\]\])

Copy to clipboard

[`numpy.diag`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")
 can define either a square 2D array with given values along the diagonal _or_ if given a 2D array returns a 1D array that is only the diagonal elements. The two array creation functions can be helpful while doing linear algebra, as such:

\>>> import numpy as np
\>>> np.diag(\[1, 2, 3\])
array(\[\[1, 0, 0\],\
       \[0, 2, 0\],\
       \[0, 0, 3\]\])
\>>> np.diag(\[1, 2, 3\], 1)
array(\[\[0, 1, 0, 0\],\
       \[0, 0, 2, 0\],\
       \[0, 0, 0, 3\],\
       \[0, 0, 0, 0\]\])
\>>> a \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> np.diag(a)
array(\[1, 4\])

Copy to clipboard

`vander(x, n)` defines a Vandermonde matrix as a 2D NumPy array. Each column of the Vandermonde matrix is a decreasing power of the input 1D array or list or tuple, `x` where the highest polynomial order is `n-1`. This array creation routine is helpful in generating linear least squares models, as such:

\>>> import numpy as np
\>>> np.vander(np.linspace(0, 2, 5), 2)
array(\[\[0. , 1. \],\
      \[0.5, 1. \],\
      \[1. , 1. \],\
      \[1.5, 1. \],\
      \[2. , 1. \]\])
\>>> np.vander(\[1, 2, 3, 4\], 2)
array(\[\[1, 1\],\
       \[2, 1\],\
       \[3, 1\],\
       \[4, 1\]\])
\>>> np.vander((1, 2, 3, 4), 4)
array(\[\[ 1,  1,  1,  1\],\
       \[ 8,  4,  2,  1\],\
       \[27,  9,  3,  1\],\
       \[64, 16,  4,  1\]\])

Copy to clipboard

### 3 - general ndarray creation functions[#](https://numpy.org/doc/stable/user/basics.creation.html#general-ndarray-creation-functions "Link to this heading")

The ndarray creation functions e.g. [`numpy.ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
, [`numpy.zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
, and [`random`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random "numpy.random.Generator.random")
 define arrays based upon the desired shape. The ndarray creation functions can create arrays with any dimension by specifying how many dimensions and length along that dimension in a tuple or list.

[`numpy.zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
 will create an array filled with 0 values with the specified shape. The default dtype is `float64`:

\>>> import numpy as np
\>>> np.zeros((2, 3))
array(\[\[0., 0., 0.\],\
       \[0., 0., 0.\]\])
\>>> np.zeros((2, 3, 2))
array(\[\[\[0., 0.\],\
        \[0., 0.\],\
        \[0., 0.\]\],\
\
       \[\[0., 0.\],\
        \[0., 0.\],\
        \[0., 0.\]\]\])

Copy to clipboard

[`numpy.ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
 will create an array filled with 1 values. It is identical to `zeros` in all other respects as such:

\>>> import numpy as np
\>>> np.ones((2, 3))
array(\[\[1., 1., 1.\],\
       \[1., 1., 1.\]\])
\>>> np.ones((2, 3, 2))
array(\[\[\[1., 1.\],\
        \[1., 1.\],\
        \[1., 1.\]\],\
\
       \[\[1., 1.\],\
        \[1., 1.\],\
        \[1., 1.\]\]\])

Copy to clipboard

The [`random`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random "numpy.random.Generator.random")
 method of the result of `default_rng` will create an array filled with random values between 0 and 1. It is included with the [`numpy.random`](https://numpy.org/doc/stable/reference/random/index.html#module-numpy.random "numpy.random")
 library. Below, two arrays are created with shapes (2,3) and (2,3,2), respectively. The seed is set to 42 so you can reproduce these pseudorandom numbers:

\>>> import numpy as np
\>>> from numpy.random import default\_rng
\>>> default\_rng(42).random((2,3))
array(\[\[0.77395605, 0.43887844, 0.85859792\],\
       \[0.69736803, 0.09417735, 0.97562235\]\])
\>>> default\_rng(42).random((2,3,2))
array(\[\[\[0.77395605, 0.43887844\],\
        \[0.85859792, 0.69736803\],\
        \[0.09417735, 0.97562235\]\],\
       \[\[0.7611397 , 0.78606431\],\
        \[0.12811363, 0.45038594\],\
        \[0.37079802, 0.92676499\]\]\])

Copy to clipboard

[`numpy.indices`](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#numpy.indices "numpy.indices")
 will create a set of arrays (stacked as a one-higher dimensioned array), one per dimension with each representing variation in that dimension:

\>>> import numpy as np
\>>> np.indices((3,3))
array(\[\[\[0, 0, 0\],\
        \[1, 1, 1\],\
        \[2, 2, 2\]\],\
       \[\[0, 1, 2\],\
        \[0, 1, 2\],\
        \[0, 1, 2\]\]\])

Copy to clipboard

This is particularly useful for evaluating functions of multiple dimensions on a regular grid.

3) Replicating, joining, or mutating existing arrays[#](https://numpy.org/doc/stable/user/basics.creation.html#replicating-joining-or-mutating-existing-arrays "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Once you have created arrays, you can replicate, join, or mutate those existing arrays to create new arrays. When you assign an array or its elements to a new variable, you have to explicitly [`numpy.copy`](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "numpy.copy")
 the array, otherwise the variable is a view into the original array. Consider the following example:

\>>> import numpy as np
\>>> a \= np.array(\[1, 2, 3, 4, 5, 6\])
\>>> b \= a\[:2\]
\>>> b += 1
\>>> print('a =', a, '; b =', b)
a = \[2 3 3 4 5 6\] ; b = \[2 3\]

Copy to clipboard

In this example, you did not create a new array. You created a variable, `b` that viewed the first 2 elements of `a`. When you added 1 to `b` you would get the same result by adding 1 to `a[:2]`. If you want to create a _new_ array, use the [`numpy.copy`](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "numpy.copy")
 array creation routine as such:

\>>> import numpy as np
\>>> a \= np.array(\[1, 2, 3, 4\])
\>>> b \= a\[:2\].copy()
\>>> b += 1
\>>> print('a = ', a, 'b = ', b)
a =  \[1 2 3 4\] b =  \[2 3\]

Copy to clipboard

For more information and examples look at [Copies and Views](https://numpy.org/doc/stable/user/quickstart.html#quickstart-copies-and-views)
.

There are a number of routines to join existing arrays e.g. [`numpy.vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
, [`numpy.hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
, and [`numpy.block`](https://numpy.org/doc/stable/reference/generated/numpy.block.html#numpy.block "numpy.block")
. Here is an example of joining four 2-by-2 arrays into a 4-by-4 array using `block`:

\>>> import numpy as np
\>>> A \= np.ones((2, 2))
\>>> B \= np.eye(2, 2)
\>>> C \= np.zeros((2, 2))
\>>> D \= np.diag((\-3, \-4))
\>>> np.block(\[\[A, B\], \[C, D\]\])
array(\[\[ 1.,  1.,  1.,  0.\],\
       \[ 1.,  1.,  0.,  1.\],\
       \[ 0.,  0., -3.,  0.\],\
       \[ 0.,  0.,  0., -4.\]\])

Copy to clipboard

Other routines use similar syntax to join ndarrays. Check the routine’s documentation for further examples and syntax.

4) Reading arrays from disk, either from standard or custom formats[#](https://numpy.org/doc/stable/user/basics.creation.html#reading-arrays-from-disk-either-from-standard-or-custom-formats "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This is the most common case of large array creation. The details depend greatly on the format of data on disk. This section gives general pointers on how to handle various formats. For more detailed examples of IO look at [How to Read and Write files](https://numpy.org/doc/stable/user/how-to-io.html#how-to-io)
.

### Standard binary formats[#](https://numpy.org/doc/stable/user/basics.creation.html#standard-binary-formats "Link to this heading")

Various fields have standard formats for array data. The following lists the ones with known Python libraries to read them and return NumPy arrays (there may be others for which it is possible to read and convert to NumPy arrays so check the last section as well)

HDF5: h5py
FITS: Astropy

Copy to clipboard

Examples of formats that cannot be read directly but for which it is not hard to convert are those formats supported by libraries like PIL (able to read and write many image formats such as jpg, png, etc).

### Common ASCII formats[#](https://numpy.org/doc/stable/user/basics.creation.html#common-ascii-formats "Link to this heading")

Delimited files such as comma separated value (csv) and tab separated value (tsv) files are used for programs like Excel and LabView. Python functions can read and parse these files line-by-line. NumPy has two standard routines for importing a file with delimited data [`numpy.loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt "numpy.loadtxt")
 and [`numpy.genfromtxt`](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt")
. These functions have more involved use cases in [Reading and writing files](https://numpy.org/doc/stable/user/how-to-io.html)
. A simple example given a `simple.csv`:

$ cat simple.csv
x, y
0, 0
1, 1
2, 4
3, 9

Copy to clipboard

Importing `simple.csv` is accomplished using [`numpy.loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt "numpy.loadtxt")
:

\>>> import numpy as np
\>>> np.loadtxt('simple.csv', delimiter \= ',', skiprows \= 1) 
array(\[\[0., 0.\],\
       \[1., 1.\],\
       \[2., 4.\],\
       \[3., 9.\]\])

Copy to clipboard

More generic ASCII files can be read using [`scipy.io`](https://docs.scipy.org/doc/scipy/reference/io.html#module-scipy.io "(in SciPy v1.18.0)")
 and [Pandas](https://pandas.pydata.org/)
.

5) Creating arrays from raw bytes through the use of strings or buffers[#](https://numpy.org/doc/stable/user/basics.creation.html#creating-arrays-from-raw-bytes-through-the-use-of-strings-or-buffers "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are a variety of approaches one can use. If the file has a relatively simple format then one can write a simple I/O library and use the NumPy `fromfile()` function and `.tofile()` method to read and write NumPy arrays directly (mind your byteorder though!) If a good C or C++ library exists that read the data, one can wrap that library with a variety of techniques though that certainly is much more work and requires significantly more advanced knowledge to interface with C or C++.

6) Use of special library functions (e.g., SciPy, pandas, and OpenCV)[#](https://numpy.org/doc/stable/user/basics.creation.html#use-of-special-library-functions-e-g-scipy-pandas-and-opencv "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NumPy is the fundamental library for array containers in the Python Scientific Computing stack. Many Python libraries, including SciPy, Pandas, and OpenCV, use NumPy ndarrays as the common format for data exchange, These libraries can create, operate on, and work with NumPy arrays.

On this page