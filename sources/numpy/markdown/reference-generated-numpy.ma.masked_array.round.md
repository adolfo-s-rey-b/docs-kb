[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.round.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_array.round.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.round.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_array.round.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_array.round.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_array.round.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_array.round.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_array.round.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_array.round.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_array.round.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_array.round.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_array.round.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_array.round.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_array.round.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_array.round.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_array.round.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_array.round.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_array.round.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_array.round.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_array.round.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_array.round.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_array.round.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.round[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.round.html#numpy-ma-masked-array-round "Link to this heading")

======================================================================================================================================================================

method

ma.masked\_array.round(_decimals\=0_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L5570-L5605)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.round.html#numpy.ma.masked_array.round "Link to this definition")

Return each element rounded to the given number of decimals.

Refer to [`numpy.around`](https://numpy.org/doc/stable/reference/generated/numpy.around.html#numpy.around "numpy.around")
 for full documentation.

See also

[`numpy.ndarray.round`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.round.html#numpy.ndarray.round "numpy.ndarray.round")

corresponding function for ndarrays

[`numpy.around`](https://numpy.org/doc/stable/reference/generated/numpy.around.html#numpy.around "numpy.around")

equivalent function

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> x \= ma.array(\[1.35, 2.5, 1.5, 1.75, 2.25, 2.75\],
...              mask\=\[0, 0, 0, 1, 0, 0\])
\>>> ma.round(x)
masked\_array(data=\[1.0, 2.0, 2.0, --, 2.0, 3.0\],
             mask=\[False, False, False,  True, False, False\],
        fill\_value=1e+20)

Copy to clipboard

Go BackOpen In Tab

On this page