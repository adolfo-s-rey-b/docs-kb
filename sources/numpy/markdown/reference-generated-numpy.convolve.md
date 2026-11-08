[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.convolve.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.convolve.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.convolve.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.convolve.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.convolve.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.convolve.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.convolve.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.convolve.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.convolve.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.convolve.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.convolve.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.convolve.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.convolve.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.convolve.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.convolve.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.convolve.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.convolve.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.convolve.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.convolve.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.convolve.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.convolve[#](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html#numpy-convolve "Link to this heading")

==============================================================================================================================

numpy.convolve(_a_, _v_, _mode\='full'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L800-L897)
[#](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html#numpy.convolve "Link to this definition")

Returns the discrete, linear convolution of two one-dimensional sequences.

The convolution operator is often seen in signal processing, where it models the effect of a linear time-invariant system on a signal [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html#r95849f33d2b1-1)
. In probability theory, the sum of two independent random variables is distributed according to the convolution of their individual distributions.

If _v_ is longer than _a_, the arrays are swapped before computation.

Parameters:

**a**(N,) array\_like

First one-dimensional input array.

**v**(M,) array\_like

Second one-dimensional input array.

**mode**{‘full’, ‘valid’, ‘same’}, optional

‘full’:

By default, mode is ‘full’. This returns the convolution at each point of overlap, with an output shape of (N+M-1,). At the end-points of the convolution, the signals do not overlap completely, and boundary effects may be seen.

‘same’:

Mode ‘same’ returns output of length `max(M, N)`. Boundary effects are still visible.

‘valid’:

Mode ‘valid’ returns output of length `max(M, N) - min(M, N) + 1`. The convolution product is only given for points where the signals overlap completely. Values outside the signal boundary have no effect.

Returns:

**out**ndarray

Discrete, linear convolution of _a_ and _v_.

See also

[`scipy.signal.fftconvolve`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.fftconvolve.html#scipy.signal.fftconvolve "(in SciPy v1.18.0)")

Convolve two arrays using the Fast Fourier Transform.

[`scipy.linalg.toeplitz`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.toeplitz.html#scipy.linalg.toeplitz "(in SciPy v1.18.0)")

Used to construct the convolution operator.

[`polymul`](https://numpy.org/doc/stable/reference/generated/numpy.polymul.html#numpy.polymul "numpy.polymul")

Polynomial multiplication. Same output as convolve, but also accepts poly1d objects as input.

Notes

The discrete convolution operation is defined as

\\\[(a \* v)\_n = \\sum\_{m = -\\infty}^{\\infty} a\_m v\_{n - m}\\\]

It can be shown that a convolution \\(x(t) \* y(t)\\) in time/space is equivalent to the multiplication \\(X(f) Y(f)\\) in the Fourier domain, after appropriate padding (padding is necessary to prevent circular convolution). Since multiplication is more efficient (faster) than convolution, the function [`scipy.signal.fftconvolve`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.fftconvolve.html#scipy.signal.fftconvolve "(in SciPy v1.18.0)")
 exploits the FFT to calculate the convolution of large data-sets.

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html#id1)\
\]

Wikipedia, “Convolution”, [https://en.wikipedia.org/wiki/Convolution](https://en.wikipedia.org/wiki/Convolution)

Examples

Try it in your browser!

Note how the convolution operator flips the second array before “sliding” the two across one another:

\>>> import numpy as np
\>>> np.convolve(\[1, 2, 3\], \[0, 1, 0.5\])
array(\[0. , 1. , 2.5, 4. , 1.5\])

Copy to clipboard

Only return the middle values of the convolution. Contains boundary effects, where zeros are taken into account:

\>>> np.convolve(\[1,2,3\],\[0,1,0.5\], 'same')
array(\[1. ,  2.5,  4. \])

Copy to clipboard

The two arrays are of the same length, so there is only one position where they completely overlap:

\>>> np.convolve(\[1,2,3\],\[0,1,0.5\], 'valid')
array(\[2.5\])

Copy to clipboard

Go BackOpen In Tab

On this page