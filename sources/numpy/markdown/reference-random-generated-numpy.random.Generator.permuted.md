[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permuted.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.permuted.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permuted.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.permuted.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.permuted.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.permuted.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.permuted.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.permuted.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.permuted.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.permuted.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.permuted.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.permuted.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.permuted.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.permuted.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.permuted.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.permuted.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.permuted.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.permuted.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.permuted.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.permuted.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.permuted.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.permuted.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.permuted[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permuted.html#numpy-random-generator-permuted "Link to this heading")

========================================================================================================================================================================================

method

random.Generator.permuted(_x_, _axis\=None_, _out\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permuted.html#numpy.random.Generator.permuted "Link to this definition")

Randomly permute _x_ along axis _axis_.

Unlike [`shuffle`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html#numpy.random.Generator.shuffle "numpy.random.Generator.shuffle")
, each slice along the given axis is shuffled independently of the others.

Parameters:

**x**array\_like, at least one-dimensional

Array to be shuffled.

**axis**int, optional

Slices of _x_ in this axis are shuffled. Each slice is shuffled independently of the others. If _axis_ is None, the flattened array is shuffled.

**out**ndarray, optional

If given, this is the destination of the shuffled array. If _out_ is None, a shuffled copy of the array is returned.

Returns:

ndarray

If _out_ is None, a shuffled copy of _x_ is returned. Otherwise, the shuffled array is stored in _out_, and _out_ is returned

See also

[`shuffle`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html#numpy.random.Generator.shuffle "numpy.random.Generator.shuffle")

[`permutation`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html#numpy.random.Generator.permutation "numpy.random.Generator.permutation")

Notes

An important distinction between methods `shuffle` and `permuted` is how they both treat the `axis` parameter which can be found at [Handling the axis parameter](https://numpy.org/doc/stable/reference/random/generator.html#generator-handling-axis-parameter)
.

Examples

Try it in your browser!

Create a [`numpy.random.Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance:

\>>> rng \= np.random.default\_rng()

Copy to clipboard

Create a test array:

\>>> x \= np.arange(24).reshape(3, 8)
\>>> x
array(\[\[ 0,  1,  2,  3,  4,  5,  6,  7\],\
       \[ 8,  9, 10, 11, 12, 13, 14, 15\],\
       \[16, 17, 18, 19, 20, 21, 22, 23\]\])

Copy to clipboard

Shuffle the rows of _x_:

\>>> y \= rng.permuted(x, axis\=1)
\>>> y
array(\[\[ 4,  3,  6,  7,  1,  2,  5,  0\],  # random\
       \[15, 10, 14,  9, 12, 11,  8, 13\],\
       \[17, 16, 20, 21, 18, 22, 23, 19\]\])

Copy to clipboard

_x_ has not been modified:

\>>> x
array(\[\[ 0,  1,  2,  3,  4,  5,  6,  7\],\
       \[ 8,  9, 10, 11, 12, 13, 14, 15\],\
       \[16, 17, 18, 19, 20, 21, 22, 23\]\])

Copy to clipboard

To shuffle the rows of _x_ in-place, pass _x_ as the _out_ parameter:

\>>> y \= rng.permuted(x, axis\=1, out\=x)
\>>> x
array(\[\[ 3,  0,  4,  7,  1,  6,  2,  5\],  # random\
       \[ 8, 14, 13,  9, 12, 11, 15, 10\],\
       \[17, 18, 16, 22, 19, 23, 20, 21\]\])

Copy to clipboard

Note that when the `out` parameter is given, the return value is `out`:

\>>> y is x
True

Copy to clipboard

Go BackOpen In Tab

On this page