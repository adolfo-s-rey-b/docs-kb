[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.choose.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.choose.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.choose.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.choose.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.choose.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.choose.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.choose.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.choose.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.choose.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.choose.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.choose.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.choose.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.choose.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.choose.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.choose.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.choose.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.choose.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.choose.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.choose.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.choose.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.choose.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.choose.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.choose[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.choose.html#numpy-ma-choose "Link to this heading")

=================================================================================================================================

ma.choose(_indices_, _choices_, _out\=None_, _mode\='raise'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L8022-L8095)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.choose.html#numpy.ma.choose "Link to this definition")

Use an index array to construct a new array from a list of choices.

Given an array of integers and a list of n choice arrays, this method will create a new array that merges each of the choice arrays. Where a value in _index_ is i, the new array will have the value that choices\[i\] contains in the same place.

Parameters:

**indices**ndarray of ints

This array must contain integers in `[0, n-1]`, where n is the number of choices.

**choices**sequence of arrays

Choice arrays. The index array and all of the choices should be broadcastable to the same shape.

**out**array, optional

If provided, the result will be inserted into this array. It should be of the appropriate shape and [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
.

**mode**{‘raise’, ‘wrap’, ‘clip’}, optional

Specifies how out-of-bounds indices will behave.

*   ‘raise’ : raise an error
    
*   ‘wrap’ : wrap around
    
*   ‘clip’ : clip to the range
    

Returns:

**merged\_array**array

See also

[`choose`](https://numpy.org/doc/stable/reference/generated/numpy.choose.html#numpy.choose "numpy.choose")

equivalent function

Examples

Try it in your browser!

\>>> import numpy as np
\>>> choice \= np.array(\[\[1,1,1\], \[2,2,2\], \[3,3,3\]\])
\>>> a \= np.array(\[2, 1, 0\])
\>>> np.ma.choose(a, choice)
masked\_array(data=\[3, 2, 1\],
             mask=False,
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page