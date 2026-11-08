[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.blackman.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.blackman.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.blackman.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.blackman.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.blackman.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.blackman.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.blackman.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.blackman.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.blackman.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.blackman.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.blackman.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.blackman.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.blackman.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.blackman.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.blackman.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.blackman.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.blackman.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.blackman.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.blackman.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.blackman.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.blackman.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.blackman.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.blackman[#](https://numpy.org/doc/stable/reference/generated/numpy.blackman.html#numpy-blackman "Link to this heading")

==============================================================================================================================

numpy.blackman(_M_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L3049-L3145)
[#](https://numpy.org/doc/stable/reference/generated/numpy.blackman.html#numpy.blackman "Link to this definition")

Return the Blackman window.

The Blackman window is a taper formed by using the first three terms of a summation of cosines. It was designed to have close to the minimal leakage possible. It is close to optimal, only slightly worse than a Kaiser window.

Parameters:

**M**int

Number of points in the output window. If zero or less, an empty array is returned.

Returns:

**out**ndarray

The window, with the maximum value normalized to one (the value one appears only if the number of samples is odd).

See also

[`bartlett`](https://numpy.org/doc/stable/reference/generated/numpy.bartlett.html#numpy.bartlett "numpy.bartlett")
, [`hamming`](https://numpy.org/doc/stable/reference/generated/numpy.hamming.html#numpy.hamming "numpy.hamming")
, [`hanning`](https://numpy.org/doc/stable/reference/generated/numpy.hanning.html#numpy.hanning "numpy.hanning")
, [`kaiser`](https://numpy.org/doc/stable/reference/generated/numpy.kaiser.html#numpy.kaiser "numpy.kaiser")

Notes

The Blackman window is defined as

Most references to the Blackman window come from the signal processing literature, where it is used as one of many windowing functions for smoothing values. It is also known as an apodization (which means “removing the foot”, i.e. smoothing discontinuities at the beginning and end of the sampled signal) or tapering function. It is known as a “near optimal” tapering function, almost as good (by some measures) as the Kaiser window.

References

\[1\]

Blackman, R.B. and Tukey, J.W., (1958) The measurement of power spectra, Dover Publications, New York.

\[2\]

Oppenheim, A.V., and R.W. Schafer. Discrete-Time Signal Processing. Upper Saddle River, NJ: Prentice-Hall, 1999, pp. 468-471.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import matplotlib.pyplot as plt
\>>> np.blackman(12)
array(\[-1.38777878e-17,   3.26064346e-02,   1.59903635e-01, # may vary\
        4.14397981e-01,   7.36045180e-01,   9.67046769e-01,\
        9.67046769e-01,   7.36045180e-01,   4.14397981e-01,\
        1.59903635e-01,   3.26064346e-02,  -1.38777878e-17\])

Copy to clipboard

Plot the window and the frequency response.

import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift
window \= np.blackman(51)
plt.plot(window)
plt.title("Blackman window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.show()  \# doctest: +SKIP

Copy to clipboard

![../../_images/numpy-blackman-1_00_00.png](https://numpy.org/doc/stable/_images/numpy-blackman-1_00_00.png)

plt.figure()
A \= fft(window, 2048) / 25.5
mag \= np.abs(fftshift(A))
freq \= np.linspace(\-0.5, 0.5, len(A))
with np.errstate(divide\='ignore', invalid\='ignore'):
    response \= 20 \* np.log10(mag)
response \= np.clip(response, \-100, 100)
plt.plot(freq, response)
plt.title("Frequency response of Blackman window")
plt.ylabel("Magnitude \[dB\]")
plt.xlabel("Normalized frequency \[cycles per sample\]")
plt.axis('tight')
plt.show()

Copy to clipboard

![../../_images/numpy-blackman-1_01_00.png](https://numpy.org/doc/stable/_images/numpy-blackman-1_01_00.png)

Go BackOpen In Tab

On this page