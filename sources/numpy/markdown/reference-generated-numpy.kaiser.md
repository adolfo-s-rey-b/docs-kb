[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.kaiser.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.kaiser.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.kaiser.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.kaiser.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.kaiser.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.kaiser.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.kaiser.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.kaiser.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.kaiser.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.kaiser.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.kaiser.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.kaiser.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.kaiser.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.kaiser.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.kaiser.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.kaiser.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.kaiser.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.kaiser.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.kaiser.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.kaiser.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.kaiser.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.kaiser.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.kaiser[#](https://numpy.org/doc/stable/reference/generated/numpy.kaiser.html#numpy-kaiser "Link to this heading")

========================================================================================================================

numpy.kaiser(_M_, _beta_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L3607-L3735)
[#](https://numpy.org/doc/stable/reference/generated/numpy.kaiser.html#numpy.kaiser "Link to this definition")

Return the Kaiser window.

The Kaiser window is a taper formed by using a Bessel function.

Parameters:

**M**int

Number of points in the output window. If zero or less, an empty array is returned.

**beta**float

Shape parameter for window.

Returns:

**out**array

The window, with the maximum value normalized to one (the value one appears only if the number of samples is odd).

See also

[`bartlett`](https://numpy.org/doc/stable/reference/generated/numpy.bartlett.html#numpy.bartlett "numpy.bartlett")
, [`blackman`](https://numpy.org/doc/stable/reference/generated/numpy.blackman.html#numpy.blackman "numpy.blackman")
, [`hamming`](https://numpy.org/doc/stable/reference/generated/numpy.hamming.html#numpy.hamming "numpy.hamming")
, [`hanning`](https://numpy.org/doc/stable/reference/generated/numpy.hanning.html#numpy.hanning "numpy.hanning")

Notes

The Kaiser window is defined as

with

\\quad -\\frac{M-1}{2} \\leq n \\leq \\frac{M-1}{2},

where I\_0 is the modified zeroth-order Bessel function.

The Kaiser was named for Jim Kaiser, who discovered a simple approximation to the DPSS window based on Bessel functions. The Kaiser window is a very good approximation to the Digital Prolate Spheroidal Sequence, or Slepian window, which is the transform which maximizes the energy in the main lobe of the window relative to total energy.

The Kaiser can approximate many other windows by varying the beta parameter.

| beta | Window shape |
| --- | --- |
| 0   | Rectangular |
| 5   | Similar to a Hamming |
| 6   | Similar to a Hanning |
| 8.6 | Similar to a Blackman |

A beta value of 14 is probably a good starting point. Note that as beta gets large, the window narrows, and so the number of samples needs to be large enough to sample the increasingly narrow spike, otherwise NaNs will get returned.

Most references to the Kaiser window come from the signal processing literature, where it is used as one of many windowing functions for smoothing values. It is also known as an apodization (which means “removing the foot”, i.e. smoothing discontinuities at the beginning and end of the sampled signal) or tapering function.

References

\[1\]

J. F. Kaiser, “Digital Filters” - Ch 7 in “Systems analysis by digital computer”, Editors: F.F. Kuo and J.F. Kaiser, p 218-285. John Wiley and Sons, New York, (1966).

\[2\]

E.R. Kanasewich, “Time Sequence Analysis in Geophysics”, The University of Alberta Press, 1975, pp. 177-178.

\[3\]

Wikipedia, “Window function”, [https://en.wikipedia.org/wiki/Window\_function](https://en.wikipedia.org/wiki/Window_function)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import matplotlib.pyplot as plt
\>>> np.kaiser(12, 14)
 array(\[7.72686684e-06, 3.46009194e-03, 4.65200189e-02, # may vary\
        2.29737120e-01, 5.99885316e-01, 9.45674898e-01,\
        9.45674898e-01, 5.99885316e-01, 2.29737120e-01,\
        4.65200189e-02, 3.46009194e-03, 7.72686684e-06\])

Copy to clipboard

Plot the window and the frequency response.

import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift
window \= np.kaiser(51, 14)
plt.plot(window)
plt.title("Kaiser window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.show()

Copy to clipboard

![../../_images/numpy-kaiser-1_00_00.png](https://numpy.org/doc/stable/_images/numpy-kaiser-1_00_00.png)

plt.figure()
A \= fft(window, 2048) / 25.5
mag \= np.abs(fftshift(A))
freq \= np.linspace(\-0.5, 0.5, len(A))
response \= 20 \* np.log10(mag)
response \= np.clip(response, \-100, 100)
plt.plot(freq, response)
plt.title("Frequency response of Kaiser window")
plt.ylabel("Magnitude \[dB\]")
plt.xlabel("Normalized frequency \[cycles per sample\]")
plt.axis('tight')
plt.show()

Copy to clipboard

![../../_images/numpy-kaiser-1_01_00.png](https://numpy.org/doc/stable/_images/numpy-kaiser-1_01_00.png)

Go BackOpen In Tab

On this page