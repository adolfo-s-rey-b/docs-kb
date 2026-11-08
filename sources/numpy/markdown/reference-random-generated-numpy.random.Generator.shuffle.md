[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.shuffle.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.shuffle.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.shuffle.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.shuffle.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.shuffle.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.shuffle.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.shuffle.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.shuffle.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.shuffle.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.shuffle.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.shuffle.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.shuffle.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.shuffle.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.shuffle.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.shuffle.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.shuffle.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.shuffle.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.shuffle.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.shuffle.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.shuffle.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.shuffle[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html#numpy-random-generator-shuffle "Link to this heading")

=====================================================================================================================================================================================

method

random.Generator.shuffle(_x_, _axis\=0_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html#numpy.random.Generator.shuffle "Link to this definition")

Modify an array or sequence in-place by shuffling its contents.

The order of sub-arrays is changed but their contents remains the same.

Parameters:

**x**ndarray or MutableSequence

The array, list or mutable sequence to be shuffled.

**axis**int, optional

The axis which _x_ is shuffled along. Default is 0. It is only supported on [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 objects.

Returns:

None

See also

[`permuted`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permuted.html#numpy.random.Generator.permuted "numpy.random.Generator.permuted")

[`permutation`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html#numpy.random.Generator.permutation "numpy.random.Generator.permutation")

Notes

An important distinction between methods `shuffle` and `permuted` is how they both treat the `axis` parameter which can be found at [Handling the axis parameter](https://numpy.org/doc/stable/reference/random/generator.html#generator-handling-axis-parameter)
.

Examples

Try it in your browser!

\>>> rng \= np.random.default\_rng()
\>>> arr \= np.arange(10)
\>>> arr
array(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\])
\>>> rng.shuffle(arr)
\>>> arr
array(\[2, 0, 7, 5, 1, 4, 8, 9, 3, 6\]) # random

Copy to clipboard

\>>> arr \= np.arange(9).reshape((3, 3))
\>>> arr
array(\[\[0, 1, 2\],\
       \[3, 4, 5\],\
       \[6, 7, 8\]\])
\>>> rng.shuffle(arr)
\>>> arr
array(\[\[3, 4, 5\], # random\
       \[6, 7, 8\],\
       \[0, 1, 2\]\])

Copy to clipboard

\>>> arr \= np.arange(9).reshape((3, 3))
\>>> arr
array(\[\[0, 1, 2\],\
       \[3, 4, 5\],\
       \[6, 7, 8\]\])
\>>> rng.shuffle(arr, axis\=1)
\>>> arr
array(\[\[2, 0, 1\], # random\
       \[5, 3, 4\],\
       \[8, 6, 7\]\])

Copy to clipboard

Go BackOpen In Tab

On this page