[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.dtype.metadata.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.dtype.metadata.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.dtype.metadata.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.dtype.metadata.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.dtype.metadata.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.dtype.metadata.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.dtype.metadata.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.dtype.metadata.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.dtype.metadata.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.dtype.metadata.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.dtype.metadata.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.dtype.metadata.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.dtype.metadata.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.dtype.metadata.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.dtype.metadata.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.dtype.metadata.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.dtype.metadata.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.dtype.metadata.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.dtype.metadata.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.dtype.metadata.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.dtype.metadata.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.dtype.metadata.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.dtype.metadata[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.metadata.html#numpy-dtype-metadata "Link to this heading")

================================================================================================================================================

attribute

dtype.metadata[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.metadata.html#numpy.dtype.metadata "Link to this definition")

Either `None` or a readonly dictionary of metadata (mappingproxy).

The metadata field can be set using any dictionary at data-type creation. NumPy currently has no uniform approach to propagating metadata; although some array operations preserve it, there is no guarantee that others will.

Warning

Although used in certain projects, this feature was long undocumented and is not well supported. Some aspects of metadata propagation are expected to change in the future.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> dt \= np.dtype(float, metadata\={"key": "value"})
\>>> dt.metadata\["key"\]
'value'
\>>> arr \= np.array(\[1, 2, 3\], dtype\=dt)
\>>> arr.dtype.metadata
mappingproxy({'key': 'value'})

Copy to clipboard

Adding arrays with identical datatypes currently preserves the metadata:

\>>> (arr + arr).dtype.metadata
mappingproxy({'key': 'value'})

Copy to clipboard

If the arrays have different dtype metadata, the first one wins:

\>>> dt2 \= np.dtype(float, metadata\={"key2": "value2"})
\>>> arr2 \= np.array(\[3, 2, 1\], dtype\=dt2)
\>>> print((arr + arr2).dtype.metadata)
{'key': 'value'}

Copy to clipboard

Go BackOpen In Tab

On this page