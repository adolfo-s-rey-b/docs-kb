[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.array_split.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.array_split.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.array_split.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.array_split.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.array_split.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.array_split.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.array_split.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.array_split.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.array_split.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.array_split.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.array_split.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.array_split.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.array_split.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.array_split.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.array_split.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.array_split.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.array_split.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.array_split.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.array_split.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.array_split.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.array\_split[#](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html#numpy-array-split "Link to this heading")

========================================================================================================================================

numpy.array\_split(_ary_, _indices\_or\_sections_, _axis\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_shape_base_impl.py#L719-L773)
[#](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html#numpy.array_split "Link to this definition")

Split an array into multiple sub-arrays.

Please refer to the `split` documentation. The only difference between these functions is that `array_split` allows _indices\_or\_sections_ to be an integer that does _not_ equally divide the axis. For an array of length l that should be split into n sections, it returns l % n sub-arrays of size l//n + 1 and the rest of size l//n.

See also

[`split`](https://numpy.org/doc/stable/reference/generated/numpy.split.html#numpy.split "numpy.split")

Split array into multiple sub-arrays of equal size.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(8.0)
\>>> np.array\_split(x, 3)
\[array(\[0.,  1.,  2.\]), array(\[3.,  4.,  5.\]), array(\[6.,  7.\])\]

Copy to clipboard

\>>> x \= np.arange(9)
\>>> np.array\_split(x, 4)
\[array(\[0, 1, 2\]), array(\[3, 4\]), array(\[5, 6\]), array(\[7, 8\])\]

Copy to clipboard

Go BackOpen In Tab

On this page