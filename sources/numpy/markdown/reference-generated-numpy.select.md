[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.select.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.select[#](https://numpy.org/doc/stable/reference/generated/numpy.select.html#numpy-select "Link to this heading")

========================================================================================================================

numpy.select(_condlist_, _choicelist_, _default\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L823-L928)
[#](https://numpy.org/doc/stable/reference/generated/numpy.select.html#numpy.select "Link to this definition")

Return an array drawn from elements in choicelist, depending on conditions.

Parameters:

**condlist**list of bool ndarrays

The list of conditions which determine from which array in _choicelist_ the output elements are taken. When multiple conditions are satisfied, the first one encountered in _condlist_ is used.

**choicelist**list of ndarrays

The list of arrays from which the output elements are taken. It has to be of the same length as _condlist_.

**default**array\_like, optional

The element inserted in _output_ when all conditions evaluate to False.

Returns:

**output**ndarray

The output at position m is the m-th element of the array in _choicelist_ where the m-th element of the corresponding array in _condlist_ is True.

See also

[`where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "numpy.where")

Return elements from one of two arrays depending on condition.

[`take`](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take "numpy.take")
, [`choose`](https://numpy.org/doc/stable/reference/generated/numpy.choose.html#numpy.choose "numpy.choose")
, [`compress`](https://numpy.org/doc/stable/reference/generated/numpy.compress.html#numpy.compress "numpy.compress")
, [`diag`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")
, [`diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html#numpy.diagonal "numpy.diagonal")

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Beginning with an array of integers from 0 to 5 (inclusive), elements less than `3` are negated, elements greater than `3` are squared, and elements not meeting either of these conditions (exactly `3`) are replaced with a _default_ value of `42`.

\>>> x \= np.arange(6)
\>>> condlist \= \[x<3, x\>3\]
\>>> choicelist \= \[\-x, x\*\*2\]
\>>> np.select(condlist, choicelist, 42)
array(\[ 0,  -1,  -2, 42, 16, 25\])

Copy to clipboard

When multiple conditions are satisfied, the first one encountered in _condlist_ is used.

\>>> condlist \= \[x<=4, x\>3\]
\>>> choicelist \= \[x, x\*\*2\]
\>>> np.select(condlist, choicelist, 55)
array(\[ 0,  1,  2,  3,  4, 25\])

Copy to clipboard

Go BackOpen In Tab

On this page