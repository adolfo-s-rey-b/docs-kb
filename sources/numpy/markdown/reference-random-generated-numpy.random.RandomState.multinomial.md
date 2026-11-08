[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.multinomial.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.multinomial.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.multinomial.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.multinomial.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.multinomial.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.multinomial.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.multinomial.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.multinomial.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.multinomial.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.multinomial.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.multinomial.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.multinomial.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.multinomial.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.multinomial.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.multinomial.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.multinomial.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.multinomial.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.multinomial.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.multinomial.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.multinomial.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.multinomial.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.multinomial.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.multinomial[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.multinomial.html#numpy-random-randomstate-multinomial "Link to this heading")

=======================================================================================================================================================================================================

method

random.RandomState.multinomial(_n_, _pvals_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.multinomial.html#numpy.random.RandomState.multinomial "Link to this definition")

Draw samples from a multinomial distribution.

The multinomial distribution is a multivariate generalization of the binomial distribution. Take an experiment with one of `p` possible outcomes. An example of such an experiment is throwing a dice, where the outcome can be 1 through 6. Each sample drawn from the distribution represents _n_ such experiments. Its values, `X_i = [X_0, X_1, ..., X_p]`, represent the number of times the outcome was `i`.

Note

New code should use the [`multinomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multinomial.html#numpy.random.Generator.multinomial "numpy.random.Generator.multinomial")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Warning

This function defaults to the C-long dtype, which is 32bit on windows and otherwise 64bit on 64bit platforms (and 32bit on 32bit ones). Since NumPy 2.0, NumPy’s default integer is 32bit on 32bit platforms and 64bit on 64bit platforms.

Parameters:

**n**int

Number of experiments.

**pvals**sequence of floats, length p

Probabilities of each of the `p` different outcomes. These must sum to 1 (however, the last element is always assumed to account for the remaining probability, as long as `sum(pvals[:-1]) <= 1)`.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. Default is None, in which case a single value is returned.

Returns:

**out**ndarray

The drawn samples, of shape _size_, if that was provided. If not, the shape is `(N,)`.

In other words, each entry `out[i,j,...,:]` is an N-dimensional value drawn from the distribution.

See also

[`random.Generator.multinomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multinomial.html#numpy.random.Generator.multinomial "numpy.random.Generator.multinomial")

which should be used for new code.

Examples

Try it in your browser!

Throw a dice 20 times:

\>>> np.random.multinomial(20, \[1/6.\]\*6, size\=1)
array(\[\[4, 1, 7, 5, 2, 1\]\]) # random

Copy to clipboard

It landed 4 times on 1, once on 2, etc.

Now, throw the dice 20 times, and 20 times again:

\>>> np.random.multinomial(20, \[1/6.\]\*6, size\=2)
array(\[\[3, 4, 3, 3, 4, 3\], # random\
       \[2, 4, 3, 4, 0, 7\]\])

Copy to clipboard

For the first run, we threw 3 times 1, 4 times 2, etc. For the second, we threw 2 times 1, 4 times 2, etc.

A loaded die is more likely to land on number 6:

\>>> np.random.multinomial(100, \[1/7.\]\*5 + \[2/7.\])
array(\[11, 16, 14, 17, 16, 26\]) # random

Copy to clipboard

The probability inputs should be normalized. As an implementation detail, the value of the last entry is ignored and assumed to take up any leftover probability mass, but this should not be relied on. A biased coin which has twice as much weight on one side as on the other should be sampled like so:

\>>> np.random.multinomial(100, \[1.0 / 3, 2.0 / 3\])  \# RIGHT
array(\[38, 62\]) # random

Copy to clipboard

not like:

\>>> np.random.multinomial(100, \[1.0, 2.0\])  \# WRONG
Traceback (most recent call last):
ValueError: pvals < 0, pvals > 1 or pvals contains NaNs

Copy to clipboard

Go BackOpen In Tab

On this page