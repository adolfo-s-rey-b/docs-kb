[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfftn.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fft.irfftn.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfftn.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fft.irfftn.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fft.irfftn.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fft.irfftn.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fft.irfftn.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fft.irfftn.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fft.irfftn.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fft.irfftn.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fft.irfftn.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fft.irfftn.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fft.irfftn.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fft.irfftn.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fft.irfftn.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fft.irfftn.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fft.irfftn.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fft.irfftn.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fft.irfftn.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fft.irfftn.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fft.irfftn.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fft.irfftn.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fft.irfftn[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfftn.html#numpy-fft-irfftn "Link to this heading")

====================================================================================================================================

fft.irfftn(_a_, _s\=None_, _axes\=None_, _norm\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/fft/_pocketfft.py#L1473-L1609)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfftn.html#numpy.fft.irfftn "Link to this definition")

Computes the inverse of [`rfftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftn.html#numpy.fft.rfftn "numpy.fft.rfftn")
.

This function computes the inverse of the N-dimensional discrete Fourier Transform for real input over any number of axes in an M-dimensional array by means of the Fast Fourier Transform (FFT). In other words, `irfftn(rfftn(a), a.shape) == a` to within numerical accuracy. (The `a.shape` is necessary like `len(a)` is for [`irfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft.html#numpy.fft.irfft "numpy.fft.irfft")
, and for the same reason.)

The input should be ordered in the same way as is returned by [`rfftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftn.html#numpy.fft.rfftn "numpy.fft.rfftn")
, i.e. as for [`irfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft.html#numpy.fft.irfft "numpy.fft.irfft")
 for the final transformation axis, and as for [`ifftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifftn.html#numpy.fft.ifftn "numpy.fft.ifftn")
 along all the other axes.

Parameters:

**a**array\_like

Input array.

**s**sequence of ints, optional

Shape (length of each transformed axis) of the output (`s[0]` refers to axis 0, `s[1]` to axis 1, etc.). _s_ is also the number of input points used along this axis, except for the last axis, where `s[-1]//2+1` points of the input are used. Along any axis, if the shape indicated by _s_ is smaller than that of the input, the input is cropped. If it is larger, the input is padded with zeros.

Changed in version 2.0: If it is `-1`, the whole input is used (no padding/trimming).

If _s_ is not given, the shape of the input along the axes specified by axes is used. Except for the last axis which is taken to be `2*(m-1)` where `m` is the length of the input along that axis.

Deprecated since version 2.0: If _s_ is not `None`, _axes_ must not be `None` either.

Deprecated since version 2.0: _s_ must contain only `int` s, not `None` values. `None` values currently mean that the default value for `n` is used in the corresponding 1-D transform, but this behaviour is deprecated.

**axes**sequence of ints, optional

Axes over which to compute the inverse FFT. If not given, the last _len(s)_ axes are used, or all axes if _s_ is also not specified. Repeated indices in _axes_ means that the inverse transform over that axis is performed multiple times.

Deprecated since version 2.0: If _s_ is specified, the corresponding _axes_ to be transformed must be explicitly specified too.

**norm**{“backward”, “ortho”, “forward”}, optional

Normalization mode (see [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
). Default is “backward”. Indicates which direction of the forward/backward pair of transforms is scaled and with what normalization factor.

New in version 1.20.0: The “backward”, “forward” values were added.

**out**ndarray, optional

If provided, the result will be placed in this array. It should be of the appropriate shape and dtype for the last transformation.

New in version 2.0.0.

Returns:

**out**ndarray

The truncated or zero-padded input, transformed along the axes indicated by _axes_, or by a combination of _s_ or _a_, as explained in the parameters section above. The length of each transformed axis is as given by the corresponding element of _s_, or the length of the input in every axis except for the last one if _s_ is not given. In the final transformed axis the length of the output when _s_ is not given is `2*(m-1)` where `m` is the length of the final transformed axis of the input. To get an odd number of output points in the final axis, _s_ must be specified.

Raises:

ValueError

If _s_ and _axes_ have different length.

IndexError

If an element of _axes_ is larger than than the number of axes of _a_.

See also

[`rfftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftn.html#numpy.fft.rfftn "numpy.fft.rfftn")

The forward n-dimensional FFT of real input, of which [`ifftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifftn.html#numpy.fft.ifftn "numpy.fft.ifftn")
 is the inverse.

[`fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")

The one-dimensional FFT, with definitions and conventions used.

[`irfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft.html#numpy.fft.irfft "numpy.fft.irfft")

The inverse of the one-dimensional FFT of real input.

[`irfft2`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft2.html#numpy.fft.irfft2 "numpy.fft.irfft2")

The inverse of the two-dimensional FFT of real input.

Notes

See [`fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
 for definitions and conventions used.

See [`rfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft "numpy.fft.rfft")
 for definitions and conventions used for real input.

The correct interpretation of the hermitian input depends on the shape of the original data, as given by _s_. This is because each input shape could correspond to either an odd or even length signal. By default, [`irfftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfftn.html#numpy.fft.irfftn "numpy.fft.irfftn")
 assumes an even output length which puts the last entry at the Nyquist frequency; aliasing with its symmetric counterpart. When performing the final complex to real transform, the last value is thus treated as purely real. To avoid losing information, the correct shape of the real input **must** be given.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.zeros((3, 2, 2))
\>>> a\[0, 0, 0\] \= 3 \* 2 \* 2
\>>> np.fft.irfftn(a)
array(\[\[\[1.,  1.\],\
        \[1.,  1.\]\],\
       \[\[1.,  1.\],\
        \[1.,  1.\]\],\
       \[\[1.,  1.\],\
        \[1.,  1.\]\]\])

Copy to clipboard

Go BackOpen In Tab

On this page