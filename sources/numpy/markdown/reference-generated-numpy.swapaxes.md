[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.swapaxes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.swapaxes.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.swapaxes.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.swapaxes.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.swapaxes.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.swapaxes.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.swapaxes.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.swapaxes.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.swapaxes.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.swapaxes.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.swapaxes.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.swapaxes.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.swapaxes.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.swapaxes.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.swapaxes.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.swapaxes.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.swapaxes.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.swapaxes.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.swapaxes.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.swapaxes.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.swapaxes.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.swapaxes.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.swapaxes[#](https://numpy.org/doc/stable/reference/generated/numpy.swapaxes.html#numpy-swapaxes "Link to this heading")

==============================================================================================================================

numpy.swapaxes(_a_, _axis1_, _axis2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L552-L597)
[#](https://numpy.org/doc/stable/reference/generated/numpy.swapaxes.html#numpy.swapaxes "Link to this definition")

Interchange two axes of an array.

Parameters:

**a**array\_like

Input array.

**axis1**int

First axis.

**axis2**int

Second axis.

Returns:

**a\_swapped**ndarray

For NumPy >= 1.10.0, if _a_ is an ndarray, then a view of _a_ is returned; otherwise a new array is created. For earlier NumPy versions a view of _a_ is returned only if the order of the axes is changed, otherwise the input array is returned.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[\[1,2,3\]\])
\>>> np.swapaxes(x,0,1)
array(\[\[1\],\
       \[2\],\
       \[3\]\])

Copy to clipboard

\>>> x \= np.array(\[\[\[0,1\],\[2,3\]\],\[\[4,5\],\[6,7\]\]\])
\>>> x
array(\[\[\[0, 1\],\
        \[2, 3\]\],\
       \[\[4, 5\],\
        \[6, 7\]\]\])

Copy to clipboard

\>>> np.swapaxes(x,0,2)
array(\[\[\[0, 4\],\
        \[2, 6\]\],\
       \[\[1, 5\],\
        \[3, 7\]\]\])

Copy to clipboard

Go BackOpen In Tab

On this page