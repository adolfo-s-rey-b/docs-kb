[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.hanning.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.hanning.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.hanning.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.hanning.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.hanning.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.hanning.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.hanning.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.hanning.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.hanning.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.hanning.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.hanning.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.hanning.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.hanning.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.hanning.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.hanning.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.hanning.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.hanning.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.hanning.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.hanning.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.hanning.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.hanning.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.hanning.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.hanning[#](https://numpy.org/doc/stable/reference/generated/numpy.hanning.html#numpy-hanning "Link to this heading")

===========================================================================================================================

numpy.hanning(_M_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L3255-L3354)
[#](https://numpy.org/doc/stable/reference/generated/numpy.hanning.html#numpy.hanning "Link to this definition")

Return the Hanning window.

The Hanning window is a taper formed by using a weighted cosine.

Parameters:

**M**int

Number of points in the output window. If zero or less, an empty array is returned.

Returns:

**out**ndarray, shape(M,)

The window, with the maximum value normalized to one (the value one appears only if _M_ is odd).

See also

[`bartlett`](https://numpy.org/doc/stable/reference/generated/numpy.bartlett.html#numpy.bartlett "numpy.bartlett")
, [`blackman`](https://numpy.org/doc/stable/reference/generated/numpy.blackman.html#numpy.blackman "numpy.blackman")
, [`hamming`](https://numpy.org/doc/stable/reference/generated/numpy.hamming.html#numpy.hamming "numpy.hamming")
, [`kaiser`](https://numpy.org/doc/stable/reference/generated/numpy.kaiser.html#numpy.kaiser "numpy.kaiser")

Notes

The Hanning window is defined as

The Hanning was named for Julius von Hann, an Austrian meteorologist. It is also known as the Cosine Bell. Some authors prefer that it be called a Hann window, to help avoid confusion with the very similar Hamming window.

Most references to the Hanning window come from the signal processing literature, where it is used as one of many windowing functions for smoothing values. It is also known as an apodization (which means “removing the foot”, i.e. smoothing discontinuities at the beginning and end of the sampled signal) or tapering function.

References

\[1\]

Blackman, R.B. and Tukey, J.W., (1958) The measurement of power spectra, Dover Publications, New York.

\[2\]

E.R. Kanasewich, “Time Sequence Analysis in Geophysics”, The University of Alberta Press, 1975, pp. 106-108.

\[3\]

Wikipedia, “Window function”, [https://en.wikipedia.org/wiki/Window\_function](https://en.wikipedia.org/wiki/Window_function)

\[4\]

W.H. Press, B.P. Flannery, S.A. Teukolsky, and W.T. Vetterling, “Numerical Recipes”, Cambridge University Press, 1986, page 425.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.hanning(12)
array(\[0.        , 0.07937323, 0.29229249, 0.57115742, 0.82743037,\
       0.97974649, 0.97974649, 0.82743037, 0.57115742, 0.29229249,\
       0.07937323, 0.        \])

Copy to clipboard

Plot the window and its frequency response.

import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift
window \= np.hanning(51)
plt.plot(window)
plt.title("Hann window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.show()

Copy to clipboard

![../../_images/numpy-hanning-1_00_00.png](https://numpy.org/doc/stable/_images/numpy-hanning-1_00_00.png)

plt.figure()
A \= fft(window, 2048) / 25.5
mag \= np.abs(fftshift(A))
freq \= np.linspace(\-0.5, 0.5, len(A))
with np.errstate(divide\='ignore', invalid\='ignore'):
    response \= 20 \* np.log10(mag)
response \= np.clip(response, \-100, 100)
plt.plot(freq, response)
plt.title("Frequency response of the Hann window")
plt.ylabel("Magnitude \[dB\]")
plt.xlabel("Normalized frequency \[cycles per sample\]")
plt.axis('tight')
plt.show()

Copy to clipboard

![../../_images/numpy-hanning-1_01_00.png](https://numpy.org/doc/stable/_images/numpy-hanning-1_01_00.png)

Go BackOpen In Tab

On this page