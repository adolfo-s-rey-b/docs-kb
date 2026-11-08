[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.c_.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.c_.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.c_.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.c_.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.c_.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.c_.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.c_.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.c_.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.c_.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.c_.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.c_.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.c_.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.c_.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.c_.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.c_.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.c_.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.c_.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.c_.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.c_.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.c_.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.c_.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.c\_[#](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy-c "Link to this heading")

============================================================================================================

numpy.c\_ _\= <numpy.lib.\_index\_tricks\_impl.CClass object>_[#](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "Link to this definition")

Translates slice objects to concatenation along the second axis.

This is short-hand for `np.r_['-1,2,0', index expression]`, which is useful because of its common occurrence. In particular, arrays will be stacked along their last axis after being upgraded to at least 2-D with 1’s post-pended to the shape (column vectors made out of 1-D arrays).

See also

[`column_stack`](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")

Stack 1-D arrays as columns into a 2-D array.

[`r_`](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")

For more detailed documentation.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.c\_\[np.array(\[1,2,3\]), np.array(\[4,5,6\])\]
array(\[\[1, 4\],\
       \[2, 5\],\
       \[3, 6\]\])
\>>> np.c\_\[np.array(\[\[1,2,3\]\]), 0, 0, np.array(\[\[4,5,6\]\])\]
array(\[\[1, 2, 3, ..., 4, 5, 6\]\])

Copy to clipboard

Go BackOpen In Tab

On this page