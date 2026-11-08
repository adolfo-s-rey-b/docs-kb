[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.fromflex.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.fromflex.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.fromflex.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.fromflex.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.fromflex.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.fromflex.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.fromflex.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.fromflex.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.fromflex.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.fromflex.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.fromflex.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.fromflex.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.fromflex.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.fromflex.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.fromflex.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.fromflex.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.fromflex.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.fromflex.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.fromflex.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.fromflex.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.fromflex.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.fromflex.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.fromflex[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.fromflex.html#numpy-ma-fromflex "Link to this heading")

=======================================================================================================================================

ma.fromflex(_fxarray_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L8749-L8811)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.fromflex.html#numpy.ma.fromflex "Link to this definition")

Build a masked array from a suitable flexible-type array.

The input array has to have a data-type with `_data` and `_mask` fields. This type of array is output by [`MaskedArray.toflex`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.toflex.html#numpy.ma.MaskedArray.toflex "numpy.ma.MaskedArray.toflex")
.

Parameters:

**fxarray**ndarray

The structured input array, containing `_data` and `_mask` fields. If present, other fields are discarded.

Returns:

**result**MaskedArray

The constructed masked array.

See also

[`MaskedArray.toflex`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.toflex.html#numpy.ma.MaskedArray.toflex "numpy.ma.MaskedArray.toflex")

Build a flexible-type array from a masked array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(np.arange(9).reshape(3, 3), mask\=\[0\] + \[1, 0\] \* 4)
\>>> rec \= x.toflex()
\>>> rec
array(\[\[(0, False), (1,  True), (2, False)\],\
       \[(3,  True), (4, False), (5,  True)\],\
       \[(6, False), (7,  True), (8, False)\]\],
      dtype=\[('\_data', '<i8'), ('\_mask', '?')\])
\>>> x2 \= np.ma.fromflex(rec)
\>>> x2
masked\_array(
  data=\[\[0, --, 2\],\
        \[--, 4, --\],\
        \[6, --, 8\]\],
  mask=\[\[False,  True, False\],\
        \[ True, False,  True\],\
        \[False,  True, False\]\],
  fill\_value=999999)

Copy to clipboard

Extra fields can be present in the structured array but are discarded:

\>>> dt \= \[('\_data', '<i4'), ('\_mask', '|b1'), ('field3', '<f4')\]
\>>> rec2 \= np.zeros((2, 2), dtype\=dt)
\>>> rec2
array(\[\[(0, False, 0.), (0, False, 0.)\],\
       \[(0, False, 0.), (0, False, 0.)\]\],
      dtype=\[('\_data', '<i4'), ('\_mask', '?'), ('field3', '<f4')\])
\>>> y \= np.ma.fromflex(rec2)
\>>> y
masked\_array(
  data=\[\[0, 0\],\
        \[0, 0\]\],
  mask=\[\[False, False\],\
        \[False, False\]\],
  fill\_value=np.int64(999999),
  dtype=int32)

Copy to clipboard

Go BackOpen In Tab

On this page