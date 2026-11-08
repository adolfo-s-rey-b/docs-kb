[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.standard_normal.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.standard_normal.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.standard_normal.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.standard_normal.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.standard_normal.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.standard_normal.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.standard_normal.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.standard_normal.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.standard_normal.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.standard_normal.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.standard_normal.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.standard_normal.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.standard_normal.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.standard_normal.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.standard_normal.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.standard_normal.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.standard_normal.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.standard_normal.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.standard_normal.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.standard_normal.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.standard\_normal[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html#numpy-random-generator-standard-normal "Link to this heading")

==============================================================================================================================================================================================================

method

random.Generator.standard\_normal(_size\=None_, _dtype\=np.float64_, _out\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html#numpy.random.Generator.standard_normal "Link to this definition")

Draw samples from a standard Normal distribution (mean=0, stdev=1).

Parameters:

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. Default is None, in which case a single value is returned.

**dtype**dtype, optional

Desired dtype of the result, only [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 and [`float32`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")
 are supported. Byteorder must be native. The default value is np.float64.

**out**ndarray, optional

Alternative output array in which to place the result. If size is not None, it must have the same shape as the provided size and must match the type of the output values.

Returns:

**out**float or ndarray

A floating-point array of shape `size` of drawn samples, or a single sample if `size` was not specified.

See also

[`normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal "numpy.random.Generator.normal")

Equivalent function with additional `loc` and `scale` arguments for setting the mean and standard deviation.

Notes

For random samples from the normal distribution with mean `mu` and standard deviation `sigma`, use one of:

mu + sigma \* rng.standard\_normal(size\=...)
rng.normal(mu, sigma, size\=...)

Copy to clipboard

Examples

Try it in your browser!

\>>> rng \= np.random.default\_rng()
\>>> rng.standard\_normal()
2.1923875335537315 # random

Copy to clipboard

\>>> s \= rng.standard\_normal(8000)
\>>> s
array(\[ 0.6888893 ,  0.78096262, -0.89086505, ...,  0.49876311,  # random\
       -0.38672696, -0.4685006 \])                                # random
\>>> s.shape
(8000,)
\>>> s \= rng.standard\_normal(size\=(3, 4, 2))
\>>> s.shape
(3, 4, 2)

Copy to clipboard

Two-by-four array of samples from the normal distribution with mean 3 and standard deviation 2.5:

\>>> 3 + 2.5 \* rng.standard\_normal(size\=(2, 4))
array(\[\[-4.49401501,  4.00950034, -1.81814867,  7.29718677\],   # random\
       \[ 0.39924804,  4.68456316,  4.99394529,  4.84057254\]\])  # random

Copy to clipboard

Go BackOpen In Tab

On this page