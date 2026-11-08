[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.prod.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.prod.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.prod.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.prod.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.prod.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.prod.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.prod.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.prod.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.prod.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.prod.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.prod.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.prod.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.prod.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.prod.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.prod.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.prod.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.prod.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.prod.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.prod.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.prod.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.prod.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.prod.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.prod[#](https://numpy.org/doc/stable/reference/generated/numpy.prod.html#numpy-prod "Link to this heading")

==================================================================================================================

numpy.prod(_a_, _axis=None_, _dtype=None_, _out=None_, _keepdims=<no value>_, _initial=<no value>_, _where=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L3325-L3443)
[#](https://numpy.org/doc/stable/reference/generated/numpy.prod.html#numpy.prod "Link to this definition")

Return the product of array elements over a given axis.

Parameters:

**a**array\_like

Input data.

**axis**None or int or tuple of ints, optional

Axis or axes along which a product is performed. The default, axis=None, will calculate the product of all the elements in the input array. If axis is negative it counts from the last to the first axis.

If axis is a tuple of ints, a product is performed on all of the axes specified in the tuple instead of a single axis or all the axes as before.

**dtype**dtype, optional

The type of the returned array, as well as of the accumulator in which the elements are multiplied. The dtype of _a_ is used by default unless _a_ has an integer dtype of less precision than the default platform integer. In that case, if _a_ is signed then the platform integer is used while if _a_ is unsigned then an unsigned integer of the same precision as the platform integer is used.

**out**ndarray, optional

Alternative output array in which to place the result. It must have the same shape as the expected output, but the type of the output values will be cast if necessary.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array.

If the default value is passed, then _keepdims_ will not be passed through to the [`prod`](https://numpy.org/doc/stable/reference/generated/numpy.prod.html#numpy.prod "numpy.prod")
 method of sub-classes of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, however any non-default value will be. If the sub-class’ method does not implement _keepdims_ any exceptions will be raised.

**initial**scalar, optional

The starting value for this product. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

**where**array\_like of bool, optional

Elements to include in the product. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

Returns:

**product\_along\_axis**ndarray, see [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 parameter above.

An array shaped as _a_ but with the specified axis removed. Returns a reference to _out_ if specified.

See also

[`ndarray.prod`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.prod.html#numpy.ndarray.prod "numpy.ndarray.prod")

equivalent method

[Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)

Notes

Arithmetic is modular when using integer types, and no error is raised on overflow. That means that, on a 32-bit platform:

\>>> x \= np.array(\[536870910, 536870910, 536870910, 536870910\])
\>>> np.prod(x)
16 # may vary

Copy to clipboard

The product of an empty array is the neutral element 1:

\>>> np.prod(\[\])
1.0

Copy to clipboard

Examples

Try it in your browser!

By default, calculate the product of all elements:

\>>> import numpy as np
\>>> np.prod(\[1.,2.\])
2.0

Copy to clipboard

Even when the input array is two-dimensional:

\>>> a \= np.array(\[\[1., 2.\], \[3., 4.\]\])
\>>> np.prod(a)
24.0

Copy to clipboard

But we can also specify the axis over which to multiply:

\>>> np.prod(a, axis\=1)
array(\[  2.,  12.\])
\>>> np.prod(a, axis\=0)
array(\[3., 8.\])

Copy to clipboard

Or select specific elements to include:

\>>> np.prod(\[1., np.nan, 3.\], where\=\[True, False, True\])
3.0

Copy to clipboard

If the type of _x_ is unsigned, then the output type is the unsigned platform integer:

\>>> x \= np.array(\[1, 2, 3\], dtype\=np.uint8)
\>>> np.prod(x).dtype \== np.uint
True

Copy to clipboard

If _x_ is of a signed integer type, then the output type is the default platform integer:

\>>> x \= np.array(\[1, 2, 3\], dtype\=np.int8)
\>>> np.prod(x).dtype \== int
True

Copy to clipboard

You can also start the product with a value other than one:

\>>> np.prod(\[1, 2\], initial\=5)
10

Copy to clipboard

Go BackOpen In Tab

On this page