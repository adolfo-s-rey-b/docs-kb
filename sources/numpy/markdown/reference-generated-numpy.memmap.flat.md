[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.memmap.flat.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.memmap.flat.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.memmap.flat.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.memmap.flat.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.memmap.flat.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.memmap.flat.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.memmap.flat.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.memmap.flat.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.memmap.flat.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.memmap.flat.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.memmap.flat.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.memmap.flat.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.memmap.flat.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.memmap.flat.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.memmap.flat.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.memmap.flat.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.memmap.flat.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.memmap.flat.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.memmap.flat.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.memmap.flat.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.memmap.flat.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.memmap.flat.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.memmap.flat[#](https://numpy.org/doc/stable/reference/generated/numpy.memmap.flat.html#numpy-memmap-flat "Link to this heading")

=======================================================================================================================================

attribute

memmap.flat[#](https://numpy.org/doc/stable/reference/generated/numpy.memmap.flat.html#numpy.memmap.flat "Link to this definition")

A 1-D iterator over the array.

This is a [`numpy.flatiter`](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
 instance, which acts similarly to, but is not a subclass of, Python’s built-in iterator object.

See also

[`flatten`](https://numpy.org/doc/stable/reference/generated/numpy.memmap.flatten.html#numpy.memmap.flatten "numpy.memmap.flatten")

Return a copy of the array collapsed into one dimension.

[`flatiter`](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(1, 7).reshape(2, 3)
\>>> x
array(\[\[1, 2, 3\],\
       \[4, 5, 6\]\])
\>>> x.flat\[3\]
4
\>>> x.T
array(\[\[1, 4\],\
       \[2, 5\],\
       \[3, 6\]\])
\>>> x.T.flat\[3\]
5
\>>> type(x.flat)
<class 'numpy.flatiter'>

Copy to clipboard

An assignment example:

\>>> x.flat \= 3; x
array(\[\[3, 3, 3\],\
       \[3, 3, 3\]\])
\>>> x.flat\[\[1,4\]\] \= 1; x
array(\[\[3, 1, 3\],\
       \[3, 1, 3\]\])

Copy to clipboard

Go BackOpen In Tab

On this page