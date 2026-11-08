[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.randn.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.randn.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.randn.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.randn.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.randn.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.randn.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.randn.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.randn.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.randn.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.randn.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.randn.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.randn.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.randn.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.randn.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.randn.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.randn.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.randn.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.randn.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.randn.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.randn.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.randn[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy-random-randn "Link to this heading")

=================================================================================================================================================

random.randn(_d0_, _d1_, _..._, _dn_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "Link to this definition")

Return a sample (or samples) from the “standard normal” distribution.

Note

This is a convenience function for users porting code from Matlab, and wraps [`standard_normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_normal.html#numpy.random.standard_normal "numpy.random.standard_normal")
. That function takes a tuple to specify the size of the output, which is consistent with other NumPy functions like [`numpy.zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
 and [`numpy.ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
.

Note

New code should use the [`standard_normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html#numpy.random.Generator.standard_normal "numpy.random.Generator.standard_normal")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

If positive int\_like arguments are provided, [`randn`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
 generates an array of shape `(d0, d1, ..., dn)`, filled with random floats sampled from a univariate “normal” (Gaussian) distribution of mean 0 and variance 1. A single float randomly sampled from the distribution is returned if no argument is provided.

Parameters:

**d0, d1, …, dn**int, optional

The dimensions of the returned array, must be non-negative. If no argument is given a single Python float is returned.

Returns:

**Z**ndarray or float

A `(d0, d1, ..., dn)`\-shaped array of floating-point samples from the standard normal distribution, or a single such float if no parameters were supplied.

See also

[`standard_normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_normal.html#numpy.random.standard_normal "numpy.random.standard_normal")

Similar, but takes a tuple as its argument.

[`normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")

Also accepts mu and sigma arguments.

[`random.Generator.standard_normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html#numpy.random.Generator.standard_normal "numpy.random.Generator.standard_normal")

which should be used for new code.

Notes

For random samples from the normal distribution with mean `mu` and standard deviation `sigma`, use:

sigma \* np.random.randn(...) + mu

Copy to clipboard

Examples

Try it in your browser!

\>>> np.random.randn()
2.1923875335537315  # random

Copy to clipboard

Two-by-four array of samples from the normal distribution with mean 3 and standard deviation 2.5:

\>>> 3 + 2.5 \* np.random.randn(2, 4)
array(\[\[-4.49401501,  4.00950034, -1.81814867,  7.29718677\],   # random\
       \[ 0.39924804,  4.68456316,  4.99394529,  4.84057254\]\])  # random

Copy to clipboard

Go BackOpen In Tab

On this page