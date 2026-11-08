[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.nested_iters.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.nested_iters.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.nested_iters.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.nested_iters.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.nested_iters.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.nested_iters.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.nested_iters.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.nested_iters.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.nested_iters.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.nested_iters.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.nested_iters.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.nested_iters.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.nested_iters.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.nested_iters.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.nested_iters.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.nested_iters.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.nested_iters.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.nested_iters.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.nested_iters.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.nested_iters.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.nested_iters.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.nested_iters.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.nested\_iters[#](https://numpy.org/doc/stable/reference/generated/numpy.nested_iters.html#numpy-nested-iters "Link to this heading")

===========================================================================================================================================

numpy.nested\_iters(_op_, _axes_, _flags\=None_, _op\_flags\=None_, _op\_dtypes\=None_, _order\='K'_, _casting\='safe'_, _buffersize\=0_)[#](https://numpy.org/doc/stable/reference/generated/numpy.nested_iters.html#numpy.nested_iters "Link to this definition")

Create nditers for use in nested loops

Create a tuple of [`nditer`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html#numpy.nditer "numpy.nditer")
 objects which iterate in nested loops over different axes of the op argument. The first iterator is used in the outermost loop, the last in the innermost loop. Advancing one will change the subsequent iterators to point at its new element.

Parameters:

**op**ndarray or sequence of array\_like

The array(s) to iterate over.

**axes**list of list of int

Each item is used as an “op\_axes” argument to an nditer

**flags, op\_flags, op\_dtypes, order, casting, buffersize (optional)**

See [`nditer`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html#numpy.nditer "numpy.nditer")
 parameters of the same name

Returns:

**iters**tuple of nditer

An nditer for each item in _axes_, outermost first

See also

[`nditer`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html#numpy.nditer "numpy.nditer")

Examples

Try it in your browser!

Basic usage. Note how y is the “flattened” version of \[a\[:, 0, :\], a\[:, 1, 0\], a\[:, 2, :\]\] since we specified the first iter’s axes as \[1\]

\>>> import numpy as np
\>>> a \= np.arange(12).reshape(2, 3, 2)
\>>> i, j \= np.nested\_iters(a, \[\[1\], \[0, 2\]\], flags\=\["multi\_index"\])
\>>> for x in i:
...      print(i.multi\_index)
...      for y in j:
...          print('', j.multi\_index, y)
(0,)
 (0, 0) 0
 (0, 1) 1
 (1, 0) 6
 (1, 1) 7
(1,)
 (0, 0) 2
 (0, 1) 3
 (1, 0) 8
 (1, 1) 9
(2,)
 (0, 0) 4
 (0, 1) 5
 (1, 0) 10
 (1, 1) 11

Copy to clipboard

Go BackOpen In Tab

On this page