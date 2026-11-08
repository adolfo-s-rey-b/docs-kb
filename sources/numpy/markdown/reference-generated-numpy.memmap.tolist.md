[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.memmap.tolist.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.memmap.tolist.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.memmap.tolist.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.memmap.tolist.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.memmap.tolist.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.memmap.tolist.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.memmap.tolist.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.memmap.tolist.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.memmap.tolist.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.memmap.tolist.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.memmap.tolist.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.memmap.tolist.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.memmap.tolist.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.memmap.tolist.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.memmap.tolist.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.memmap.tolist.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.memmap.tolist.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.memmap.tolist.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.memmap.tolist.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.memmap.tolist.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.memmap.tolist.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.memmap.tolist.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.memmap.tolist[#](https://numpy.org/doc/stable/reference/generated/numpy.memmap.tolist.html#numpy-memmap-tolist "Link to this heading")

=============================================================================================================================================

method

memmap.tolist()[#](https://numpy.org/doc/stable/reference/generated/numpy.memmap.tolist.html#numpy.memmap.tolist "Link to this definition")

Return the array as an `a.ndim`\-levels deep nested list of Python scalars.

Return a copy of the array data as a (nested) Python list. Data items are converted to the nearest compatible builtin Python type, via the [`item`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.item.html#numpy.ndarray.item "numpy.ndarray.item")
 method.

If `a.ndim` is 0, then since the depth of the nested list is 0, it will not be a list at all, but a simple Python scalar.

Parameters:

**none**

Returns:

**y**object, or list of object, or list of list of object, or …

The possibly nested list of array elements.

Notes

The array may be recreated via `a = np.array(a.tolist())`, although this may sometimes lose precision.

Examples

Try it in your browser!

For a 1D array, `a.tolist()` is almost the same as `list(a)`, except that `tolist` changes numpy scalars to Python scalars:

\>>> import numpy as np
\>>> a \= np.uint32(\[1, 2\])
\>>> a\_list \= list(a)
\>>> a\_list
\[np.uint32(1), np.uint32(2)\]
\>>> type(a\_list\[0\])
<class 'numpy.uint32'>
\>>> a\_tolist \= a.tolist()
\>>> a\_tolist
\[1, 2\]
\>>> type(a\_tolist\[0\])
<class 'int'>

Copy to clipboard

Additionally, for a 2D array, `tolist` applies recursively:

\>>> a \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> list(a)
\[array(\[1, 2\]), array(\[3, 4\])\]
\>>> a.tolist()
\[\[1, 2\], \[3, 4\]\]

Copy to clipboard

The base case for this recursion is a 0D array:

\>>> a \= np.array(1)
\>>> list(a)
Traceback (most recent call last):
  ...
TypeError: iteration over a 0-d array
\>>> a.tolist()
1

Copy to clipboard

Go BackOpen In Tab

On this page