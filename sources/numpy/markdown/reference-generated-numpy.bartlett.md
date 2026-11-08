[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.bartlett.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.bartlett.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.bartlett.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.bartlett.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.bartlett.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.bartlett.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.bartlett.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.bartlett.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.bartlett.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.bartlett.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.bartlett.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.bartlett.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.bartlett.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.bartlett.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.bartlett.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.bartlett.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.bartlett.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.bartlett.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.bartlett.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.bartlett.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.bartlett.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.bartlett.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.bartlett[#](https://numpy.org/doc/stable/reference/generated/numpy.bartlett.html#numpy-bartlett "Link to this heading")

==============================================================================================================================

numpy.bartlett(_M_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L3148-L3252)
[#](https://numpy.org/doc/stable/reference/generated/numpy.bartlett.html#numpy.bartlett "Link to this definition")

Return the Bartlett window.

The Bartlett window is very similar to a triangular window, except that the end points are at zero. It is often used in signal processing for tapering a signal, without generating too much ripple in the frequency domain.

Parameters:

**M**int

Number of points in the output window. If zero or less, an empty array is returned.

Returns:

**out**array

The triangular window, with the maximum value normalized to one (the value one appears only if the number of samples is odd), with the first and last samples equal to zero.

See also

[`blackman`](https://numpy.org/doc/stable/reference/generated/numpy.blackman.html#numpy.blackman "numpy.blackman")
, [`hamming`](https://numpy.org/doc/stable/reference/generated/numpy.hamming.html#numpy.hamming "numpy.hamming")
, [`hanning`](https://numpy.org/doc/stable/reference/generated/numpy.hanning.html#numpy.hanning "numpy.hanning")
, [`kaiser`](https://numpy.org/doc/stable/reference/generated/numpy.kaiser.html#numpy.kaiser "numpy.kaiser")

Notes

The Bartlett window is defined as

Most references to the Bartlett window come from the signal processing literature, where it is used as one of many windowing functions for smoothing values. Note that convolution with this window produces linear interpolation. It is also known as an apodization (which means “removing the foot”, i.e. smoothing discontinuities at the beginning and end of the sampled signal) or tapering function. The Fourier transform of the Bartlett window is the product of two sinc functions. Note the excellent discussion in Kanasewich [\[2\]](https://numpy.org/doc/stable/reference/generated/numpy.bartlett.html#r3a7a5a2c0d2a-2)
.

References

\[1\]

M.S. Bartlett, “Periodogram Analysis and Continuous Spectra”, Biometrika 37, 1-16, 1950.

\[[2](https://numpy.org/doc/stable/reference/generated/numpy.bartlett.html#id1)\
\]

E.R. Kanasewich, “Time Sequence Analysis in Geophysics”, The University of Alberta Press, 1975, pp. 109-110.

\[3\]

A.V. Oppenheim and R.W. Schafer, “Discrete-Time Signal Processing”, Prentice-Hall, 1999, pp. 468-471.

\[4\]

Wikipedia, “Window function”, [https://en.wikipedia.org/wiki/Window\_function](https://en.wikipedia.org/wiki/Window_function)

\[5\]

W.H. Press, B.P. Flannery, S.A. Teukolsky, and W.T. Vetterling, “Numerical Recipes”, Cambridge University Press, 1986, page 429.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import matplotlib.pyplot as plt
\>>> np.bartlett(12)
array(\[ 0.        ,  0.18181818,  0.36363636,  0.54545455,  0.72727273, # may vary\
        0.90909091,  0.90909091,  0.72727273,  0.54545455,  0.36363636,\
        0.18181818,  0.        \])

Copy to clipboard

Plot the window and its frequency response (requires SciPy and matplotlib).

import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift
window \= np.bartlett(51)
plt.plot(window)
plt.title("Bartlett window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.show()

Copy to clipboard

![../../_images/numpy-bartlett-1_00_00.png](https://numpy.org/doc/stable/_images/numpy-bartlett-1_00_00.png)

plt.figure()
A \= fft(window, 2048) / 25.5
mag \= np.abs(fftshift(A))
freq \= np.linspace(\-0.5, 0.5, len(A))
with np.errstate(divide\='ignore', invalid\='ignore'):
    response \= 20 \* np.log10(mag)
response \= np.clip(response, \-100, 100)
plt.plot(freq, response)
plt.title("Frequency response of Bartlett window")
plt.ylabel("Magnitude \[dB\]")
plt.xlabel("Normalized frequency \[cycles per sample\]")
plt.axis('tight')
plt.show()

Copy to clipboard

![../../_images/numpy-bartlett-1_01_00.png](https://numpy.org/doc/stable/_images/numpy-bartlett-1_01_00.png)

Go BackOpen In Tab

On this page