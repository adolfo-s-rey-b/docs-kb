[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.correlate.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.correlate.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.correlate.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.correlate.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.correlate.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.correlate.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.correlate.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.correlate.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.correlate.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.correlate.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.correlate.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.correlate.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.correlate.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.correlate.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.correlate.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.correlate.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.correlate.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.correlate.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.correlate.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.correlate.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.correlate.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.correlate.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.correlate[#](https://numpy.org/doc/stable/reference/generated/numpy.correlate.html#numpy-correlate "Link to this heading")

=================================================================================================================================

numpy.correlate(_a_, _v_, _mode\='valid'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L720-L793)
[#](https://numpy.org/doc/stable/reference/generated/numpy.correlate.html#numpy.correlate "Link to this definition")

Cross-correlation of two 1-dimensional sequences.

This function computes the correlation as generally defined in signal processing texts [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.correlate.html#rd663958e4897-1)
:

\\\[c\_k = \\sum\_n a\_{n+k} \\cdot \\overline{v}\_n\\\]

with a and v sequences being zero-padded where necessary and \\(\\overline v\\) denoting complex conjugation.

Parameters:

**a, v**array\_like

Input sequences.

**mode**{‘valid’, ‘same’, ‘full’}, optional

Refer to the [`convolve`](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html#numpy.convolve "numpy.convolve")
 docstring. Note that the default is ‘valid’, unlike [`convolve`](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html#numpy.convolve "numpy.convolve")
, which uses ‘full’.

Returns:

**out**ndarray

Discrete cross-correlation of _a_ and _v_.

See also

[`convolve`](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html#numpy.convolve "numpy.convolve")

Discrete, linear convolution of two one-dimensional sequences.

[`scipy.signal.correlate`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.correlate.html#scipy.signal.correlate "(in SciPy v1.18.0)")

uses FFT which has superior performance on large arrays.

Notes

The definition of correlation above is not unique and sometimes correlation may be defined differently. Another common definition is [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.correlate.html#rd663958e4897-1)
:

\\\[c'\_k = \\sum\_n a\_{n} \\cdot \\overline{v\_{n+k}}\\\]

which is related to \\(c\_k\\) by \\(c'\_k = c\_{-k}\\).

[`numpy.correlate`](https://numpy.org/doc/stable/reference/generated/numpy.correlate.html#numpy.correlate "numpy.correlate")
 may perform slowly in large arrays (i.e. n = 1e5) because it does not use the FFT to compute the convolution; in that case, [`scipy.signal.correlate`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.correlate.html#scipy.signal.correlate "(in SciPy v1.18.0)")
 might be preferable.

References

\[1\] ([1](https://numpy.org/doc/stable/reference/generated/numpy.correlate.html#id1)
,[2](https://numpy.org/doc/stable/reference/generated/numpy.correlate.html#id2)
)

Wikipedia, “Cross-correlation”, [https://en.wikipedia.org/wiki/Cross-correlation](https://en.wikipedia.org/wiki/Cross-correlation)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.correlate(\[1, 2, 3\], \[0, 1, 0.5\])
array(\[3.5\])
\>>> np.correlate(\[1, 2, 3\], \[0, 1, 0.5\], "same")
array(\[2. ,  3.5,  3. \])
\>>> np.correlate(\[1, 2, 3\], \[0, 1, 0.5\], "full")
array(\[0.5,  2. ,  3.5,  3. ,  0. \])

Copy to clipboard

Using complex sequences:

\>>> np.correlate(\[1+1j, 2, 3\-1j\], \[0, 1, 0.5j\], 'full')
array(\[ 0.5-0.5j,  1.0+0.j ,  1.5-1.5j,  3.0-1.j ,  0.0+0.j \])

Copy to clipboard

Note that you get the time reversed, complex conjugated result (\\(\\overline{c\_{-k}}\\)) when the two input sequences a and v change places:

\>>> np.correlate(\[0, 1, 0.5j\], \[1+1j, 2, 3\-1j\], 'full')
array(\[ 0.0+0.j ,  3.0+1.j ,  1.5+1.5j,  1.0+0.j ,  0.5+0.5j\])

Copy to clipboard

Go BackOpen In Tab

On this page