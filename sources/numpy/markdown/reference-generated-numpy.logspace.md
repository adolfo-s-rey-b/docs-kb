[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.logspace.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.logspace.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.logspace.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.logspace.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.logspace.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.logspace.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.logspace.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.logspace.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.logspace.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.logspace.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.logspace.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.logspace.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.logspace.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.logspace.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.logspace.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.logspace.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.logspace.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.logspace.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.logspace.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.logspace.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.logspace[#](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy-logspace "Link to this heading")

==============================================================================================================================

numpy.logspace(_start_, _stop_, _num\=50_, _endpoint\=True_, _base\=10.0_, _dtype\=None_, _axis\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/function_base.py#L196-L303)
[#](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "Link to this definition")

Return numbers spaced evenly on a log scale.

In linear space, the sequence starts at `base ** start` (_base_ to the power of _start_) and ends with `base ** stop` (see _endpoint_ below).

Changed in version 1.25.0: Non-scalar ‘base\` is now supported

Parameters:

**start**array\_like

`base ** start` is the starting value of the sequence.

**stop**array\_like

`base ** stop` is the final value of the sequence, unless _endpoint_ is False. In that case, `num + 1` values are spaced over the interval in log-space, of which all but the last (a sequence of length _num_) are returned.

**num**integer, optional

Number of samples to generate. Default is 50.

**endpoint**boolean, optional

If true, _stop_ is the last sample. Otherwise, it is not included. Default is True.

**base**array\_like, optional

The base of the log space. The step size between the elements in `ln(samples) / ln(base)` (or `log_base(samples)`) is uniform. Default is 10.0.

**dtype**dtype

The type of the output array. If [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is not given, the data type is inferred from _start_ and _stop_. The inferred type will never be an integer; _float_ is chosen even if the arguments would produce an array of integers.

**axis**int, optional

The axis in the result to store the samples. Relevant only if start, stop, or base are array-like. By default (0), the samples will be along a new axis inserted at the beginning. Use -1 to get an axis at the end.

Returns:

**samples**ndarray

_num_ samples, equally spaced on a log scale.

See also

[`arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")

Similar to linspace, with the step size specified instead of the number of samples. Note that, when used with a float endpoint, the endpoint may or may not be included.

[`linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")

Similar to logspace, but with the samples uniformly distributed in linear space, instead of log space.

[`geomspace`](https://numpy.org/doc/stable/reference/generated/numpy.geomspace.html#numpy.geomspace "numpy.geomspace")

Similar to logspace, but with endpoints specified directly.

[How to create arrays with regularly-spaced values](https://numpy.org/doc/stable/user/how-to-partition.html#how-to-partition)

Notes

If base is a scalar, logspace is equivalent to the code

\>>> y \= np.linspace(start, stop, num\=num, endpoint\=endpoint)
... 
\>>> power(base, y).astype(dtype)
... 

Copy to clipboard

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.logspace(2.0, 3.0, num\=4)
array(\[ 100.        ,  215.443469  ,  464.15888336, 1000.        \])
\>>> np.logspace(2.0, 3.0, num\=4, endpoint\=False)
array(\[100.        ,  177.827941  ,  316.22776602,  562.34132519\])
\>>> np.logspace(2.0, 3.0, num\=4, base\=2.0)
array(\[4.        ,  5.0396842 ,  6.34960421,  8.        \])
\>>> np.logspace(2.0, 3.0, num\=4, base\=\[2.0, 3.0\], axis\=-1)
array(\[\[ 4.        ,  5.0396842 ,  6.34960421,  8.        \],\
       \[ 9.        , 12.98024613, 18.72075441, 27.        \]\])

Copy to clipboard

Graphical illustration:

\>>> import matplotlib.pyplot as plt
\>>> N \= 10
\>>> x1 \= np.logspace(0.1, 1, N, endpoint\=True)
\>>> x2 \= np.logspace(0.1, 1, N, endpoint\=False)
\>>> y \= np.zeros(N)
\>>> plt.plot(x1, y, 'o')
\[<matplotlib.lines.Line2D object at 0x...>\]
\>>> plt.plot(x2, y + 0.5, 'o')
\[<matplotlib.lines.Line2D object at 0x...>\]
\>>> plt.ylim(\[\-0.5, 1\])
(-0.5, 1)
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-logspace-1.png](https://numpy.org/doc/stable/_images/numpy-logspace-1.png)

Go BackOpen In Tab

On this page