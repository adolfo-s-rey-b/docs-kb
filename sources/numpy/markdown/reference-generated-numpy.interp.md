[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.interp.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.interp.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.interp.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.interp.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.interp.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.interp.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.interp.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.interp.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.interp.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.interp.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.interp.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.interp.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.interp.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.interp.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.interp.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.interp.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.interp.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.interp.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.interp.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.interp.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.interp.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.interp.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.interp[#](https://numpy.org/doc/stable/reference/generated/numpy.interp.html#numpy-interp "Link to this heading")

========================================================================================================================

numpy.interp(_x_, _xp_, _fp_, _left\=None_, _right\=None_, _period\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L1549-L1686)
[#](https://numpy.org/doc/stable/reference/generated/numpy.interp.html#numpy.interp "Link to this definition")

One-dimensional linear interpolation for monotonically increasing sample points.

Returns the one-dimensional piecewise linear interpolant to a function with given discrete data points (_xp_, _fp_), evaluated at _x_.

Parameters:

**x**array\_like

The x-coordinates at which to evaluate the interpolated values.

**xp**1-D sequence of floats

The x-coordinates of the data points, must be increasing if argument _period_ is not specified. Otherwise, _xp_ is internally sorted after normalizing the periodic boundaries with `xp = xp % period`.

**fp**1-D sequence of float or complex

The y-coordinates of the data points, same length as _xp_.

**left**optional float or complex corresponding to fp

Value to return for _x < xp\[0\]_, default is _fp\[0\]_.

**right**optional float or complex corresponding to fp

Value to return for _x > xp\[-1\]_, default is _fp\[-1\]_.

**period**None or float, optional

A period for the x-coordinates. This parameter allows the proper interpolation of angular x-coordinates. Parameters _left_ and _right_ are ignored if _period_ is specified.

Returns:

**y**float or complex (corresponding to fp) or ndarray

The interpolated values, same shape as _x_.

Raises:

ValueError

If _xp_ and _fp_ have different length If _xp_ or _fp_ are not 1-D sequences If _period == 0_

Warning

The x-coordinate sequence is expected to be increasing, but this is not explicitly enforced. However, if the sequence _xp_ is non-increasing, interpolation results are meaningless.

Note that, since NaN is unsortable, _xp_ also cannot contain NaNs.

A simple check for _xp_ being strictly increasing is:

np.all(np.diff(xp) \> 0)

Copy to clipboard

See also

[`scipy.interpolate`](https://docs.scipy.org/doc/scipy/reference/interpolate.html#module-scipy.interpolate "(in SciPy v1.18.0)")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> xp \= \[1, 2, 3\]
\>>> fp \= \[3, 2, 0\]
\>>> np.interp(2.5, xp, fp)
1.0
\>>> np.interp(\[0, 1, 1.5, 2.72, 3.14\], xp, fp)
array(\[3.  , 3.  , 2.5 , 0.56, 0.  \])
\>>> UNDEF \= \-99.0
\>>> np.interp(3.14, xp, fp, right\=UNDEF)
\-99.0

Copy to clipboard

Plot an interpolant to the sine function:

\>>> x \= np.linspace(0, 2\*np.pi, 10)
\>>> y \= np.sin(x)
\>>> xvals \= np.linspace(0, 2\*np.pi, 50)
\>>> yinterp \= np.interp(xvals, x, y)
\>>> import matplotlib.pyplot as plt
\>>> plt.plot(x, y, 'o')
\[<matplotlib.lines.Line2D object at 0x...>\]
\>>> plt.plot(xvals, yinterp, '-x')
\[<matplotlib.lines.Line2D object at 0x...>\]
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-interp-1_00_00.png](https://numpy.org/doc/stable/_images/numpy-interp-1_00_00.png)

Interpolation with periodic x-coordinates:

\>>> x \= \[\-180, \-170, \-185, 185, \-10, \-5, 0, 365\]
\>>> xp \= \[190, \-190, 350, \-350\]
\>>> fp \= \[5, 10, 3, 4\]
\>>> np.interp(x, xp, fp, period\=360)
array(\[7.5 , 5.  , 8.75, 6.25, 3.  , 3.25, 3.5 , 3.75\])

Copy to clipboard

Complex interpolation:

\>>> x \= \[1.5, 4.0\]
\>>> xp \= \[2,3,5\]
\>>> fp \= \[1.0j, 0, 2+3j\]
\>>> np.interp(x, xp, fp)
array(\[0.+1.j , 1.+1.5j\])

Copy to clipboard

Go BackOpen In Tab

On this page