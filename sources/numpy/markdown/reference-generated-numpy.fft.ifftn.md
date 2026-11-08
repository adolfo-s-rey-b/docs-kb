[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifftn.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fft.ifftn.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifftn.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fft.ifftn.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fft.ifftn.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fft.ifftn.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fft.ifftn.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fft.ifftn.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fft.ifftn.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fft.ifftn.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fft.ifftn.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fft.ifftn.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fft.ifftn.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fft.ifftn.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fft.ifftn.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fft.ifftn.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fft.ifftn.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fft.ifftn.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fft.ifftn.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fft.ifftn.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fft.ifftn.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fft.ifftn.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fft.ifftn[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifftn.html#numpy-fft-ifftn "Link to this heading")

=================================================================================================================================

fft.ifftn(_a_, _s\=None_, _axes\=None_, _norm\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/fft/_pocketfft.py#L887-L1016)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifftn.html#numpy.fft.ifftn "Link to this definition")

Compute the N-dimensional inverse discrete Fourier Transform.

This function computes the inverse of the N-dimensional discrete Fourier Transform over any number of axes in an M-dimensional array by means of the Fast Fourier Transform (FFT). In other words, `ifftn(fftn(a)) == a` to within numerical accuracy. For a description of the definitions and conventions used, see [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
.

The input, analogously to [`ifft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html#numpy.fft.ifft "numpy.fft.ifft")
, should be ordered in the same way as is returned by [`fftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftn.html#numpy.fft.fftn "numpy.fft.fftn")
, i.e. it should have the term for zero frequency in all axes in the low-order corner, the positive frequency terms in the first half of all axes, the term for the Nyquist frequency in the middle of all axes and the negative frequency terms in the second half of all axes, in order of decreasingly negative frequency.

Parameters:

**a**array\_like

Input array, can be complex.

**s**sequence of ints, optional

Shape (length of each transformed axis) of the output (`s[0]` refers to axis 0, `s[1]` to axis 1, etc.). This corresponds to `n` for `ifft(x, n)`. Along any axis, if the given shape is smaller than that of the input, the input is cropped. If it is larger, the input is padded with zeros.

Changed in version 2.0: If it is `-1`, the whole input is used (no padding/trimming).

If _s_ is not given, the shape of the input along the axes specified by _axes_ is used. See notes for issue on [`ifft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html#numpy.fft.ifft "numpy.fft.ifft")
 zero padding.

Deprecated since version 2.0: If _s_ is not `None`, _axes_ must not be `None` either.

Deprecated since version 2.0: _s_ must contain only `int` s, not `None` values. `None` values currently mean that the default value for `n` is used in the corresponding 1-D transform, but this behaviour is deprecated.

**axes**sequence of ints, optional

Axes over which to compute the IFFT. If not given, the last `len(s)` axes are used, or all axes if _s_ is also not specified. Repeated indices in _axes_ means that the inverse transform over that axis is performed multiple times.

Deprecated since version 2.0: If _s_ is specified, the corresponding _axes_ to be transformed must be explicitly specified too.

**norm**{“backward”, “ortho”, “forward”}, optional

Normalization mode (see [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
). Default is “backward”. Indicates which direction of the forward/backward pair of transforms is scaled and with what normalization factor.

New in version 1.20.0: The “backward”, “forward” values were added.

**out**complex ndarray, optional

If provided, the result will be placed in this array. It should be of the appropriate shape and dtype for all axes (and hence is incompatible with passing in all but the trivial `s`).

New in version 2.0.0.

Returns:

**out**complex ndarray

The truncated or zero-padded input, transformed along the axes indicated by _axes_, or by a combination of _s_ or _a_, as explained in the parameters section above.

Raises:

ValueError

If _s_ and _axes_ have different length.

IndexError

If an element of _axes_ is larger than than the number of axes of _a_.

See also

[`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")

Overall view of discrete Fourier transforms, with definitions and conventions used.

[`fftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftn.html#numpy.fft.fftn "numpy.fft.fftn")

The forward _n_\-dimensional FFT, of which [`ifftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifftn.html#numpy.fft.ifftn "numpy.fft.ifftn")
 is the inverse.

[`ifft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html#numpy.fft.ifft "numpy.fft.ifft")

The one-dimensional inverse FFT.

[`ifft2`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft2.html#numpy.fft.ifft2 "numpy.fft.ifft2")

The two-dimensional inverse FFT.

[`ifftshift`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifftshift.html#numpy.fft.ifftshift "numpy.fft.ifftshift")

Undoes [`fftshift`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftshift.html#numpy.fft.fftshift "numpy.fft.fftshift")
, shifts zero-frequency terms to beginning of array.

Notes

See [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
 for definitions and conventions used.

Zero-padding, analogously with [`ifft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html#numpy.fft.ifft "numpy.fft.ifft")
, is performed by appending zeros to the input along the specified dimension. Although this is the common approach, it might lead to surprising results. If another form of zero padding is desired, it must be performed before [`ifftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifftn.html#numpy.fft.ifftn "numpy.fft.ifftn")
 is called.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.eye(4)
\>>> np.fft.ifftn(np.fft.fftn(a, axes\=(0,)), axes\=(1,))
array(\[\[1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j\], # may vary\
       \[0.+0.j,  1.+0.j,  0.+0.j,  0.+0.j\],\
       \[0.+0.j,  0.+0.j,  1.+0.j,  0.+0.j\],\
       \[0.+0.j,  0.+0.j,  0.+0.j,  1.+0.j\]\])

Copy to clipboard

Create and plot an image with band-limited frequency content:

\>>> import matplotlib.pyplot as plt
\>>> n \= np.zeros((200,200), dtype\=np.complex128)
\>>> n\[60:80, 20:40\] \= np.exp(1j\*np.random.uniform(0, 2\*np.pi, (20, 20)))
\>>> im \= np.fft.ifftn(n).real
\>>> plt.imshow(im)
<matplotlib.image.AxesImage object at 0x...>
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-fft-ifftn-1.png](https://numpy.org/doc/stable/_images/numpy-fft-ifftn-1.png)

Go BackOpen In Tab

On this page