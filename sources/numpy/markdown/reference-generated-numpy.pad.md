[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.pad.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.pad.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.pad.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.pad.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.pad.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.pad.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.pad.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.pad.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.pad.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.pad.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.pad.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.pad.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.pad.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.pad.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.pad.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.pad.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.pad.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.pad.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.pad.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.pad.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.pad.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.pad.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.pad[#](https://numpy.org/doc/stable/reference/generated/numpy.pad.html#numpy-pad "Link to this heading")

===============================================================================================================

numpy.pad(_array_, _pad\_width_, _mode\='constant'_, _\*\*kwargs_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_arraypad_impl.py#L546-L926)
[#](https://numpy.org/doc/stable/reference/generated/numpy.pad.html#numpy.pad "Link to this definition")

Pad an array.

Parameters:

**array**array\_like of rank N

The array to pad.

**pad\_width**{sequence, array\_like, int, dict}

Number of values padded to the edges of each axis. `((before_1, after_1), ... (before_N, after_N))` unique pad widths for each axis. `(before, after)` or `((before, after),)` yields same before and after pad for each axis. `(pad,)` or `int` is a shortcut for before = after = pad width for all axes. If a `dict`, each key is an axis and its corresponding value is an `int` or `int` pair describing the padding `(before, after)` or `pad` width for that axis.

**mode**str or function, optional

One of the following string values or a user supplied function.

‘constant’ (default)

Pads with a constant value.

‘edge’

Pads with the edge values of array.

‘linear\_ramp’

Pads with the linear ramp between end\_value and the array edge value.

‘maximum’

Pads with the maximum value of all or part of the vector along each axis.

‘mean’

Pads with the mean value of all or part of the vector along each axis.

‘median’

Pads with the median value of all or part of the vector along each axis.

‘minimum’

Pads with the minimum value of all or part of the vector along each axis.

‘reflect’

Pads with the reflection of the vector mirrored on the first and last values of the vector along each axis.

‘symmetric’

Pads with the reflection of the vector mirrored along the edge of the array.

‘wrap’

Pads with the wrap of the vector along the axis. The first values are used to pad the end and the end values are used to pad the beginning.

‘empty’

Pads with undefined values.

<function>

Padding function, see Notes.

**stat\_length**sequence or int, optional

Used in ‘maximum’, ‘mean’, ‘median’, and ‘minimum’. Number of values at edge of each axis used to calculate the statistic value.

`((before_1, after_1), ... (before_N, after_N))` unique statistic lengths for each axis.

`(before, after)` or `((before, after),)` yields same before and after statistic lengths for each axis.

`(stat_length,)` or `int` is a shortcut for `before = after = statistic` length for all axes.

Default is `None`, to use the entire axis.

**constant\_values**sequence or scalar, optional

Used in ‘constant’. The values to set the padded values for each axis.

`((before_1, after_1), ... (before_N, after_N))` unique pad constants for each axis.

`(before, after)` or `((before, after),)` yields same before and after constants for each axis.

`(constant,)` or `constant` is a shortcut for `before = after = constant` for all axes.

Default is 0.

**end\_values**sequence or scalar, optional

Used in ‘linear\_ramp’. The values used for the ending value of the linear\_ramp and that will form the edge of the padded array.

`((before_1, after_1), ... (before_N, after_N))` unique end values for each axis.

`(before, after)` or `((before, after),)` yields same before and after end values for each axis.

`(constant,)` or `constant` is a shortcut for `before = after = constant` for all axes.

Default is 0.

**reflect\_type**{‘even’, ‘odd’}, optional

Used in ‘reflect’, and ‘symmetric’. The ‘even’ style is the default with an unaltered reflection around the edge value. For the ‘odd’ style, the extended part of the array is created by subtracting the reflected values from two times the edge value.

Returns:

**pad**ndarray

Padded array of rank equal to [`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
 with shape increased according to _pad\_width_.

Notes

For an array with rank greater than 1, some of the padding of later axes is calculated from padding of previous axes. This is easiest to think about with a rank 2 array where the corners of the padded array are calculated by using padded values from the first axis.

The padding function, if used, should modify a rank 1 array in-place. It has the following signature:

padding\_func(vector, iaxis\_pad\_width, iaxis, kwargs)

Copy to clipboard

where

vectorndarray

A rank 1 array already padded with zeros. Padded values are vector\[:iaxis\_pad\_width\[0\]\] and vector\[-iaxis\_pad\_width\[1\]:\].

iaxis\_pad\_widthtuple

A 2-tuple of ints, iaxis\_pad\_width\[0\] represents the number of values padded at the beginning of vector where iaxis\_pad\_width\[1\] represents the number of values padded at the end of vector.

iaxisint

The axis currently being calculated.

kwargsdict

Any keyword arguments the function requires.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= \[1, 2, 3, 4, 5\]
\>>> np.pad(a, (2, 3), 'constant', constant\_values\=(4, 6))
array(\[4, 4, 1, ..., 6, 6, 6\])

Copy to clipboard

\>>> np.pad(a, (2, 3), 'edge')
array(\[1, 1, 1, ..., 5, 5, 5\])

Copy to clipboard

\>>> np.pad(a, (2, 3), 'linear\_ramp', end\_values\=(5, \-4))
array(\[ 5,  3,  1,  2,  3,  4,  5,  2, -1, -4\])

Copy to clipboard

\>>> np.pad(a, (2,), 'maximum')
array(\[5, 5, 1, 2, 3, 4, 5, 5, 5\])

Copy to clipboard

\>>> np.pad(a, (2,), 'mean')
array(\[3, 3, 1, 2, 3, 4, 5, 3, 3\])

Copy to clipboard

\>>> np.pad(a, (2,), 'median')
array(\[3, 3, 1, 2, 3, 4, 5, 3, 3\])

Copy to clipboard

\>>> a \= \[\[1, 2\], \[3, 4\]\]
\>>> np.pad(a, ((3, 2), (2, 3)), 'minimum')
array(\[\[1, 1, 1, 2, 1, 1, 1\],\
       \[1, 1, 1, 2, 1, 1, 1\],\
       \[1, 1, 1, 2, 1, 1, 1\],\
       \[1, 1, 1, 2, 1, 1, 1\],\
       \[3, 3, 3, 4, 3, 3, 3\],\
       \[1, 1, 1, 2, 1, 1, 1\],\
       \[1, 1, 1, 2, 1, 1, 1\]\])

Copy to clipboard

\>>> a \= \[1, 2, 3, 4, 5\]
\>>> np.pad(a, (2, 3), 'reflect')
array(\[3, 2, 1, 2, 3, 4, 5, 4, 3, 2\])

Copy to clipboard

\>>> np.pad(a, (2, 3), 'reflect', reflect\_type\='odd')
array(\[-1,  0,  1,  2,  3,  4,  5,  6,  7,  8\])

Copy to clipboard

\>>> np.pad(a, (2, 3), 'symmetric')
array(\[2, 1, 1, 2, 3, 4, 5, 5, 4, 3\])

Copy to clipboard

\>>> np.pad(a, (2, 3), 'symmetric', reflect\_type\='odd')
array(\[0, 1, 1, 2, 3, 4, 5, 5, 6, 7\])

Copy to clipboard

\>>> np.pad(a, (2, 3), 'wrap')
array(\[4, 5, 1, 2, 3, 4, 5, 1, 2, 3\])

Copy to clipboard

\>>> def pad\_with(vector, pad\_width, iaxis, kwargs):
...     pad\_value \= kwargs.get('padder', 10)
...     vector\[:pad\_width\[0\]\] \= pad\_value
...     vector\[\-pad\_width\[1\]:\] \= pad\_value
\>>> a \= np.arange(6)
\>>> a \= a.reshape((2, 3))
\>>> np.pad(a, 2, pad\_with)
array(\[\[10, 10, 10, 10, 10, 10, 10\],\
       \[10, 10, 10, 10, 10, 10, 10\],\
       \[10, 10,  0,  1,  2, 10, 10\],\
       \[10, 10,  3,  4,  5, 10, 10\],\
       \[10, 10, 10, 10, 10, 10, 10\],\
       \[10, 10, 10, 10, 10, 10, 10\]\])
\>>> np.pad(a, 2, pad\_with, padder\=100)
array(\[\[100, 100, 100, 100, 100, 100, 100\],\
       \[100, 100, 100, 100, 100, 100, 100\],\
       \[100, 100,   0,   1,   2, 100, 100\],\
       \[100, 100,   3,   4,   5, 100, 100\],\
       \[100, 100, 100, 100, 100, 100, 100\],\
       \[100, 100, 100, 100, 100, 100, 100\]\])

Copy to clipboard

\>>> a \= np.arange(1, 7).reshape(2, 3)
\>>> np.pad(a, {1: (1, 2)})
array(\[\[0, 1, 2, 3, 0, 0\],\
       \[0, 4, 5, 6, 0, 0\]\])
\>>> np.pad(a, {\-1: 2})
array(\[\[0, 0, 1, 2, 3, 0, 0\],\
       \[0, 0, 4, 5, 6, 0, 0\]\])
\>>> np.pad(a, {0: (3, 0)})
array(\[\[0, 0, 0\],\
       \[0, 0, 0\],\
       \[0, 0, 0\],\
       \[1, 2, 3\],\
       \[4, 5, 6\]\])
\>>> np.pad(a, {0: (3, 0), 1: 2})
array(\[\[0, 0, 0, 0, 0, 0, 0\],\
       \[0, 0, 0, 0, 0, 0, 0\],\
       \[0, 0, 0, 0, 0, 0, 0\],\
       \[0, 0, 1, 2, 3, 0, 0\],\
       \[0, 0, 4, 5, 6, 0, 0\]\])

Copy to clipboard

Go BackOpen In Tab

On this page