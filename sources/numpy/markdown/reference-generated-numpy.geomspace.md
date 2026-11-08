[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.geomspace.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.geomspace.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.geomspace.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.geomspace.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.geomspace.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.geomspace.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.geomspace.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.geomspace.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.geomspace.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.geomspace.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.geomspace.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.geomspace.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.geomspace.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.geomspace.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.geomspace.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.geomspace.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.geomspace.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.geomspace.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.geomspace.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.geomspace.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.geomspace.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.geomspace.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.geomspace[#](https://numpy.org/doc/stable/reference/generated/numpy.geomspace.html#numpy-geomspace "Link to this heading")

=================================================================================================================================

numpy.geomspace(_start_, _stop_, _num\=50_, _endpoint\=True_, _dtype\=None_, _axis\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/function_base.py#L311-L453)
[#](https://numpy.org/doc/stable/reference/generated/numpy.geomspace.html#numpy.geomspace "Link to this definition")

Return numbers spaced evenly on a log scale (a geometric progression).

This is similar to [`logspace`](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
, but with endpoints specified directly. Each output sample is a constant multiple of the previous.

Parameters:

**start**array\_like

The starting value of the sequence.

**stop**array\_like

The final value of the sequence, unless _endpoint_ is False. In that case, `num + 1` values are spaced over the interval in log-space, of which all but the last (a sequence of length _num_) are returned.

**num**integer, optional

Number of samples to generate. Default is 50.

**endpoint**boolean, optional

If true, _stop_ is the last sample. Otherwise, it is not included. Default is True.

**dtype**dtype

The type of the output array. If [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is not given, the data type is inferred from _start_ and _stop_. The inferred dtype will never be an integer; _float_ is chosen even if the arguments would produce an array of integers.

**axis**int, optional

The axis in the result to store the samples. Relevant only if start or stop are array-like. By default (0), the samples will be along a new axis inserted at the beginning. Use -1 to get an axis at the end.

Returns:

**samples**ndarray

_num_ samples, equally spaced on a log scale.

See also

[`logspace`](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")

Similar to geomspace, but with endpoints specified using log and base.

[`linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")

Similar to geomspace, but with arithmetic instead of geometric progression.

[`arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")

Similar to linspace, with the step size specified instead of the number of samples.

[How to create arrays with regularly-spaced values](https://numpy.org/doc/stable/user/how-to-partition.html#how-to-partition)

Notes

If the inputs or dtype are complex, the output will follow a logarithmic spiral in the complex plane. (There are an infinite number of spirals passing through two points; the output will follow the shortest such path.)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.geomspace(1, 1000, num\=4)
array(\[    1.,    10.,   100.,  1000.\])
\>>> np.geomspace(1, 1000, num\=3, endpoint\=False)
array(\[   1.,   10.,  100.\])
\>>> np.geomspace(1, 1000, num\=4, endpoint\=False)
array(\[   1.        ,    5.62341325,   31.6227766 ,  177.827941  \])
\>>> np.geomspace(1, 256, num\=9)
array(\[   1.,    2.,    4.,    8.,   16.,   32.,   64.,  128.,  256.\])

Copy to clipboard

Note that the above may not produce exact integers:

\>>> np.geomspace(1, 256, num\=9, dtype\=np.int\_)
array(\[  1,   2,   4,   7,  16,  32,  63, 127, 256\])
\>>> np.around(np.geomspace(1, 256, num\=9)).astype(np.int\_)
array(\[  1,   2,   4,   8,  16,  32,  64, 128, 256\])

Copy to clipboard

Negative, decreasing, and complex inputs are allowed:

\>>> np.geomspace(1000, 1, num\=4)
array(\[1000.,  100.,   10.,    1.\])
\>>> np.geomspace(\-1000, \-1, num\=4)
array(\[-1000.,  -100.,   -10.,    -1.\])
\>>> np.geomspace(1j, 1000j, num\=4)  \# Straight line
array(\[0.   +1.j, 0.  +10.j, 0. +100.j, 0.+1000.j\])
\>>> np.geomspace(\-1+0j, 1+0j, num\=5)  \# Circle
array(\[-1.00000000e+00+1.22464680e-16j, -7.07106781e-01+7.07106781e-01j,\
        6.12323400e-17+1.00000000e+00j,  7.07106781e-01+7.07106781e-01j,\
        1.00000000e+00+0.00000000e+00j\])

Copy to clipboard

Graphical illustration of _endpoint_ parameter:

\>>> import matplotlib.pyplot as plt
\>>> N \= 10
\>>> y \= np.zeros(N)
\>>> plt.semilogx(np.geomspace(1, 1000, N, endpoint\=True), y + 1, 'o')
\[<matplotlib.lines.Line2D object at 0x...>\]
\>>> plt.semilogx(np.geomspace(1, 1000, N, endpoint\=False), y + 2, 'o')
\[<matplotlib.lines.Line2D object at 0x...>\]
\>>> plt.axis(\[0.5, 2000, 0, 3\])
\[0.5, 2000, 0, 3\]
\>>> plt.grid(True, color\='0.7', linestyle\='-', which\='both', axis\='both')
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-geomspace-1.png](https://numpy.org/doc/stable/_images/numpy-geomspace-1.png)

Go BackOpen In Tab

On this page