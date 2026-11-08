[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.logseries.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.logseries.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.logseries.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.logseries.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.logseries.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.logseries.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.logseries.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.logseries.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.logseries.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.logseries.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.logseries.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.logseries.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.logseries.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.logseries.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.logseries.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.logseries.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.logseries.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.logseries.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.logseries.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.logseries.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.logseries.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.logseries.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.logseries[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.logseries.html#numpy-random-generator-logseries "Link to this heading")

===========================================================================================================================================================================================

method

random.Generator.logseries(_p_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.logseries.html#numpy.random.Generator.logseries "Link to this definition")

Draw samples from a logarithmic series distribution.

Samples are drawn from a log series distribution with specified shape parameter, 0 <= `p` < 1.

Parameters:

**p**float or array\_like of floats

Shape parameter for the distribution. Must be in the range \[0, 1).\
\
**size**int or tuple of ints, optional\
\
Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `p` is a scalar. Otherwise, `np.array(p).size` samples are drawn.\
\
Returns:\
\
**out**ndarray or scalar\
\
Drawn samples from the parameterized logarithmic series distribution.\
\
See also\
\
[`scipy.stats.logser`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.logser.html#scipy.stats.logser "(in SciPy v1.18.0)")\
\
probability density function, distribution or cumulative density function, etc.\
\
Notes\
\
The probability mass function for the Log Series distribution is\
\
\\\[P(k) = \\frac{-p^k}{k \\ln(1-p)},\\\]\
\
where p = probability.\
\
The log series distribution is frequently used to represent species richness and occurrence, first proposed by Fisher, Corbet, and Williams in 1943 [\[2\]](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.logseries.html#r8738ed783818-2)\
. It may also be used to model the numbers of occupants seen in cars [\[3\]](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.logseries.html#r8738ed783818-3)\
.\
\
References\
\
\[1\]\
\
Buzas, Martin A.; Culver, Stephen J., Understanding regional species diversity through the log series distribution of occurrences: BIODIVERSITY RESEARCH Diversity & Distributions, Volume 5, Number 5, September 1999 , pp. 187-195(9).\
\
\[[2](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.logseries.html#id1)\
\]\
\
Fisher, R.A,, A.S. Corbet, and C.B. Williams. 1943. The relation between the number of species and the number of individuals in a random sample of an animal population. Journal of Animal Ecology, 12:42-58.\
\
\[[3](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.logseries.html#id2)\
\]\
\
D. J. Hand, F. Daly, D. Lunn, E. Ostrowski, A Handbook of Small Data Sets, CRC Press, 1994.\
\
\[4\]\
\
Wikipedia, “Logarithmic distribution”, [https://en.wikipedia.org/wiki/Logarithmic\_distribution](https://en.wikipedia.org/wiki/Logarithmic_distribution)\
\
Examples\
\
Try it in your browser!\
\
Draw samples from the distribution:\
\
\>>> a \= .6\
\>>> rng \= np.random.default\_rng()\
\>>> s \= rng.logseries(a, 10000)\
\>>> import matplotlib.pyplot as plt\
\>>> bins \= np.arange(\-.5, max(s) + .5 )\
\>>> count, bins, \_ \= plt.hist(s, bins\=bins, label\='Sample count')\
\
Copy to clipboard\
\
Plot against the distribution:\
\
\>>> def logseries(k, p):\
...     return \-p\*\*k/(k\*np.log(1\-p))\
\>>> centres \= np.arange(1, max(s) + 1)\
\>>> plt.plot(centres, logseries(centres, a) \* s.size, 'r', label\='logseries PMF')\
\>>> plt.legend()\
\>>> plt.show()\
\
Copy to clipboard\
\
![../../../_images/numpy-random-Generator-logseries-1.png](https://numpy.org/doc/stable/_images/numpy-random-Generator-logseries-1.png)\
\
Go BackOpen In Tab\
\
On this page