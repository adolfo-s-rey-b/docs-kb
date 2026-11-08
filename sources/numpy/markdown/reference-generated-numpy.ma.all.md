[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.all.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.all.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.all.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.all.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.all.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.all.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.all.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.all.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.all.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.all.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.all.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.all.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.all.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.all.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.all.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.all.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.all.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.all.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.all.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.all.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.all.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.all.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.all[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.all.html#numpy-ma-all "Link to this heading")

========================================================================================================================

ma.all(_self_, _axis=None_, _out=None_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7079-L7080)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.all.html#numpy.ma.all "Link to this definition")

Returns True if all elements evaluate to True.

The output array is masked where all the values along the given axis are masked: if the output would have been a scalar and that all the values are masked, then the output is [`masked`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.masked "numpy.ma.masked")
.

Refer to [`numpy.all`](https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy.all "numpy.all")
 for full documentation.

See also

[`numpy.ndarray.all`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.all.html#numpy.ndarray.all "numpy.ndarray.all")

corresponding function for ndarrays

[`numpy.all`](https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy.all "numpy.all")

equivalent function

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.ma.array(\[1,2,3\]).all()
True
\>>> a \= np.ma.array(\[1,2,3\], mask\=True)
\>>> (a.all() is np.ma.masked)
True

Copy to clipboard

Go BackOpen In Tab

On this page