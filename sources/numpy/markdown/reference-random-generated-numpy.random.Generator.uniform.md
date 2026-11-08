[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.uniform.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.uniform.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.uniform.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.uniform.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.uniform.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.uniform.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.uniform.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.uniform.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.uniform.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.uniform.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.uniform.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.uniform.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.uniform.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.uniform.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.uniform.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.uniform.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.uniform.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.uniform.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.uniform.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.uniform.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.uniform.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.uniform.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.uniform[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.uniform.html#numpy-random-generator-uniform "Link to this heading")

=====================================================================================================================================================================================

method

random.Generator.uniform(_low\=0.0_, _high\=1.0_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.uniform.html#numpy.random.Generator.uniform "Link to this definition")

Draw samples from a uniform distribution.

Samples are uniformly distributed over the half-open interval `[low, high)` (includes low, but excludes high). In other words, any value within the given interval is equally likely to be drawn by [`uniform`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.uniform.html#numpy.random.Generator.uniform "numpy.random.Generator.uniform")\
.\
\
Parameters:\
\
**low**float or array\_like of floats, optional\
\
Lower boundary of the output interval. All values generated will be greater than or equal to low. The default value is 0.\
\
**high**float or array\_like of floats\
\
Upper boundary of the output interval. All values generated will be less than high. The high limit may be included in the returned array of floats due to floating-point rounding in the equation `low + (high-low) * random_sample()`. high - low must be non-negative. The default value is 1.0.\
\
**size**int or tuple of ints, optional\
\
Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `low` and `high` are both scalars. Otherwise, `np.broadcast(low, high).size` samples are drawn.\
\
Returns:\
\
**out**ndarray or scalar\
\
Drawn samples from the parameterized uniform distribution.\
\
See also\
\
[`integers`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html#numpy.random.Generator.integers "numpy.random.Generator.integers")\
\
Discrete uniform distribution, yielding integers.\
\
[`random`](https://numpy.org/doc/stable/reference/random/index.html#module-numpy.random "numpy.random")\
\
Floats uniformly distributed over `[0, 1)`.\
\
Notes\
\
The probability density function of the uniform distribution is\
\
anywhere within the interval `[a, b)`, and zero elsewhere.\
\
When `high` == `low`, values of `low` will be returned.\
\
Examples\
\
Try it in your browser!\
\
Draw samples from the distribution:\
\
\>>> rng \= np.random.default\_rng()\
\>>> s \= rng.uniform(\-1,0,1000)\
\
Copy to clipboard\
\
All values are within the given interval:\
\
\>>> np.all(s \>= \-1)\
True\
\>>> np.all(s < 0)\
True\
\
Copy to clipboard\
\
Display the histogram of the samples, along with the probability density function:\
\
\>>> import matplotlib.pyplot as plt\
\>>> count, bins, \_ \= plt.hist(s, 15, density\=True)\
\>>> plt.plot(bins, np.ones\_like(bins), linewidth\=2, color\='r')\
\>>> plt.show()\
\
Copy to clipboard\
\
![../../../_images/numpy-random-Generator-uniform-1.png](https://numpy.org/doc/stable/_images/numpy-random-Generator-uniform-1.png)\
\
Go BackOpen In Tab\
\
On this page