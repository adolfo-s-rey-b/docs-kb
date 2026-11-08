[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.argmin.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.argmin.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.argmin.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.argmin.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.argmin.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.argmin.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.argmin.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.argmin.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.argmin.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.argmin.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.argmin.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.argmin.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.argmin.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.argmin.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.argmin.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.argmin.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.argmin.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.argmin.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.argmin.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.argmin.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.argmin.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.argmin.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.argmin[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.argmin.html#numpy-ma-maskedarray-argmin "Link to this heading")

=====================================================================================================================================================================

method

ma.MaskedArray.argmin(_axis=None_, _fill\_value=None_, _out=None_, _\*_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L5694-L5740)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.argmin.html#numpy.ma.MaskedArray.argmin "Link to this definition")

Return array of indices to the minimum values along the given axis.

Parameters:

**axis**{None, integer}

If None, the index is into the flattened array, otherwise along the specified axis

**fill\_value**scalar or None, optional

Value used to fill in the masked values. If None, the output of minimum\_fill\_value(self.\_data) is used instead.

**out**{None, array}, optional

Array into which the result can be placed. Its type is preserved and it must be of the right shape to hold the output.

Returns:

ndarray or scalar

If multi-dimension input, returns a new ndarray of indices to the minimum values along the given axis. Otherwise, returns a scalar of index to the minimum values along the given axis.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(np.arange(4), mask\=\[1,1,0,0\])
\>>> x \= x.reshape((2,2))
\>>> x
masked\_array(
  data=\[\[--, --\],\
        \[2, 3\]\],
  mask=\[\[ True,  True\],\
        \[False, False\]\],
  fill\_value=999999)
\>>> x.argmin(axis\=0, fill\_value\=-1)
array(\[0, 0\])
\>>> x.argmin(axis\=0, fill\_value\=9)
array(\[1, 1\])

Copy to clipboard

Go BackOpen In Tab

On this page