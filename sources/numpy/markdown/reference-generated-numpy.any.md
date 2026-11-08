[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.any.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.any.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.any.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.any.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.any.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.any.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.any.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.any.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.any.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.any.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.any.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.any.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.any.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.any.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.any.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.any.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.any.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.any.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.any.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.any.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.any.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.any.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.any[#](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy-any "Link to this heading")

===============================================================================================================

numpy.any(_a_, _axis=None_, _out=None_, _keepdims=<no value>_, _\*_, _where=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L2474-L2578)
[#](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any "Link to this definition")

Test whether any array element along a given axis evaluates to True.

Returns single boolean if _axis_ is `None`

Parameters:

**a**array\_like

Input array or object that can be converted to an array.

**axis**None or int or tuple of ints, optional

Axis or axes along which a logical OR reduction is performed. The default (`axis=None`) is to perform a logical OR over all the dimensions of the input array. _axis_ may be negative, in which case it counts from the last to the first axis. If this is a tuple of ints, a reduction is performed on multiple axes, instead of a single axis or all the axes as before.

**out**ndarray, optional

Alternate output array in which to place the result. It must have the same shape as the expected output and its type is preserved (e.g., if it is of type float, then it will remain so, returning 1.0 for True and 0.0 for False, regardless of the type of _a_). See [Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)
 for more details.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array.

If the default value is passed, then _keepdims_ will not be passed through to the [`any`](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any "numpy.any")
 method of sub-classes of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, however any non-default value will be. If the sub-class’ method does not implement _keepdims_ any exceptions will be raised.

**where**array\_like of bool, optional

Elements to include in checking for any _True_ values. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

New in version 1.20.0.

Returns:

**any**bool or ndarray

A new boolean or [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 is returned unless _out_ is specified, in which case a reference to _out_ is returned.

See also

[`ndarray.any`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.any.html#numpy.ndarray.any "numpy.ndarray.any")

equivalent method

[`all`](https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy.all "numpy.all")

Test whether all elements along a given axis evaluate to True.

Notes

Not a Number (NaN), positive infinity and negative infinity evaluate to _True_ because these are not equal to zero.

Changed in version 2.0: Before NumPy 2.0, `any` did not return booleans for object dtype input arrays. This behavior is still available via `np.logical_or.reduce`.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.any(\[\[True, False\], \[True, True\]\])
True

Copy to clipboard

\>>> np.any(\[\[True,  False, True \],\
...         \[False, False, False\]\], axis\=0)
array(\[ True, False, True\])

Copy to clipboard

\>>> np.any(\[\-1, 0, 5\])
True

Copy to clipboard

\>>> np.any(\[\[np.nan\], \[np.inf\]\], axis\=1, keepdims\=True)
array(\[\[ True\],\
       \[ True\]\])

Copy to clipboard

\>>> np.any(\[\[True, False\], \[False, False\]\], where\=\[\[False\], \[True\]\])
False

Copy to clipboard

\>>> a \= np.array(\[\[1, 0, 0\],\
...               \[0, 0, 1\],\
...               \[0, 0, 0\]\])
\>>> np.any(a, axis\=0)
array(\[ True, False,  True\])
\>>> np.any(a, axis\=1)
array(\[ True,  True, False\])

Copy to clipboard

\>>> o\=np.array(False)
\>>> z\=np.any(\[\-1, 4, 5\], out\=o)
\>>> z, o
(array(True), array(True))
\>>> \# Check now that z is a reference to o
\>>> z is o
True
\>>> id(z), id(o) \# identity of z and o              
(191614240, 191614240)

Copy to clipboard

Go BackOpen In Tab

On this page