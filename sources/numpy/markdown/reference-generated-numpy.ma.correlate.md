[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.correlate.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.correlate.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.correlate.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.correlate.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.correlate.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.correlate.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.correlate.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.correlate.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.correlate.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.correlate.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.correlate.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.correlate.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.correlate.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.correlate.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.correlate.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.correlate.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.correlate.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.correlate.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.correlate.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.correlate.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.correlate.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.correlate.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.correlate[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.correlate.html#numpy-ma-correlate "Link to this heading")

==========================================================================================================================================

ma.correlate(_a_, _v_, _mode\='valid'_, _propagate\_mask\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L8371-L8427)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.correlate.html#numpy.ma.correlate "Link to this definition")

Cross-correlation of two 1-dimensional sequences.

Parameters:

**a, v**array\_like

Input sequences.

**mode**{‘valid’, ‘same’, ‘full’}, optional

Refer to the _np.convolve_ docstring. Note that the default is ‘valid’, unlike [`convolve`](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html#numpy.convolve "numpy.convolve")
, which uses ‘full’.

**propagate\_mask**bool

If True, then a result element is masked if any masked element contributes towards it. If False, then a result element is only masked if no non-masked element contribute towards it

Returns:

**out**MaskedArray

Discrete cross-correlation of _a_ and _v_.

See also

[`numpy.correlate`](https://numpy.org/doc/stable/reference/generated/numpy.correlate.html#numpy.correlate "numpy.correlate")

Equivalent function in the top-level NumPy module.

Examples

Try it in your browser!

Basic correlation:

\>>> a \= np.ma.array(\[1, 2, 3\])
\>>> v \= np.ma.array(\[0, 1, 0\])
\>>> np.ma.correlate(a, v, mode\='valid')
masked\_array(data=\[2\],
             mask=\[False\],
       fill\_value=999999)

Copy to clipboard

Correlation with masked elements:

\>>> a \= np.ma.array(\[1, 2, 3\], mask\=\[False, True, False\])
\>>> v \= np.ma.array(\[0, 1, 0\])
\>>> np.ma.correlate(a, v, mode\='valid', propagate\_mask\=True)
masked\_array(data=\[--\],
             mask=\[ True\],
       fill\_value=999999,
            dtype=int64)

Copy to clipboard

Correlation with different modes and mixed array types:

\>>> a \= np.ma.array(\[1, 2, 3\])
\>>> v \= np.ma.array(\[0, 1, 0\])
\>>> np.ma.correlate(a, v, mode\='full')
masked\_array(data=\[0, 1, 2, 3, 0\],
             mask=\[False, False, False, False, False\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page