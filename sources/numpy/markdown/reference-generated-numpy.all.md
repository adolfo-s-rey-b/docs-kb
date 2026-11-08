[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.all.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.all.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.all.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.all.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.all.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.all.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.all.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.all.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.all.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.all.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.all.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.all.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.all.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.all.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.all.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.all.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.all.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.all.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.all.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.all.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.all.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.all.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.all[#](https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy-all "Link to this heading")

===============================================================================================================

numpy.all(_a_, _axis=None_, _out=None_, _keepdims=<no value>_, _\*_, _where=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L2586-L2673)
[#](https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy.all "Link to this definition")

Test whether all array elements along a given axis evaluate to True.

Parameters:

**a**array\_like

Input array or object that can be converted to an array.

**axis**None or int or tuple of ints, optional

Axis or axes along which a logical AND reduction is performed. The default (`axis=None`) is to perform a logical AND over all the dimensions of the input array. _axis_ may be negative, in which case it counts from the last to the first axis. If this is a tuple of ints, a reduction is performed on multiple axes, instead of a single axis or all the axes as before.

**out**ndarray, optional

Alternate output array in which to place the result. It must have the same shape as the expected output and its type is preserved (e.g., if `dtype(out)` is float, the result will consist of 0.0’s and 1.0’s). See [Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)
 for more details.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array.

If the default value is passed, then _keepdims_ will not be passed through to the [`all`](https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy.all "numpy.all")
 method of sub-classes of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, however any non-default value will be. If the sub-class’ method does not implement _keepdims_ any exceptions will be raised.

**where**array\_like of bool, optional

Elements to include in checking for all _True_ values. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

New in version 1.20.0.

Returns:

**all**ndarray, bool

A new boolean or array is returned unless _out_ is specified, in which case a reference to _out_ is returned.

See also

[`ndarray.all`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.all.html#numpy.ndarray.all "numpy.ndarray.all")

equivalent method

[`any`](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any "numpy.any")

Test whether any element along a given axis evaluates to True.

Notes

Not a Number (NaN), positive infinity and negative infinity evaluate to _True_ because these are not equal to zero.

Changed in version 2.0: Before NumPy 2.0, `all` did not return booleans for object dtype input arrays. This behavior is still available via `np.logical_and.reduce`.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.all(\[\[True,False\],\[True,True\]\])
False

Copy to clipboard

\>>> np.all(\[\[True,False\],\[True,True\]\], axis\=0)
array(\[ True, False\])

Copy to clipboard

\>>> np.all(\[\-1, 4, 5\])
True

Copy to clipboard

\>>> np.all(\[1.0, np.nan\])
True

Copy to clipboard

\>>> np.all(\[\[True, True\], \[False, True\]\], where\=\[\[True\], \[False\]\])
True

Copy to clipboard

\>>> o\=np.array(False)
\>>> z\=np.all(\[\-1, 4, 5\], out\=o)
\>>> id(z), id(o), z
(28293632, 28293632, array(True)) # may vary

Copy to clipboard

Go BackOpen In Tab

On this page