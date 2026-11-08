[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fft.hfft.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fft.hfft.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fft.hfft.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fft.hfft.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fft.hfft.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fft.hfft.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fft.hfft.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fft.hfft.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fft.hfft.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fft.hfft.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fft.hfft.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fft.hfft.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fft.hfft.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fft.hfft.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fft.hfft.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fft.hfft.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fft.hfft.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fft.hfft.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fft.hfft.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fft.hfft.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fft.hfft.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fft.hfft.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fft.hfft[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.hfft.html#numpy-fft-hfft "Link to this heading")

==============================================================================================================================

fft.hfft(_a_, _n\=None_, _axis\=\-1_, _norm\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/fft/_pocketfft.py#L529-L629)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.hfft.html#numpy.fft.hfft "Link to this definition")

Compute the FFT of a signal that has Hermitian symmetry, i.e., a real spectrum.

Parameters:

**a**array\_like

The input array.

**n**int, optional

Length of the transformed axis of the output. For _n_ output points, `n//2 + 1` input points are necessary. If the input is longer than this, it is cropped. If it is shorter than this, it is padded with zeros. If _n_ is not given, it is taken to be `2*(m-1)` where `m` is the length of the input along the axis specified by _axis_.

**axis**int, optional

Axis over which to compute the FFT. If not given, the last axis is used.

**norm**{“backward”, “ortho”, “forward”}, optional

Normalization mode (see [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
). Default is “backward”. Indicates which direction of the forward/backward pair of transforms is scaled and with what normalization factor.

New in version 1.20.0: The “backward”, “forward” values were added.

**out**ndarray, optional

If provided, the result will be placed in this array. It should be of the appropriate shape and dtype.

New in version 2.0.0.

Returns:

**out**ndarray

The truncated or zero-padded input, transformed along the axis indicated by _axis_, or the last one if _axis_ is not specified. The length of the transformed axis is _n_, or, if _n_ is not given, `2*m - 2` where `m` is the length of the transformed axis of the input. To get an odd number of output points, _n_ must be specified, for instance as `2*m - 1` in the typical case,

Raises:

IndexError

If _axis_ is not a valid axis of _a_.

See also

[`rfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft "numpy.fft.rfft")

Compute the one-dimensional FFT for real input.

[`ihfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ihfft.html#numpy.fft.ihfft "numpy.fft.ihfft")

The inverse of [`hfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.hfft.html#numpy.fft.hfft "numpy.fft.hfft")
.

Notes

[`hfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.hfft.html#numpy.fft.hfft "numpy.fft.hfft")
/[`ihfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ihfft.html#numpy.fft.ihfft "numpy.fft.ihfft")
 are a pair analogous to [`rfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft "numpy.fft.rfft")
/[`irfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft.html#numpy.fft.irfft "numpy.fft.irfft")
, but for the opposite case: here the signal has Hermitian symmetry in the time domain and is real in the frequency domain. So here it’s [`hfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.hfft.html#numpy.fft.hfft "numpy.fft.hfft")
 for which you must supply the length of the result if it is to be odd.

*   even: `ihfft(hfft(a, 2*len(a) - 2)) == a`, within roundoff error,
    
*   odd: `ihfft(hfft(a, 2*len(a) - 1)) == a`, within roundoff error.
    

The correct interpretation of the hermitian input depends on the length of the original data, as given by _n_. This is because each input shape could correspond to either an odd or even length signal. By default, [`hfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.hfft.html#numpy.fft.hfft "numpy.fft.hfft")
 assumes an even output length which puts the last entry at the Nyquist frequency; aliasing with its symmetric counterpart. By Hermitian symmetry, the value is thus treated as purely real. To avoid losing information, the shape of the full signal **must** be given.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> signal \= np.array(\[1, 2, 3, 4, 3, 2\])
\>>> np.fft.fft(signal)
array(\[15.+0.j,  -4.+0.j,   0.+0.j,  -1.-0.j,   0.+0.j,  -4.+0.j\]) # may vary
\>>> np.fft.hfft(signal\[:4\]) \# Input first half of signal
array(\[15.,  -4.,   0.,  -1.,   0.,  -4.\])
\>>> np.fft.hfft(signal, 6)  \# Input entire signal and truncate
array(\[15.,  -4.,   0.,  -1.,   0.,  -4.\])

Copy to clipboard

\>>> signal \= np.array(\[\[1, 1.j\], \[\-1.j, 2\]\])
\>>> np.conj(signal.T) \- signal   \# check Hermitian symmetry
array(\[\[ 0.-0.j,  -0.+0.j\], # may vary\
       \[ 0.+0.j,  0.-0.j\]\])
\>>> freq\_spectrum \= np.fft.hfft(signal)
\>>> freq\_spectrum
array(\[\[ 1.,  1.\],\
       \[ 2., -2.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page