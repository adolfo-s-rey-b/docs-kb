[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.H.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matrix.H.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matrix.H.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matrix.H.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matrix.H.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matrix.H.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matrix.H.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matrix.H.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matrix.H.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matrix.H.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matrix.H.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matrix.H.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matrix.H.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matrix.H.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matrix.H.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matrix.H.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matrix.H.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matrix.H.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matrix.H.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matrix.H.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matrix.H.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matrix.H.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.H[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.H.html#numpy-matrix-h "Link to this heading")

==============================================================================================================================

property

_property_ matrix.H[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.H.html#numpy.matrix.H "Link to this definition")

Returns the (complex) conjugate transpose of _self_.

Equivalent to `np.transpose(self)` if _self_ is real-valued.

Parameters:

**None**

Returns:

**ret**matrix object

complex conjugate transpose of _self_

Examples

Try it in your browser!

\>>> x \= np.matrix(np.arange(12).reshape((3,4)))
\>>> z \= x \- 1j\*x; z
matrix(\[\[  0. +0.j,   1. -1.j,   2. -2.j,   3. -3.j\],\
        \[  4. -4.j,   5. -5.j,   6. -6.j,   7. -7.j\],\
        \[  8. -8.j,   9. -9.j,  10.-10.j,  11.-11.j\]\])
\>>> z.getH()
matrix(\[\[ 0. -0.j,  4. +4.j,  8. +8.j\],\
        \[ 1. +1.j,  5. +5.j,  9. +9.j\],\
        \[ 2. +2.j,  6. +6.j, 10.+10.j\],\
        \[ 3. +3.j,  7. +7.j, 11.+11.j\]\])

Copy to clipboard

Go BackOpen In Tab

On this page