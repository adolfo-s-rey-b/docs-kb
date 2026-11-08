[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.moveaxis.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.moveaxis.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.moveaxis.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.moveaxis.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.moveaxis.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.moveaxis.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.moveaxis.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.moveaxis.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.moveaxis.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.moveaxis.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.moveaxis.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.moveaxis.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.moveaxis.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.moveaxis.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.moveaxis.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.moveaxis.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.moveaxis.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.moveaxis.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.moveaxis.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.moveaxis.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.moveaxis.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.moveaxis.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.moveaxis[#](https://numpy.org/doc/stable/reference/generated/numpy.moveaxis.html#numpy-moveaxis "Link to this heading")

==============================================================================================================================

numpy.moveaxis(_a_, _source_, _destination_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L1488-L1555)
[#](https://numpy.org/doc/stable/reference/generated/numpy.moveaxis.html#numpy.moveaxis "Link to this definition")

Move axes of an array to new positions.

Other axes remain in their original order.

Parameters:

**a**np.ndarray

The array whose axes should be reordered.

**source**int or sequence of int

Original positions of the axes to move. These must be unique.

**destination**int or sequence of int

Destination positions for each of the original axes. These must also be unique.

Returns:

**result**np.ndarray

Array with moved axes. This array is a view of the input array.

See also

[`transpose`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose "numpy.transpose")

Permute the dimensions of an array.

[`swapaxes`](https://numpy.org/doc/stable/reference/generated/numpy.swapaxes.html#numpy.swapaxes "numpy.swapaxes")

Interchange two axes of an array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.zeros((3, 4, 5))
\>>> np.moveaxis(x, 0, \-1).shape
(4, 5, 3)
\>>> np.moveaxis(x, \-1, 0).shape
(5, 3, 4)

Copy to clipboard

These all achieve the same result:

\>>> np.transpose(x).shape
(5, 4, 3)
\>>> np.swapaxes(x, 0, \-1).shape
(5, 4, 3)
\>>> np.moveaxis(x, \[0, 1\], \[\-1, \-2\]).shape
(5, 4, 3)
\>>> np.moveaxis(x, \[0, 1, 2\], \[\-1, \-2, \-3\]).shape
(5, 4, 3)

Copy to clipboard

Go BackOpen In Tab

On this page