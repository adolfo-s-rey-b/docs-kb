[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.exponential.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.exponential.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.exponential.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.exponential.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.exponential.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.exponential.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.exponential.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.exponential.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.exponential.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.exponential.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.exponential.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.exponential.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.exponential.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.exponential.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.exponential.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.exponential.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.exponential.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.exponential.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.exponential.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.exponential.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.exponential[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html#numpy-random-exponential "Link to this heading")

===================================================================================================================================================================

random.exponential(_scale\=1.0_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html#numpy.random.exponential "Link to this definition")

Draw samples from an exponential distribution.

Its probability density function is

\\\[f(x; \\frac{1}{\\beta}) = \\frac{1}{\\beta} \\exp(-\\frac{x}{\\beta}),\\\]

for `x > 0` and 0 elsewhere. \\(\\beta\\) is the scale parameter, which is the inverse of the rate parameter \\(\\lambda = 1/\\beta\\). The rate parameter is an alternative, widely used parameterization of the exponential distribution [\[3\]](https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html#r3cbd6af2d0d3-3)
.

The exponential distribution is a continuous analogue of the geometric distribution. It describes many common situations, such as the size of raindrops measured over many rainstorms [\[1\]](https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html#r3cbd6af2d0d3-1)
, or the time between page requests to Wikipedia [\[2\]](https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html#r3cbd6af2d0d3-2)
.

Note

New code should use the [`exponential`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.exponential.html#numpy.random.Generator.exponential "numpy.random.Generator.exponential")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**scale**float or array\_like of floats

The scale parameter, \\(\\beta = 1/\\lambda\\). Must be non-negative.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `scale` is a scalar. Otherwise, `np.array(scale).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized exponential distribution.

See also

[`random.Generator.exponential`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.exponential.html#numpy.random.Generator.exponential "numpy.random.Generator.exponential")

which should be used for new code.

References

\[[1](https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html#id2)\
\]

Peyton Z. Peebles Jr., “Probability, Random Variables and Random Signal Principles”, 4th ed, 2001, p. 57.

\[[2](https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html#id3)\
\]

Wikipedia, “Poisson process”, [https://en.wikipedia.org/wiki/Poisson\_process](https://en.wikipedia.org/wiki/Poisson_process)

\[[3](https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html#id1)\
\]

Wikipedia, “Exponential distribution”, [https://en.wikipedia.org/wiki/Exponential\_distribution](https://en.wikipedia.org/wiki/Exponential_distribution)

Examples

Try it in your browser!

A real world example: Assume a company has 10000 customer support agents and the average time between customer calls is 4 minutes.

\>>> n \= 10000
\>>> time\_between\_calls \= np.random.default\_rng().exponential(scale\=4, size\=n)

Copy to clipboard

What is the probability that a customer will call in the next 4 to 5 minutes?

\>>> x \= ((time\_between\_calls < 5).sum())/n
\>>> y \= ((time\_between\_calls < 4).sum())/n
\>>> x\-y
0.08 # may vary

Copy to clipboard

Go BackOpen In Tab

On this page