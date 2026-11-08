[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fft.ifft.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fft.ifft.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fft.ifft.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fft.ifft.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fft.ifft.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fft.ifft.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fft.ifft.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fft.ifft.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fft.ifft.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fft.ifft.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fft.ifft.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fft.ifft.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fft.ifft.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fft.ifft.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fft.ifft.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fft.ifft.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fft.ifft.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fft.ifft.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fft.ifft.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fft.ifft.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fft.ifft[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html#numpy-fft-ifft "Link to this heading")

==============================================================================================================================

fft.ifft(_a_, _n\=None_, _axis\=\-1_, _norm\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/fft/_pocketfft.py#L219-L321)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html#numpy.fft.ifft "Link to this definition")

Compute the one-dimensional inverse discrete Fourier Transform.

This function computes the inverse of the one-dimensional _n_\-point discrete Fourier transform computed by [`fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
. In other words, `ifft(fft(a)) == a` to within numerical accuracy. For a general description of the algorithm and definitions, see [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
.

The input should be ordered in the same way as is returned by [`fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
, i.e.,

*   `a[0]` should contain the zero frequency term,
    
*   `a[1:n//2]` should contain the positive-frequency terms,
    
*   `a[n//2 + 1:]` should contain the negative-frequency terms, in increasing order starting from the most negative frequency.
    

For an even number of input points, `A[n//2]` represents the sum of the values at the positive and negative Nyquist frequencies, as the two are aliased together. See [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
 for details.

Parameters:

**a**array\_like

Input array, can be complex.

**n**int, optional

Length of the transformed axis of the output. If _n_ is smaller than the length of the input, the input is cropped. If it is larger, the input is padded with zeros. If _n_ is not given, the length of the input along the axis specified by _axis_ is used. See notes about padding issues.

**axis**int, optional

Axis over which to compute the inverse DFT. If not given, the last axis is used.

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

An introduction, with definitions and general explanations.

[`fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")

The one-dimensional (forward) FFT, of which [`ifft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html#numpy.fft.ifft "numpy.fft.ifft")
 is the inverse

[`ifft2`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft2.html#numpy.fft.ifft2 "numpy.fft.ifft2")

The two-dimensional inverse FFT.

[`ifftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifftn.html#numpy.fft.ifftn "numpy.fft.ifftn")

The n-dimensional inverse FFT.

Notes

If the input parameter _n_ is larger than the size of the input, the input is padded by appending zeros at the end. Even though this is the common approach, it might lead to surprising results. If a different padding is desired, it must be performed before calling [`ifft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html#numpy.fft.ifft "numpy.fft.ifft")
.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.fft.ifft(\[0, 4, 0, 0\])
array(\[ 1.+0.j,  0.+1.j, -1.+0.j,  0.-1.j\]) # may vary

Copy to clipboard

Create and plot a band-limited signal with random phases:

\>>> import matplotlib.pyplot as plt
\>>> t \= np.arange(400)
\>>> n \= np.zeros((400,), dtype\=np.complex128)
\>>> n\[40:60\] \= np.exp(1j\*np.random.uniform(0, 2\*np.pi, (20,)))
\>>> s \= np.fft.ifft(n)
\>>> plt.plot(t, s.real, label\='real')
\[<matplotlib.lines.Line2D object at ...>\]
\>>> plt.plot(t, s.imag, '--', label\='imaginary')
\[<matplotlib.lines.Line2D object at ...>\]
\>>> plt.legend()
<matplotlib.legend.Legend object at ...>
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-fft-ifft-1.png](https://numpy.org/doc/stable/_images/numpy-fft-ifft-1.png)

Go BackOpen In Tab

On this page