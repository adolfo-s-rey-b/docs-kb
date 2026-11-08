[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.permutation.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.permutation.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.permutation.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.permutation.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.permutation.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.permutation.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.permutation.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.permutation.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.permutation.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.permutation.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.permutation.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.permutation.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.permutation.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.permutation.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.permutation.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.permutation.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.permutation.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.permutation.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.permutation.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.permutation.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.permutation[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html#numpy-random-generator-permutation "Link to this heading")

=================================================================================================================================================================================================

method

random.Generator.permutation(_x_, _axis\=0_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html#numpy.random.Generator.permutation "Link to this definition")

Randomly permute a sequence, or return a permuted range.

Parameters:

**x**int or array\_like

If _x_ is an integer, randomly permute `np.arange(x)`. If _x_ is an array, make a copy and shuffle the elements randomly.

**axis**int, optional

The axis which _x_ is shuffled along. Default is 0.

Returns:

**out**ndarray

Permuted sequence or array range.

Examples

Try it in your browser!

\>>> rng \= np.random.default\_rng()
\>>> rng.permutation(10)
array(\[1, 7, 4, 3, 0, 9, 2, 5, 8, 6\]) # random

Copy to clipboard

\>>> rng.permutation(\[1, 4, 9, 12, 15\])
array(\[15,  1,  9,  4, 12\]) # random

Copy to clipboard

\>>> arr \= np.arange(9).reshape((3, 3))
\>>> rng.permutation(arr)
array(\[\[6, 7, 8\], # random\
       \[0, 1, 2\],\
       \[3, 4, 5\]\])

Copy to clipboard

\>>> rng.permutation("abc")
Traceback (most recent call last):
    ...
numpy.exceptions.AxisError: axis 0 is out of bounds for array of dimension 0

Copy to clipboard

\>>> arr \= np.arange(9).reshape((3, 3))
\>>> rng.permutation(arr, axis\=1)
array(\[\[0, 2, 1\], # random\
       \[3, 5, 4\],\
       \[6, 8, 7\]\])

Copy to clipboard

Go BackOpen In Tab

On this page