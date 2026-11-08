[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_power.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.matrix_power.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_power.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.matrix_power.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.matrix_power.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.matrix_power.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.matrix_power.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.matrix_power.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.matrix_power.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.matrix_power.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.matrix_power.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.matrix_power.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.matrix_power.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.matrix_power.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.matrix_power.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.matrix_power.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.matrix_power.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.matrix_power.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.matrix_power.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.matrix_power.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.matrix_power.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.matrix_power.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.matrix\_power[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_power.html#numpy-linalg-matrix-power "Link to this heading")

================================================================================================================================================================

linalg.matrix\_power(_a_, _n_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L667-L780)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_power.html#numpy.linalg.matrix_power "Link to this definition")

Raise a square matrix to the (integer) power _n_.

For positive integers _n_, the power is computed by repeated matrix squarings and matrix multiplications. If `n == 0`, the identity matrix of the same shape as M is returned. If `n < 0`, the inverse is computed and then raised to the `abs(n)`.

Note

Stacks of object matrices are not currently supported.

Parameters:

**a**(…, M, M) array\_like

Matrix to be “powered”.

**n**int

The exponent can be any integer or long integer, positive, negative, or zero.

Returns:

**a\*\*n**(…, M, M) ndarray or matrix object

The return value is the same shape and type as _M_; if the exponent is positive or zero then the type of the elements is the same as those of _M_. If the exponent is negative the elements are floating-point.

Raises:

LinAlgError

For matrices that are not square or that (for negative powers) cannot be inverted numerically.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.linalg import matrix\_power
\>>> i \= np.array(\[\[0, 1\], \[\-1, 0\]\]) \# matrix equiv. of the imaginary unit
\>>> matrix\_power(i, 3) \# should = -i
array(\[\[ 0, -1\],\
       \[ 1,  0\]\])
\>>> matrix\_power(i, 0)
array(\[\[1, 0\],\
       \[0, 1\]\])
\>>> matrix\_power(i, \-3) \# should = 1/(-i) = i, but w/ f.p. elements
array(\[\[ 0.,  1.\],\
       \[-1.,  0.\]\])

Copy to clipboard

Somewhat more sophisticated example

\>>> q \= np.zeros((4, 4))
\>>> q\[0:2, 0:2\] \= \-i
\>>> q\[2:4, 2:4\] \= i
\>>> q \# one of the three quaternion units not equal to 1
array(\[\[ 0., -1.,  0.,  0.\],\
       \[ 1.,  0.,  0.,  0.\],\
       \[ 0.,  0.,  0.,  1.\],\
       \[ 0.,  0., -1.,  0.\]\])
\>>> matrix\_power(q, 2) \# = -np.eye(4)
array(\[\[-1.,  0.,  0.,  0.\],\
       \[ 0., -1.,  0.,  0.\],\
       \[ 0.,  0., -1.,  0.\],\
       \[ 0.,  0.,  0., -1.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page