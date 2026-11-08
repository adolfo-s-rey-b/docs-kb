[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.setxor1d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.setxor1d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.setxor1d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.setxor1d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.setxor1d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.setxor1d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.setxor1d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.setxor1d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.setxor1d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.setxor1d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.setxor1d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.setxor1d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.setxor1d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.setxor1d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.setxor1d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.setxor1d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.setxor1d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.setxor1d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.setxor1d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.setxor1d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.setxor1d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.setxor1d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.setxor1d[#](https://numpy.org/doc/stable/reference/generated/numpy.setxor1d.html#numpy-setxor1d "Link to this heading")

==============================================================================================================================

numpy.setxor1d(_ar1_, _ar2_, _assume\_unique\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_arraysetops_impl.py#L762-L803)
[#](https://numpy.org/doc/stable/reference/generated/numpy.setxor1d.html#numpy.setxor1d "Link to this definition")

Find the set exclusive-or of two arrays.

Return the sorted, unique values that are in only one (not both) of the input arrays.

Parameters:

**ar1, ar2**array\_like

Input arrays.

**assume\_unique**bool

If True, the input arrays are both assumed to be unique, which can speed up the calculation. Default is False.

Returns:

**setxor1d**ndarray

Sorted 1D array of unique values that are in only one of the input arrays.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[1, 2, 3, 2, 4\])
\>>> b \= np.array(\[2, 3, 5, 7, 5\])
\>>> np.setxor1d(a,b)
array(\[1, 4, 5, 7\])

Copy to clipboard

Go BackOpen In Tab

On this page