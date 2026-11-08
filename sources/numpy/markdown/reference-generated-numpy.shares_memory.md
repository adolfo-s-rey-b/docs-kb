[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.shares_memory.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.shares_memory.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.shares_memory.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.shares_memory.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.shares_memory.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.shares_memory.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.shares_memory.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.shares_memory.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.shares_memory.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.shares_memory.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.shares_memory.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.shares_memory.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.shares_memory.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.shares_memory.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.shares_memory.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.shares_memory.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.shares_memory.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.shares_memory.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.shares_memory.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.shares_memory.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.shares_memory.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.shares_memory.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.shares\_memory[#](https://numpy.org/doc/stable/reference/generated/numpy.shares_memory.html#numpy-shares-memory "Link to this heading")

==============================================================================================================================================

numpy.shares\_memory(_a_, _b_, _/_, _max\_work\=\-1_)[#](https://numpy.org/doc/stable/reference/generated/numpy.shares_memory.html#numpy.shares_memory "Link to this definition")

Determine if two arrays share memory.

Warning

This function can be exponentially slow for some inputs, unless _max\_work_ is set to zero or a positive integer. If in doubt, use [`numpy.may_share_memory`](https://numpy.org/doc/stable/reference/generated/numpy.may_share_memory.html#numpy.may_share_memory "numpy.may_share_memory")
 instead.

Parameters:

**a, b**ndarray

Input arrays

**max\_work**int, optional

Effort to spend on solving the overlap problem (maximum number of candidate solutions to consider). The following special values are recognized:

max\_work=-1 (default)

The problem is solved exactly. In this case, the function returns True only if there is an element shared between the arrays. Finding the exact solution may take extremely long in some cases.

max\_work=0

Only the memory bounds of a and b are checked. This is equivalent to using `may_share_memory()`.

Returns:

**out**bool

Raises:

numpy.exceptions.TooHardError

Exceeded max\_work.

See also

[`may_share_memory`](https://numpy.org/doc/stable/reference/generated/numpy.may_share_memory.html#numpy.may_share_memory "numpy.may_share_memory")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[1, 2, 3, 4\])
\>>> np.shares\_memory(x, np.array(\[5, 6, 7\]))
False
\>>> np.shares\_memory(x\[::2\], x)
True
\>>> np.shares\_memory(x\[::2\], x\[1::2\])
False

Copy to clipboard

Checking whether two arrays share memory is NP-complete, and runtime may increase exponentially in the number of dimensions. Hence, _max\_work_ should generally be set to a finite number, as it is possible to construct examples that take extremely long to run:

\>>> from numpy.lib.stride\_tricks import as\_strided
\>>> x \= np.zeros(\[192163377\], dtype\=np.int8)
\>>> x1 \= as\_strided(
...     x, strides\=(36674, 61119, 85569), shape\=(1049, 1049, 1049))
\>>> x2 \= as\_strided(
...     x\[64023025:\], strides\=(12223, 12224, 1), shape\=(1049, 1049, 1))
\>>> np.shares\_memory(x1, x2, max\_work\=1000)
Traceback (most recent call last):
...
numpy.exceptions.TooHardError: Exceeded max\_work

Copy to clipboard

Running `np.shares_memory(x1, x2)` without _max\_work_ set takes around 1 minute for this case. It is possible to find problems that take still significantly longer.

Go BackOpen In Tab

On this page