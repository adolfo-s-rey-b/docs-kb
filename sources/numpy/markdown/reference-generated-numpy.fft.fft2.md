[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft2.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fft.fft2.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft2.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fft.fft2.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fft.fft2.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fft.fft2.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fft.fft2.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fft.fft2.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fft.fft2.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fft.fft2.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fft.fft2.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fft.fft2.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fft.fft2.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fft.fft2.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fft.fft2.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fft.fft2.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fft.fft2.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fft.fft2.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fft.fft2.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fft.fft2.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fft.fft2.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fft.fft2.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fft.fft2[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft2.html#numpy-fft-fft2 "Link to this heading")

==============================================================================================================================

fft.fft2(_a_, _s\=None_, _axes\=(-2, \-1)_, _norm\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/fft/_pocketfft.py#L1019-L1141)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft2.html#numpy.fft.fft2 "Link to this definition")

Compute the 2-dimensional discrete Fourier Transform.

This function computes the _n_\-dimensional discrete Fourier Transform over any axes in an _M_\-dimensional array by means of the Fast Fourier Transform (FFT). By default, the transform is computed over the last two axes of the input array, i.e., a 2-dimensional FFT.

Parameters:

**a**array\_like

Input array, can be complex

**s**sequence of ints, optional

Shape (length of each transformed axis) of the output (`s[0]` refers to axis 0, `s[1]` to axis 1, etc.). This corresponds to `n` for `fft(x, n)`. Along each axis, if the given shape is smaller than that of the input, the input is cropped. If it is larger, the input is padded with zeros.

Changed in version 2.0: If it is `-1`, the whole input is used (no padding/trimming).

If _s_ is not given, the shape of the input along the axes specified by _axes_ is used.

Deprecated since version 2.0: If _s_ is not `None`, _axes_ must not be `None` either.

Deprecated since version 2.0: _s_ must contain only `int` s, not `None` values. `None` values currently mean that the default value for `n` is used in the corresponding 1-D transform, but this behaviour is deprecated.

**axes**sequence of ints, optional

Axes over which to compute the FFT. If not given, the last two axes are used. A repeated index in _axes_ means the transform over that axis is performed multiple times. A one-element sequence means that a one-dimensional FFT is performed. Default: `(-2, -1)`.

Deprecated since version 2.0: If _s_ is specified, the corresponding _axes_ to be transformed must not be `None`.

**norm**{“backward”, “ortho”, “forward”}, optional

Normalization mode (see [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
). Default is “backward”. Indicates which direction of the forward/backward pair of transforms is scaled and with what normalization factor.

New in version 1.20.0: The “backward”, “forward” values were added.

**out**complex ndarray, optional

If provided, the result will be placed in this array. It should be of the appropriate shape and dtype for all axes (and hence only the last axis can have `s` not equal to the shape at that axis).

New in version 2.0.0.

Returns:

**out**complex ndarray

The truncated or zero-padded input, transformed along the axes indicated by _axes_, or the last two axes if _axes_ is not given.

Raises:

ValueError

If _s_ and _axes_ have different length, or _axes_ not given and `len(s) != 2`.

IndexError

If an element of _axes_ is larger than than the number of axes of _a_.

See also

[`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")

Overall view of discrete Fourier transforms, with definitions and conventions used.

[`ifft2`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft2.html#numpy.fft.ifft2 "numpy.fft.ifft2")

The inverse two-dimensional FFT.

[`fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")

The one-dimensional FFT.

[`fftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftn.html#numpy.fft.fftn "numpy.fft.fftn")

The _n_\-dimensional FFT.

[`fftshift`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftshift.html#numpy.fft.fftshift "numpy.fft.fftshift")

Shifts zero-frequency terms to the center of the array. For two-dimensional input, swaps first and third quadrants, and second and fourth quadrants.

Notes

[`fft2`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft2.html#numpy.fft.fft2 "numpy.fft.fft2")
 is just [`fftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftn.html#numpy.fft.fftn "numpy.fft.fftn")
 with a different default for _axes_.

The output, analogously to [`fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
, contains the term for zero frequency in the low-order corner of the transformed axes, the positive frequency terms in the first half of these axes, the term for the Nyquist frequency in the middle of the axes and the negative frequency terms in the second half of the axes, in order of decreasingly negative frequency.

See [`fftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftn.html#numpy.fft.fftn "numpy.fft.fftn")
 for details and a plotting example, and [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
 for definitions and conventions used.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.mgrid\[:5, :5\]\[0\]
\>>> np.fft.fft2(a)
array(\[\[ 50.  +0.j        ,   0.  +0.j        ,   0.  +0.j        , # may vary\
          0.  +0.j        ,   0.  +0.j        \],\
       \[-12.5+17.20477401j,   0.  +0.j        ,   0.  +0.j        ,\
          0.  +0.j        ,   0.  +0.j        \],\
       \[-12.5 +4.0614962j ,   0.  +0.j        ,   0.  +0.j        ,\
          0.  +0.j        ,   0.  +0.j        \],\
       \[-12.5 -4.0614962j ,   0.  +0.j        ,   0.  +0.j        ,\
          0.  +0.j        ,   0.  +0.j        \],\
       \[-12.5-17.20477401j,   0.  +0.j        ,   0.  +0.j        ,\
          0.  +0.j        ,   0.  +0.j        \]\])

Copy to clipboard

Go BackOpen In Tab

On this page