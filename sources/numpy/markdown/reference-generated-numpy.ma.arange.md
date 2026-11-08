[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.arange.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.arange.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.arange.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.arange.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.arange.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.arange.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.arange.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.arange.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.arange.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.arange.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.arange.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.arange.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.arange.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.arange.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.arange.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.arange.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.arange.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.arange.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.arange.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.arange.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.arange.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.arange.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.arange[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.arange.html#numpy-ma-arange "Link to this heading")

=================================================================================================================================

ma.arange(\[_start_, \]_stop_, \[_step_, \]_dtype=None_, _\*_, _device=None_, _like=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L8820-L8832)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.arange.html#numpy.ma.arange "Link to this definition")

Return evenly spaced values within a given interval.

`arange` can be called with a varying number of positional arguments:

*   `arange(stop)`: Values are generated within the half-open interval `[0, stop)` (in other words, the interval including _start_ but excluding _stop_).\
    \
*   `arange(start, stop)`: Values are generated within the half-open interval `[start, stop)`.\
    \
*   `arange(start, stop, step)` Values are generated within the half-open interval `[start, stop)`, with spacing between values given by `step`.\
    \
\
For integer arguments the function is roughly equivalent to the Python built-in [`range`](https://docs.python.org/3/library/stdtypes.html#range "(in Python v3.14)")\
, but returns an ndarray rather than a `range` instance.\
\
When using a non-integer step, such as 0.1, it is often better to use [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")\
.\
\
See the Warning sections below for more information.\
\
Parameters:\
\
**start**integer or real, optional\
\
Start of interval. The interval includes this value. The default start value is 0.\
\
**stop**integer or real\
\
End of interval. The interval does not include this value, except in some cases where _step_ is not an integer and floating point round-off affects the length of _out_.\
\
**step**integer or real, optional\
\
Spacing between values. For any output _out_, this is the distance between two adjacent values, `out[i+1] - out[i]`. The default step size is 1. If _step_ is specified as a position argument, _start_ must also be given.\
\
**dtype**dtype, optional\
\
The type of the output array. If [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")\
 is not given, infer the data type from the other input arguments.\
\
**device**str, optional\
\
The device on which to place the created array. Default: `None`. For Array-API interoperability only, so must be `"cpu"` if passed.\
\
New in version 2.0.0.\
\
**like**array\_like, optional\
\
Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as `like` supports the `__array_function__` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.\
\
New in version 1.20.0.\
\
Returns:\
\
**arange**MaskedArray\
\
Array of evenly spaced values.\
\
For floating point arguments, the length of the result is `ceil((stop - start)/step)`. Because of floating point overflow, this rule may result in the last element of _out_ being greater than _stop_.\
\
Warning\
\
The length of the output might not be numerically stable.\
\
Another stability issue is due to the internal implementation of [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")\
. The actual step value used to populate the array is `dtype(start + step) - dtype(start)` and not _step_. Precision loss can occur here, due to casting or due to using floating points when _start_ is much larger than _step_. This can lead to unexpected behaviour. For example:\
\
\>>> np.arange(0, 5, 0.5, dtype\=np.int\_)\
array(\[0, 0, 0, 0, 0, 0, 0, 0, 0, 0\])\
\>>> np.arange(\-3, 3, 0.5, dtype\=np.int\_)\
array(\[-3, -2, -1,  0,  1,  2,  3,  4,  5,  6,  7,  8\])\
\
Copy to clipboard\
\
In such cases, the use of [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")\
 should be preferred.\
\
The built-in [`range`](https://docs.python.org/3/library/stdtypes.html#range "(in Python v3.14)")\
 generates [Python built-in integers that have arbitrary size](https://docs.python.org/3/c-api/long.html "(in Python v3.14)")\
, while [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")\
 produces [`numpy.int32`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int32 "numpy.int32")\
 or [`numpy.int64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")\
 numbers. This may result in incorrect results for large integer values:\
\
\>>> power \= 40\
\>>> modulo \= 10000\
\>>> x1 \= \[(n \*\* power) % modulo for n in range(8)\]\
\>>> x2 \= \[(n \*\* power) % modulo for n in np.arange(8)\]\
\>>> print(x1)\
\[0, 1, 7776, 8801, 6176, 625, 6576, 4001\]  # correct\
\>>> print(x2)\
\[0, 1, 7776, 7185, 0, 5969, 4816, 3361\]  # incorrect\
\
Copy to clipboard\
\
See also\
\
[`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")\
\
Evenly spaced numbers with careful handling of endpoints.\
\
[`numpy.ogrid`](https://numpy.org/doc/stable/reference/generated/numpy.ogrid.html#numpy.ogrid "numpy.ogrid")\
\
Arrays of evenly spaced numbers in N-dimensions.\
\
[`numpy.mgrid`](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")\
\
Grid-shaped arrays of evenly spaced numbers in N-dimensions.\
\
[How to create arrays with regularly-spaced values](https://numpy.org/doc/stable/user/how-to-partition.html#how-to-partition)\
\
Examples\
\
Try it in your browser!\
\
\>>> import numpy as np\
\>>> np.arange(3)\
array(\[0, 1, 2\])\
\>>> np.arange(3.0)\
array(\[ 0.,  1.,  2.\])\
\>>> np.arange(3,7)\
array(\[3, 4, 5, 6\])\
\>>> np.arange(3,7,2)\
array(\[3, 5\])\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
On this page