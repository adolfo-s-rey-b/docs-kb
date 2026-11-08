[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.compress.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.compress.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.compress.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.compress.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.compress.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.compress.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.compress.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.compress.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.compress.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.compress.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.compress.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.compress.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.compress.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.compress.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.compress.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.compress.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.compress.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.compress.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.compress.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.compress.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.compress.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.compress.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.compress[#](https://numpy.org/doc/stable/reference/generated/numpy.compress.html#numpy-compress "Link to this heading")

==============================================================================================================================

numpy.compress(_condition_, _a_, _axis\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L2175-L2237)
[#](https://numpy.org/doc/stable/reference/generated/numpy.compress.html#numpy.compress "Link to this definition")

Return selected slices of an array along given axis.

When working along a given axis, a slice along that axis is returned in _output_ for each index where _condition_ evaluates to True. When working on a 1-D array, [`compress`](https://numpy.org/doc/stable/reference/generated/numpy.compress.html#numpy.compress "numpy.compress")
 is equivalent to [`extract`](https://numpy.org/doc/stable/reference/generated/numpy.extract.html#numpy.extract "numpy.extract")
.

Parameters:

**condition**1-D array of bools

Array that selects which entries to return. If len(condition) is less than the size of _a_ along the given axis, then output is truncated to the length of the condition array.

**a**array\_like

Array from which to extract a part.

**axis**int, optional

Axis along which to take slices. If None (default), work on the flattened array.

**out**ndarray, optional

Output array. Its type is preserved and it must be of the right shape to hold the output.

Returns:

**compressed\_array**ndarray

A copy of _a_ without the slices along axis for which _condition_ is false.

See also

[`take`](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take "numpy.take")
, [`choose`](https://numpy.org/doc/stable/reference/generated/numpy.choose.html#numpy.choose "numpy.choose")
, [`diag`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")
, [`diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html#numpy.diagonal "numpy.diagonal")
, [`select`](https://numpy.org/doc/stable/reference/generated/numpy.select.html#numpy.select "numpy.select")

[`ndarray.compress`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.compress.html#numpy.ndarray.compress "numpy.ndarray.compress")

Equivalent method in ndarray

[`extract`](https://numpy.org/doc/stable/reference/generated/numpy.extract.html#numpy.extract "numpy.extract")

Equivalent method when working on 1-D arrays

[Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[1, 2\], \[3, 4\], \[5, 6\]\])
\>>> a
array(\[\[1, 2\],\
       \[3, 4\],\
       \[5, 6\]\])
\>>> np.compress(\[0, 1\], a, axis\=0)
array(\[\[3, 4\]\])
\>>> np.compress(\[False, True, True\], a, axis\=0)
array(\[\[3, 4\],\
       \[5, 6\]\])
\>>> np.compress(\[False, True\], a, axis\=1)
array(\[\[2\],\
       \[4\],\
       \[6\]\])

Copy to clipboard

Working on the flattened array does not return slices along an axis but selects elements.

\>>> np.compress(\[False, True\], a)
array(\[2\])

Copy to clipboard

Go BackOpen In Tab

On this page