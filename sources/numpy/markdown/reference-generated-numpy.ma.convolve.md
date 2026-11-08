[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.convolve.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.convolve.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.convolve.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.convolve.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.convolve.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.convolve.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.convolve.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.convolve.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.convolve.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.convolve.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.convolve.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.convolve.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.convolve.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.convolve.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.convolve.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.convolve.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.convolve.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.convolve.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.convolve.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.convolve.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.convolve.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.convolve.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.convolve[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.convolve.html#numpy-ma-convolve "Link to this heading")

=======================================================================================================================================

ma.convolve(_a_, _v_, _mode\='full'_, _propagate\_mask\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L8430-L8455)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.convolve.html#numpy.ma.convolve "Link to this definition")

Returns the discrete, linear convolution of two one-dimensional sequences.

Parameters:

**a, v**array\_like

Input sequences.

**mode**{‘valid’, ‘same’, ‘full’}, optional

Refer to the _np.convolve_ docstring.

**propagate\_mask**bool

If True, then if any masked element is included in the sum for a result element, then the result is masked. If False, then the result element is only masked if no non-masked cells contribute towards it

Returns:

**out**MaskedArray

Discrete, linear convolution of _a_ and _v_.

See also

[`numpy.convolve`](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html#numpy.convolve "numpy.convolve")

Equivalent function in the top-level NumPy module.

On this page