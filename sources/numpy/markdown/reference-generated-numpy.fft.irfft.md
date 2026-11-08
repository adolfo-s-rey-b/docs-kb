[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fft.irfft.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fft.irfft.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fft.irfft.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fft.irfft.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fft.irfft.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fft.irfft.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fft.irfft.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fft.irfft.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fft.irfft.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fft.irfft.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fft.irfft.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fft.irfft.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fft.irfft.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fft.irfft.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fft.irfft.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fft.irfft.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fft.irfft.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fft.irfft.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fft.irfft.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fft.irfft.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fft.irfft[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft.html#numpy-fft-irfft "Link to this heading")

=================================================================================================================================

fft.irfft(_a_, _n\=None_, _axis\=\-1_, _norm\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/fft/_pocketfft.py#L421-L526)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft.html#numpy.fft.irfft "Link to this definition")

Computes the inverse of [`rfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft "numpy.fft.rfft")
.

This function computes the inverse of the one-dimensional _n_\-point discrete Fourier Transform of real input computed by [`rfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft "numpy.fft.rfft")
. In other words, `irfft(rfft(a), len(a)) == a` to within numerical accuracy. (See Notes below for why `len(a)` is necessary here.)

The input is expected to be in the form returned by [`rfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft "numpy.fft.rfft")
, i.e. the real zero-frequency term followed by the complex positive frequency terms in order of increasing frequency. Since the discrete Fourier Transform of real input is Hermitian-symmetric, the negative frequency terms are taken to be the complex conjugates of the corresponding positive frequency terms.

Parameters:

**a**array\_like

The input array.

**n**int, optional

Length of the transformed axis of the output. For _n_ output points, `n//2+1` input points are necessary. If the input is longer than this, it is cropped. If it is shorter than this, it is padded with zeros. If _n_ is not given, it is taken to be `2*(m-1)` where `m` is the length of the input along the axis specified by _axis_.

**axis**int, optional

Axis over which to compute the inverse FFT. If not given, the last axis is used.

**norm**{“backward”, “ortho”, “forward”}, optional

Normalization mode (see [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
). Default is “backward”. Indicates which direction of the forward/backward pair of transforms is scaled and with what normalization factor.

New in version 1.20.0: The “backward”, “forward” values were added.

**out**ndarray, optional

If provided, the result will be placed in this array. It should be of the appropriate shape and dtype.

New in version 2.0.0.

Returns:

**out**ndarray

The truncated or zero-padded input, transformed along the axis indicated by _axis_, or the last one if _axis_ is not specified. The length of the transformed axis is _n_, or, if _n_ is not given, `2*(m-1)` where `m` is the length of the transformed axis of the input. To get an odd number of output points, _n_ must be specified.

Raises:

IndexError

If _axis_ is not a valid axis of _a_.

See also

[`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")

For definition of the DFT and conventions used.

[`rfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft "numpy.fft.rfft")

The one-dimensional FFT of real input, of which [`irfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft.html#numpy.fft.irfft "numpy.fft.irfft")
 is inverse.

[`fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")

The one-dimensional FFT.

[`irfft2`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft2.html#numpy.fft.irfft2 "numpy.fft.irfft2")

The inverse of the two-dimensional FFT of real input.

[`irfftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfftn.html#numpy.fft.irfftn "numpy.fft.irfftn")

The inverse of the _n_\-dimensional FFT of real input.

Notes

Returns the real valued _n_\-point inverse discrete Fourier transform of _a_, where _a_ contains the non-negative frequency terms of a Hermitian-symmetric sequence. _n_ is the length of the result, not the input.

If you specify an _n_ such that _a_ must be zero-padded or truncated, the extra/removed values will be added/removed at high frequencies. One can thus resample a series to _m_ points via Fourier interpolation by: `a_resamp = irfft(rfft(a), m)`.

The correct interpretation of the hermitian input depends on the length of the original data, as given by _n_. This is because each input shape could correspond to either an odd or even length signal. By default, [`irfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft.html#numpy.fft.irfft "numpy.fft.irfft")
 assumes an even output length which puts the last entry at the Nyquist frequency; aliasing with its symmetric counterpart. By Hermitian symmetry, the value is thus treated as purely real. To avoid losing information, the correct length of the real input **must** be given.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.fft.ifft(\[1, \-1j, \-1, 1j\])
array(\[0.+0.j,  1.+0.j,  0.+0.j,  0.+0.j\]) # may vary
\>>> np.fft.irfft(\[1, \-1j, \-1\])
array(\[0.,  1.,  0.,  0.\])

Copy to clipboard

Notice how the last term in the input to the ordinary [`ifft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html#numpy.fft.ifft "numpy.fft.ifft")
 is the complex conjugate of the second term, and the output has zero imaginary part everywhere. When calling [`irfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft.html#numpy.fft.irfft "numpy.fft.irfft")
, the negative frequencies are not specified, and the output array is purely real.

Go BackOpen In Tab

On this page