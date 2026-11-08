[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_exponential.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.standard_exponential.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.standard_exponential.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.standard\_exponential[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_exponential.html#numpy-random-generator-standard-exponential "Link to this heading")

=============================================================================================================================================================================================================================

method

random.Generator.standard\_exponential(_size\=None_, _dtype\=np.float64_, _method\='zig'_, _out\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_exponential.html#numpy.random.Generator.standard_exponential "Link to this definition")

Draw samples from the standard exponential distribution.

[`standard_exponential`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_exponential.html#numpy.random.Generator.standard_exponential "numpy.random.Generator.standard_exponential")
 is identical to the exponential distribution with a scale parameter of 1.

Parameters:

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. Default is None, in which case a single value is returned.

**dtype**dtype, optional

Desired dtype of the result, only [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 and [`float32`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")
 are supported. Byteorder must be native. The default value is np.float64.

**method**str, optional

Either ‘inv’ or ‘zig’. ‘inv’ uses the default inverse CDF method. ‘zig’ uses the much faster Ziggurat method of Marsaglia and Tsang [\[1\]](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_exponential.html#rb9e18afb0ed4-1)
.

**out**ndarray, optional

Alternative output array in which to place the result. If size is not None, it must have the same shape as the provided size and must match the type of the output values.

Returns:

**out**float or ndarray

Drawn samples.

References

\[[1](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_exponential.html#id1)\
\]

Marsaglia, G. and Tsang, W. W. (2000). The Ziggurat method for generating random variables. Journal of Statistical Software, 5, 1-7. [https://doi.org/10.18637/jss.v005.i08](https://doi.org/10.18637/jss.v005.i08)

Examples

Try it in your browser!

Output a 3x8000 array:

\>>> rng \= np.random.default\_rng()
\>>> n \= rng.standard\_exponential((3, 8000))

Copy to clipboard

Go BackOpen In Tab

On this page