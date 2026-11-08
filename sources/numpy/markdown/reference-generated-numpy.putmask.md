[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.putmask.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.putmask[#](https://numpy.org/doc/stable/reference/generated/numpy.putmask.html#numpy-putmask "Link to this heading")

===========================================================================================================================

numpy.putmask(_a_, _/_, _mask_, _values_)[#](https://numpy.org/doc/stable/reference/generated/numpy.putmask.html#numpy.putmask "Link to this definition")

Changes elements of an array based on conditional and input values.

Sets `a.flat[n] = values[n]` for each n where `mask.flat[n]==True`.

If _values_ is not the same size as _a_ and _mask_ then it will repeat. This gives behavior different from `a[mask] = values`.

Parameters:

**a**ndarray

Target array.

**mask**array\_like

Boolean mask array. It has to be the same shape as _a_.

**values**array\_like

Values to put into _a_ where _mask_ is True. If _values_ is smaller than _a_ it will be repeated.

See also

[`place`](https://numpy.org/doc/stable/reference/generated/numpy.place.html#numpy.place "numpy.place")
, [`put`](https://numpy.org/doc/stable/reference/generated/numpy.put.html#numpy.put "numpy.put")
, [`take`](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take "numpy.take")
, [`copyto`](https://numpy.org/doc/stable/reference/generated/numpy.copyto.html#numpy.copyto "numpy.copyto")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(6).reshape(2, 3)
\>>> np.putmask(x, x\>2, x\*\*2)
\>>> x
array(\[\[ 0,  1,  2\],\
       \[ 9, 16, 25\]\])

Copy to clipboard

If _values_ is smaller than _a_ it is repeated:

\>>> x \= np.arange(5)
\>>> np.putmask(x, x\>1, \[\-33, \-44\])
\>>> x
array(\[  0,   1, -33, -44, -33\])

Copy to clipboard

Go BackOpen In Tab

On this page