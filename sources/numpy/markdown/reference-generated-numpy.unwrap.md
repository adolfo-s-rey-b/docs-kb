[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.unwrap.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.unwrap.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.unwrap.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.unwrap.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.unwrap.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.unwrap.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.unwrap.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.unwrap.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.unwrap.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.unwrap.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.unwrap.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.unwrap.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.unwrap.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.unwrap.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.unwrap.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.unwrap.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.unwrap.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.unwrap.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.unwrap.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.unwrap.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.unwrap.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.unwrap.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.unwrap[#](https://numpy.org/doc/stable/reference/generated/numpy.unwrap.html#numpy-unwrap "Link to this heading")

========================================================================================================================

numpy.unwrap(_p_, _discont\=None_, _axis\=\-1_, _\*_, _period\=6.283185307179586_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L1751-L1863)
[#](https://numpy.org/doc/stable/reference/generated/numpy.unwrap.html#numpy.unwrap "Link to this definition")

Unwrap by taking the complement of large deltas with respect to the period.

This unwraps a signal _p_ by changing elements which have an absolute difference from their predecessor of more than `max(discont, period/2)` to their _period_\-complementary values.

For the default case where _period_ is \\(2\\pi\\) and _discont_ is \\(\\pi\\), this unwraps a radian phase _p_ such that adjacent differences are never greater than \\(\\pi\\) by adding \\(2k\\pi\\) for some integer \\(k\\).

Parameters:

**p**array\_like

Input array.

**discont**float, optional

Maximum discontinuity between values, default is `period/2`. Values below `period/2` are treated as if they were `period/2`. To have an effect different from the default, _discont_ should be larger than `period/2`.

**axis**int, optional

Axis along which unwrap will operate, default is the last axis.

**period**float, optional

Size of the range over which the input wraps. By default, it is `2 pi`.

New in version 1.21.0.

Returns:

**out**ndarray

Output array.

See also

[`rad2deg`](https://numpy.org/doc/stable/reference/generated/numpy.rad2deg.html#numpy.rad2deg "numpy.rad2deg")
, [`deg2rad`](https://numpy.org/doc/stable/reference/generated/numpy.deg2rad.html#numpy.deg2rad "numpy.deg2rad")

Notes

If the discontinuity in _p_ is smaller than `period/2`, but larger than _discont_, no unwrapping is done because taking the complement would only make the discontinuity larger.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> phase \= np.linspace(0, np.pi, num\=5)
\>>> phase\[3:\] += np.pi
\>>> phase
array(\[ 0.        ,  0.78539816,  1.57079633,  5.49778714,  6.28318531\]) # may vary
\>>> np.unwrap(phase)
array(\[ 0.        ,  0.78539816,  1.57079633, -0.78539816,  0.        \]) # may vary
\>>> np.unwrap(\[0, 1, 2, \-1, 0\], period\=4)
array(\[0, 1, 2, 3, 4\])
\>>> np.unwrap(\[ 1, 2, 3, 4, 5, 6, 1, 2, 3\], period\=6)
array(\[1, 2, 3, 4, 5, 6, 7, 8, 9\])
\>>> np.unwrap(\[2, 3, 4, 5, 2, 3, 4, 5\], period\=4)
array(\[2, 3, 4, 5, 6, 7, 8, 9\])
\>>> phase\_deg \= np.mod(np.linspace(0 ,720, 19), 360) \- 180
\>>> np.unwrap(phase\_deg, period\=360)
array(\[-180., -140., -100.,  -60.,  -20.,   20.,   60.,  100.,  140.,\
        180.,  220.,  260.,  300.,  340.,  380.,  420.,  460.,  500.,\
        540.\])

Copy to clipboard

This example plots the unwrapping of the wrapped input signal _w_. First generate _w_, then apply [`unwrap`](https://numpy.org/doc/stable/reference/generated/numpy.unwrap.html#numpy.unwrap "numpy.unwrap")
 to get _u_.

\>>> t \= np.linspace(0, 25, 801)
\>>> w \= np.mod(1.5 \* np.sin(1.1 \* t + 0.26) \* (1 \- t / 6 + (t / 23) \*\* 3), 2.0) \- 1
\>>> u \= np.unwrap(w, period\=2.0)

Copy to clipboard

Plot _w_ and _u_.

\>>> import matplotlib.pyplot as plt
\>>> plt.plot(t, w, label\='w (a signal wrapped to \[-1, 1\])')
\>>> plt.plot(t, u, linewidth\=2.5, alpha\=0.5, label\='unwrap(w, period=2)')
\>>> plt.xlabel('t')
\>>> plt.grid(alpha\=0.6)
\>>> plt.legend(framealpha\=1, shadow\=True)
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-unwrap-1.png](https://numpy.org/doc/stable/_images/numpy-unwrap-1.png)

Go BackOpen In Tab

On this page