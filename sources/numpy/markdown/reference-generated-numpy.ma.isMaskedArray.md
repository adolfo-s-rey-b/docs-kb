[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.isMaskedArray.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.isMaskedArray.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.isMaskedArray.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.isMaskedArray.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.isMaskedArray.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.isMaskedArray.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.isMaskedArray.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.isMaskedArray.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.isMaskedArray.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.isMaskedArray.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.isMaskedArray.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.isMaskedArray.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.isMaskedArray.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.isMaskedArray.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.isMaskedArray.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.isMaskedArray.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.isMaskedArray.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.isMaskedArray.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.isMaskedArray.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.isMaskedArray.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.isMaskedArray.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.isMaskedArray.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.isMaskedArray[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.isMaskedArray.html#numpy-ma-ismaskedarray "Link to this heading")

======================================================================================================================================================

ma.isMaskedArray(_x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L6685-L6734)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.isMaskedArray.html#numpy.ma.isMaskedArray "Link to this definition")

Test whether input is an instance of MaskedArray.

This function returns True if _x_ is an instance of MaskedArray and returns False otherwise. Any object is accepted as input.

Parameters:

**x**object

Object to test.

Returns:

**result**bool

True if _x_ is a MaskedArray.

See also

[`isMA`](https://numpy.org/doc/stable/reference/generated/numpy.ma.isMA.html#numpy.ma.isMA "numpy.ma.isMA")

Alias to isMaskedArray.

[`isarray`](https://numpy.org/doc/stable/reference/generated/numpy.ma.isarray.html#numpy.ma.isarray "numpy.ma.isarray")

Alias to isMaskedArray.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> a \= np.eye(3, 3)
\>>> a
array(\[\[ 1.,  0.,  0.\],\
       \[ 0.,  1.,  0.\],\
       \[ 0.,  0.,  1.\]\])
\>>> m \= ma.masked\_values(a, 0)
\>>> m
masked\_array(
  data=\[\[1.0, --, --\],\
        \[--, 1.0, --\],\
        \[--, --, 1.0\]\],
  mask=\[\[False,  True,  True\],\
        \[ True, False,  True\],\
        \[ True,  True, False\]\],
  fill\_value=0.0)
\>>> ma.isMaskedArray(a)
False
\>>> ma.isMaskedArray(m)
True
\>>> ma.isMaskedArray(\[0, 1, 2\])
False

Copy to clipboard

Go BackOpen In Tab

On this page