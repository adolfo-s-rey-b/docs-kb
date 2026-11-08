[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.triangular.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.triangular.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.triangular.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.triangular.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.triangular.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.triangular.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.triangular.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.triangular.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.triangular.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.triangular.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.triangular.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.triangular.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.triangular.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.triangular.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.triangular.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.triangular.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.triangular.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.triangular.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.triangular.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.triangular.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.triangular.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.triangular.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.triangular[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.triangular.html#numpy-random-generator-triangular "Link to this heading")

==============================================================================================================================================================================================

method

random.Generator.triangular(_left_, _mode_, _right_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.triangular.html#numpy.random.Generator.triangular "Link to this definition")

Draw samples from the triangular distribution over the interval `[left, right]`.

The triangular distribution is a continuous probability distribution with lower limit left, peak at mode, and upper limit right. Unlike the other distributions, these parameters directly define the shape of the pdf.

Parameters:

**left**float or array\_like of floats

Lower limit.

**mode**float or array\_like of floats

The value where the peak of the distribution occurs. The value must fulfill the condition `left <= mode <= right`.

**right**float or array\_like of floats

Upper limit, must be larger than _left_.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `left`, `mode`, and `right` are all scalars. Otherwise, `np.broadcast(left, mode, right).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized triangular distribution.

Notes

The probability density function for the triangular distribution is

The triangular distribution is often used in ill-defined problems where the underlying distribution is not known, but some knowledge of the limits and mode exists. Often it is used in simulations.

References

\[1\]

Wikipedia, “Triangular distribution” [https://en.wikipedia.org/wiki/Triangular\_distribution](https://en.wikipedia.org/wiki/Triangular_distribution)

Examples

Try it in your browser!

Draw values from the distribution and plot the histogram:

\>>> import matplotlib.pyplot as plt
\>>> rng \= np.random.default\_rng()
\>>> h \= plt.hist(rng.triangular(\-3, 0, 8, 100000), bins\=200,
...              density\=True)
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-Generator-triangular-1.png](https://numpy.org/doc/stable/_images/numpy-random-Generator-triangular-1.png)

Go BackOpen In Tab

On this page