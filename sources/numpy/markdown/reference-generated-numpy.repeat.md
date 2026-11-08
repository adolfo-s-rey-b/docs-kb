[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.repeat.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.repeat.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.repeat.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.repeat.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.repeat.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.repeat.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.repeat.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.repeat.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.repeat.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.repeat.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.repeat.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.repeat.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.repeat.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.repeat.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.repeat.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.repeat.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.repeat.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.repeat.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.repeat.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.repeat.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.repeat[#](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy-repeat "Link to this heading")

========================================================================================================================

numpy.repeat(_a_, _repeats_, _axis\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L437-L481)
[#](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "Link to this definition")

Repeat each element of an array after themselves

Parameters:

**a**array\_like

Input array.

**repeats**int or array of ints

The number of repetitions for each element. _repeats_ is broadcasted to fit the shape of the given axis.

**axis**int, optional

The axis along which to repeat values. By default, use the flattened input array, and return a flat output array.

Returns:

**repeated\_array**ndarray

Output array which has the same shape as _a_, except along the given axis.

See also

[`tile`](https://numpy.org/doc/stable/reference/generated/numpy.tile.html#numpy.tile "numpy.tile")

Tile an array.

[`unique`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")

Find the unique elements of an array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.repeat(3, 4)
array(\[3, 3, 3, 3\])
\>>> x \= np.array(\[\[1,2\],\[3,4\]\])
\>>> np.repeat(x, 2)
array(\[1, 1, 2, 2, 3, 3, 4, 4\])
\>>> np.repeat(x, 3, axis\=1)
array(\[\[1, 1, 1, 2, 2, 2\],\
       \[3, 3, 3, 4, 4, 4\]\])
\>>> np.repeat(x, \[1, 2\], axis\=0)
array(\[\[1, 2\],\
       \[3, 4\],\
       \[3, 4\]\])

Copy to clipboard

Go BackOpen In Tab

On this page