[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.flat.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.char.chararray.flat[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.flat.html#numpy-char-chararray-flat "Link to this heading")

===============================================================================================================================================================

attribute

char.chararray.flat[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.flat.html#numpy.char.chararray.flat "Link to this definition")

A 1-D iterator over the array.

This is a [`numpy.flatiter`](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
 instance, which acts similarly to, but is not a subclass of, Python’s built-in iterator object.

See also

[`flatten`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.flatten.html#numpy.char.chararray.flatten "numpy.char.chararray.flatten")

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