[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftfreq.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fft.rfftfreq.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftfreq.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fft.rfftfreq.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fft.rfftfreq.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fft.rfftfreq.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fft.rfftfreq.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fft.rfftfreq.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fft.rfftfreq.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fft.rfftfreq.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fft.rfftfreq.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fft.rfftfreq.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fft.rfftfreq.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fft.rfftfreq.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fft.rfftfreq.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fft.rfftfreq.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fft.rfftfreq.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fft.rfftfreq.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fft.rfftfreq.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fft.rfftfreq.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fft.rfftfreq.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fft.rfftfreq.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fft.rfftfreq[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftfreq.html#numpy-fft-rfftfreq "Link to this heading")

==========================================================================================================================================

fft.rfftfreq(_n_, _d\=1.0_, _device\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/fft/_helper.py#L180-L235)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftfreq.html#numpy.fft.rfftfreq "Link to this definition")

Return the Discrete Fourier Transform sample frequencies (for usage with rfft, irfft).

The returned float array _f_ contains the frequency bin centers in cycles per unit of the sample spacing (with zero at the start). For instance, if the sample spacing is in seconds, then the frequency unit is cycles/second.

Given a window length _n_ and a sample spacing _d_:

f \= \[0, 1, ...,     n/2\-1,     n/2\] / (d\*n)   if n is even
f \= \[0, 1, ..., (n\-1)/2\-1, (n\-1)/2\] / (d\*n)   if n is odd

Copy to clipboard

Unlike [`fftfreq`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftfreq.html#numpy.fft.fftfreq "numpy.fft.fftfreq")
 (but like [`scipy.fftpack.rfftfreq`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.fftpack.rfftfreq.html#scipy.fftpack.rfftfreq "(in SciPy v1.18.0)")
) the Nyquist frequency component is considered to be positive.

Parameters:

**n**int

Window length.

**d**scalar, optional

Sample spacing (inverse of the sampling rate). Defaults to 1.

**device**str, optional

The device on which to place the created array. Default: `None`. For Array-API interoperability only, so must be `"cpu"` if passed.

New in version 2.0.0.

Returns:

**f**ndarray

Array of length `n//2 + 1` containing the sample frequencies.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> signal \= np.array(\[\-2, 8, 6, 4, 1, 0, 3, 5, \-3, 4\], dtype\=np.float64)
\>>> fourier \= np.fft.rfft(signal)
\>>> n \= signal.size
\>>> sample\_rate \= 100
\>>> freq \= np.fft.fftfreq(n, d\=1./sample\_rate)
\>>> freq
array(\[  0.,  10.,  20., ..., -30., -20., -10.\])
\>>> freq \= np.fft.rfftfreq(n, d\=1./sample\_rate)
\>>> freq
array(\[  0.,  10.,  20.,  30.,  40.,  50.\])

Copy to clipboard

Go BackOpen In Tab

On this page