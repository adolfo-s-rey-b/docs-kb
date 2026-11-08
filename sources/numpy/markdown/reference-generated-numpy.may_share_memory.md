[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.may_share_memory.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.may\_share\_memory[#](https://numpy.org/doc/stable/reference/generated/numpy.may_share_memory.html#numpy-may-share-memory "Link to this heading")

========================================================================================================================================================

numpy.may\_share\_memory(_a_, _b_, _/_, _max\_work\=0_)[#](https://numpy.org/doc/stable/reference/generated/numpy.may_share_memory.html#numpy.may_share_memory "Link to this definition")

Determine if two arrays might share memory

A return of True does not necessarily mean that the two arrays share any element. It just means that they _might_.

Only the memory bounds of a and b are checked by default.

Parameters:

**a, b**ndarray

Input arrays

**max\_work**int, optional

Effort to spend on solving the overlap problem. See [`shares_memory`](https://numpy.org/doc/stable/reference/generated/numpy.shares_memory.html#numpy.shares_memory "numpy.shares_memory")
 for details. Default for `may_share_memory` is to do a bounds check.

Returns:

**out**bool

See also

[`shares_memory`](https://numpy.org/doc/stable/reference/generated/numpy.shares_memory.html#numpy.shares_memory "numpy.shares_memory")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.may\_share\_memory(np.array(\[1,2\]), np.array(\[5,8,9\]))
False
\>>> x \= np.zeros(\[3, 4\])
\>>> np.may\_share\_memory(x\[:,0\], x\[:,1\])
True

Copy to clipboard

Go BackOpen In Tab

On this page