[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.vonmises.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.vonmises.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.vonmises.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.vonmises.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.vonmises.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.vonmises.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.vonmises.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.vonmises.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.vonmises.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.vonmises.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.vonmises.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.vonmises.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.vonmises.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.vonmises.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.vonmises.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.vonmises.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.vonmises.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.vonmises.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.vonmises.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.vonmises.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.vonmises.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.vonmises.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.vonmises[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.vonmises.html#numpy-random-generator-vonmises "Link to this heading")

========================================================================================================================================================================================

method

random.Generator.vonmises(_mu_, _kappa_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.vonmises.html#numpy.random.Generator.vonmises "Link to this definition")

Draw samples from a von Mises distribution.

Samples are drawn from a von Mises distribution with specified mode (mu) and concentration (kappa), on the interval \[-pi, pi\].

The von Mises distribution (also known as the circular normal distribution) is a continuous probability distribution on the unit circle. It may be thought of as the circular analogue of the normal distribution.

Parameters:

**mu**float or array\_like of floats

Mode (“center”) of the distribution.

**kappa**float or array\_like of floats

Concentration of the distribution, has to be >=0.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `mu` and `kappa` are both scalars. Otherwise, `np.broadcast(mu, kappa).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized von Mises distribution.

See also

[`scipy.stats.vonmises`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.vonmises.html#scipy.stats.vonmises "(in SciPy v1.18.0)")

probability density function, distribution, or cumulative density function, etc.

Notes

The probability density for the von Mises distribution is

\\\[p(x) = \\frac{e^{\\kappa cos(x-\\mu)}}{2\\pi I\_0(\\kappa)},\\\]

where \\(\\mu\\) is the mode and \\(\\kappa\\) the concentration, and \\(I\_0(\\kappa)\\) is the modified Bessel function of order 0.

The von Mises is named for Richard Edler von Mises, who was born in Austria-Hungary, in what is now the Ukraine. He fled to the United States in 1939 and became a professor at Harvard. He worked in probability theory, aerodynamics, fluid mechanics, and philosophy of science.

References

\[1\]

Abramowitz, M. and Stegun, I. A. (Eds.). “Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables, 9th printing,” New York: Dover, 1972.

\[2\]

von Mises, R., “Mathematical Theory of Probability and Statistics”, New York: Academic Press, 1964.

Examples

Try it in your browser!

Draw samples from the distribution:

\>>> mu, kappa \= 0.0, 4.0 \# mean and concentration
\>>> rng \= np.random.default\_rng()
\>>> s \= rng.vonmises(mu, kappa, 1000)

Copy to clipboard

Display the histogram of the samples, along with the probability density function:

\>>> import matplotlib.pyplot as plt
\>>> from scipy.special import i0  
\>>> plt.hist(s, 50, density\=True)
\>>> x \= np.linspace(\-np.pi, np.pi, num\=51)
\>>> y \= np.exp(kappa\*np.cos(x\-mu))/(2\*np.pi\*i0(kappa))  
\>>> plt.plot(x, y, linewidth\=2, color\='r')  
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-Generator-vonmises-1.png](https://numpy.org/doc/stable/_images/numpy-random-Generator-vonmises-1.png)

Go BackOpen In Tab

On this page