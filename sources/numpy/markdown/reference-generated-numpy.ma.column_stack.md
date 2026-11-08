[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.column_stack.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.column_stack.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.column_stack.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.column_stack.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.column_stack.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.column_stack.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.column_stack.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.column_stack.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.column_stack.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.column_stack.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.column_stack.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.column_stack.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.column_stack.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.column_stack.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.column_stack.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.column_stack.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.column_stack.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.column_stack.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.column_stack.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.column_stack.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.column_stack.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.column_stack.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.column\_stack[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.column_stack.html#numpy-ma-column-stack "Link to this heading")

====================================================================================================================================================

ma.column\_stack(_tup_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_shape_base_impl.py#L607-L648)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.column_stack.html#numpy.ma.column_stack "Link to this definition")

Stack 1-D arrays as columns into a 2-D array.

Take a sequence of 1-D arrays and stack them as columns to make a single 2-D array. 2-D arrays are stacked as-is, just like with [`hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
. 1-D arrays are turned into 2-D columns first.

Parameters:

**tup**sequence of 1-D or 2-D arrays.

Arrays to stack. All of them must have the same first dimension.

Returns:

**stacked**2-D array

The array formed by stacking the given arrays.

See also

[`stack`](https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack "numpy.stack")
, [`hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
, [`vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
, [`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")

Notes

The function is applied to both the `_data` and the `_mask`, if any.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array((1,2,3))
\>>> b \= np.array((4,5,6))
\>>> np.column\_stack((a,b))
array(\[\[1, 4\],\
       \[2, 5\],\
       \[3, 6\]\])

Copy to clipboard

Go BackOpen In Tab

On this page