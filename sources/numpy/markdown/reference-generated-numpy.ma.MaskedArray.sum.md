[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.sum.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.sum.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.sum.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.sum.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.sum.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.sum.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.sum.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.sum.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.sum.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.sum.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.sum.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.sum.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.sum.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.sum.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.sum.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.sum.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.sum.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.sum.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.sum.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.sum.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.sum.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.sum.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.sum[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.sum.html#numpy-ma-maskedarray-sum "Link to this heading")

============================================================================================================================================================

method

ma.MaskedArray.sum(_axis=None_, _dtype=None_, _out=None_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L5198-L5259)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.sum.html#numpy.ma.MaskedArray.sum "Link to this definition")

Return the sum of the array elements over the given axis.

Masked elements are set to 0 internally.

Refer to [`numpy.sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
 for full documentation.

See also

[`numpy.ndarray.sum`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sum.html#numpy.ndarray.sum "numpy.ndarray.sum")

corresponding function for ndarrays

[`numpy.sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")

equivalent function

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(\[\[1,2,3\],\[4,5,6\],\[7,8,9\]\], mask\=\[0\] + \[1,0\]\*4)
\>>> x
masked\_array(
  data=\[\[1, --, 3\],\
        \[--, 5, --\],\
        \[7, --, 9\]\],
  mask=\[\[False,  True, False\],\
        \[ True, False,  True\],\
        \[False,  True, False\]\],
  fill\_value=999999)
\>>> x.sum()
25
\>>> x.sum(axis\=1)
masked\_array(data=\[4, 5, 16\],
             mask=\[False, False, False\],
       fill\_value=999999)
\>>> x.sum(axis\=0)
masked\_array(data=\[8, 5, 12\],
             mask=\[False, False, False\],
       fill\_value=999999)
\>>> print(type(x.sum(axis\=0, dtype\=np.int64)\[0\]))
<class 'numpy.int64'>

Copy to clipboard

Go BackOpen In Tab

On this page