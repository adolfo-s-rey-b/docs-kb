[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.argmax.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_array.argmax.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.argmax.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_array.argmax.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_array.argmax.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_array.argmax.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_array.argmax.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_array.argmax.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_array.argmax.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_array.argmax.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_array.argmax.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_array.argmax.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_array.argmax.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_array.argmax.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_array.argmax.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_array.argmax.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_array.argmax.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_array.argmax.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_array.argmax.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_array.argmax.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_array.argmax.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_array.argmax.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.argmax[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.argmax.html#numpy-ma-masked-array-argmax "Link to this heading")

=========================================================================================================================================================================

method

ma.masked\_array.argmax(_axis=None_, _fill\_value=None_, _out=None_, _\*_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L5742-L5780)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.argmax.html#numpy.ma.masked_array.argmax "Link to this definition")

Returns array of indices of the maximum values along the given axis. Masked values are treated as if they had the value fill\_value.

Parameters:

**axis**{None, integer}

If None, the index is into the flattened array, otherwise along the specified axis

**fill\_value**scalar or None, optional

Value used to fill in the masked values. If None, the output of maximum\_fill\_value(self.\_data) is used instead.

**out**{None, array}, optional

Array into which the result can be placed. Its type is preserved and it must be of the right shape to hold the output.

Returns:

**index\_array**{integer\_array}

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.arange(6).reshape(2,3)
\>>> a.argmax()
5
\>>> a.argmax(0)
array(\[1, 1, 1\])
\>>> a.argmax(1)
array(\[2, 2\])

Copy to clipboard

Go BackOpen In Tab

On this page