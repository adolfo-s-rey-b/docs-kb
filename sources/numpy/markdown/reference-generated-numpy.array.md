[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.array.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.array.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.array.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.array.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.array.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.array.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.array.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.array.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.array.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.array.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.array.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.array.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.array.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.array.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.array.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.array.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.array.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.array.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.array.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.array.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.array.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.array[#](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy-array "Link to this heading")

=====================================================================================================================

numpy.array(_object_, _dtype\=None_, _\*_, _copy\=True_, _order\='K'_, _subok\=False_, _ndmin\=0_, _ndmax\=0_, _like\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "Link to this definition")

Create an array.

Parameters:

**object**array\_like

An array, any object exposing the array interface, an object whose `__array__` method returns an array, or any (nested) sequence. If object is a scalar, a 0-dimensional array containing object is returned.

**dtype**data-type, optional

The desired data-type for the array. If not given, NumPy will try to use a default `dtype` that can represent the values (by applying promotion rules when necessary.)

**copy**bool, optional

If `True` (default), then the array data is copied. If `None`, a copy will only be made if `__array__` returns a copy, if obj is a nested sequence, or if a copy is needed to satisfy any of the other requirements (`dtype`, `order`, etc.). Note that any copy of the data is shallow, i.e., for arrays with object dtype, the new array will point to the same objects. See Examples for [`ndarray.copy`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.copy.html#numpy.ndarray.copy "numpy.ndarray.copy")
. For `False` it raises a `ValueError` if a copy cannot be avoided. Default: `True`.

**order**{‘K’, ‘A’, ‘C’, ‘F’}, optional

Specify the memory layout of the array. If object is not an array, the newly created array will be in C order (row major) unless ‘F’ is specified, in which case it will be in Fortran order (column major). If object is an array the following holds.

| order | no copy | copy=True |
| --- | --- | --- |
| ‘K’ | unchanged | F & C order preserved, otherwise most similar order |
| ‘A’ | unchanged | F order if input is F and not C, otherwise C order |
| ‘C’ | C order | C order |
| ‘F’ | F order | F order |

When `copy=None` and a copy is made for other reasons, the result is the same as if `copy=True`, with some exceptions for ‘A’, see the Notes section. The default order is ‘K’.

**subok**bool, optional

If True, then sub-classes will be passed-through, otherwise the returned array will be forced to be a base-class array (default).

**ndmin**int, optional

Specifies the minimum number of dimensions that the resulting array should have. Ones will be prepended to the shape as needed to meet this requirement.

**ndmax**int, optional

Specifies the maximum number of dimensions to create when inferring shape from nested sequences. By default (ndmax=0), NumPy recurses through all nesting levels (up to the compile-time constant `NPY_MAXDIMS`). Setting `ndmax` stops recursion at the specified depth, preserving deeper nested structures as objects instead of promoting them to higher-dimensional arrays. In this case, `dtype=np.object_` is required.

New in version 2.4.0.

**like**array\_like, optional

Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as `like` supports the `__array_function__` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

Returns:

**out**ndarray

An array object satisfying the specified requirements.

See also

[`empty_like`](https://numpy.org/doc/stable/reference/generated/numpy.empty_like.html#numpy.empty_like "numpy.empty_like")

Return an empty array with shape and type of input.

[`ones_like`](https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html#numpy.ones_like "numpy.ones_like")

Return an array of ones with shape and type of input.

[`zeros_like`](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")

Return an array of zeros with shape and type of input.

[`full_like`](https://numpy.org/doc/stable/reference/generated/numpy.full_like.html#numpy.full_like "numpy.full_like")

Return a new array with shape of input filled with value.

[`empty`](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")

Return a new uninitialized array.

[`ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")

Return a new array setting values to one.

[`zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")

Return a new array setting values to zero.

[`full`](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")

Return a new array of given shape filled with value.

[`copy`](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "numpy.copy")

Return an array copy of the given object.

Notes

When order is ‘A’ and `object` is an array in neither ‘C’ nor ‘F’ order, and a copy is forced by a change in dtype, then the order of the result is not necessarily ‘C’ as expected. This is likely a bug.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.array(\[1, 2, 3\])
array(\[1, 2, 3\])

Copy to clipboard

Upcasting:

\>>> np.array(\[1, 2, 3.0\])
array(\[ 1.,  2.,  3.\])

Copy to clipboard

More than one dimension:

\>>> np.array(\[\[1, 2\], \[3, 4\]\])
array(\[\[1, 2\],\
       \[3, 4\]\])

Copy to clipboard

Minimum dimensions 2:

\>>> np.array(\[1, 2, 3\], ndmin\=2)
array(\[\[1, 2, 3\]\])

Copy to clipboard

Type provided:

\>>> np.array(\[1, 2, 3\], dtype\=np.complex128)
array(\[ 1.+0.j,  2.+0.j,  3.+0.j\])

Copy to clipboard

Data-type consisting of more than one element:

\>>> x \= np.array(\[(1,2),(3,4)\],dtype\=\[('a','<i4'),('b','<i4')\])
\>>> x\['a'\]
array(\[1, 3\], dtype=int32)

Copy to clipboard

Creating an array from sub-classes:

\>>> np.array(np.asmatrix('1 2; 3 4'))
array(\[\[1, 2\],\
       \[3, 4\]\])

Copy to clipboard

\>>> np.array(np.asmatrix('1 2; 3 4'), subok\=True)
matrix(\[\[1, 2\],\
        \[3, 4\]\])

Copy to clipboard

Limiting the maximum dimensions with `ndmax`:

\>>> a \= np.array(\[\[1, 2\], \[3, 4\]\], dtype\=np.object\_, ndmax\=2)
\>>> a
array(\[\[1, 2\],\
       \[3, 4\]\], dtype=object)
\>>> a.shape
(2, 2)

Copy to clipboard

\>>> b \= np.array(\[\[1, 2\], \[3, 4\]\], dtype\=np.object\_, ndmax\=1)
\>>> b
array(\[list(\[1, 2\]), list(\[3, 4\])\], dtype=object)
\>>> b.shape
(2,)

Copy to clipboard

Go BackOpen In Tab

On this page