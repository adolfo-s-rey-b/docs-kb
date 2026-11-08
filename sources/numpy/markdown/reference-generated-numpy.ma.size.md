[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.size.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.size.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.size.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.size.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.size.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.size.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.size.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.size.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.size.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.size.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.size.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.size.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.size.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.size.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.size.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.size.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.size.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.size.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.size.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.size.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.size.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.size.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.size[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.size.html#numpy-ma-size "Link to this heading")

===========================================================================================================================

ma.size(_obj_, _axis\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7781-L7783)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.size.html#numpy.ma.size "Link to this definition")

Return the number of elements along a given axis.

Parameters:

**a**array\_like

Input data.

**axis**None or int or tuple of ints, optional

Axis or axes along which the elements are counted. By default, give the total number of elements.

Changed in version 2.4: Extended to accept multiple axes.

Returns:

**element\_count**int

Number of elements along the specified axis.

See also

[`shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")

dimensions of array

[`ndarray.shape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html#numpy.ndarray.shape "numpy.ndarray.shape")

dimensions of array

[`ndarray.size`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html#numpy.ndarray.size "numpy.ndarray.size")

number of elements in array

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[1,2,3\],\[4,5,6\]\])
\>>> np.size(a)
6
\>>> np.size(a,axis\=1)
3
\>>> np.size(a,axis\=0)
2
\>>> np.size(a,axis\=(0,1))
6

Copy to clipboard

Go BackOpen In Tab

On this page