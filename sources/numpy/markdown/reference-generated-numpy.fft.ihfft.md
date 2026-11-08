[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fft.ihfft.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fft.ihfft.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fft.ihfft.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fft.ihfft.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fft.ihfft.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fft.ihfft.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fft.ihfft.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fft.ihfft.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fft.ihfft.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fft.ihfft.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fft.ihfft.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fft.ihfft.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fft.ihfft.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fft.ihfft.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fft.ihfft.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fft.ihfft.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fft.ihfft.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fft.ihfft.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fft.ihfft.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fft.ihfft.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fft.ihfft.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fft.ihfft.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fft.ihfft[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.ihfft.html#numpy-fft-ihfft "Link to this heading")

=================================================================================================================================

fft.ihfft(_a_, _n\=None_, _axis\=\-1_, _norm\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/fft/_pocketfft.py#L632-L701)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.ihfft.html#numpy.fft.ihfft "Link to this definition")

Compute the inverse FFT of a signal that has Hermitian symmetry.

Parameters:

**a**array\_like

Input array.

**n**int, optional

Length of the inverse FFT, the number of points along transformation axis in the input to use. If _n_ is smaller than the length of the input, the input is cropped. If it is larger, the input is padded with zeros. If _n_ is not given, the length of the input along the axis specified by _axis_ is used.

**axis**int, optional

Axis over which to compute the inverse FFT. If not given, the last axis is used.

**norm**{“backward”, “ortho”, “forward”}, optional

Normalization mode (see [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
). Default is “backward”. Indicates which direction of the forward/backward pair of transforms is scaled and with what normalization factor.

New in version 1.20.0: The “backward”, “forward” values were added.

**out**complex ndarray, optional

If provided, the result will be placed in this array. It should be of the appropriate shape and dtype.

New in version 2.0.0.

Returns:

**out**complex ndarray

The truncated or zero-padded input, transformed along the axis indicated by _axis_, or the last one if _axis_ is not specified. The length of the transformed axis is `n//2 + 1`.

See also

[`hfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.hfft.html#numpy.fft.hfft "numpy.fft.hfft")
, [`irfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft.html#numpy.fft.irfft "numpy.fft.irfft")

Notes

[`hfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.hfft.html#numpy.fft.hfft "numpy.fft.hfft")
/[`ihfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ihfft.html#numpy.fft.ihfft "numpy.fft.ihfft")
 are a pair analogous to [`rfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft "numpy.fft.rfft")
/[`irfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft.html#numpy.fft.irfft "numpy.fft.irfft")
, but for the opposite case: here the signal has Hermitian symmetry in the time domain and is real in the frequency domain. So here it’s [`hfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.hfft.html#numpy.fft.hfft "numpy.fft.hfft")
 for which you must supply the length of the result if it is to be odd:

*   even: `ihfft(hfft(a, 2*len(a) - 2)) == a`, within roundoff error,
    
*   odd: `ihfft(hfft(a, 2*len(a) - 1)) == a`, within roundoff error.
    

Examples

Try it in your browser!

\>>> import numpy as np
\>>> spectrum \= np.array(\[ 15, \-4, 0, \-1, 0, \-4\])
\>>> np.fft.ifft(spectrum)
array(\[1.+0.j,  2.+0.j,  3.+0.j,  4.+0.j,  3.+0.j,  2.+0.j\]) # may vary
\>>> np.fft.ihfft(spectrum)
array(\[ 1.-0.j,  2.-0.j,  3.-0.j,  4.-0.j\]) # may vary

Copy to clipboard

Go BackOpen In Tab

On this page