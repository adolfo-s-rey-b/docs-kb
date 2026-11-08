[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.tril.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.tril.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.tril.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.tril.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.tril.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.tril.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.tril.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.tril.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.tril.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.tril.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.tril.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.tril.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.tril.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.tril.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.tril.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.tril.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.tril.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.tril.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.tril.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.tril.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.tril.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.tril.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.tril[#](https://numpy.org/doc/stable/reference/generated/numpy.tril.html#numpy-tril "Link to this heading")

==================================================================================================================

numpy.tril(_m_, _k\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_twodim_base_impl.py#L481-L534)
[#](https://numpy.org/doc/stable/reference/generated/numpy.tril.html#numpy.tril "Link to this definition")

Lower triangle of an array.

Return a copy of an array with elements above the _k_\-th diagonal zeroed. For arrays with `ndim` exceeding 2, [`tril`](https://numpy.org/doc/stable/reference/generated/numpy.tril.html#numpy.tril "numpy.tril")
 will apply to the final two axes.

Parameters:

**m**array\_like, shape (…, M, N)

Input array.

**k**int, optional

Diagonal above which to zero elements. _k = 0_ (the default) is the main diagonal, _k < 0_ is below it and _k > 0_ is above.

Returns:

**tril**ndarray, shape (…, M, N)

Lower triangle of _m_, of same shape and data-type as _m_.

See also

[`triu`](https://numpy.org/doc/stable/reference/generated/numpy.triu.html#numpy.triu "numpy.triu")

same thing, only for the upper triangle

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.tril(\[\[1,2,3\],\[4,5,6\],\[7,8,9\],\[10,11,12\]\], \-1)
array(\[\[ 0,  0,  0\],\
       \[ 4,  0,  0\],\
       \[ 7,  8,  0\],\
       \[10, 11, 12\]\])

Copy to clipboard

\>>> np.tril(np.arange(3\*4\*5).reshape(3, 4, 5))
array(\[\[\[ 0,  0,  0,  0,  0\],\
        \[ 5,  6,  0,  0,  0\],\
        \[10, 11, 12,  0,  0\],\
        \[15, 16, 17, 18,  0\]\],\
       \[\[20,  0,  0,  0,  0\],\
        \[25, 26,  0,  0,  0\],\
        \[30, 31, 32,  0,  0\],\
        \[35, 36, 37, 38,  0\]\],\
       \[\[40,  0,  0,  0,  0\],\
        \[45, 46,  0,  0,  0\],\
        \[50, 51, 52,  0,  0\],\
        \[55, 56, 57, 58,  0\]\]\])

Copy to clipboard

Go BackOpen In Tab

On this page