[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.mean.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_array.mean.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.mean.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_array.mean.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_array.mean.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_array.mean.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_array.mean.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_array.mean.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_array.mean.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_array.mean.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_array.mean.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_array.mean.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_array.mean.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_array.mean.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_array.mean.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_array.mean.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_array.mean.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_array.mean.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_array.mean.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_array.mean.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_array.mean.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_array.mean.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.mean[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.mean.html#numpy-ma-masked-array-mean "Link to this heading")

===================================================================================================================================================================

method

ma.masked\_array.mean(_axis=None_, _dtype=None_, _out=None_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L5376-L5430)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.mean.html#numpy.ma.masked_array.mean "Link to this definition")

Returns the average of the array elements along given axis.

Masked entries are ignored, and result elements which are not finite will be masked.

Refer to [`numpy.mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
 for full documentation.

See also

[`numpy.ndarray.mean`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.mean.html#numpy.ndarray.mean "numpy.ndarray.mean")

corresponding function for ndarrays

[`numpy.mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")

Equivalent function

[`numpy.ma.average`](https://numpy.org/doc/stable/reference/generated/numpy.ma.average.html#numpy.ma.average "numpy.ma.average")

Weighted average.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.ma.array(\[1,2,3\], mask\=\[False, False, True\])
\>>> a
masked\_array(data=\[1, 2, --\],
             mask=\[False, False,  True\],
       fill\_value=999999)
\>>> a.mean()
1.5

Copy to clipboard

Go BackOpen In Tab

On this page