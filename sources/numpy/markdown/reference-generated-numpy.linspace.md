[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linspace.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linspace.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linspace.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linspace.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linspace.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linspace.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linspace.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linspace.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linspace.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linspace.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linspace.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linspace.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linspace.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linspace.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linspace.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linspace.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linspace.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linspace.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linspace.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linspace.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linspace[#](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy-linspace "Link to this heading")

==============================================================================================================================

numpy.linspace(_start_, _stop_, _num\=50_, _endpoint\=True_, _retstep\=False_, _dtype\=None_, _axis\=0_, _\*_, _device\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/function_base.py#L27-L188)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "Link to this definition")

Return evenly spaced numbers over a specified interval.

Returns _num_ evenly spaced samples, calculated over the interval \[_start_, _stop_\].

The endpoint of the interval can optionally be excluded.

Changed in version 1.20.0: Values are rounded towards `-inf` instead of `0` when an integer `dtype` is specified. The old behavior can still be obtained with `np.linspace(start, stop, num).astype(np.int_)`

Parameters:

**start**array\_like

The starting value of the sequence.

**stop**array\_like

The end value of the sequence, unless _endpoint_ is set to False. In that case, the sequence consists of all but the last of `num + 1` evenly spaced samples, so that _stop_ is excluded. Note that the step size changes when _endpoint_ is False.

**num**int, optional

Number of samples to generate. Default is 50. Must be non-negative.

**endpoint**bool, optional

If True, _stop_ is the last sample. Otherwise, it is not included. Default is True.

**retstep**bool, optional

If True, return (_samples_, _step_), where _step_ is the spacing between samples.

**dtype**dtype, optional

The type of the output array. If [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is not given, the data type is inferred from _start_ and _stop_. The inferred dtype will never be an integer; _float_ is chosen even if the arguments would produce an array of integers.

**axis**int, optional

The axis in the result to store the samples. Relevant only if start or stop are array-like. By default (0), the samples will be along a new axis inserted at the beginning. Use -1 to get an axis at the end.

**device**str, optional

The device on which to place the created array. Default: None. For Array-API interoperability only, so must be `"cpu"` if passed.

New in version 2.0.0.

Returns:

**samples**ndarray

There are _num_ equally spaced samples in the closed interval `[start, stop]` or the half-open interval `[start, stop)` (depending on whether _endpoint_ is True or False).\
\
**step**float, optional\
\
Only returned if _retstep_ is True\
\
Size of spacing between samples.\
\
See also\
\
[`arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")\
\
Similar to [`linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")\
, but uses a step size (instead of the number of samples).\
\
[`geomspace`](https://numpy.org/doc/stable/reference/generated/numpy.geomspace.html#numpy.geomspace "numpy.geomspace")\
\
Similar to [`linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")\
, but with numbers spaced evenly on a log scale (a geometric progression).\
\
[`logspace`](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")\
\
Similar to [`geomspace`](https://numpy.org/doc/stable/reference/generated/numpy.geomspace.html#numpy.geomspace "numpy.geomspace")\
, but with the end points specified as logarithms.\
\
[How to create arrays with regularly-spaced values](https://numpy.org/doc/stable/user/how-to-partition.html#how-to-partition)\
\
Examples\
\
Try it in your browser!\
\
\>>> import numpy as np\
\>>> np.linspace(2.0, 3.0, num\=5)\
array(\[2.  , 2.25, 2.5 , 2.75, 3.  \])\
\>>> np.linspace(2.0, 3.0, num\=5, endpoint\=False)\
array(\[2. ,  2.2,  2.4,  2.6,  2.8\])\
\>>> np.linspace(2.0, 3.0, num\=5, retstep\=True)\
(array(\[2.  ,  2.25,  2.5 ,  2.75,  3.  \]), 0.25)\
\
Copy to clipboard\
\
Graphical illustration:\
\
\>>> import matplotlib.pyplot as plt\
\>>> N \= 8\
\>>> y \= np.zeros(N)\
\>>> x1 \= np.linspace(0, 10, N, endpoint\=True)\
\>>> x2 \= np.linspace(0, 10, N, endpoint\=False)\
\>>> plt.plot(x1, y, 'o')\
\[<matplotlib.lines.Line2D object at 0x...>\]\
\>>> plt.plot(x2, y + 0.5, 'o')\
\[<matplotlib.lines.Line2D object at 0x...>\]\
\>>> plt.ylim(\[\-0.5, 1\])\
(-0.5, 1)\
\>>> plt.show()\
\
Copy to clipboard\
\
![../../_images/numpy-linspace-1.png](https://numpy.org/doc/stable/_images/numpy-linspace-1.png)\
\
Go BackOpen In Tab\
\
On this page