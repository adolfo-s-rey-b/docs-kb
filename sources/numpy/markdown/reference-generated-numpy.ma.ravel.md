[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.ravel.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.ravel.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.ravel.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.ravel.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.ravel.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.ravel.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.ravel.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.ravel.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.ravel.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.ravel.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.ravel.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.ravel.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.ravel.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.ravel.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.ravel.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.ravel.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.ravel.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.ravel.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.ravel.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.ravel.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.ravel.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.ravel.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.ravel[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.ravel.html#numpy-ma-ravel "Link to this heading")

==============================================================================================================================

ma.ravel(_self_, _order\='C'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7079-L7080)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.ravel.html#numpy.ma.ravel "Link to this definition")

Returns a 1D version of self, as a view.

Parameters:

**order**{‘C’, ‘F’, ‘A’, ‘K’}, optional

The elements of _a_ are read using this index order. ‘C’ means to index the elements in C-like order, with the last axis index changing fastest, back to the first axis index changing slowest. ‘F’ means to index the elements in Fortran-like index order, with the first index changing fastest, and the last index changing slowest. Note that the ‘C’ and ‘F’ options take no account of the memory layout of the underlying array, and only refer to the order of axis indexing. ‘A’ means to read the elements in Fortran-like index order if _m_ is Fortran _contiguous_ in memory, C-like order otherwise. ‘K’ means to read the elements in the order they occur in memory, except for reversing the data when strides are negative. By default, ‘C’ index order is used. (Masked arrays currently use ‘A’ on the data when ‘K’ is passed.)

Returns:

MaskedArray

Output view is of shape `(self.size,)` (or `(np.ma.product(self.shape),)`).

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
\>>> x.ravel()
masked\_array(data=\[1, --, 3, --, 5, --, 7, --, 9\],
             mask=\[False,  True, False,  True, False,  True, False,  True,\
                   False\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page