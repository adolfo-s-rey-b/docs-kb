[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.s_.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.s_.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.s_.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.s_.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.s_.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.s_.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.s_.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.s_.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.s_.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.s_.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.s_.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.s_.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.s_.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.s_.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.s_.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.s_.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.s_.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.s_.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.s_.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.s_.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.s_.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.s_.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.s\_[#](https://numpy.org/doc/stable/reference/generated/numpy.s_.html#numpy-s "Link to this heading")

============================================================================================================

numpy.s\_ _\= <numpy.lib.\_index\_tricks\_impl.IndexExpression object>_[#](https://numpy.org/doc/stable/reference/generated/numpy.s_.html#numpy.s_ "Link to this definition")

A nicer way to build up index tuples for arrays.

Note

Use one of the two predefined instances `index_exp` or [`s_`](https://numpy.org/doc/stable/reference/generated/numpy.s_.html#numpy.s_ "numpy.s_")
 rather than directly using _IndexExpression_.

For any index combination, including slicing and axis insertion, `a[indices]` is the same as `a[np.index_exp[indices]]` for any array _a_. However, `np.index_exp[indices]` can be used anywhere in Python code and returns a tuple of slice objects that can be used in the construction of complex index expressions.

Parameters:

**maketuple**bool

If True, always returns a tuple.

See also

[`s_`](https://numpy.org/doc/stable/reference/generated/numpy.s_.html#numpy.s_ "numpy.s_")

Predefined instance without tuple conversion: _s\_ = IndexExpression(maketuple=False)_. The `index_exp` is another predefined instance that always returns a tuple: _index\_exp = IndexExpression(maketuple=True)_.

Notes

You can do all this with [`slice`](https://docs.python.org/3/library/functions.html#slice "(in Python v3.14)")
 plus a few special objects, but there’s a lot to remember and this version is simpler because it uses the standard array indexing syntax.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.s\_\[2::2\]
slice(2, None, 2)
\>>> np.index\_exp\[2::2\]
(slice(2, None, 2),)

Copy to clipboard

\>>> np.array(\[0, 1, 2, 3, 4\])\[np.s\_\[2::2\]\]
array(\[2, 4\])

Copy to clipboard

Go BackOpen In Tab

On this page