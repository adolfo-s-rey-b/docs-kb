[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.zipf.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.zipf.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.zipf.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.zipf.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.zipf.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.zipf.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.zipf.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.zipf.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.zipf.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.zipf.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.zipf.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.zipf.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.zipf.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.zipf.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.zipf.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.zipf.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.zipf.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.zipf.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.zipf.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.zipf.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.zipf.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.zipf.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.zipf[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.zipf.html#numpy-random-randomstate-zipf "Link to this heading")

==================================================================================================================================================================================

method

random.RandomState.zipf(_a_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.zipf.html#numpy.random.RandomState.zipf "Link to this definition")

Draw samples from a Zipf distribution.

Samples are drawn from a Zipf distribution with specified parameter _a_ > 1.

The Zipf distribution (also known as the zeta distribution) is a discrete probability distribution that satisfies Zipf’s law: the frequency of an item is inversely proportional to its rank in a frequency table.

Note

New code should use the [`zipf`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.zipf.html#numpy.random.Generator.zipf "numpy.random.Generator.zipf")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**a**float or array\_like of floats

Distribution parameter. Must be greater than 1.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `a` is a scalar. Otherwise, `np.array(a).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized Zipf distribution.

See also

[`scipy.stats.zipf`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.zipf.html#scipy.stats.zipf "(in SciPy v1.18.0)")

probability density function, distribution, or cumulative density function, etc.

[`random.Generator.zipf`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.zipf.html#numpy.random.Generator.zipf "numpy.random.Generator.zipf")

which should be used for new code.

Notes

The probability mass function (PMF) for the Zipf distribution is

\\\[p(k) = \\frac{k^{-a}}{\\zeta(a)},\\\]

for integers \\(k \\geq 1\\), where \\(\\zeta\\) is the Riemann Zeta function.

It is named for the American linguist George Kingsley Zipf, who noted that the frequency of any word in a sample of a language is inversely proportional to its rank in the frequency table.

References

\[1\]

Zipf, G. K., “Selected Studies of the Principle of Relative Frequency in Language,” Cambridge, MA: Harvard Univ. Press, 1932.

Examples

Try it in your browser!

Draw samples from the distribution:

\>>> a \= 4.0
\>>> n \= 20000
\>>> s \= np.random.zipf(a, n)

Copy to clipboard

Display the histogram of the samples, along with the expected histogram based on the probability density function:

\>>> import matplotlib.pyplot as plt
\>>> from scipy.special import zeta  

Copy to clipboard

[`bincount`](https://numpy.org/doc/stable/reference/generated/numpy.bincount.html#numpy.bincount "numpy.bincount")
 provides a fast histogram for small integers.

\>>> count \= np.bincount(s)
\>>> k \= np.arange(1, s.max() + 1)

Copy to clipboard

\>>> plt.bar(k, count\[1:\], alpha\=0.5, label\='sample count')
\>>> plt.plot(k, n\*(k\*\*-a)/zeta(a), 'k.-', alpha\=0.5,
...          label\='expected count')   
\>>> plt.semilogy()
\>>> plt.grid(alpha\=0.4)
\>>> plt.legend()
\>>> plt.title(f'Zipf sample, a={a}, size={n}')
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-RandomState-zipf-1.png](https://numpy.org/doc/stable/_images/numpy-random-RandomState-zipf-1.png)

Go BackOpen In Tab

On this page