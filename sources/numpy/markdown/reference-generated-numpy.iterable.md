[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.iterable.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.iterable[#](https://numpy.org/doc/stable/reference/generated/numpy.iterable.html#numpy-iterable "Link to this heading")

==============================================================================================================================

numpy.iterable(_y_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L374-L417)
[#](https://numpy.org/doc/stable/reference/generated/numpy.iterable.html#numpy.iterable "Link to this definition")

Check whether or not an object can be iterated over.

Parameters:

**y**object

Input object.

Returns:

**b**bool

Return `True` if the object has an iterator method or is a sequence and `False` otherwise.

Notes

In most cases, the results of `np.iterable(obj)` are consistent with `isinstance(obj, collections.abc.Iterable)`. One notable exception is the treatment of 0-dimensional arrays:

\>>> from collections.abc import Iterable
\>>> a \= np.array(1.0)  \# 0-dimensional numpy array
\>>> isinstance(a, Iterable)
True
\>>> np.iterable(a)
False

Copy to clipboard

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.iterable(\[1, 2, 3\])
True
\>>> np.iterable(2)
False

Copy to clipboard

Go BackOpen In Tab

On this page