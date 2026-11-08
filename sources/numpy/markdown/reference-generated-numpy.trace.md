[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.trace.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.trace.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.trace.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.trace.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.trace.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.trace.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.trace.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.trace.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.trace.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.trace.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.trace.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.trace.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.trace.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.trace.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.trace.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.trace.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.trace.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.trace.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.trace.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.trace.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.trace.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.trace.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.trace[#](https://numpy.org/doc/stable/reference/generated/numpy.trace.html#numpy-trace "Link to this heading")

=====================================================================================================================

numpy.trace(_a_, _offset\=0_, _axis1\=0_, _axis2\=1_, _dtype\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L1844-L1910)
[#](https://numpy.org/doc/stable/reference/generated/numpy.trace.html#numpy.trace "Link to this definition")

Return the sum along diagonals of the array.

If _a_ is 2-D, the sum along its diagonal with the given offset is returned, i.e., the sum of elements `a[i,i+offset]` for all i.

If _a_ has more than two dimensions, then the axes specified by axis1 and axis2 are used to determine the 2-D sub-arrays whose traces are returned. The shape of the resulting array is the same as that of _a_ with _axis1_ and _axis2_ removed.

Parameters:

**a**array\_like

Input array, from which the diagonals are taken.

**offset**int, optional

Offset of the diagonal from the main diagonal. Can be both positive and negative. Defaults to 0.

**axis1, axis2**int, optional

Axes to be used as the first and second axis of the 2-D sub-arrays from which the diagonals should be taken. Defaults are the first two axes of _a_.

**dtype**dtype, optional

Determines the data-type of the returned array and of the accumulator where the elements are summed. If dtype has the value None and _a_ is of integer type of precision less than the default integer precision, then the default integer precision is used. Otherwise, the precision is the same as that of _a_.

**out**ndarray, optional

Array into which the output is placed. Its type is preserved and it must be of the right shape to hold the output.

Returns:

**sum\_along\_diagonals**ndarray

If _a_ is 2-D, the sum along the diagonal is returned. If _a_ has larger dimensions, then an array of sums along diagonals is returned.

See also

[`diag`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")
, [`diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html#numpy.diagonal "numpy.diagonal")
, [`diagflat`](https://numpy.org/doc/stable/reference/generated/numpy.diagflat.html#numpy.diagflat "numpy.diagflat")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.trace(np.eye(3))
3.0
\>>> a \= np.arange(8).reshape((2,2,2))
\>>> np.trace(a)
array(\[6, 8\])

Copy to clipboard

\>>> a \= np.arange(24).reshape((2,2,2,3))
\>>> np.trace(a).shape
(2, 3)

Copy to clipboard

Go BackOpen In Tab

On this page