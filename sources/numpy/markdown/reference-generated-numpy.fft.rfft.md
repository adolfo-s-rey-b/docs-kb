[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fft.rfft.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fft.rfft.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fft.rfft.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fft.rfft.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fft.rfft.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fft.rfft.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fft.rfft.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fft.rfft.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fft.rfft.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fft.rfft.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fft.rfft.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fft.rfft.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fft.rfft.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fft.rfft.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fft.rfft.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fft.rfft.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fft.rfft.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fft.rfft.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fft.rfft.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fft.rfft.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fft.rfft[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy-fft-rfft "Link to this heading")

==============================================================================================================================

fft.rfft(_a_, _n\=None_, _axis\=\-1_, _norm\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/fft/_pocketfft.py#L324-L418)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft "Link to this definition")

Compute the one-dimensional discrete Fourier Transform for real input.

This function computes the one-dimensional _n_\-point discrete Fourier Transform (DFT) of a real-valued array by means of an efficient algorithm called the Fast Fourier Transform (FFT).

Parameters:

**a**array\_like

Input array

**n**int, optional

Number of points along transformation axis in the input to use. If _n_ is smaller than the length of the input, the input is cropped. If it is larger, the input is padded with zeros. If _n_ is not given, the length of the input along the axis specified by _axis_ is used.

**axis**int, optional

Axis over which to compute the FFT. If not given, the last axis is used.

**norm**{“backward”, “ortho”, “forward”}, optional

Normalization mode (see [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
). Default is “backward”. Indicates which direction of the forward/backward pair of transforms is scaled and with what normalization factor.

New in version 1.20.0: The “backward”, “forward” values were added.

**out**complex ndarray, optional

If provided, the result will be placed in this array. It should be of the appropriate shape and dtype.

New in version 2.0.0.

Returns:

**out**complex ndarray

The truncated or zero-padded input, transformed along the axis indicated by _axis_, or the last one if _axis_ is not specified. If _n_ is even, the length of the transformed axis is `(n/2)+1`. If _n_ is odd, the length is `(n+1)/2`.

Raises:

IndexError

If _axis_ is not a valid axis of _a_.

See also

[`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")

For definition of the DFT and conventions used.

[`irfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft.html#numpy.fft.irfft "numpy.fft.irfft")

The inverse of [`rfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft "numpy.fft.rfft")
.

[`fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")

The one-dimensional FFT of general (complex) input.

[`fftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftn.html#numpy.fft.fftn "numpy.fft.fftn")

The _n_\-dimensional FFT.

[`rfftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftn.html#numpy.fft.rfftn "numpy.fft.rfftn")

The _n_\-dimensional FFT of real input.

Notes

When the DFT is computed for purely real input, the output is Hermitian-symmetric, i.e. the negative frequency terms are just the complex conjugates of the corresponding positive-frequency terms, and the negative-frequency terms are therefore redundant. This function does not compute the negative frequency terms, and the length of the transformed axis of the output is therefore `n//2 + 1`.

When `A = rfft(a)` and fs is the sampling frequency, `A[0]` contains the zero-frequency term 0\*fs, which is real due to Hermitian symmetry.

If _n_ is even, `A[-1]` contains the term representing both positive and negative Nyquist frequency (+fs/2 and -fs/2), and must also be purely real. If _n_ is odd, there is no term at fs/2; `A[-1]` contains the largest positive frequency (fs/2\*(n-1)/n), and is complex in the general case.

If the input _a_ contains an imaginary part, it is silently discarded.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.fft.fft(\[0, 1, 0, 0\])
array(\[ 1.+0.j,  0.-1.j, -1.+0.j,  0.+1.j\]) # may vary
\>>> np.fft.rfft(\[0, 1, 0, 0\])
array(\[ 1.+0.j,  0.-1.j, -1.+0.j\]) # may vary

Copy to clipboard

Notice how the final element of the [`fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
 output is the complex conjugate of the second element, for real input. For [`rfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft "numpy.fft.rfft")
, this symmetry is exploited to compute only the non-negative frequency terms.

Go BackOpen In Tab

On this page