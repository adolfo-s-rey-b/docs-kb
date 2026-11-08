[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.at.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ufunc.at.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.at.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ufunc.at.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ufunc.at.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ufunc.at.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ufunc.at.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ufunc.at.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ufunc.at.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ufunc.at.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ufunc.at.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ufunc.at.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ufunc.at.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ufunc.at.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ufunc.at.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ufunc.at.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ufunc.at.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ufunc.at.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ufunc.at.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ufunc.at.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ufunc.at.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ufunc.at.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ufunc.at[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.at.html#numpy-ufunc-at "Link to this heading")

==============================================================================================================================

method

ufunc.at(_a_, _indices_, _b\=None_, _/_)[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.at.html#numpy.ufunc.at "Link to this definition")

Performs unbuffered in place operation on operand ‘a’ for elements specified by ‘indices’. For addition ufunc, this method is equivalent to `a[indices] += b`, except that results are accumulated for elements that are indexed more than once. For example, `a[[0,0]] += 1` will only increment the first element once because of buffering, whereas `add.at(a, [0,0], 1)` will increment the first element twice.

Parameters:

**a**array\_like

The array to perform in place operation on.

**indices**array\_like or tuple

Array like index object or slice object for indexing into first operand. If first operand has multiple dimensions, indices can be a tuple of array like index objects or slice objects.

**b**array\_like

Second operand for ufuncs requiring two operands. Operand must be broadcastable over first operand after indexing or slicing.

Examples

Try it in your browser!

Set items 0 and 1 to their negative values:

\>>> import numpy as np
\>>> a \= np.array(\[1, 2, 3, 4\])
\>>> np.negative.at(a, \[0, 1\])
\>>> a
array(\[-1, -2,  3,  4\])

Copy to clipboard

Increment items 0 and 1, and increment item 2 twice:

\>>> a \= np.array(\[1, 2, 3, 4\])
\>>> np.add.at(a, \[0, 1, 2, 2\], 1)
\>>> a
array(\[2, 3, 5, 4\])

Copy to clipboard

Add items 0 and 1 in first array to second array, and store results in first array:

\>>> a \= np.array(\[1, 2, 3, 4\])
\>>> b \= np.array(\[1, 2\])
\>>> np.add.at(a, \[0, 1\], b)
\>>> a
array(\[2, 4, 3, 4\])

Copy to clipboard

Go BackOpen In Tab

On this page