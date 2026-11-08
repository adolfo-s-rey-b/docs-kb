[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.diag[#](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy-diag "Link to this heading")

==================================================================================================================

numpy.diag(_v_, _k\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_twodim_base_impl.py#L260-L330)
[#](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "Link to this definition")

Extract a diagonal or construct a diagonal array.

See the more detailed documentation for `numpy.diagonal` if you use this function to extract a diagonal and wish to write to the resulting array; whether it returns a copy or a view depends on what version of numpy you are using.

Parameters:

**v**array\_like

If _v_ is a 2-D array, return a copy of its _k_\-th diagonal. If _v_ is a 1-D array, return a 2-D array with _v_ on the _k_\-th diagonal.

**k**int, optional

Diagonal in question. The default is 0. Use _k>0_ for diagonals above the main diagonal, and _k<0_ for diagonals below the main diagonal.

Returns:

**out**ndarray

The extracted diagonal or constructed diagonal array.

See also

[`diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html#numpy.diagonal "numpy.diagonal")

Return specified diagonals.

[`diagflat`](https://numpy.org/doc/stable/reference/generated/numpy.diagflat.html#numpy.diagflat "numpy.diagflat")

Create a 2-D array with the flattened input as a diagonal.

[`trace`](https://numpy.org/doc/stable/reference/generated/numpy.trace.html#numpy.trace "numpy.trace")

Sum along diagonals.

[`triu`](https://numpy.org/doc/stable/reference/generated/numpy.triu.html#numpy.triu "numpy.triu")

Upper triangle of an array.

[`tril`](https://numpy.org/doc/stable/reference/generated/numpy.tril.html#numpy.tril "numpy.tril")

Lower triangle of an array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(9).reshape((3,3))
\>>> x
array(\[\[0, 1, 2\],\
       \[3, 4, 5\],\
       \[6, 7, 8\]\])

Copy to clipboard

\>>> np.diag(x)
array(\[0, 4, 8\])
\>>> np.diag(x, k\=1)
array(\[1, 5\])
\>>> np.diag(x, k\=-1)
array(\[3, 7\])

Copy to clipboard

\>>> np.diag(np.diag(x))
array(\[\[0, 0, 0\],\
       \[0, 4, 0\],\
       \[0, 0, 8\]\])

Copy to clipboard

Go BackOpen In Tab

On this page