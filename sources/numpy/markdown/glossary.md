[Skip to main content](https://numpy.org/doc/stable/glossary.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/glossary.html)
[2.5 (stable)](https://numpy.org/doc/stable/glossary.html)
[2.4](https://numpy.org/doc/2.4/glossary.html)
[2.3](https://numpy.org/doc/2.3/glossary.html)
[2.2](https://numpy.org/doc/2.2/glossary.html)
[2.1](https://numpy.org/doc/2.1/glossary.html)
[2.0](https://numpy.org/doc/2.0/glossary.html)
[1.26](https://numpy.org/doc/1.26/glossary.html)
[1.25](https://numpy.org/doc/1.25/glossary.html)
[1.24](https://numpy.org/doc/1.24/glossary.html)
[1.23](https://numpy.org/doc/1.23/glossary.html)
[1.22](https://numpy.org/doc/1.22/glossary.html)
[1.21](https://numpy.org/doc/1.21/glossary.html)
[1.20](https://numpy.org/doc/1.20/glossary.html)
[1.19](https://numpy.org/doc/1.19/glossary.html)
[1.18](https://numpy.org/doc/1.18/glossary.html)
[1.17](https://numpy.org/doc/1.17/glossary.html)
[1.16](https://numpy.org/doc/1.16/glossary.html)
[1.15](https://numpy.org/doc/1.15/glossary.html)
[1.14](https://numpy.org/doc/1.14/glossary.html)
[1.13](https://numpy.org/doc/1.13/glossary.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Glossary[#](https://numpy.org/doc/stable/glossary.html#glossary "Link to this heading")

========================================================================================

(_n_,)[#](https://numpy.org/doc/stable/glossary.html#term-n "Link to this term")

A parenthesized number followed by a comma denotes a tuple with one element. The trailing comma distinguishes a one-element tuple from a parenthesized `n`.

\-1[#](https://numpy.org/doc/stable/glossary.html#term-1 "Link to this term")

*   **In a dimension entry**, instructs NumPy to choose the length that will keep the total number of array elements the same.
    
    \>>> np.arange(12).reshape(4, \-1).shape
    (4, 3)
    
    Copy to clipboard
    
*   **In an index**, any negative value [denotes](https://docs.python.org/dev/faq/programming.html#what-s-a-negative-index)
     indexing from the right.
    

…[#](https://numpy.org/doc/stable/glossary.html#term-.-.-. "Link to this term")

An [`Ellipsis`](https://docs.python.org/3/library/constants.html#Ellipsis "(in Python v3.14)")
.

*   **When indexing an array**, shorthand that the missing axes, if they exist, are full slices.
    
    \>>> a \= np.arange(24).reshape(2,3,4)
    
    Copy to clipboard
    
    \>>> a\[...\].shape
    (2, 3, 4)
    
    Copy to clipboard
    
    \>>> a\[...,0\].shape
    (2, 3)
    
    Copy to clipboard
    
    \>>> a\[0,...\].shape
    (3, 4)
    
    Copy to clipboard
    
    \>>> a\[0,...,0\].shape
    (3,)
    
    Copy to clipboard
    
    It can be used at most once; `a[...,0,...]` raises an [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "(in Python v3.14)")
    .
    
*   **In printouts**, NumPy substitutes `...` for the middle elements of large arrays. To see the entire array, use [`numpy.printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.printoptions.html#numpy.printoptions "numpy.printoptions")
    

:[#](https://numpy.org/doc/stable/glossary.html#term-0 "Link to this term")

The Python [slice](https://docs.python.org/3/glossary.html#term-slice "(in Python v3.14)")
 operator. In ndarrays, slicing can be applied to every axis:

\>>> a \= np.arange(24).reshape(2,3,4)
\>>> a
array(\[\[\[ 0,  1,  2,  3\],\
        \[ 4,  5,  6,  7\],\
        \[ 8,  9, 10, 11\]\],\
\
       \[\[12, 13, 14, 15\],\
        \[16, 17, 18, 19\],\
        \[20, 21, 22, 23\]\]\])

\>>> a\[1:,\-2:,:\-1\]
array(\[\[\[16, 17, 18\],\
        \[20, 21, 22\]\]\])

Copy to clipboard

Trailing slices can be omitted:

\>>> a\[1\] \== a\[1,:,:\]
array(\[\[ True,  True,  True,  True\],\
       \[ True,  True,  True,  True\],\
       \[ True,  True,  True,  True\]\])

Copy to clipboard

In contrast to Python, where slicing creates a copy, in NumPy slicing creates a [view](https://numpy.org/doc/stable/glossary.html#term-view)
.

For details, see [Combining advanced and basic indexing](https://numpy.org/doc/stable/user/basics.indexing.html#combining-advanced-and-basic-indexing)
.

<[#](https://numpy.org/doc/stable/glossary.html#term-2 "Link to this term")

In a dtype declaration, indicates that the data is [little-endian](https://numpy.org/doc/stable/glossary.html#term-little-endian)
 (the bracket is big on the right).

\>>> dt \= np.dtype('<f')  \# little-endian single-precision float

Copy to clipboard

\>[#](https://numpy.org/doc/stable/glossary.html#term-3 "Link to this term")

In a dtype declaration, indicates that the data is [big-endian](https://numpy.org/doc/stable/glossary.html#term-big-endian)
 (the bracket is big on the left).

\>>> dt \= np.dtype('>H')  \# big-endian unsigned short

Copy to clipboard

advanced indexing[#](https://numpy.org/doc/stable/glossary.html#term-advanced-indexing "Link to this term")

Rather than using a [scalar](https://numpy.org/doc/stable/reference/arrays.scalars.html)
 or slice as an index, an axis can be indexed with an array, providing fine-grained selection. This is known as [advanced indexing](https://numpy.org/doc/stable/user/basics.indexing.html#advanced-indexing)
 or “fancy indexing”.

along an axis[#](https://numpy.org/doc/stable/glossary.html#term-along-an-axis "Link to this term")

An operation _along axis n_ of array `a` behaves as if its argument were an array of slices of `a` where each slice has a successive index of axis _n_.

For example, if `a` is a 3 x _N_ array, an operation along axis 0 behaves as if its argument were an array containing slices of each row:

\>>> np.array((a\[0,:\], a\[1,:\], a\[2,:\])) 

Copy to clipboard

To make it concrete, we can pick the operation to be the array-reversal function [`numpy.flip`](https://numpy.org/doc/stable/reference/generated/numpy.flip.html#numpy.flip "numpy.flip")
, which accepts an `axis` argument. We construct a 3 x 4 array `a`:

\>>> a \= np.arange(12).reshape(3,4)
\>>> a
array(\[\[ 0,  1,  2,  3\],\
       \[ 4,  5,  6,  7\],\
       \[ 8,  9, 10, 11\]\])

Copy to clipboard

Reversing along axis 0 (the row axis) yields

\>>> np.flip(a,axis\=0)
array(\[\[ 8,  9, 10, 11\],\
       \[ 4,  5,  6,  7\],\
       \[ 0,  1,  2,  3\]\])

Copy to clipboard

Recalling the definition of _along an axis_, `flip` along axis 0 is treating its argument as if it were

\>>> np.array((a\[0,:\], a\[1,:\], a\[2,:\]))
array(\[\[ 0,  1,  2,  3\],\
       \[ 4,  5,  6,  7\],\
       \[ 8,  9, 10, 11\]\])

Copy to clipboard

and the result of `np.flip(a,axis=0)` is to reverse the slices:

\>>> np.array((a\[2,:\],a\[1,:\],a\[0,:\]))
array(\[\[ 8,  9, 10, 11\],\
       \[ 4,  5,  6,  7\],\
       \[ 0,  1,  2,  3\]\])

Copy to clipboard

array[#](https://numpy.org/doc/stable/glossary.html#term-array "Link to this term")

Used synonymously in the NumPy docs with [ndarray](https://numpy.org/doc/stable/glossary.html#term-ndarray)
.

array\_like[#](https://numpy.org/doc/stable/glossary.html#term-array_like "Link to this term")

Any [scalar](https://numpy.org/doc/stable/reference/arrays.scalars.html)
 or [sequence](https://docs.python.org/3/glossary.html#term-sequence "(in Python v3.14)")
 that can be interpreted as an ndarray. In addition to ndarrays and scalars this category includes lists (possibly nested and with different element types) and tuples. Any argument accepted by [numpy.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
 is array\_like.

\>>> a \= np.array(\[\[1, 2.0\], \[0, 0\], (1+1j, 3.)\])

\>>> a
array(\[\[1.+0.j, 2.+0.j\],\
       \[0.+0.j, 0.+0.j\],\
       \[1.+1.j, 3.+0.j\]\])

Copy to clipboard

array scalar[#](https://numpy.org/doc/stable/glossary.html#term-array-scalar "Link to this term")

An [array scalar](https://numpy.org/doc/stable/reference/arrays.scalars.html)
 is an instance of the types/classes float32, float64, etc.. For uniformity in handling operands, NumPy treats a scalar as an array of zero dimension. In contrast, a 0-dimensional array is an [ndarray](https://numpy.org/doc/stable/reference/arrays.ndarray.html)
 instance containing precisely one value.

axis[#](https://numpy.org/doc/stable/glossary.html#term-axis "Link to this term")

Another term for an array dimension. Axes are numbered left to right; axis 0 is the first element in the shape tuple.

In a two-dimensional vector, the elements of axis 0 are rows and the elements of axis 1 are columns.

In higher dimensions, the picture changes. NumPy prints higher-dimensional vectors as replications of row-by-column building blocks, as in this three-dimensional vector:

\>>> a \= np.arange(12).reshape(2,2,3)
\>>> a
array(\[\[\[ 0,  1,  2\],\
        \[ 3,  4,  5\]\],\
       \[\[ 6,  7,  8\],\
        \[ 9, 10, 11\]\]\])

Copy to clipboard

`a` is depicted as a two-element array whose elements are 2x3 vectors. From this point of view, rows and columns are the final two axes, respectively, in any shape.

This rule helps you anticipate how a vector will be printed, and conversely how to find the index of any of the printed elements. For instance, in the example, the last two values of 8’s index must be 0 and 2. Since 8 appears in the second of the two 2x3’s, the first index must be 1:

\>>> a\[1,0,2\]
8

Copy to clipboard

A convenient way to count dimensions in a printed vector is to count `[` symbols after the open-parenthesis. This is useful in distinguishing, say, a (1,2,3) shape from a (2,3) shape:\
\
\>>> a \= np.arange(6).reshape(2,3)\
\>>> a.ndim\
2\
\>>> a\
array(\[\[0, 1, 2\],\
       \[3, 4, 5\]\])\
\
Copy to clipboard\
\
\>>> a \= np.arange(6).reshape(1,2,3)\
\>>> a.ndim\
3\
\>>> a\
array(\[\[\[0, 1, 2\],\
        \[3, 4, 5\]\]\])\
\
Copy to clipboard\
\
.base[#](https://numpy.org/doc/stable/glossary.html#term-.base "Link to this term")\
\
If an array does not own its memory, then its [base](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.base.html)\
 attribute returns the object whose memory the array is referencing. That object may be referencing the memory from still another object, so the owning object may be `a.base.base.base...`. Some writers erroneously claim that testing `base` determines if arrays are [view](https://numpy.org/doc/stable/glossary.html#term-view)\
s. For the correct way, see [`numpy.shares_memory`](https://numpy.org/doc/stable/reference/generated/numpy.shares_memory.html#numpy.shares_memory "numpy.shares_memory")\
.\
\
big-endian[#](https://numpy.org/doc/stable/glossary.html#term-big-endian "Link to this term")\
\
See [Endianness](https://en.wikipedia.org/wiki/Endianness)\
.\
\
BLAS[#](https://numpy.org/doc/stable/glossary.html#term-BLAS "Link to this term")\
\
[Basic Linear Algebra Subprograms](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms)\
\
broadcast[#](https://numpy.org/doc/stable/glossary.html#term-broadcast "Link to this term")\
\
_broadcasting_ is NumPy’s ability to process ndarrays of different sizes as if all were the same size.\
\
It permits an elegant do-what-I-mean behavior where, for instance, adding a scalar to a vector adds the scalar value to every element.\
\
\>>> a \= np.arange(3)\
\>>> a\
array(\[0, 1, 2\])\
\
Copy to clipboard\
\
\>>> a + \[3, 3, 3\]\
array(\[3, 4, 5\])\
\
Copy to clipboard\
\
\>>> a + 3\
array(\[3, 4, 5\])\
\
Copy to clipboard\
\
Ordinarily, vector operands must all be the same size, because NumPy works element by element – for instance, `c = a * b` is\
\
 c\[0,0,0\] \= a\[0,0,0\] \* b\[0,0,0\]\
 c\[0,0,1\] \= a\[0,0,1\] \* b\[0,0,1\]\
...\
\
Copy to clipboard\
\
But in certain useful cases, NumPy can duplicate data along “missing” axes or “too-short” dimensions so shapes will match. The duplication costs no memory or time. For details, see [Broadcasting.](https://numpy.org/doc/stable/user/basics.broadcasting.html)\
\
C order[#](https://numpy.org/doc/stable/glossary.html#term-C-order "Link to this term")\
\
Same as [row-major](https://numpy.org/doc/stable/glossary.html#term-row-major)\
.\
\
casting[#](https://numpy.org/doc/stable/glossary.html#term-casting "Link to this term")\
\
The process of converting array data from one dtype to another. There exist several casting modes, defined by the following casting rules:\
\
*   `no`: The data types should not be cast at all. Any mismatch in data types between the arrays will raise a _TypeError_.\
    \
*   `equiv`: Only byte-order changes are allowed.\
    \
*   `safe`: Only casts that can preserve values are allowed. Upcasting (e.g., from int to float) is allowed, but downcasting is not.\
    \
*   `same_kind`: The ‘same\_kind’ casting option allows safe casts and casts within a kind, like float64 to float32.\
    \
*   `unsafe`: any data conversions may be done.\
    \
\
column-major[#](https://numpy.org/doc/stable/glossary.html#term-column-major "Link to this term")\
\
See [Row- and column-major order](https://en.wikipedia.org/wiki/Row-_and_column-major_order)\
.\
\
contiguous[#](https://numpy.org/doc/stable/glossary.html#term-contiguous "Link to this term")\
\
An array is contiguous if:\
\
*   it occupies an unbroken block of memory, and\
    \
*   array elements with higher indexes occupy higher addresses (that is, no [stride](https://numpy.org/doc/stable/glossary.html#term-stride)\
     is negative).\
    \
\
There are two types of proper-contiguous NumPy arrays:\
\
*   Fortran-contiguous arrays refer to data that is stored column-wise, i.e. the indexing of data as stored in memory starts from the lowest dimension;\
    \
*   C-contiguous, or simply contiguous arrays, refer to data that is stored row-wise, i.e. the indexing of data as stored in memory starts from the highest dimension.\
    \
\
For one-dimensional arrays these notions coincide.\
\
For example, a 2x2 array `A` is Fortran-contiguous if its elements are stored in memory in the following order:\
\
A\[0,0\] A\[1,0\] A\[0,1\] A\[1,1\]\
\
Copy to clipboard\
\
and C-contiguous if the order is as follows:\
\
A\[0,0\] A\[0,1\] A\[1,0\] A\[1,1\]\
\
Copy to clipboard\
\
To test whether an array is C-contiguous, use the `.flags.c_contiguous` attribute of NumPy arrays. To test for Fortran contiguity, use the `.flags.f_contiguous` attribute.\
\
copy[#](https://numpy.org/doc/stable/glossary.html#term-copy "Link to this term")\
\
See [view](https://numpy.org/doc/stable/glossary.html#term-view)\
.\
\
dimension[#](https://numpy.org/doc/stable/glossary.html#term-dimension "Link to this term")\
\
See [axis](https://numpy.org/doc/stable/glossary.html#term-axis)\
.\
\
dtype[#](https://numpy.org/doc/stable/glossary.html#term-dtype "Link to this term")\
\
The datatype describing the (identically typed) elements in an ndarray. It can be changed to reinterpret the array contents. For details, see [Data type objects (dtype).](https://numpy.org/doc/stable/reference/arrays.dtypes.html)\
\
fancy indexing[#](https://numpy.org/doc/stable/glossary.html#term-fancy-indexing "Link to this term")\
\
Another term for [advanced indexing](https://numpy.org/doc/stable/glossary.html#term-advanced-indexing)\
.\
\
field[#](https://numpy.org/doc/stable/glossary.html#term-field "Link to this term")\
\
In a [structured data type](https://numpy.org/doc/stable/glossary.html#term-structured-data-type)\
, each subtype is called a _field_. The _field_ has a name (a string), a type (any valid dtype), and an optional _title_. See [Data type objects (dtype)](https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes)\
.\
\
Fortran order[#](https://numpy.org/doc/stable/glossary.html#term-Fortran-order "Link to this term")\
\
Same as [column-major](https://numpy.org/doc/stable/glossary.html#term-column-major)\
.\
\
flattened[#](https://numpy.org/doc/stable/glossary.html#term-flattened "Link to this term")\
\
See [ravel](https://numpy.org/doc/stable/glossary.html#term-ravel)\
.\
\
homogeneous[#](https://numpy.org/doc/stable/glossary.html#term-homogeneous "Link to this term")\
\
All elements of a homogeneous array have the same type. ndarrays, in contrast to Python lists, are homogeneous. The type can be complicated, as in a [structured array](https://numpy.org/doc/stable/glossary.html#term-structured-array)\
, but all elements have that type.\
\
NumPy [object arrays](https://numpy.org/doc/stable/glossary.html#term-object-array)\
, which contain references to Python objects, fill the role of heterogeneous arrays.\
\
itemsize[#](https://numpy.org/doc/stable/glossary.html#term-itemsize "Link to this term")\
\
The size of the dtype element in bytes.\
\
little-endian[#](https://numpy.org/doc/stable/glossary.html#term-little-endian "Link to this term")\
\
See [Endianness](https://en.wikipedia.org/wiki/Endianness)\
.\
\
mask[#](https://numpy.org/doc/stable/glossary.html#term-mask "Link to this term")\
\
A boolean array used to select only certain elements for an operation:\
\
\>>> x \= np.arange(5)\
\>>> x\
array(\[0, 1, 2, 3, 4\])\
\
Copy to clipboard\
\
\>>> mask \= (x \> 2)\
\>>> mask\
array(\[False, False, False, True,  True\])\
\
Copy to clipboard\
\
\>>> x\[mask\] \= \-1\
\>>> x\
array(\[ 0,  1,  2,  -1, -1\])\
\
Copy to clipboard\
\
masked array[#](https://numpy.org/doc/stable/glossary.html#term-masked-array "Link to this term")\
\
Bad or missing data can be cleanly ignored by putting it in a masked array, which has an internal boolean array indicating invalid entries. Operations with masked arrays ignore these entries.\
\
\>>> a \= np.ma.masked\_array(\[np.nan, 2, np.nan\], \[True, False, True\])\
\>>> a\
masked\_array(data=\[--, 2.0, --\],\
             mask=\[ True, False,  True\],\
       fill\_value=1e+20)\
\
\>>> a + \[1, 2, 3\]\
masked\_array(data=\[--, 4.0, --\],\
             mask=\[ True, False,  True\],\
       fill\_value=1e+20)\
\
Copy to clipboard\
\
For details, see [Masked arrays.](https://numpy.org/doc/stable/reference/maskedarray.html)\
\
matrix[#](https://numpy.org/doc/stable/glossary.html#term-matrix "Link to this term")\
\
NumPy’s two-dimensional [matrix class](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html)\
 should no longer be used; use regular ndarrays.\
\
ndarray[#](https://numpy.org/doc/stable/glossary.html#term-ndarray "Link to this term")\
\
[NumPy’s basic structure](https://numpy.org/doc/stable/reference/arrays.html)\
.\
\
object array[#](https://numpy.org/doc/stable/glossary.html#term-object-array "Link to this term")\
\
An array whose dtype is `object`; that is, it contains references to Python objects. Indexing the array dereferences the Python objects, so unlike other ndarrays, an object array has the ability to hold heterogeneous objects.\
\
ravel[#](https://numpy.org/doc/stable/glossary.html#term-ravel "Link to this term")\
\
[numpy.ravel](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html)\
 and [numpy.flatten](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html)\
 both flatten an ndarray. `ravel` will return a view if possible; `flatten` always returns a copy.\
\
Flattening collapses a multidimensional array to a single dimension; details of how this is done (for instance, whether `a[n+1]` should be the next row or next column) are parameters.\
\
record array[#](https://numpy.org/doc/stable/glossary.html#term-record-array "Link to this term")\
\
A [structured array](https://numpy.org/doc/stable/glossary.html#term-structured-array)\
 with allowing access in an attribute style (`a.field`) in addition to `a['field']`. For details, see [numpy.recarray.](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html)\
\
row-major[#](https://numpy.org/doc/stable/glossary.html#term-row-major "Link to this term")\
\
See [Row- and column-major order](https://en.wikipedia.org/wiki/Row-_and_column-major_order)\
. NumPy creates arrays in row-major order by default.\
\
scalar[#](https://numpy.org/doc/stable/glossary.html#term-scalar "Link to this term")\
\
In NumPy, usually a synonym for [array scalar](https://numpy.org/doc/stable/glossary.html#term-array-scalar)\
.\
\
shape[#](https://numpy.org/doc/stable/glossary.html#term-shape "Link to this term")\
\
A tuple showing the length of each dimension of an ndarray. The length of the tuple itself is the number of dimensions ([numpy.ndim](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ndim.html)\
). The product of the tuple elements is the number of elements in the array. For details, see [numpy.ndarray.shape](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html)\
.\
\
stride[#](https://numpy.org/doc/stable/glossary.html#term-stride "Link to this term")\
\
Physical memory is one-dimensional; strides provide a mechanism to map a given index to an address in memory. For an N-dimensional array, its `strides` attribute is an N-element tuple; advancing from index `i` to index `i+1` on axis `n` means adding `a.strides[n]` bytes to the address.\
\
Strides are computed automatically from an array’s dtype and shape, but can be directly specified using [as\_strided](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.as_strided.html)\
. Bounds validation can be enabled with the `check_bounds` parameter.\
\
For details, see [numpy.ndarray.strides](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.strides.html)\
.\
\
To see how striding underlies the power of NumPy views, see [The NumPy array: a structure for efficient numerical computation.](https://arxiv.org/pdf/1102.1523.pdf)\
\
structured array[#](https://numpy.org/doc/stable/glossary.html#term-structured-array "Link to this term")\
\
Array whose [dtype](https://numpy.org/doc/stable/glossary.html#term-dtype)\
 is a [structured data type](https://numpy.org/doc/stable/glossary.html#term-structured-data-type)\
.\
\
structured data type[#](https://numpy.org/doc/stable/glossary.html#term-structured-data-type "Link to this term")\
\
Users can create arbitrarily complex [dtypes](https://numpy.org/doc/stable/glossary.html#term-dtype)\
 that can include other arrays and dtypes. These composite dtypes are called [structured data types.](https://numpy.org/doc/stable/user/basics.rec.html)\
\
subarray[#](https://numpy.org/doc/stable/glossary.html#term-subarray "Link to this term")\
\
An array nested in a [structured data type](https://numpy.org/doc/stable/glossary.html#term-structured-data-type)\
, as `b` is here:\
\
\>>> dt \= np.dtype(\[('a', np.int32), ('b', np.float32, (3,))\])\
\>>> np.zeros(3, dtype\=dt)\
array(\[(0, \[0., 0., 0.\]), (0, \[0., 0., 0.\]), (0, \[0., 0., 0.\])\],\
      dtype=\[('a', '<i4'), ('b', '<f4', (3,))\])\
\
Copy to clipboard\
\
subarray data type[#](https://numpy.org/doc/stable/glossary.html#term-subarray-data-type "Link to this term")\
\
An element of a structured datatype that behaves like an ndarray.\
\
title[#](https://numpy.org/doc/stable/glossary.html#term-title "Link to this term")\
\
An alias for a field name in a structured datatype.\
\
type[#](https://numpy.org/doc/stable/glossary.html#term-type "Link to this term")\
\
In NumPy, usually a synonym for [dtype](https://numpy.org/doc/stable/glossary.html#term-dtype)\
. For the more general Python meaning, [see here.](https://docs.python.org/3/glossary.html#term-type "(in Python v3.14)")\
\
ufunc[#](https://numpy.org/doc/stable/glossary.html#term-ufunc "Link to this term")\
\
NumPy’s fast element-by-element computation ([vectorization](https://numpy.org/doc/stable/glossary.html#term-vectorization)\
) gives a choice which function gets applied. The general term for the function is `ufunc`, short for `universal function`. NumPy routines have built-in ufuncs, but users can also [write their own.](https://numpy.org/doc/stable/reference/ufuncs.html)\
\
vectorization[#](https://numpy.org/doc/stable/glossary.html#term-vectorization "Link to this term")\
\
NumPy hands off array processing to C, where looping and computation are much faster than in Python. To exploit this, programmers using NumPy eliminate Python loops in favor of array-to-array operations. [vectorization](https://numpy.org/doc/stable/glossary.html#term-vectorization)\
 can refer both to the C offloading and to structuring NumPy code to leverage it.\
\
view[#](https://numpy.org/doc/stable/glossary.html#term-view "Link to this term")\
\
Without touching underlying data, NumPy can make one array appear to change its datatype and shape.\
\
An array created this way is a _view_, and NumPy often exploits the performance gain of using a view versus making a new array.\
\
A potential drawback is that writing to a view can alter the original as well. If this is a problem, NumPy instead needs to create a physically distinct array – a [`copy`](https://docs.python.org/3/library/copy.html#module-copy "(in Python v3.14)")\
.\
\
Some NumPy routines always return views, some always return copies, some may return one or the other, and for some the choice can be specified. Responsibility for managing views and copies falls to the programmer. [`numpy.shares_memory`](https://numpy.org/doc/stable/reference/generated/numpy.shares_memory.html#numpy.shares_memory "numpy.shares_memory")\
 will check whether `b` is a view of `a`, but an exact answer isn’t always feasible, as the documentation page explains.\
\
\>>> x \= np.arange(5)\
\>>> x\
array(\[0, 1, 2, 3, 4\])\
\
Copy to clipboard\
\
\>>> y \= x\[::2\]\
\>>> y\
array(\[0, 2, 4\])\
\
Copy to clipboard\
\
\>>> x\[0\] \= 3 \# changing x changes y as well, since y is a view on x\
\>>> y\
array(\[3, 2, 4\])\
\
Copy to clipboard