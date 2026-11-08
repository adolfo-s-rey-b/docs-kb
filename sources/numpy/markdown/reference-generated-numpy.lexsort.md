[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lexsort.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lexsort.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lexsort.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lexsort.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lexsort.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lexsort.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lexsort.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lexsort.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lexsort.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lexsort.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lexsort.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lexsort.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lexsort.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lexsort.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lexsort.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lexsort.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lexsort.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lexsort.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lexsort.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lexsort.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lexsort[#](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy-lexsort "Link to this heading")

===========================================================================================================================

numpy.lexsort(_keys_, _axis\=\-1_)[#](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort "Link to this definition")

Perform an indirect stable sort using a sequence of keys.

Given multiple sorting keys, lexsort returns an array of integer indices that describes the sort order by multiple keys. The last key in the sequence is used for the primary sort order, ties are broken by the second-to-last key, and so on.

Parameters:

**keys**(k, m, n, …) array-like

The _k_ keys to be sorted. The _last_ key (e.g, the last row if _keys_ is a 2D array) is the primary sort key. Each element of _keys_ along the zeroth axis must be an array-like object of the same shape.

**axis**int, optional

Axis to be indirectly sorted. By default, sort over the last axis of each sequence. Separate slices along _axis_ sorted over independently; see last example.

Returns:

**indices**(m, n, …) ndarray of ints

Array of indices that sort the keys along the specified axis.

See also

[`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")

Indirect sort.

[`ndarray.sort`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sort.html#numpy.ndarray.sort "numpy.ndarray.sort")

In-place sort.

[`sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")

Return a sorted copy of an array.

Examples

Try it in your browser!

Sort names: first by surname, then by name.

\>>> import numpy as np
\>>> surnames \=    ('Hertz',    'Galilei', 'Hertz')
\>>> first\_names \= ('Heinrich', 'Galileo', 'Gustav')
\>>> ind \= np.lexsort((first\_names, surnames))
\>>> ind
array(\[1, 2, 0\])

Copy to clipboard

\>>> \[surnames\[i\] + ", " + first\_names\[i\] for i in ind\]
\['Galilei, Galileo', 'Hertz, Gustav', 'Hertz, Heinrich'\]

Copy to clipboard

Sort according to two numerical keys, first by elements of `a`, then breaking ties according to elements of `b`:

\>>> a \= \[1, 5, 1, 4, 3, 4, 4\]  \# First sequence
\>>> b \= \[9, 4, 0, 4, 0, 2, 1\]  \# Second sequence
\>>> ind \= np.lexsort((b, a))  \# Sort by \`a\`, then by \`b\`
\>>> ind
array(\[2, 0, 4, 6, 5, 3, 1\])
\>>> \[(a\[i\], b\[i\]) for i in ind\]
\[(1, 0), (1, 9), (3, 0), (4, 1), (4, 2), (4, 4), (5, 4)\]

Copy to clipboard

Compare against [`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")
, which would sort each key independently.

\>>> np.argsort((b, a), kind\='stable')
array(\[\[2, 4, 6, 5, 1, 3, 0\],\
       \[0, 2, 4, 3, 5, 6, 1\]\])

Copy to clipboard

To sort lexicographically with [`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")
, we would need to provide a structured array.

\>>> x \= np.array(\[(ai, bi) for ai, bi in zip(a, b)\],
...              dtype \= np.dtype(\[('x', int), ('y', int)\]))
\>>> np.argsort(x)  \# or np.argsort(x, order=('x', 'y'))
array(\[2, 0, 4, 6, 5, 3, 1\])

Copy to clipboard

The zeroth axis of _keys_ always corresponds with the sequence of keys, so 2D arrays are treated just like other sequences of keys.

\>>> arr \= np.asarray(\[b, a\])
\>>> ind2 \= np.lexsort(arr)
\>>> np.testing.assert\_equal(ind2, ind)

Copy to clipboard

Accordingly, the _axis_ parameter refers to an axis of _each_ key, not of the _keys_ argument itself. For instance, the array `arr` is treated as a sequence of two 1-D keys, so specifying `axis=0` is equivalent to using the default axis, `axis=-1`.

\>>> np.testing.assert\_equal(np.lexsort(arr, axis\=0),
...                         np.lexsort(arr, axis\=-1))

Copy to clipboard

For higher-dimensional arrays, the axis parameter begins to matter. The resulting array has the same shape as each key, and the values are what we would expect if [`lexsort`](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort "numpy.lexsort")
 were performed on corresponding slices of the keys independently. For instance,

\>>> x \= \[\[1, 2, 3, 4\],\
...      \[4, 3, 2, 1\],\
...      \[2, 1, 4, 3\]\]
\>>> y \= \[\[2, 2, 1, 1\],\
...      \[1, 2, 1, 2\],\
...      \[1, 1, 2, 1\]\]
\>>> np.lexsort((x, y), axis\=1)
array(\[\[2, 3, 0, 1\],\
       \[2, 0, 3, 1\],\
       \[1, 0, 3, 2\]\])

Copy to clipboard

Each row of the result is what we would expect if we were to perform [`lexsort`](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort "numpy.lexsort")
 on the corresponding row of the keys:

\>>> for i in range(3):
...     print(np.lexsort((x\[i\], y\[i\])))
\[2 3 0 1\]
\[2 0 3 1\]
\[1 0 3 2\]

Copy to clipboard

Go BackOpen In Tab

On this page