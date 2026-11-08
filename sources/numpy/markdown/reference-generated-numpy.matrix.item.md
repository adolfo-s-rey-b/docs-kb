[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.item.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.item[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.item.html#numpy-matrix-item "Link to this heading")

=======================================================================================================================================

method

matrix.item(_\*args_)[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.item.html#numpy.matrix.item "Link to this definition")

Copy an element of an array to a standard Python scalar and return it.

Parameters:

**\*args**Arguments (variable number and type)

*   none: in this case, the method only works for arrays with one element (_a.size == 1_), which element is copied into a standard Python scalar object and returned.
    
*   int\_type: this argument is interpreted as a flat index into the array, specifying which element to copy and return.
    
*   tuple of int\_types: functions as does a single int\_type argument, except that the argument is interpreted as an nd-index into the array.
    

Returns:

**z**Standard Python scalar object

A copy of the specified element of the array as a suitable Python scalar

Notes

When the data type of _a_ is longdouble or clongdouble, item() returns a scalar array object because there is no available Python scalar that would not lose information. Void arrays return a buffer object for item(), unless fields are defined, in which case a tuple is returned.

[`item`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.item.html#numpy.matrix.item "numpy.matrix.item")
 is very similar to a\[args\], except, instead of an array scalar, a standard Python scalar is returned. This can be useful for speeding up access to elements of the array and doing arithmetic on elements of the array using Python’s optimized math.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.random.seed(123)
\>>> x \= np.random.randint(9, size\=(3, 3))
\>>> x
array(\[\[2, 2, 6\],\
       \[1, 3, 6\],\
       \[1, 0, 1\]\])
\>>> x.item(3)
1
\>>> x.item(7)
0
\>>> x.item((0, 1))
2
\>>> x.item((2, 2))
1

Copy to clipboard

For an array with object dtype, elements are returned as-is.

\>>> a \= np.array(\[np.int64(1)\], dtype\=np.object\_)
\>>> a.item() #return np.int64
np.int64(1)

Copy to clipboard

Go BackOpen In Tab

On this page