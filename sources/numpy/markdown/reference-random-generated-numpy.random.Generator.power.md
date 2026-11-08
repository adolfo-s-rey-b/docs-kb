[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.power.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.power.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.power.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.power.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.power.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.power.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.power.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.power.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.power.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.power.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.power.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.power.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.power.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.power.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.power.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.power.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.power.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.power.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.power.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.power.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.power.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.power.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.power[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.power.html#numpy-random-generator-power "Link to this heading")

===============================================================================================================================================================================

method

random.Generator.power(_a_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.power.html#numpy.random.Generator.power "Link to this definition")

Draws samples in \[0, 1\] from a power distribution with positive exponent a - 1.

Also known as the power function distribution.

Parameters:

**a**float or array\_like of floats

Parameter of the distribution. Must be non-negative.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `a` is a scalar. Otherwise, `np.array(a).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized power distribution.

Raises:

ValueError

If a <= 0.

Notes

The probability density function is

The power function distribution is just the inverse of the Pareto distribution. It may also be seen as a special case of the Beta distribution.

It is used, for example, in modeling the over-reporting of insurance claims.

References

\[1\]

Christian Kleiber, Samuel Kotz, “Statistical size distributions in economics and actuarial sciences”, Wiley, 2003.

\[2\]

Heckert, N. A. and Filliben, James J. “NIST Handbook 148: Dataplot Reference Manual, Volume 2: Let Subcommands and Library Functions”, National Institute of Standards and Technology Handbook Series, June 2003. [https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/powpdf.pdf](https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/powpdf.pdf)

Examples

Try it in your browser!

Draw samples from the distribution:

\>>> rng \= np.random.default\_rng()
\>>> a \= 5. \# shape
\>>> samples \= 1000
\>>> s \= rng.power(a, samples)

Copy to clipboard

Display the histogram of the samples, along with the probability density function:

\>>> import matplotlib.pyplot as plt
\>>> count, bins, \_ \= plt.hist(s, bins\=30)
\>>> x \= np.linspace(0, 1, 100)
\>>> y \= a\*x\*\*(a\-1.)
\>>> normed\_y \= samples\*np.diff(bins)\[0\]\*y
\>>> plt.plot(x, normed\_y)
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-Generator-power-1_00_00.png](https://numpy.org/doc/stable/_images/numpy-random-Generator-power-1_00_00.png)

Compare the power function distribution to the inverse of the Pareto.

\>>> from scipy import stats  
\>>> rvs \= rng.power(5, 1000000)
\>>> rvsp \= rng.pareto(5, 1000000)
\>>> xx \= np.linspace(0,1,100)
\>>> powpdf \= stats.powerlaw.pdf(xx,5)  

Copy to clipboard

\>>> plt.figure()
\>>> plt.hist(rvs, bins\=50, density\=True)
\>>> plt.plot(xx,powpdf,'r-')  
\>>> plt.title('power(5)')

Copy to clipboard

\>>> plt.figure()
\>>> plt.hist(1./(1.+rvsp), bins\=50, density\=True)
\>>> plt.plot(xx,powpdf,'r-')  
\>>> plt.title('inverse of 1 + Generator.pareto(5)')

Copy to clipboard

\>>> plt.figure()
\>>> plt.hist(1./(1.+rvsp), bins\=50, density\=True)
\>>> plt.plot(xx,powpdf,'r-')  
\>>> plt.title('inverse of stats.pareto(5)')

Copy to clipboard

![../../../_images/numpy-random-Generator-power-1_01_00.png](https://numpy.org/doc/stable/_images/numpy-random-Generator-power-1_01_00.png)

![../../../_images/numpy-random-Generator-power-1_01_01.png](https://numpy.org/doc/stable/_images/numpy-random-Generator-power-1_01_01.png)

![../../../_images/numpy-random-Generator-power-1_01_02.png](https://numpy.org/doc/stable/_images/numpy-random-Generator-power-1_01_02.png)

Go BackOpen In Tab

On this page