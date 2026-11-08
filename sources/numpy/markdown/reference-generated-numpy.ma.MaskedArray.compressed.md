[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.compressed.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.compressed.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.compressed.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.compressed.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.compressed.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.compressed.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.compressed.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.compressed.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.compressed.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.compressed.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.compressed.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.compressed.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.compressed.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.compressed.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.compressed.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.compressed.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.compressed.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.compressed.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.compressed.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.compressed.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.compressed.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.compressed.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.compressed[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.compressed.html#numpy-ma-maskedarray-compressed "Link to this heading")

=================================================================================================================================================================================

method

ma.MaskedArray.compressed()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L3938-L3972)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.compressed.html#numpy.ma.MaskedArray.compressed "Link to this definition")

Return all the non-masked data as a 1-D array.

Returns:

**data**ndarray

A new [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 holding the non-masked data is returned.

Notes

The result is **not** a MaskedArray!

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(np.arange(5), mask\=\[0\]\*2 + \[1\]\*3)
\>>> x.compressed()
array(\[0, 1\])
\>>> type(x.compressed())
<class 'numpy.ndarray'>

Copy to clipboard

N-D arrays are compressed to 1-D.

\>>> arr \= \[\[1, 2\], \[3, 4\]\]
\>>> mask \= \[\[1, 0\], \[0, 1\]\]
\>>> x \= np.ma.array(arr, mask\=mask)
\>>> x.compressed()
array(\[2, 3\])

Copy to clipboard

Go BackOpen In Tab

On this page