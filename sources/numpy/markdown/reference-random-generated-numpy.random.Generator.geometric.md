[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.geometric.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.geometric.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.geometric.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.geometric.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.geometric.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.geometric.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.geometric.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.geometric.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.geometric.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.geometric.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.geometric.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.geometric.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.geometric.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.geometric.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.geometric.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.geometric.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.geometric.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.geometric.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.geometric.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.geometric.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.geometric.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.geometric.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.geometric[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.geometric.html#numpy-random-generator-geometric "Link to this heading")

===========================================================================================================================================================================================

method

random.Generator.geometric(_p_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.geometric.html#numpy.random.Generator.geometric "Link to this definition")

Draw samples from the geometric distribution.

Bernoulli trials are experiments with one of two outcomes: success or failure (an example of such an experiment is flipping a coin). The geometric distribution models the number of trials that must be run in order to achieve success. It is therefore supported on the positive integers, `k = 1, 2, ...`.

The probability mass function of the geometric distribution is

where _p_ is the probability of success of an individual trial.

Parameters:

**p**float or array\_like of floats

The probability of success of an individual trial.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `p` is a scalar. Otherwise, `np.array(p).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized geometric distribution.

References

\[1\]

Wikipedia, “Geometric distribution”, [https://en.wikipedia.org/wiki/Geometric\_distribution](https://en.wikipedia.org/wiki/Geometric_distribution)

Examples

Try it in your browser!

Draw 10,000 values from the geometric distribution, with the probability of an individual success equal to `p = 0.35`:

\>>> p, size \= 0.35, 10000
\>>> rng \= np.random.default\_rng()
\>>> sample \= rng.geometric(p\=p, size\=size)

Copy to clipboard

What proportion of trials succeeded after a single run?

\>>> (sample \== 1).sum()/size
0.34889999999999999  # may vary

Copy to clipboard

The geometric distribution with `p=0.35` looks as follows:

\>>> import matplotlib.pyplot as plt
\>>> count, bins, \_ \= plt.hist(sample, bins\=30, density\=True)
\>>> plt.plot(bins, (1\-p)\*\*(bins\-1)\*p)
\>>> plt.xlim(\[0, 25\])
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-Generator-geometric-1.png](https://numpy.org/doc/stable/_images/numpy-random-Generator-geometric-1.png)

Go BackOpen In Tab

On this page