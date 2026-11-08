[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multinomial.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.multinomial.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multinomial.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.multinomial.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.multinomial.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.multinomial.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.multinomial.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.multinomial.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.multinomial.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.multinomial.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.multinomial.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.multinomial.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.multinomial.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.multinomial.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.multinomial.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.multinomial.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.multinomial.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.multinomial.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.multinomial.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.multinomial.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.multinomial.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.multinomial.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.multinomial[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multinomial.html#numpy-random-generator-multinomial "Link to this heading")

=================================================================================================================================================================================================

method

random.Generator.multinomial(_n_, _pvals_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multinomial.html#numpy.random.Generator.multinomial "Link to this definition")

Draw samples from a multinomial distribution.

The multinomial distribution is a multivariate generalization of the binomial distribution. Take an experiment with one of `p` possible outcomes. An example of such an experiment is throwing a dice, where the outcome can be 1 through 6. Each sample drawn from the distribution represents _n_ such experiments. Its values, `X_i = [X_0, X_1, ..., X_p]`, represent the number of times the outcome was `i`.

Parameters:

**n**int or array-like of ints

Number of experiments.

**pvals**array-like of floats

Probabilities of each of the `p` different outcomes with shape `(k0, k1, ..., kn, p)`. Each element `pvals[i,j,...,:]` must sum to 1 (however, the last element is always assumed to account for the remaining probability, as long as `sum(pvals[..., :-1], axis=-1) <= 1.0`. Must have at least 1 dimension where pvals.shape\[-1\] > 0.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn each with `p` elements. Default is None where the output size is determined by the broadcast shape of `n` and all by the final dimension of `pvals`, which is denoted as `b=(b0, b1, ..., bq)`. If size is not None, then it must be compatible with the broadcast shape `b`. Specifically, size must have `q` or more elements and size\[-(q-j):\] must equal `bj`.

Returns:

**out**ndarray

The drawn samples, of shape size, if provided. When size is provided, the output shape is size + (p,) If not specified, the shape is determined by the broadcast shape of `n` and `pvals`, `(b0, b1, ..., bq)` augmented with the dimension of the multinomial, `p`, so that that output shape is `(b0, b1, ..., bq, p)`.

Each entry `out[i,j,...,:]` is a `p`\-dimensional value drawn from the distribution.

Examples

Try it in your browser!

Throw a dice 20 times:

\>>> rng \= np.random.default\_rng()
\>>> rng.multinomial(20, \[1/6.\]\*6, size\=1)
array(\[\[4, 1, 7, 5, 2, 1\]\])  # random

Copy to clipboard

It landed 4 times on 1, once on 2, etc.

Now, throw the dice 20 times, and 20 times again:

\>>> rng.multinomial(20, \[1/6.\]\*6, size\=2)
array(\[\[3, 4, 3, 3, 4, 3\],\
       \[2, 4, 3, 4, 0, 7\]\])  # random

Copy to clipboard

For the first run, we threw 3 times 1, 4 times 2, etc. For the second, we threw 2 times 1, 4 times 2, etc.

Now, do one experiment throwing the dice 10 time, and 10 times again, and another throwing the dice 20 times, and 20 times again:

\>>> rng.multinomial(\[\[10\], \[20\]\], \[1/6.\]\*6, size\=(2, 2))
array(\[\[\[2, 4, 0, 1, 2, 1\],\
        \[1, 3, 0, 3, 1, 2\]\],\
       \[\[1, 4, 4, 4, 4, 3\],\
        \[3, 3, 2, 5, 5, 2\]\]\])  # random

Copy to clipboard

The first array shows the outcomes of throwing the dice 10 times, and the second shows the outcomes from throwing the dice 20 times.

A loaded die is more likely to land on number 6:

\>>> rng.multinomial(100, \[1/7.\]\*5 + \[2/7.\])
array(\[11, 16, 14, 17, 16, 26\])  # random

Copy to clipboard

Simulate 10 throws of a 4-sided die and 20 throws of a 6-sided die

\>>> rng.multinomial(\[10, 20\],\[\[1/4\]\*4 + \[0\]\*2, \[1/6\]\*6\])
array(\[\[2, 1, 4, 3, 0, 0\],\
       \[3, 3, 3, 6, 1, 4\]\], dtype=int64)  # random

Copy to clipboard

Generate categorical random variates from two categories where the first has 3 outcomes and the second has 2.

\>>> rng.multinomial(1, \[\[.1, .5, .4 \], \[.3, .7, .0\]\])
array(\[\[0, 0, 1\],\
       \[0, 1, 0\]\], dtype=int64)  # random

Copy to clipboard

`argmax(axis=-1)` is then used to return the categories.

\>>> pvals \= \[\[.1, .5, .4 \], \[.3, .7, .0\]\]
\>>> rvs \= rng.multinomial(1, pvals, size\=(4,2))
\>>> rvs.argmax(axis\=-1)
array(\[\[0, 1\],\
       \[2, 0\],\
       \[2, 1\],\
       \[2, 0\]\], dtype=int64)  # random

Copy to clipboard

The same output dimension can be produced using broadcasting.

\>>> rvs \= rng.multinomial(\[\[1\]\] \* 4, pvals)
\>>> rvs.argmax(axis\=-1)
array(\[\[0, 1\],\
       \[2, 0\],\
       \[2, 1\],\
       \[2, 0\]\], dtype=int64)  # random

Copy to clipboard

The probability inputs should be normalized. As an implementation detail, the value of the last entry is ignored and assumed to take up any leftover probability mass, but this should not be relied on. A biased coin which has twice as much weight on one side as on the other should be sampled like so:

\>>> rng.multinomial(100, \[1.0 / 3, 2.0 / 3\])  \# RIGHT
array(\[38, 62\])  # random

Copy to clipboard

not like:

\>>> rng.multinomial(100, \[1.0, 2.0\])  \# WRONG
Traceback (most recent call last):
ValueError: pvals < 0, pvals > 1 or pvals contains NaNs

Copy to clipboard

Go BackOpen In Tab

On this page