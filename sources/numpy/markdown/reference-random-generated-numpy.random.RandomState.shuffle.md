[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.shuffle.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.shuffle.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.shuffle.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.shuffle.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.shuffle.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.shuffle.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.shuffle.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.shuffle.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.shuffle.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.shuffle.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.shuffle.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.shuffle.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.shuffle.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.shuffle.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.shuffle.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.shuffle.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.shuffle.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.shuffle.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.shuffle.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.shuffle.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.shuffle.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.shuffle.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.shuffle[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.shuffle.html#numpy-random-randomstate-shuffle "Link to this heading")

===========================================================================================================================================================================================

method

random.RandomState.shuffle(_x_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.shuffle.html#numpy.random.RandomState.shuffle "Link to this definition")

Modify a sequence in-place by shuffling its contents.

This function only shuffles the array along the first axis of a multi-dimensional array. The order of sub-arrays is changed but their contents remains the same.

Note

New code should use the [`shuffle`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html#numpy.random.Generator.shuffle "numpy.random.Generator.shuffle")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**x**ndarray or MutableSequence

The array, list or mutable sequence to be shuffled.

Returns:

None

See also

[`random.Generator.shuffle`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html#numpy.random.Generator.shuffle "numpy.random.Generator.shuffle")

which should be used for new code.

Examples

Try it in your browser!

\>>> arr \= np.arange(10)
\>>> np.random.shuffle(arr)
\>>> arr
\[1 7 5 2 9 4 3 6 0 8\] # random

Copy to clipboard

Multi-dimensional arrays are only shuffled along the first axis:

\>>> arr \= np.arange(9).reshape((3, 3))
\>>> np.random.shuffle(arr)
\>>> arr
array(\[\[3, 4, 5\], # random\
       \[6, 7, 8\],\
       \[0, 1, 2\]\])

Copy to clipboard

Go BackOpen In Tab

On this page