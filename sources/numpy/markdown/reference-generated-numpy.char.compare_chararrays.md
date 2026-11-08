[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.compare_chararrays.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.char.compare_chararrays.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.char.compare_chararrays.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.char.compare_chararrays.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.char.compare_chararrays.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.char.compare_chararrays.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.char.compare_chararrays.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.char.compare_chararrays.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.char.compare_chararrays.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.char.compare_chararrays.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.char.compare_chararrays.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.char.compare_chararrays.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.char.compare_chararrays.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.char.compare_chararrays.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.char.compare_chararrays.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.char.compare_chararrays.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.char.compare_chararrays.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.char.compare_chararrays.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.char.compare_chararrays.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.char.compare_chararrays.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.char.compare_chararrays.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.char.compare_chararrays.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.compare\_chararrays[#](https://numpy.org/doc/stable/reference/generated/numpy.char.compare_chararrays.html#numpy-char-compare-chararrays "Link to this heading")

============================================================================================================================================================================

char.compare\_chararrays(_a1_, _a2_, _cmp_, _rstrip_)[#](https://numpy.org/doc/stable/reference/generated/numpy.char.compare_chararrays.html#numpy.char.compare_chararrays "Link to this definition")

Performs element-wise comparison of two string arrays using the comparison operator specified by _cmp_.

Parameters:

**a1, a2**array\_like

Arrays to be compared.

**cmp**{“<”, “<=”, “==”, “>=”, “>”, “!=”}

Type of comparison.

**rstrip**bool

If True, the spaces at the end of strings are removed before the comparison.

Returns:

**out**ndarray

The output array of type [`numpy.bool`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool "numpy.bool")
 with the same shape as _a1_ and _a2_.

Raises:

ValueError

If _cmp_ is not valid.

TypeError

If at least one of _a1_ or _a2_ is a non-string array

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\["a", "b", "cde"\])
\>>> b \= np.array(\["a", "a", "dec"\])
\>>> np.char.compare\_chararrays(a, b, ">", True)
array(\[False,  True, False\])

Copy to clipboard

Go BackOpen In Tab

On this page