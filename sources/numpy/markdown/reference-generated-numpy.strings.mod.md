[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.strings.mod.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.strings.mod.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.strings.mod.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.strings.mod.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.strings.mod.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.strings.mod.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.strings.mod.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.strings.mod.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.strings.mod.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.strings.mod.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.strings.mod.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.strings.mod.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.strings.mod.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.strings.mod.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.strings.mod.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.strings.mod.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.strings.mod.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.strings.mod.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.strings.mod.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.strings.mod.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.strings.mod.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.strings.mod.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.strings.mod[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.mod.html#numpy-strings-mod "Link to this heading")

=======================================================================================================================================

strings.mod(_a_, _values_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L217-L252)
[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.mod.html#numpy.strings.mod "Link to this definition")

Return (a % i), that is pre-Python 2.6 string formatting (interpolation), element-wise for a pair of array\_likes of str or unicode.

Parameters:

**a**array\_like, with `bytes_` or `str_` dtype

**values**array\_like of values

These values will be element-wise interpolated into the string.

Returns:

**out**ndarray

Output array of `StringDType`, `bytes_` or `str_` dtype, depending on input types

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\["NumPy is a %s library"\])
\>>> np.strings.mod(a, values\=\["Python"\])
array(\['NumPy is a Python library'\], dtype='<U25')

Copy to clipboard

\>>> a \= np.array(\[b'%d bytes', b'%d bits'\])
\>>> values \= np.array(\[8, 64\])
\>>> np.strings.mod(a, values)
array(\[b'8 bytes', b'64 bits'\], dtype='|S7')

Copy to clipboard

Go BackOpen In Tab

On this page