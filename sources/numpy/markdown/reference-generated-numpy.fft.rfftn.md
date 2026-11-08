[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftn.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fft.rfftn.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftn.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fft.rfftn.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fft.rfftn.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fft.rfftn.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fft.rfftn.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fft.rfftn.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fft.rfftn.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fft.rfftn.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fft.rfftn.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fft.rfftn.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fft.rfftn.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fft.rfftn.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fft.rfftn.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fft.rfftn.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fft.rfftn.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fft.rfftn.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fft.rfftn.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fft.rfftn.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fft.rfftn.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fft.rfftn.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fft.rfftn[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftn.html#numpy-fft-rfftn "Link to this heading")

=================================================================================================================================

fft.rfftn(_a_, _s\=None_, _axes\=None_, _norm\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/fft/_pocketfft.py#L1266-L1390)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftn.html#numpy.fft.rfftn "Link to this definition")

Compute the N-dimensional discrete Fourier Transform for real input.

This function computes the N-dimensional discrete Fourier Transform over any number of axes in an M-dimensional real array by means of the Fast Fourier Transform (FFT). By default, all axes are transformed, with the real transform performed over the last axis, while the remaining transforms are complex.

Parameters:

**a**array\_like

Input array, taken to be real.

**s**sequence of ints, optional

Shape (length along each transformed axis) to use from the input. (`s[0]` refers to axis 0, `s[1]` to axis 1, etc.). The final element of _s_ corresponds to _n_ for `rfft(x, n)`, while for the remaining axes, it corresponds to _n_ for `fft(x, n)`. Along any axis, if the given shape is smaller than that of the input, the input is cropped. If it is larger, the input is padded with zeros.

Changed in version 2.0: If it is `-1`, the whole input is used (no padding/trimming).

If _s_ is not given, the shape of the input along the axes specified by _axes_ is used.

Deprecated since version 2.0: If _s_ is not `None`, _axes_ must not be `None` either.

Deprecated since version 2.0: _s_ must contain only `int` s, not `None` values. `None` values currently mean that the default value for `n` is used in the corresponding 1-D transform, but this behaviour is deprecated.

**axes**sequence of ints, optional

Axes over which to compute the FFT. If not given, the last `len(s)` axes are used, or all axes if _s_ is also not specified.

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

The truncated or zero-padded input, transformed along the axes indicated by _axes_, or by a combination of _s_ and _a_, as explained in the parameters section above. The length of the last axis transformed will be `s[-1]//2+1`, while the remaining transformed axes will have lengths according to _s_, or unchanged from the input.

Raises:

ValueError

If _s_ and _axes_ have different length.

IndexError

If an element of _axes_ is larger than than the number of axes of _a_.

See also

[`irfftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfftn.html#numpy.fft.irfftn "numpy.fft.irfftn")

The inverse of [`rfftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftn.html#numpy.fft.rfftn "numpy.fft.rfftn")
, i.e. the inverse of the n-dimensional FFT of real input.

[`fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")

The one-dimensional FFT, with definitions and conventions used.

[`rfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft "numpy.fft.rfft")

The one-dimensional FFT of real input.

[`fftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftn.html#numpy.fft.fftn "numpy.fft.fftn")

The n-dimensional FFT.

[`rfft2`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft2.html#numpy.fft.rfft2 "numpy.fft.rfft2")

The two-dimensional FFT of real input.

Notes

The transform for real input is performed over the last transformation axis, as by [`rfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft "numpy.fft.rfft")
, then the transform over the remaining axes is performed as by [`fftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftn.html#numpy.fft.fftn "numpy.fft.fftn")
. The order of the output is as for [`rfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft "numpy.fft.rfft")
 for the final transformation axis, and as for [`fftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftn.html#numpy.fft.fftn "numpy.fft.fftn")
 for the remaining transformation axes.

See [`fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
 for details, definitions and conventions used.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.ones((2, 2, 2))
\>>> np.fft.rfftn(a)
array(\[\[\[8.+0.j,  0.+0.j\], # may vary\
        \[0.+0.j,  0.+0.j\]\],\
       \[\[0.+0.j,  0.+0.j\],\
        \[0.+0.j,  0.+0.j\]\]\])

Copy to clipboard

\>>> np.fft.rfftn(a, axes\=(2, 0))
array(\[\[\[4.+0.j,  0.+0.j\], # may vary\
        \[4.+0.j,  0.+0.j\]\],\
       \[\[0.+0.j,  0.+0.j\],\
        \[0.+0.j,  0.+0.j\]\]\])

Copy to clipboard

Go BackOpen In Tab

On this page