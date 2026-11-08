[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.dsplit.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.dsplit.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.dsplit.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.dsplit.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.dsplit.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.dsplit.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.dsplit.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.dsplit.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.dsplit.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.dsplit.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.dsplit.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.dsplit.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.dsplit.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.dsplit.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.dsplit.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.dsplit.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.dsplit.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.dsplit.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.dsplit.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.dsplit.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.dsplit.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.dsplit.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.dsplit[#](https://numpy.org/doc/stable/reference/generated/numpy.dsplit.html#numpy-dsplit "Link to this heading")

========================================================================================================================

numpy.dsplit(_ary_, _indices\_or\_sections_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_shape_base_impl.py#L988-L1031)
[#](https://numpy.org/doc/stable/reference/generated/numpy.dsplit.html#numpy.dsplit "Link to this definition")

Split array into multiple sub-arrays along the 3rd axis (depth).

Please refer to the [`split`](https://numpy.org/doc/stable/reference/generated/numpy.split.html#numpy.split "numpy.split")
 documentation. [`dsplit`](https://numpy.org/doc/stable/reference/generated/numpy.dsplit.html#numpy.dsplit "numpy.dsplit")
 is equivalent to [`split`](https://numpy.org/doc/stable/reference/generated/numpy.split.html#numpy.split "numpy.split")
 with `axis=2`, the array is always split along the third axis provided the array dimension is greater than or equal to 3.

See also

[`split`](https://numpy.org/doc/stable/reference/generated/numpy.split.html#numpy.split "numpy.split")

Split an array into multiple sub-arrays of equal size.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(16.0).reshape(2, 2, 4)
\>>> x
array(\[\[\[ 0.,   1.,   2.,   3.\],\
        \[ 4.,   5.,   6.,   7.\]\],\
       \[\[ 8.,   9.,  10.,  11.\],\
        \[12.,  13.,  14.,  15.\]\]\])
\>>> np.dsplit(x, 2)
\[array(\[\[\[ 0.,  1.\],\
        \[ 4.,  5.\]\],\
       \[\[ 8.,  9.\],\
        \[12., 13.\]\]\]), array(\[\[\[ 2.,  3.\],\
        \[ 6.,  7.\]\],\
       \[\[10., 11.\],\
        \[14., 15.\]\]\])\]
\>>> np.dsplit(x, np.array(\[3, 6\]))
\[array(\[\[\[ 0.,   1.,   2.\],\
        \[ 4.,   5.,   6.\]\],\
       \[\[ 8.,   9.,  10.\],\
        \[12.,  13.,  14.\]\]\]),\
 array(\[\[\[ 3.\],\
        \[ 7.\]\],\
       \[\[11.\],\
        \[15.\]\]\]),\
array(\[\], shape=(2, 2, 0), dtype=float64)\]

Copy to clipboard

Go BackOpen In Tab

On this page