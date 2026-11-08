[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.copyto.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.copyto.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.copyto.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.copyto.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.copyto.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.copyto.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.copyto.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.copyto.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.copyto.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.copyto.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.copyto.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.copyto.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.copyto.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.copyto.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.copyto.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.copyto.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.copyto.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.copyto.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.copyto.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.copyto.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.copyto.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.copyto.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.copyto[#](https://numpy.org/doc/stable/reference/generated/numpy.copyto.html#numpy-copyto "Link to this heading")

========================================================================================================================

numpy.copyto(_dst_, _src_, _casting\='same\_kind'_, _where\=True_)[#](https://numpy.org/doc/stable/reference/generated/numpy.copyto.html#numpy.copyto "Link to this definition")

Copies values from one array to another, broadcasting as necessary.

Raises a TypeError if the _casting_ rule is violated, and if [`where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "numpy.where")
 is provided, it selects which elements to copy.

Parameters:

**dst**ndarray

The array into which values are copied.

**src**array\_like

The array from which values are copied.

**casting**{‘no’, ‘equiv’, ‘safe’, ‘same\_kind’, ‘unsafe’}, optional

Controls what kind of data casting may occur when copying.

*   ‘no’ means the data types should not be cast at all.
    
*   ‘equiv’ means only byte-order changes are allowed.
    
*   ‘safe’ means only casts which can preserve values are allowed.
    
*   ‘same\_kind’ means only safe casts or casts within a kind, like float64 to float32, are allowed.
    
*   ‘unsafe’ means any data conversions may be done.
    

**where**array\_like of bool, optional

A boolean array which is broadcasted to match the dimensions of _dst_, and selects elements to copy from _src_ to _dst_ wherever it contains the value True.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> A \= np.array(\[4, 5, 6\])
\>>> B \= \[1, 2, 3\]
\>>> np.copyto(A, B)
\>>> A
array(\[1, 2, 3\])

Copy to clipboard

\>>> A \= np.array(\[\[1, 2, 3\], \[4, 5, 6\]\])
\>>> B \= \[\[4, 5, 6\], \[7, 8, 9\]\]
\>>> np.copyto(A, B)
\>>> A
array(\[\[4, 5, 6\],\
       \[7, 8, 9\]\])

Copy to clipboard

Go BackOpen In Tab

On this page