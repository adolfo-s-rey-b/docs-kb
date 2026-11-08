[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftfreq.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fft.fftfreq.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftfreq.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fft.fftfreq.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fft.fftfreq.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fft.fftfreq.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fft.fftfreq.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fft.fftfreq.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fft.fftfreq.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fft.fftfreq.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fft.fftfreq.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fft.fftfreq.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fft.fftfreq.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fft.fftfreq.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fft.fftfreq.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fft.fftfreq.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fft.fftfreq.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fft.fftfreq.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fft.fftfreq.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fft.fftfreq.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fft.fftfreq.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fft.fftfreq.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fft.fftfreq[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftfreq.html#numpy-fft-fftfreq "Link to this heading")

=======================================================================================================================================

fft.fftfreq(_n_, _d\=1.0_, _device\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/fft/_helper.py#L125-L177)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftfreq.html#numpy.fft.fftfreq "Link to this definition")

Return the Discrete Fourier Transform sample frequencies.

The returned float array _f_ contains the frequency bin centers in cycles per unit of the sample spacing (with zero at the start). For instance, if the sample spacing is in seconds, then the frequency unit is cycles/second.

Given a window length _n_ and a sample spacing _d_:

f \= \[0, 1, ...,   n/2\-1,     \-n/2, ..., \-1\] / (d\*n)   if n is even
f \= \[0, 1, ..., (n\-1)/2, \-(n\-1)/2, ..., \-1\] / (d\*n)   if n is odd

Copy to clipboard

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

Array of length _n_ containing the sample frequencies.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> signal \= np.array(\[\-2, 8, 6, 4, 1, 0, 3, 5\], dtype\=np.float64)
\>>> fourier \= np.fft.fft(signal)
\>>> n \= signal.size
\>>> timestep \= 0.1
\>>> freq \= np.fft.fftfreq(n, d\=timestep)
\>>> freq
array(\[ 0.  ,  1.25,  2.5 , ..., -3.75, -2.5 , -1.25\])

Copy to clipboard

Go BackOpen In Tab

On this page