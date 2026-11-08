[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.prod.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.prod[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.prod.html#numpy-ma-prod "Link to this heading")

===========================================================================================================================

ma.prod(_self_, _axis=None_, _dtype=None_, _out=None_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7079-L7080)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.prod.html#numpy.ma.prod "Link to this definition")

Return the product of the array elements over the given axis.

Masked elements are set to 1 internally for computation.

Refer to [`numpy.prod`](https://numpy.org/doc/stable/reference/generated/numpy.prod.html#numpy.prod "numpy.prod")
 for full documentation.

See also

[`numpy.ndarray.prod`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.prod.html#numpy.ndarray.prod "numpy.ndarray.prod")

corresponding function for ndarrays

[`numpy.prod`](https://numpy.org/doc/stable/reference/generated/numpy.prod.html#numpy.prod "numpy.prod")

equivalent function

Notes

Arithmetic is modular when using integer types, and no error is raised on overflow.

On this page