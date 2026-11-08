[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.diagflat.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.diagflat.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.diagflat.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.diagflat.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.diagflat.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.diagflat.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.diagflat.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.diagflat.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.diagflat.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.diagflat.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.diagflat.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.diagflat.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.diagflat.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.diagflat.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.diagflat.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.diagflat.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.diagflat.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.diagflat.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.diagflat.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.diagflat.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.diagflat.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.diagflat.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.diagflat[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.diagflat.html#numpy-ma-diagflat "Link to this heading")

=======================================================================================================================================

ma.diagflat(_v_, _k\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_twodim_base_impl.py#L333-L388)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.diagflat.html#numpy.ma.diagflat "Link to this definition")

Create a two-dimensional array with the flattened input as a diagonal.

Parameters:

**v**array\_like

Input data, which is flattened and set as the _k_\-th diagonal of the output.

**k**int, optional

Diagonal to set; 0, the default, corresponds to the “main” diagonal, a positive (negative) _k_ giving the number of the diagonal above (below) the main.

Returns:

**out**ndarray

The 2-D output array.

See also

[`diag`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")

MATLAB work-alike for 1-D and 2-D arrays.

[`diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html#numpy.diagonal "numpy.diagonal")

Return specified diagonals.

[`trace`](https://numpy.org/doc/stable/reference/generated/numpy.trace.html#numpy.trace "numpy.trace")

Sum along diagonals.

Notes

The function is applied to both the `_data` and the `_mask`, if any.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.diagflat(\[\[1,2\], \[3,4\]\])
array(\[\[1, 0, 0, 0\],\
       \[0, 2, 0, 0\],\
       \[0, 0, 3, 0\],\
       \[0, 0, 0, 4\]\])

Copy to clipboard

\>>> np.diagflat(\[1,2\], 1)
array(\[\[0, 1, 0\],\
       \[0, 0, 2\],\
       \[0, 0, 0\]\])

Copy to clipboard

Go BackOpen In Tab

On this page