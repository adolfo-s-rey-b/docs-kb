[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.apply_over_axes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.apply_over_axes.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.apply_over_axes.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.apply_over_axes.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.apply_over_axes.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.apply_over_axes.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.apply_over_axes.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.apply_over_axes.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.apply_over_axes.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.apply_over_axes.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.apply_over_axes.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.apply_over_axes.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.apply_over_axes.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.apply_over_axes.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.apply_over_axes.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.apply_over_axes.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.apply_over_axes.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.apply_over_axes.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.apply_over_axes.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.apply_over_axes.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.apply_over_axes.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.apply_over_axes.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.apply\_over\_axes[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.apply_over_axes.html#numpy-ma-apply-over-axes "Link to this heading")

==============================================================================================================================================================

ma.apply\_over\_axes(_func_, _a_, _axes_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L435-L457)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.apply_over_axes.html#numpy.ma.apply_over_axes "Link to this definition")

Apply a function repeatedly over multiple axes.

_func_ is called as _res = func(a, axis)_, where _axis_ is the first element of _axes_. The result _res_ of the function call must have either the same dimensions as _a_ or one less dimension. If _res_ has one less dimension than _a_, a dimension is inserted before _axis_. The call to _func_ is then repeated for each axis in _axes_, with _res_ as the first argument.

Parameters:

**func**function

This function must take two arguments, _func(a, axis)_.

**a**array\_like

Input array.

**axes**array\_like

Axes over which _func_ is applied; the elements must be integers.

Returns:

**apply\_over\_axis**ndarray

The output array. The number of dimensions is the same as _a_, but the shape can be different. This depends on whether _func_ changes the shape of its output with respect to its input.

See also

[`apply_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.apply_along_axis.html#numpy.apply_along_axis "numpy.apply_along_axis")

Apply a function to 1-D slices of an array along the given axis.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.ma.arange(24).reshape(2,3,4)
\>>> a\[:,0,1\] \= np.ma.masked
\>>> a\[:,1,:\] \= np.ma.masked
\>>> a
masked\_array(
  data=\[\[\[0, --, 2, 3\],\
         \[--, --, --, --\],\
         \[8, 9, 10, 11\]\],\
        \[\[12, --, 14, 15\],\
         \[--, --, --, --\],\
         \[20, 21, 22, 23\]\]\],
  mask=\[\[\[False,  True, False, False\],\
         \[ True,  True,  True,  True\],\
         \[False, False, False, False\]\],\
        \[\[False,  True, False, False\],\
         \[ True,  True,  True,  True\],\
         \[False, False, False, False\]\]\],
  fill\_value=999999)
\>>> np.ma.apply\_over\_axes(np.ma.sum, a, \[0,2\])
masked\_array(
  data=\[\[\[46\],\
         \[--\],\
         \[124\]\]\],
  mask=\[\[\[False\],\
         \[ True\],\
         \[False\]\]\],
  fill\_value=999999)

Copy to clipboard

Tuple axis arguments to ufuncs are equivalent:

\>>> np.ma.sum(a, axis\=(0,2)).reshape((1,\-1,1))
masked\_array(
  data=\[\[\[46\],\
         \[--\],\
         \[124\]\]\],
  mask=\[\[\[False\],\
         \[ True\],\
         \[False\]\]\],
  fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page