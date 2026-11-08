[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft2.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fft.rfft2.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft2.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fft.rfft2.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fft.rfft2.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fft.rfft2.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fft.rfft2.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fft.rfft2.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fft.rfft2.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fft.rfft2.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fft.rfft2.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fft.rfft2.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fft.rfft2.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fft.rfft2.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fft.rfft2.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fft.rfft2.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fft.rfft2.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fft.rfft2.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fft.rfft2.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fft.rfft2.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fft.rfft2.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fft.rfft2.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fft.rfft2[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft2.html#numpy-fft-rfft2 "Link to this heading")

=================================================================================================================================

fft.rfft2(_a_, _s\=None_, _axes\=(-2, \-1)_, _norm\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/fft/_pocketfft.py#L1393-L1470)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft2.html#numpy.fft.rfft2 "Link to this definition")

Compute the 2-dimensional FFT of a real array.

Parameters:

**a**array

Input array, taken to be real.

**s**sequence of ints, optional

Shape of the FFT.

Changed in version 2.0: If it is `-1`, the whole input is used (no padding/trimming).

Deprecated since version 2.0: If _s_ is not `None`, _axes_ must not be `None` either.

Deprecated since version 2.0: _s_ must contain only `int` s, not `None` values. `None` values currently mean that the default value for `n` is used in the corresponding 1-D transform, but this behaviour is deprecated.

**axes**sequence of ints, optional

Axes over which to compute the FFT. Default: `(-2, -1)`.

Deprecated since version 2.0: If _s_ is specified, the corresponding _axes_ to be transformed must not be `None`.

**norm**{“backward”, “ortho”, “forward”}, optional

Normalization mode (see [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
). Default is “backward”. Indicates which direction of the forward/backward pair of transforms is scaled and with what normalization factor.

New in version 1.20.0: The “backward”, “forward” values were added.

**out**complex ndarray, optional

If provided, the result will be placed in this array. It should be of the appropriate shape and dtype for the last inverse transform. incompatible with passing in all but the trivial `s`).

New in version 2.0.0.

Returns:

**out**ndarray

The result of the real 2-D FFT.

See also

[`rfftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftn.html#numpy.fft.rfftn "numpy.fft.rfftn")

Compute the N-dimensional discrete Fourier Transform for real input.

Notes

This is really just [`rfftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftn.html#numpy.fft.rfftn "numpy.fft.rfftn")
 with different default behavior. For more details see [`rfftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftn.html#numpy.fft.rfftn "numpy.fft.rfftn")
.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.mgrid\[:5, :5\]\[0\]
\>>> np.fft.rfft2(a)
array(\[\[ 50.  +0.j        ,   0.  +0.j        ,   0.  +0.j        \],\
       \[-12.5+17.20477401j,   0.  +0.j        ,   0.  +0.j        \],\
       \[-12.5 +4.0614962j ,   0.  +0.j        ,   0.  +0.j        \],\
       \[-12.5 -4.0614962j ,   0.  +0.j        ,   0.  +0.j        \],\
       \[-12.5-17.20477401j,   0.  +0.j        ,   0.  +0.j        \]\])

Copy to clipboard

Go BackOpen In Tab

On this page