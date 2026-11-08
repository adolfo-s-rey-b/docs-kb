[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matlib.randn.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matlib.randn.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matlib.randn.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matlib.randn.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matlib.randn.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matlib.randn.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matlib.randn.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matlib.randn.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matlib.randn.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matlib.randn.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matlib.randn.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matlib.randn.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matlib.randn.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matlib.randn.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matlib.randn.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matlib.randn.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matlib.randn.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matlib.randn.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matlib.randn.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matlib.randn.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matlib.randn.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matlib.randn.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matlib.randn[#](https://numpy.org/doc/stable/reference/generated/numpy.matlib.randn.html#numpy-matlib-randn "Link to this heading")

==========================================================================================================================================

matlib.randn(_\*args_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matlib.py#L279-L330)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matlib.randn.html#numpy.matlib.randn "Link to this definition")

Return a random matrix with data from the “standard normal” distribution.

[`randn`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.randn.html#numpy.matlib.randn "numpy.matlib.randn")
 generates a matrix filled with random floats sampled from a univariate “normal” (Gaussian) distribution of mean 0 and variance 1.

Parameters:

**\*args**Arguments

Shape of the output. If given as N integers, each integer specifies the size of one dimension. If given as a tuple, this tuple gives the complete shape.

Returns:

**Z**matrix of floats

A matrix of floating-point samples drawn from the standard normal distribution.

See also

[`rand`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.rand.html#numpy.matlib.rand "numpy.matlib.rand")
, [`numpy.random.RandomState.randn`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.randn.html#numpy.random.RandomState.randn "numpy.random.RandomState.randn")

Notes

For random samples from the normal distribution with mean `mu` and standard deviation `sigma`, use:

sigma \* np.matlib.randn(...) + mu

Copy to clipboard

Examples

Try it in your browser!

\>>> np.random.seed(123)
\>>> import numpy.matlib
\>>> np.matlib.randn(1)
matrix(\[\[-1.0856306\]\])
\>>> np.matlib.randn(1, 2, 3)
matrix(\[\[ 0.99734545,  0.2829785 , -1.50629471\],\
        \[-0.57860025,  1.65143654, -2.42667924\]\])

Copy to clipboard

Two-by-four matrix of samples from the normal distribution with mean 3 and standard deviation 2.5:

\>>> 2.5 \* np.matlib.randn((2, 4)) + 3
matrix(\[\[1.92771843, 6.16484065, 0.83314899, 1.30278462\],\
        \[2.76322758, 6.72847407, 1.40274501, 1.8900451 \]\])

Copy to clipboard

Go BackOpen In Tab

On this page