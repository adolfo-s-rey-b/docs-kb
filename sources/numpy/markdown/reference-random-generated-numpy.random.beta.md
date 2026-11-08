[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.beta.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.beta.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.beta.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.beta.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.beta.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.beta.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.beta.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.beta.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.beta.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.beta.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.beta.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.beta.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.beta.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.beta.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.beta.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.beta.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.beta.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.beta.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.beta.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.beta.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.beta.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.beta.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.beta[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.beta.html#numpy-random-beta "Link to this heading")

==============================================================================================================================================

random.beta(_a_, _b_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.beta.html#numpy.random.beta "Link to this definition")

Draw samples from a Beta distribution.

The Beta distribution is a special case of the Dirichlet distribution, and is related to the Gamma distribution. It has the probability distribution function

\\\[f(x; a,b) = \\frac{1}{B(\\alpha, \\beta)} x^{\\alpha - 1} (1 - x)^{\\beta - 1},\\\]

where the normalization, B, is the beta function,

\\\[B(\\alpha, \\beta) = \\int\_0^1 t^{\\alpha - 1} (1 - t)^{\\beta - 1} dt.\\\]

It is often seen in Bayesian inference and order statistics.

Note

New code should use the [`beta`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.beta.html#numpy.random.Generator.beta "numpy.random.Generator.beta")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**a**float or array\_like of floats

Alpha, positive (>0).

**b**float or array\_like of floats

Beta, positive (>0).

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `a` and `b` are both scalars. Otherwise, `np.broadcast(a, b).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized beta distribution.

See also

[`random.Generator.beta`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.beta.html#numpy.random.Generator.beta "numpy.random.Generator.beta")

which should be used for new code.

On this page