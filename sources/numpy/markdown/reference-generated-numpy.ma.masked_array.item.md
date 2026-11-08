[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.item.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_array.item.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.item.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_array.item.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_array.item.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_array.item.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_array.item.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_array.item.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_array.item.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_array.item.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_array.item.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_array.item.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_array.item.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_array.item.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_array.item.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_array.item.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_array.item.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_array.item.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_array.item.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_array.item.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_array.item.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_array.item.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.item[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.item.html#numpy-ma-masked-array-item "Link to this heading")

===================================================================================================================================================================

method

ma.masked\_array.item(_\*args_)[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.item.html#numpy.ma.masked_array.item "Link to this definition")

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

[`item`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.item.html#numpy.ma.masked_array.item "numpy.ma.masked_array.item")
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