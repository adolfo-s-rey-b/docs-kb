[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fft.fft.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fft.fft.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fft.fft.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fft.fft.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fft.fft.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fft.fft.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fft.fft.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fft.fft.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fft.fft.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fft.fft.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fft.fft.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fft.fft.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fft.fft.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fft.fft.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fft.fft.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fft.fft.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fft.fft.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fft.fft.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fft.fft.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fft.fft.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fft.fft[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html#numpy-fft-fft "Link to this heading")

===========================================================================================================================

fft.fft(_a_, _n\=None_, _axis\=\-1_, _norm\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/fft/_pocketfft.py#L120-L216)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html#numpy.fft.fft "Link to this definition")

Compute the one-dimensional discrete Fourier Transform.

This function computes the one-dimensional _n_\-point discrete Fourier Transform (DFT) with the efficient Fast Fourier Transform (FFT) algorithm [\[CT\]](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html#r8913bc1f0021-ct)
.

Parameters:

**a**array\_like

Input array, can be complex.

**n**int, optional

Length of the transformed axis of the output. If _n_ is smaller than the length of the input, the input is cropped. If it is larger, the input is padded with zeros. If _n_ is not given, the length of the input along the axis specified by _axis_ is used.

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

The truncated or zero-padded input, transformed along the axis indicated by _axis_, or the last one if _axis_ is not specified.

Raises:

IndexError

If _axis_ is not a valid axis of _a_.

See also

[`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")

for definition of the DFT and conventions used.

[`ifft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html#numpy.fft.ifft "numpy.fft.ifft")

The inverse of [`fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
.

[`fft2`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft2.html#numpy.fft.fft2 "numpy.fft.fft2")

The two-dimensional FFT.

[`fftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftn.html#numpy.fft.fftn "numpy.fft.fftn")

The _n_\-dimensional FFT.

[`rfftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftn.html#numpy.fft.rfftn "numpy.fft.rfftn")

The _n_\-dimensional FFT of real input.

[`fftfreq`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftfreq.html#numpy.fft.fftfreq "numpy.fft.fftfreq")

Frequency bins for given FFT parameters.

Notes

FFT (Fast Fourier Transform) refers to a way the discrete Fourier Transform (DFT) can be calculated efficiently, by using symmetries in the calculated terms. The symmetry is highest when _n_ is a power of 2, and the transform is therefore most efficient for these sizes.

The DFT is defined, with the conventions used in this implementation, in the documentation for the [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
 module.

References

\[[CT](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html#id1)\
\]

Cooley, James W., and John W. Tukey, 1965, “An algorithm for the machine calculation of complex Fourier series,” _Math. Comput._ 19: 297-301.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.fft.fft(np.exp(2j \* np.pi \* np.arange(8) / 8))
array(\[-2.33486982e-16+1.14423775e-17j,  8.00000000e+00-1.25557246e-15j,\
        2.33486982e-16+2.33486982e-16j,  0.00000000e+00+1.22464680e-16j,\
       -1.14423775e-17+2.33486982e-16j,  0.00000000e+00+5.20784380e-16j,\
        1.14423775e-17+1.14423775e-17j,  0.00000000e+00+1.22464680e-16j\])

Copy to clipboard

In this example, real input has an FFT which is Hermitian, i.e., symmetric in the real part and anti-symmetric in the imaginary part, as described in the [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
 documentation:

\>>> import matplotlib.pyplot as plt
\>>> t \= np.arange(256)
\>>> sp \= np.fft.fft(np.sin(t))
\>>> freq \= np.fft.fftfreq(t.shape\[\-1\])
\>>> \_ \= plt.plot(freq, sp.real, freq, sp.imag)
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-fft-fft-1.png](https://numpy.org/doc/stable/_images/numpy-fft-fft-1.png)

Go BackOpen In Tab

On this page