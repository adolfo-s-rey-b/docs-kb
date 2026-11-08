[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.triu.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.triu.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.triu.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.triu.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.triu.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.triu.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.triu.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.triu.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.triu.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.triu.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.triu.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.triu.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.triu.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.triu.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.triu.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.triu.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.triu.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.triu.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.triu.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.triu.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.triu.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.triu.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.triu[#](https://numpy.org/doc/stable/reference/generated/numpy.triu.html#numpy-triu "Link to this heading")

==================================================================================================================

numpy.triu(_m_, _k\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_twodim_base_impl.py#L537-L579)
[#](https://numpy.org/doc/stable/reference/generated/numpy.triu.html#numpy.triu "Link to this definition")

Upper triangle of an array.

Return a copy of an array with the elements below the _k_\-th diagonal zeroed. For arrays with `ndim` exceeding 2, [`triu`](https://numpy.org/doc/stable/reference/generated/numpy.triu.html#numpy.triu "numpy.triu")
 will apply to the final two axes.

Please refer to the documentation for [`tril`](https://numpy.org/doc/stable/reference/generated/numpy.tril.html#numpy.tril "numpy.tril")
 for further details.

See also

[`tril`](https://numpy.org/doc/stable/reference/generated/numpy.tril.html#numpy.tril "numpy.tril")

lower triangle of an array

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.triu(\[\[1,2,3\],\[4,5,6\],\[7,8,9\],\[10,11,12\]\], \-1)
array(\[\[ 1,  2,  3\],\
       \[ 4,  5,  6\],\
       \[ 0,  8,  9\],\
       \[ 0,  0, 12\]\])

Copy to clipboard

\>>> np.triu(np.arange(3\*4\*5).reshape(3, 4, 5))
array(\[\[\[ 0,  1,  2,  3,  4\],\
        \[ 0,  6,  7,  8,  9\],\
        \[ 0,  0, 12, 13, 14\],\
        \[ 0,  0,  0, 18, 19\]\],\
       \[\[20, 21, 22, 23, 24\],\
        \[ 0, 26, 27, 28, 29\],\
        \[ 0,  0, 32, 33, 34\],\
        \[ 0,  0,  0, 38, 39\]\],\
       \[\[40, 41, 42, 43, 44\],\
        \[ 0, 46, 47, 48, 49\],\
        \[ 0,  0, 52, 53, 54\],\
        \[ 0,  0,  0, 58, 59\]\]\])

Copy to clipboard

Go BackOpen In Tab

On this page