[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.sum.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.sum[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.sum.html#numpy-ma-sum "Link to this heading")

========================================================================================================================

ma.sum(_self_, _axis=None_, _dtype=None_, _out=None_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7079-L7080)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.sum.html#numpy.ma.sum "Link to this definition")

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