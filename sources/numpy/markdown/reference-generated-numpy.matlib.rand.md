[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matlib.rand.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matlib.rand.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matlib.rand.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matlib.rand.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matlib.rand.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matlib.rand.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matlib.rand.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matlib.rand.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matlib.rand.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matlib.rand.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matlib.rand.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matlib.rand.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matlib.rand.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matlib.rand.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matlib.rand.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matlib.rand.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matlib.rand.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matlib.rand.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matlib.rand.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matlib.rand.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matlib.rand.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matlib.rand.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matlib.rand[#](https://numpy.org/doc/stable/reference/generated/numpy.matlib.rand.html#numpy-matlib-rand "Link to this heading")

=======================================================================================================================================

matlib.rand(_\*args_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matlib.py#L233-L277)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matlib.rand.html#numpy.matlib.rand "Link to this definition")

Return a matrix of random values with given shape.

Create a matrix of the given shape and propagate it with random samples from a uniform distribution over `[0, 1)`.\
\
Parameters:\
\
**\*args**Arguments\
\
Shape of the output. If given as N integers, each integer specifies the size of one dimension. If given as a tuple, this tuple gives the complete shape.\
\
Returns:\
\
**out**ndarray\
\
The matrix of random values with shape given by _\*args_.\
\
See also\
\
[`randn`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.randn.html#numpy.matlib.randn "numpy.matlib.randn")\
, [`numpy.random.RandomState.rand`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.rand.html#numpy.random.RandomState.rand "numpy.random.RandomState.rand")\
\
Examples\
\
Try it in your browser!\
\
\>>> np.random.seed(123)\
\>>> import numpy.matlib\
\>>> np.matlib.rand(2, 3)\
matrix(\[\[0.69646919, 0.28613933, 0.22685145\],\
        \[0.55131477, 0.71946897, 0.42310646\]\])\
\>>> np.matlib.rand((2, 3))\
matrix(\[\[0.9807642 , 0.68482974, 0.4809319 \],\
        \[0.39211752, 0.34317802, 0.72904971\]\])\
\
Copy to clipboard\
\
If the first argument is a tuple, other arguments are ignored:\
\
\>>> np.matlib.rand((2, 3), 4)\
matrix(\[\[0.43857224, 0.0596779 , 0.39804426\],\
        \[0.73799541, 0.18249173, 0.17545176\]\])\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
On this page