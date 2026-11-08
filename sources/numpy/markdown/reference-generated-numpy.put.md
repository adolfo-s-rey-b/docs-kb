[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.put.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.put.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.put.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.put.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.put.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.put.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.put.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.put.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.put.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.put.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.put.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.put.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.put.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.put.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.put.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.put.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.put.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.put.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.put.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.put.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.put.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.put.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.put[#](https://numpy.org/doc/stable/reference/generated/numpy.put.html#numpy-put "Link to this heading")

===============================================================================================================

numpy.put(_a_, _ind_, _v_, _mode\='raise'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L488-L545)
[#](https://numpy.org/doc/stable/reference/generated/numpy.put.html#numpy.put "Link to this definition")

Replaces specified elements of an array with given values.

The indexing works on the flattened target array. [`put`](https://numpy.org/doc/stable/reference/generated/numpy.put.html#numpy.put "numpy.put")
 is roughly equivalent to:

a.flat\[ind\] \= v

Copy to clipboard

Parameters:

**a**ndarray

Target array.

**ind**array\_like

Target indices, interpreted as integers.

**v**array\_like

Values to place in _a_ at target indices. If _v_ is shorter than _ind_ it will be repeated as necessary.

**mode**{‘raise’, ‘wrap’, ‘clip’}, optional

Specifies how out-of-bounds indices will behave.

*   ‘raise’ – raise an error (default)
    
*   ‘wrap’ – wrap around
    
*   ‘clip’ – clip to the range
    

‘clip’ mode means that all indices that are too large are replaced by the index that addresses the last element along that axis. Note that this disables indexing with negative numbers. In ‘raise’ mode, if an exception occurs the target array may still be modified.

See also

[`putmask`](https://numpy.org/doc/stable/reference/generated/numpy.putmask.html#numpy.putmask "numpy.putmask")
, [`place`](https://numpy.org/doc/stable/reference/generated/numpy.place.html#numpy.place "numpy.place")

[`put_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.put_along_axis.html#numpy.put_along_axis "numpy.put_along_axis")

Put elements by matching the array and the index arrays

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.arange(5)
\>>> np.put(a, \[0, 2\], \[\-44, \-55\])
\>>> a
array(\[-44,   1, -55,   3,   4\])

Copy to clipboard

\>>> a \= np.arange(5)
\>>> np.put(a, 22, \-5, mode\='clip')
\>>> a
array(\[ 0,  1,  2,  3, -5\])

Copy to clipboard

Go BackOpen In Tab

On this page