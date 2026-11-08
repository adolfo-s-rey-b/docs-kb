[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftshift.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fft.fftshift.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftshift.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fft.fftshift.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fft.fftshift.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fft.fftshift.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fft.fftshift.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fft.fftshift.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fft.fftshift.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fft.fftshift.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fft.fftshift.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fft.fftshift.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fft.fftshift.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fft.fftshift.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fft.fftshift.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fft.fftshift.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fft.fftshift.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fft.fftshift.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fft.fftshift.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fft.fftshift.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fft.fftshift.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fft.fftshift.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fft.fftshift[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftshift.html#numpy-fft-fftshift "Link to this heading")

==========================================================================================================================================

fft.fftshift(_x_, _axes\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/fft/_helper.py#L19-L74)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftshift.html#numpy.fft.fftshift "Link to this definition")

Shift the zero-frequency component to the center of the spectrum.

This function swaps half-spaces for all axes listed (defaults to all). Note that `y[0]` is the Nyquist component only if `len(x)` is even.

Parameters:

**x**array\_like

Input array.

**axes**int or shape tuple, optional

Axes over which to shift. Default is None, which shifts all axes.

Returns:

**y**ndarray

The shifted array.

See also

[`ifftshift`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifftshift.html#numpy.fft.ifftshift "numpy.fft.ifftshift")

The inverse of [`fftshift`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftshift.html#numpy.fft.fftshift "numpy.fft.fftshift")
.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> freqs \= np.fft.fftfreq(10, 0.1)
\>>> freqs
array(\[ 0.,  1.,  2., ..., -3., -2., -1.\])
\>>> np.fft.fftshift(freqs)
array(\[-5., -4., -3., -2., -1.,  0.,  1.,  2.,  3.,  4.\])

Copy to clipboard

Shift the zero-frequency component only along the second axis:

\>>> freqs \= np.fft.fftfreq(9, d\=1./9).reshape(3, 3)
\>>> freqs
array(\[\[ 0.,  1.,  2.\],\
       \[ 3.,  4., -4.\],\
       \[-3., -2., -1.\]\])
\>>> np.fft.fftshift(freqs, axes\=(1,))
array(\[\[ 2.,  0.,  1.\],\
       \[-4.,  3.,  4.\],\
       \[-1., -3., -2.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page