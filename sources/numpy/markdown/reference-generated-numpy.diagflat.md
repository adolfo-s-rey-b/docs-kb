[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.diagflat.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.diagflat[#](https://numpy.org/doc/stable/reference/generated/numpy.diagflat.html#numpy-diagflat "Link to this heading")

==============================================================================================================================

numpy.diagflat(_v_, _k\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_twodim_base_impl.py#L333-L388)
[#](https://numpy.org/doc/stable/reference/generated/numpy.diagflat.html#numpy.diagflat "Link to this definition")

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