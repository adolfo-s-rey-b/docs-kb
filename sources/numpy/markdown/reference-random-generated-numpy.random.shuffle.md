[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.shuffle.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.shuffle[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.shuffle.html#numpy-random-shuffle "Link to this heading")

=======================================================================================================================================================

random.shuffle(_x_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.shuffle.html#numpy.random.shuffle "Link to this definition")

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