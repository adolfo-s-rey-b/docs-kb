[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.iscontiguous.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_array.iscontiguous.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_array.iscontiguous.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.iscontiguous[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.iscontiguous.html#numpy-ma-masked-array-iscontiguous "Link to this heading")

===========================================================================================================================================================================================

method

ma.masked\_array.iscontiguous()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L4950-L4976)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.iscontiguous.html#numpy.ma.masked_array.iscontiguous "Link to this definition")

Return a boolean indicating whether the data is contiguous.

Parameters:

**None**

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(\[1, 2, 3\])
\>>> x.iscontiguous()
True

Copy to clipboard

[`iscontiguous`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.iscontiguous.html#numpy.ma.masked_array.iscontiguous "numpy.ma.masked_array.iscontiguous")
 returns one of the flags of the masked array:

\>>> x.flags
  C\_CONTIGUOUS : True
  F\_CONTIGUOUS : True
  OWNDATA : False
  WRITEABLE : True
  ALIGNED : True
  WRITEBACKIFCOPY : False

Copy to clipboard

Go BackOpen In Tab

On this page