[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.uniform.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.uniform.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.uniform.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.uniform.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.uniform.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.uniform.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.uniform.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.uniform.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.uniform.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.uniform.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.uniform.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.uniform.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.uniform.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.uniform.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.uniform.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.uniform.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.uniform.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.uniform.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.uniform.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.uniform.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.uniform[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy-random-uniform "Link to this heading")

=======================================================================================================================================================

random.uniform(_low\=0.0_, _high\=1.0_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "Link to this definition")

Draw samples from a uniform distribution.

Samples are uniformly distributed over the half-open interval `[low, high)` (includes low, but excludes high). In other words, any value within the given interval is equally likely to be drawn by [`uniform`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")\
.\
\
Note\
\
New code should use the [`uniform`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.uniform.html#numpy.random.Generator.uniform "numpy.random.Generator.uniform")\
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")\
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)\
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
Upper boundary of the output interval. All values generated will be less than or equal to high. The high limit may be included in the returned array of floats due to floating-point rounding in the equation `low + (high-low) * random_sample()`. The default value is 1.0.\
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
[`randint`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")\
\
Discrete uniform distribution, yielding integers.\
\
[`random_integers`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_integers.html#numpy.random.random_integers "numpy.random.random_integers")\
\
Discrete uniform distribution over the closed interval `[low, high]`.\
\
[`random_sample`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_sample.html#numpy.random.random_sample "numpy.random.random_sample")\
\
Floats uniformly distributed over `[0, 1)`.\
\
[`random`](https://numpy.org/doc/stable/reference/random/index.html#module-numpy.random "numpy.random")\
\
Alias for [`random_sample`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_sample.html#numpy.random.random_sample "numpy.random.random_sample")\
.\
\
[`rand`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")\
\
Convenience function that accepts dimensions as input, e.g., `rand(2,2)` would generate a 2-by-2 array of floats, uniformly distributed over `[0, 1)`.\
\
[`random.Generator.uniform`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.uniform.html#numpy.random.Generator.uniform "numpy.random.Generator.uniform")\
\
which should be used for new code.\
\
Notes\
\
The probability density function of the uniform distribution is\
\
\\\[p(x) = \\frac{1}{b - a}\\\]\
\
anywhere within the interval `[a, b)`, and zero elsewhere.\
\
When `high` == `low`, values of `low` will be returned. If `high` < `low`, the results are officially undefined and may eventually raise an error, i.e. do not rely on this function to behave when passed arguments satisfying that inequality condition. The `high` limit may be included in the returned array of floats due to floating-point rounding in the equation `low + (high-low) * random_sample()`. For example:\
\
\>>> x \= np.float32(5\*0.99999999)\
\>>> x\
np.float32(5.0)\
\
Copy to clipboard\
\
Examples\
\
Try it in your browser!\
\
Draw samples from the distribution:\
\
\>>> s \= np.random.uniform(\-1,0,1000)\
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
\>>> count, bins, ignored \= plt.hist(s, 15, density\=True)\
\>>> plt.plot(bins, np.ones\_like(bins), linewidth\=2, color\='r')\
\>>> plt.show()\
\
Copy to clipboard\
\
![../../../_images/numpy-random-uniform-1.png](https://numpy.org/doc/stable/_images/numpy-random-uniform-1.png)\
\
Go BackOpen In Tab\
\
On this page