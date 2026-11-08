[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.gcd.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.gcd.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.gcd.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.gcd.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.gcd.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.gcd.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.gcd.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.gcd.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.gcd.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.gcd.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.gcd.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.gcd.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.gcd.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.gcd.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.gcd.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.gcd.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.gcd.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.gcd.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.gcd.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.gcd.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.gcd.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.gcd.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.gcd[#](https://numpy.org/doc/stable/reference/generated/numpy.gcd.html#numpy-gcd "Link to this heading")

===============================================================================================================

numpy.gcd(_x1_, _x2_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'gcd'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.gcd.html#numpy.gcd "Link to this definition")

Returns the greatest common divisor of `|x1|` and `|x2|`

Parameters:

**x1, x2**array\_like, int

Arrays of values. If `x1.shape != x2.shape`, they must be broadcastable to a common shape (which becomes the shape of the output).

Returns:

**y**ndarray or scalar

The greatest common divisor of the absolute value of the inputs This is a scalar if both _x1_ and _x2_ are scalars.

See also

[`lcm`](https://numpy.org/doc/stable/reference/generated/numpy.lcm.html#numpy.lcm "numpy.lcm")

The lowest common multiple

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.gcd(12, 20)
4
\>>> np.gcd.reduce(\[15, 25, 35\])
5
\>>> np.gcd(np.arange(6), 20)
array(\[20,  1,  2,  1,  4,  5\])

Copy to clipboard

Go BackOpen In Tab

On this page