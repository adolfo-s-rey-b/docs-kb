[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.random_sample.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.random_sample.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.random_sample.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.random_sample.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.random_sample.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.random_sample.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.random_sample.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.random_sample.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.random_sample.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.random_sample.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.random_sample.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.random_sample.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.random_sample.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.random_sample.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.random_sample.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.random_sample.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.random_sample.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.random_sample.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.random_sample.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.random_sample.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.random_sample.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.random_sample.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.random\_sample[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.random_sample.html#numpy-random-randomstate-random-sample "Link to this heading")

==============================================================================================================================================================================================================

method

random.RandomState.random\_sample(_size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.random_sample.html#numpy.random.RandomState.random_sample "Link to this definition")

Return random floats in the half-open interval \[0.0, 1.0).\
\
Results are from the “continuous uniform” distribution over the stated interval. To sample \\(Unif\[a, b), b > a\\) multiply the output of [`random_sample`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.random_sample.html#numpy.random.RandomState.random_sample "numpy.random.RandomState.random_sample")\
 by _(b-a)_ and add _a_:\
\
(b \- a) \* random\_sample() + a\
\
Copy to clipboard\
\
Note\
\
New code should use the [`random`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random "numpy.random.Generator.random")\
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")\
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)\
.\
\
Parameters:\
\
**size**int or tuple of ints, optional\
\
Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. Default is None, in which case a single value is returned.\
\
Returns:\
\
**out**float or ndarray of floats\
\
Array of random floats of shape [`size`](https://numpy.org/doc/stable/reference/generated/numpy.size.html#numpy.size "numpy.size")\
 (unless `size=None`, in which case a single float is returned).\
\
See also\
\
[`random.Generator.random`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random "numpy.random.Generator.random")\
\
which should be used for new code.\
\
Examples\
\
Try it in your browser!\
\
\>>> np.random.random\_sample()\
0.47108547995356098 # random\
\>>> type(np.random.random\_sample())\
<class 'float'>\
\>>> np.random.random\_sample((5,))\
array(\[ 0.30220482,  0.86820401,  0.1654503 ,  0.11659149,  0.54323428\]) # random\
\
Copy to clipboard\
\
Three-by-two array of random numbers from \[-5, 0):\
\
\>>> 5 \* np.random.random\_sample((3, 2)) \- 5\
array(\[\[-3.99149989, -0.52338984\], # random\
       \[-2.99091858, -0.79479508\],\
       \[-1.23204345, -1.75224494\]\])\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
On this page