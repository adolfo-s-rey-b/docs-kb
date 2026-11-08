[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.standard_exponential.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.standard_exponential.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.standard_exponential.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.standard\_exponential[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.standard_exponential.html#numpy-random-randomstate-standard-exponential "Link to this heading")

===================================================================================================================================================================================================================================

method

random.RandomState.standard\_exponential(_size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.standard_exponential.html#numpy.random.RandomState.standard_exponential "Link to this definition")

Draw samples from the standard exponential distribution.

[`standard_exponential`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.standard_exponential.html#numpy.random.RandomState.standard_exponential "numpy.random.RandomState.standard_exponential")
 is identical to the exponential distribution with a scale parameter of 1.

Note

New code should use the [`standard_exponential`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_exponential.html#numpy.random.Generator.standard_exponential "numpy.random.Generator.standard_exponential")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. Default is None, in which case a single value is returned.

Returns:

**out**float or ndarray

Drawn samples.

See also

[`random.Generator.standard_exponential`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_exponential.html#numpy.random.Generator.standard_exponential "numpy.random.Generator.standard_exponential")

which should be used for new code.

Examples

Try it in your browser!

Output a 3x8000 array:

\>>> n \= np.random.standard\_exponential((3, 8000))

Copy to clipboard

Go BackOpen In Tab

On this page