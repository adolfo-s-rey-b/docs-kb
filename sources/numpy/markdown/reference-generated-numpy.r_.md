[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.r_.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.r_.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.r_.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.r_.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.r_.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.r_.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.r_.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.r_.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.r_.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.r_.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.r_.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.r_.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.r_.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.r_.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.r_.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.r_.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.r_.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.r_.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.r_.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.r_.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.r_.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.r\_[#](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy-r "Link to this heading")

============================================================================================================

numpy.r\_ _\= <numpy.lib.\_index\_tricks\_impl.RClass object>_[#](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "Link to this definition")

Translates slice objects to concatenation along the first axis.

This is a simple way to build up arrays quickly. There are two use cases.

1.  If the index expression contains comma separated arrays, then stack them along their first axis.
    
2.  If the index expression contains slice notation or scalars then create a 1-D array with a range indicated by the slice notation.
    

If slice notation is used, the syntax `start:stop:step` is equivalent to `np.arange(start, stop, step)` inside of the brackets. However, if `step` is an imaginary number (i.e. 100j) then its integer portion is interpreted as a number-of-points desired and the start and stop are inclusive. In other words `start:stop:stepj` is interpreted as `np.linspace(start, stop, step, endpoint=1)` inside of the brackets. After expansion of slice notation, all comma separated sequences are concatenated together.

Optional character strings placed as the first element of the index expression can be used to change the output. The strings ‘r’ or ‘c’ result in matrix output. If the result is 1-D and ‘r’ is specified a 1 x N (row) matrix is produced. If the result is 1-D and ‘c’ is specified, then an N x 1 (column) matrix is produced. If the result is 2-D then both provide the same matrix result.

A string integer specifies which axis to stack multiple comma separated arrays along. A string of two comma-separated integers allows indication of the minimum number of dimensions to force each entry into as the second integer (the axis to concatenate along is still the first integer).

A string with three comma-separated integers allows specification of the axis to concatenate along, the minimum number of dimensions to force the entries to, and which axis should contain the start of the arrays which are less than the specified number of dimensions. In other words the third integer allows you to specify where the 1’s should be placed in the shape of the arrays that have their shapes upgraded. By default, they are placed in the front of the shape tuple. The third argument allows you to specify where the start of the array should be instead. Thus, a third argument of ‘0’ would place the 1’s at the end of the array shape. Negative integers specify where in the new shape tuple the last dimension of upgraded arrays should be placed, so the default is ‘-1’.

Parameters:

**Not a function, so takes no parameters**

Returns:

A concatenated ndarray or matrix.

See also

[`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")

Join a sequence of arrays along an existing axis.

[`c_`](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")

Translates slice objects to concatenation along the second axis.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.r\_\[np.array(\[1,2,3\]), 0, 0, np.array(\[4,5,6\])\]
array(\[1, 2, 3, ..., 4, 5, 6\])
\>>> np.r\_\[\-1:1:6j, \[0\]\*3, 5, 6\]
array(\[-1. , -0.6, -0.2,  0.2,  0.6,  1. ,  0. ,  0. ,  0. ,  5. ,  6. \])

Copy to clipboard

String integers specify the axis to concatenate along or the minimum number of dimensions to force entries into.

\>>> a \= np.array(\[\[0, 1, 2\], \[3, 4, 5\]\])
\>>> np.r\_\['-1', a, a\] \# concatenate along last axis
array(\[\[0, 1, 2, 0, 1, 2\],\
       \[3, 4, 5, 3, 4, 5\]\])
\>>> np.r\_\['0,2', \[1,2,3\], \[4,5,6\]\] \# concatenate along first axis, dim>=2
array(\[\[1, 2, 3\],\
       \[4, 5, 6\]\])

Copy to clipboard

\>>> np.r\_\['0,2,0', \[1,2,3\], \[4,5,6\]\]
array(\[\[1\],\
       \[2\],\
       \[3\],\
       \[4\],\
       \[5\],\
       \[6\]\])
\>>> np.r\_\['1,2,0', \[1,2,3\], \[4,5,6\]\]
array(\[\[1, 4\],\
       \[2, 5\],\
       \[3, 6\]\])

Copy to clipboard

Using ‘r’ or ‘c’ as a first string argument creates a matrix.

\>>> np.r\_\['r',\[1,2,3\], \[4,5,6\]\]
matrix(\[\[1, 2, 3, 4, 5, 6\]\])

Copy to clipboard

Go BackOpen In Tab

On this page