[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.resize.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.resize[#](https://numpy.org/doc/stable/reference/generated/numpy.resize.html#numpy-resize "Link to this heading")

========================================================================================================================

numpy.resize(_a_, _new\_shape_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L1546-L1627)
[#](https://numpy.org/doc/stable/reference/generated/numpy.resize.html#numpy.resize "Link to this definition")

Return a new array with the specified shape.

If the new array is larger than the original array, then the new array is filled with repeated copies of _a_. Note that this behavior is different from a.resize(new\_shape) which fills with zeros instead of repeated copies of _a_.

Parameters:

**a**array\_like

Array to be resized.

**new\_shape**int or tuple of int

Shape of resized array.

Returns:

**reshaped\_array**ndarray

The new array is formed from the data in the old array, repeated if necessary to fill out the required number of elements. The data are repeated iterating over the array in C-order.

See also

[`numpy.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")

Reshape an array without changing the total size.

[`numpy.pad`](https://numpy.org/doc/stable/reference/generated/numpy.pad.html#numpy.pad "numpy.pad")

Enlarge and pad an array.

[`numpy.repeat`](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "numpy.repeat")

Repeat elements of an array.

[`ndarray.resize`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.resize.html#numpy.ndarray.resize "numpy.ndarray.resize")

resize an array in-place.

Notes

When the total size of the array does not change [`reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")
 should be used. In most other cases either indexing (to reduce the size) or padding (to increase the size) may be a more appropriate solution.

Warning: This functionality does **not** consider axes separately, i.e. it does not apply interpolation/extrapolation. It fills the return array with the required number of elements, iterating over _a_ in C-order, disregarding axes (and cycling back from the start if the new shape is larger). This functionality is therefore not suitable to resize images, or data where each axis represents a separate and distinct entity.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[0,1\],\[2,3\]\])
\>>> np.resize(a,(2,3))
array(\[\[0, 1, 2\],\
       \[3, 0, 1\]\])
\>>> np.resize(a,(1,4))
array(\[\[0, 1, 2, 3\]\])
\>>> np.resize(a,(2,4))
array(\[\[0, 1, 2, 3\],\
       \[0, 1, 2, 3\]\])

Copy to clipboard

Go BackOpen In Tab

On this page