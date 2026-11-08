[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.permutation.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.permutation.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.permutation.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.permutation.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.permutation.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.permutation.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.permutation.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.permutation.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.permutation.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.permutation.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.permutation.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.permutation.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.permutation.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.permutation.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.permutation.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.permutation.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.permutation.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.permutation.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.permutation.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.permutation.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.permutation.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.permutation.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.permutation[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.permutation.html#numpy-random-randomstate-permutation "Link to this heading")

=======================================================================================================================================================================================================

method

random.RandomState.permutation(_x_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.permutation.html#numpy.random.RandomState.permutation "Link to this definition")

Randomly permute a sequence, or return a permuted range.

If _x_ is a multi-dimensional array, it is only shuffled along its first index.

Note

New code should use the [`permutation`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html#numpy.random.Generator.permutation "numpy.random.Generator.permutation")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**x**int or array\_like

If _x_ is an integer, randomly permute `np.arange(x)`. If _x_ is an array, make a copy and shuffle the elements randomly.

Returns:

**out**ndarray

Permuted sequence or array range.

See also

[`random.Generator.permutation`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html#numpy.random.Generator.permutation "numpy.random.Generator.permutation")

which should be used for new code.

Examples

Try it in your browser!

\>>> np.random.permutation(10)
array(\[1, 7, 4, 3, 0, 9, 2, 5, 8, 6\]) # random

Copy to clipboard

\>>> np.random.permutation(\[1, 4, 9, 12, 15\])
array(\[15,  1,  9,  4, 12\]) # random

Copy to clipboard

\>>> arr \= np.arange(9).reshape((3, 3))
\>>> np.random.permutation(arr)
array(\[\[6, 7, 8\], # random\
       \[0, 1, 2\],\
       \[3, 4, 5\]\])

Copy to clipboard

Go BackOpen In Tab

On this page