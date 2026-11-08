[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.put.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.put.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.put.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.put.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.put.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.put.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.put.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.put.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.put.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.put.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.put.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.put.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.put.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.put.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.put.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.put.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.put.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.put.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.put.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.put.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.put.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.put.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.put[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.put.html#numpy-ma-put "Link to this heading")

========================================================================================================================

ma.put(_a_, _indices_, _values_, _mode\='raise'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7511-L7549)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.put.html#numpy.ma.put "Link to this definition")

Set storage-indexed locations to corresponding values.

This function is equivalent to [`MaskedArray.put`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.put.html#numpy.ma.MaskedArray.put "numpy.ma.MaskedArray.put")
, see that method for details.

See also

[`MaskedArray.put`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.put.html#numpy.ma.MaskedArray.put "numpy.ma.MaskedArray.put")

Examples

Try it in your browser!

Putting values in a masked array:

\>>> a \= np.ma.array(\[1, 2, 3, 4\], mask\=\[False, True, False, False\])
\>>> np.ma.put(a, \[1, 3\], \[10, 30\])
\>>> a
masked\_array(data=\[ 1, 10,  3, 30\],
             mask=False,
       fill\_value=999999)

Copy to clipboard

Using put with a 2D array:

\>>> b \= np.ma.array(\[\[1, 2\], \[3, 4\]\], mask\=\[\[False, True\], \[False, False\]\])
\>>> np.ma.put(b, \[\[0, 1\], \[1, 0\]\], \[\[10, 20\], \[30, 40\]\])
\>>> b
masked\_array(
  data=\[\[40, 30\],\
        \[ 3,  4\]\],
  mask=False,
  fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page