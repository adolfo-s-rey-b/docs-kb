[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.dirichlet.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.dirichlet.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.dirichlet.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.dirichlet[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.dirichlet.html#numpy-random-randomstate-dirichlet "Link to this heading")

=================================================================================================================================================================================================

method

random.RandomState.dirichlet(_alpha_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.dirichlet.html#numpy.random.RandomState.dirichlet "Link to this definition")

Draw samples from the Dirichlet distribution.

Draw [`size`](https://numpy.org/doc/stable/reference/generated/numpy.size.html#numpy.size "numpy.size")
 samples of dimension k from a Dirichlet distribution. A Dirichlet-distributed random variable can be seen as a multivariate generalization of a Beta distribution. The Dirichlet distribution is a conjugate prior of a multinomial distribution in Bayesian inference.

Note

New code should use the [`dirichlet`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.dirichlet.html#numpy.random.Generator.dirichlet "numpy.random.Generator.dirichlet")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**alpha**sequence of floats, length k

Parameter of the distribution (length `k` for sample of length `k`).

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n)`, then `m * n * k` samples are drawn. Default is None, in which case a vector of length `k` is returned.

Returns:

**samples**ndarray,

The drawn samples, of shape `(size, k)`.

Raises:

ValueError

If any value in `alpha` is less than or equal to zero

See also

[`random.Generator.dirichlet`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.dirichlet.html#numpy.random.Generator.dirichlet "numpy.random.Generator.dirichlet")

which should be used for new code.

Notes

The Dirichlet distribution is a distribution over vectors \\(x\\) that fulfil the conditions \\(x\_i>0\\) and \\(\\sum\_{i=1}^k x\_i = 1\\).

The probability density function \\(p\\) of a Dirichlet-distributed random vector \\(X\\) is proportional to

\\\[p(x) \\propto \\prod\_{i=1}^{k}{x^{\\alpha\_i-1}\_i},\\\]

where \\(\\alpha\\) is a vector containing the positive concentration parameters.

The method uses the following property for computation: let \\(Y\\) be a random vector which has components that follow a standard gamma distribution, then \\(X = \\frac{1}{\\sum\_{i=1}^k{Y\_i}} Y\\) is Dirichlet-distributed

References

\[1\]

David McKay, “Information Theory, Inference and Learning Algorithms,” chapter 23, [https://www.inference.org.uk/mackay/itila/](https://www.inference.org.uk/mackay/itila/)

\[2\]

Wikipedia, “Dirichlet distribution”, [https://en.wikipedia.org/wiki/Dirichlet\_distribution](https://en.wikipedia.org/wiki/Dirichlet_distribution)

Examples

Try it in your browser!

Taking an example cited in Wikipedia, this distribution can be used if one wanted to cut strings (each of initial length 1.0) into K pieces with different lengths, where each piece had, on average, a designated average length, but allowing some variation in the relative sizes of the pieces.

\>>> s \= np.random.dirichlet((10, 5, 3), 20).transpose()

Copy to clipboard

\>>> import matplotlib.pyplot as plt
\>>> plt.barh(range(20), s\[0\])
\>>> plt.barh(range(20), s\[1\], left\=s\[0\], color\='g')
\>>> plt.barh(range(20), s\[2\], left\=s\[0\]+s\[1\], color\='r')
\>>> plt.title("Lengths of Strings")

Copy to clipboard

![../../../_images/numpy-random-RandomState-dirichlet-1.png](https://numpy.org/doc/stable/_images/numpy-random-RandomState-dirichlet-1.png)

Go BackOpen In Tab

On this page