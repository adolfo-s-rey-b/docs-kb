[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.cumsum.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.cumsum.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.cumsum.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.cumsum[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.cumsum.html#numpy-ma-maskedarray-cumsum "Link to this heading")

=====================================================================================================================================================================

method

ma.MaskedArray.cumsum(_axis\=None_, _dtype\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L5261-L5301)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.cumsum.html#numpy.ma.MaskedArray.cumsum "Link to this definition")

Return the cumulative sum of the array elements over the given axis.

Masked values are set to 0 internally during the computation. However, their position is saved, and the result will be masked at the same locations.

Refer to [`numpy.cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")
 for full documentation.

See also

[`numpy.ndarray.cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.cumsum.html#numpy.ndarray.cumsum "numpy.ndarray.cumsum")

corresponding function for ndarrays

[`numpy.cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")

equivalent function

Notes

The mask is lost if _out_ is not a valid [`ma.MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 !

Arithmetic is modular when using integer types, and no error is raised on overflow.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> marr \= np.ma.array(np.arange(10), mask\=\[0,0,0,1,1,1,0,0,0,0\])
\>>> marr.cumsum()
masked\_array(data=\[0, 1, 3, --, --, --, 9, 16, 24, 33\],
             mask=\[False, False, False,  True,  True,  True, False, False,\
                   False, False\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page