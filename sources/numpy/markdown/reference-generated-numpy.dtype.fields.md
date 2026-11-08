[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.dtype.fields.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.dtype.fields.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.dtype.fields.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.dtype.fields.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.dtype.fields.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.dtype.fields.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.dtype.fields.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.dtype.fields.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.dtype.fields.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.dtype.fields.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.dtype.fields.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.dtype.fields.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.dtype.fields.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.dtype.fields.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.dtype.fields.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.dtype.fields.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.dtype.fields.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.dtype.fields.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.dtype.fields.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.dtype.fields.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.dtype.fields.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.dtype.fields.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.dtype.fields[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.fields.html#numpy-dtype-fields "Link to this heading")

==========================================================================================================================================

attribute

dtype.fields[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.fields.html#numpy.dtype.fields "Link to this definition")

Dictionary of named fields defined for this data type, or `None`.

The dictionary is indexed by keys that are the names of the fields. Each entry in the dictionary is a tuple fully describing the field:

(dtype, offset\[, title\])

Copy to clipboard

Offset is limited to C int, which is signed and usually 32 bits. If present, the optional title can be any object (if it is a string or unicode then it will also be a key in the fields dictionary, otherwise it’s meta-data). Notice also that the first two elements of the tuple can be passed directly as arguments to the `ndarray.getfield` and `ndarray.setfield` methods.

See also

[`ndarray.getfield`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.getfield.html#numpy.ndarray.getfield "numpy.ndarray.getfield")
, [`ndarray.setfield`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.setfield.html#numpy.ndarray.setfield "numpy.ndarray.setfield")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> dt \= np.dtype(\[('name', np.str\_, 16), ('grades', np.float64, (2,))\])
\>>> print(dt.fields)
{'name': (dtype('<U16'), 0), 'grades': (dtype(('<f8', (2,))), 64)}

Copy to clipboard

Go BackOpen In Tab

On this page