[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.random.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.random.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.random.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.random.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.random.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.random.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.random.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.random.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.random.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.random.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.random.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.random.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.random.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.random.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.random.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.random.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.random.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.random.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.random.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.random.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.random[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy-random-generator-random "Link to this heading")

==================================================================================================================================================================================

method

random.Generator.random(_size\=None_, _dtype\=np.float64_, _out\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random "Link to this definition")

Return random floats in the half-open interval \[0.0, 1.0).\
\
Results are from the “continuous uniform” distribution over the stated interval. To sample use [`uniform`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.uniform.html#numpy.random.Generator.uniform "numpy.random.Generator.uniform")\
 or multiply the output of [`random`](https://numpy.org/doc/stable/reference/random/index.html#module-numpy.random "numpy.random")\
 by `(b - a)` and add `a`:\
\
(b \- a) \* random() + a\
\
Copy to clipboard\
\
Parameters:\
\
**size**int or tuple of ints, optional\
\
Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. Default is None, in which case a single value is returned.\
\
**dtype**dtype, optional\
\
Desired dtype of the result, only [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
 and [`float32`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")\
 are supported. Byteorder must be native. The default value is np.float64.\
\
**out**ndarray, optional\
\
Alternative output array in which to place the result. If size is not None, it must have the same shape as the provided size and must match the type of the output values.\
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
[`uniform`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.uniform.html#numpy.random.Generator.uniform "numpy.random.Generator.uniform")\
\
Draw samples from the parameterized uniform distribution.\
\
Examples\
\
Try it in your browser!\
\
\>>> rng \= np.random.default\_rng()\
\>>> rng.random()\
0.47108547995356098 # random\
\>>> type(rng.random())\
<class 'float'>\
\>>> rng.random((5,))\
array(\[ 0.30220482,  0.86820401,  0.1654503 ,  0.11659149,  0.54323428\]) # random\
\
Copy to clipboard\
\
Three-by-two array of random numbers from \[-5, 0):\
\
\>>> 5 \* rng.random((3, 2)) \- 5\
array(\[\[-3.99149989, -0.52338984\], # random\
       \[-2.99091858, -0.79479508\],\
       \[-1.23204345, -1.75224494\]\])\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
On this page