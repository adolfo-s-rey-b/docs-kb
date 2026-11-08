[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftn.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fft.fftn.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftn.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fft.fftn.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fft.fftn.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fft.fftn.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fft.fftn.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fft.fftn.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fft.fftn.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fft.fftn.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fft.fftn.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fft.fftn.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fft.fftn.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fft.fftn.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fft.fftn.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fft.fftn.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fft.fftn.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fft.fftn.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fft.fftn.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fft.fftn.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fft.fftn.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fft.fftn.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fft.fftn[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftn.html#numpy-fft-fftn "Link to this heading")

==============================================================================================================================

fft.fftn(_a_, _s\=None_, _axes\=None_, _norm\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/fft/_pocketfft.py#L755-L884)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftn.html#numpy.fft.fftn "Link to this definition")

Compute the N-dimensional discrete Fourier Transform.

This function computes the _N_\-dimensional discrete Fourier Transform over any number of axes in an _M_\-dimensional array by means of the Fast Fourier Transform (FFT).

Parameters:

**a**array\_like

Input array, can be complex.

**s**sequence of ints, optional

Shape (length of each transformed axis) of the output (`s[0]` refers to axis 0, `s[1]` to axis 1, etc.). This corresponds to `n` for `fft(x, n)`. Along any axis, if the given shape is smaller than that of the input, the input is cropped. If it is larger, the input is padded with zeros.

Changed in version 2.0: If it is `-1`, the whole input is used (no padding/trimming).

If _s_ is not given, the shape of the input along the axes specified by _axes_ is used.

Deprecated since version 2.0: If _s_ is not `None`, _axes_ must not be `None` either.

Deprecated since version 2.0: _s_ must contain only `int` s, not `None` values. `None` values currently mean that the default value for `n` is used in the corresponding 1-D transform, but this behaviour is deprecated.

**axes**sequence of ints, optional

Axes over which to compute the FFT. If not given, the last `len(s)` axes are used, or all axes if _s_ is also not specified. Repeated indices in _axes_ means that the transform over that axis is performed multiple times.

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

The truncated or zero-padded input, transformed along the axes indicated by _axes_, or by a combination of _s_ and _a_, as explained in the parameters section above.

Raises:

ValueError

If _s_ and _axes_ have different length.

IndexError

If an element of _axes_ is larger than than the number of axes of _a_.

See also

[`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")

Overall view of discrete Fourier transforms, with definitions and conventions used.

[`ifftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifftn.html#numpy.fft.ifftn "numpy.fft.ifftn")

The inverse of [`fftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftn.html#numpy.fft.fftn "numpy.fft.fftn")
, the inverse _n_\-dimensional FFT.

[`fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")

The one-dimensional FFT, with definitions and conventions used.

[`rfftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftn.html#numpy.fft.rfftn "numpy.fft.rfftn")

The _n_\-dimensional FFT of real input.

[`fft2`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft2.html#numpy.fft.fft2 "numpy.fft.fft2")

The two-dimensional FFT.

[`fftshift`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftshift.html#numpy.fft.fftshift "numpy.fft.fftshift")

Shifts zero-frequency terms to centre of array

Notes

The output, analogously to [`fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
, contains the term for zero frequency in the low-order corner of all axes, the positive frequency terms in the first half of all axes, the term for the Nyquist frequency in the middle of all axes and the negative frequency terms in the second half of all axes, in order of decreasingly negative frequency.

See [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
 for details, definitions and conventions used.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.mgrid\[:3, :3, :3\]\[0\]
\>>> np.fft.fftn(a, axes\=(1, 2))
array(\[\[\[ 0.+0.j,   0.+0.j,   0.+0.j\], # may vary\
        \[ 0.+0.j,   0.+0.j,   0.+0.j\],\
        \[ 0.+0.j,   0.+0.j,   0.+0.j\]\],\
       \[\[ 9.+0.j,   0.+0.j,   0.+0.j\],\
        \[ 0.+0.j,   0.+0.j,   0.+0.j\],\
        \[ 0.+0.j,   0.+0.j,   0.+0.j\]\],\
       \[\[18.+0.j,   0.+0.j,   0.+0.j\],\
        \[ 0.+0.j,   0.+0.j,   0.+0.j\],\
        \[ 0.+0.j,   0.+0.j,   0.+0.j\]\]\])
\>>> np.fft.fftn(a, (2, 2), axes\=(0, 1))
array(\[\[\[ 2.+0.j,  2.+0.j,  2.+0.j\], # may vary\
        \[ 0.+0.j,  0.+0.j,  0.+0.j\]\],\
       \[\[-2.+0.j, -2.+0.j, -2.+0.j\],\
        \[ 0.+0.j,  0.+0.j,  0.+0.j\]\]\])

Copy to clipboard

\>>> import matplotlib.pyplot as plt
\>>> \[X, Y\] \= np.meshgrid(2 \* np.pi \* np.arange(200) / 12,
...                      2 \* np.pi \* np.arange(200) / 34)
\>>> S \= np.sin(X) + np.cos(Y) + np.random.uniform(0, 1, X.shape)
\>>> FS \= np.fft.fftn(S)
\>>> plt.imshow(np.log(np.abs(np.fft.fftshift(FS))\*\*2))
<matplotlib.image.AxesImage object at 0x...>
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-fft-fftn-1.png](https://numpy.org/doc/stable/_images/numpy-fft-fftn-1.png)

Go BackOpen In Tab

On this page