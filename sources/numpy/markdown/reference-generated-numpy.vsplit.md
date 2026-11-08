[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.vsplit.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.vsplit.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.vsplit.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.vsplit.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.vsplit.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.vsplit.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.vsplit.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.vsplit.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.vsplit.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.vsplit.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.vsplit.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.vsplit.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.vsplit.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.vsplit.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.vsplit.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.vsplit.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.vsplit.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.vsplit.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.vsplit.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.vsplit.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.vsplit.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.vsplit.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.vsplit[#](https://numpy.org/doc/stable/reference/generated/numpy.vsplit.html#numpy-vsplit "Link to this heading")

========================================================================================================================

numpy.vsplit(_ary_, _indices\_or\_sections_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_shape_base_impl.py#L934-L985)
[#](https://numpy.org/doc/stable/reference/generated/numpy.vsplit.html#numpy.vsplit "Link to this definition")

Split an array into multiple sub-arrays vertically (row-wise).

Please refer to the `split` documentation. `vsplit` is equivalent to `split` with _axis=0_ (default), the array is always split along the first axis regardless of the array dimension.

See also

[`split`](https://numpy.org/doc/stable/reference/generated/numpy.split.html#numpy.split "numpy.split")

Split an array into multiple sub-arrays of equal size.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(16.0).reshape(4, 4)
\>>> x
array(\[\[ 0.,   1.,   2.,   3.\],\
       \[ 4.,   5.,   6.,   7.\],\
       \[ 8.,   9.,  10.,  11.\],\
       \[12.,  13.,  14.,  15.\]\])
\>>> np.vsplit(x, 2)
\[array(\[\[0., 1., 2., 3.\],\
        \[4., 5., 6., 7.\]\]),\
 array(\[\[ 8.,  9., 10., 11.\],\
        \[12., 13., 14., 15.\]\])\]
\>>> np.vsplit(x, np.array(\[3, 6\]))
\[array(\[\[ 0.,  1.,  2.,  3.\],\
        \[ 4.,  5.,  6.,  7.\],\
        \[ 8.,  9., 10., 11.\]\]),\
 array(\[\[12., 13., 14., 15.\]\]),\
 array(\[\], shape=(0, 4), dtype=float64)\]

Copy to clipboard

With a higher dimensional array the split is still along the first axis.

\>>> x \= np.arange(8.0).reshape(2, 2, 2)
\>>> x
array(\[\[\[0.,  1.\],\
        \[2.,  3.\]\],\
       \[\[4.,  5.\],\
        \[6.,  7.\]\]\])
\>>> np.vsplit(x, 2)
\[array(\[\[\[0., 1.\],\
         \[2., 3.\]\]\]),\
 array(\[\[\[4., 5.\],\
         \[6., 7.\]\]\])\]

Copy to clipboard

Go BackOpen In Tab

On this page