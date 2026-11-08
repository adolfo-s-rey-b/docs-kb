[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.chisquare.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.chisquare.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.chisquare.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.chisquare.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.chisquare.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.chisquare.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.chisquare.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.chisquare.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.chisquare.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.chisquare.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.chisquare.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.chisquare.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.chisquare.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.chisquare.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.chisquare.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.chisquare.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.chisquare.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.chisquare.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.chisquare.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.chisquare.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.chisquare.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.chisquare.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.chisquare[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.chisquare.html#numpy-random-chisquare "Link to this heading")

=============================================================================================================================================================

random.chisquare(_df_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.chisquare.html#numpy.random.chisquare "Link to this definition")

Draw samples from a chi-square distribution.

When _df_ independent random variables, each with standard normal distributions (mean 0, variance 1), are squared and summed, the resulting distribution is chi-square (see Notes). This distribution is often used in hypothesis testing.

Note

New code should use the [`chisquare`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.chisquare.html#numpy.random.Generator.chisquare "numpy.random.Generator.chisquare")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**df**float or array\_like of floats

Number of degrees of freedom, must be > 0.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `df` is a scalar. Otherwise, `np.array(df).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized chi-square distribution.

Raises:

ValueError

When _df_ <= 0 or when an inappropriate [`size`](https://numpy.org/doc/stable/reference/generated/numpy.size.html#numpy.size "numpy.size")
 (e.g. `size=-1`) is given.

See also

[`random.Generator.chisquare`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.chisquare.html#numpy.random.Generator.chisquare "numpy.random.Generator.chisquare")

which should be used for new code.

Notes

The variable obtained by summing the squares of _df_ independent, standard normally distributed random variables:

\\\[Q = \\sum\_{i=1}^{\\mathtt{df}} X^2\_i\\\]

is chi-square distributed, denoted

\\\[Q \\sim \\chi^2\_k.\\\]

The probability density function of the chi-squared distribution is

\\\[p(x) = \\frac{(1/2)^{k/2}}{\\Gamma(k/2)} x^{k/2 - 1} e^{-x/2},\\\]

where \\(\\Gamma\\) is the gamma function,

\\\[\\Gamma(x) = \\int\_0^{-\\infty} t^{x - 1} e^{-t} dt.\\\]

References

\[1\]

NIST “Engineering Statistics Handbook” [https://www.itl.nist.gov/div898/handbook/eda/section3/eda3666.htm](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3666.htm)

Examples

Try it in your browser!

\>>> np.random.chisquare(2,4)
array(\[ 1.89920014,  9.00867716,  3.13710533,  5.62318272\]) # random

Copy to clipboard

Go BackOpen In Tab

On this page