[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.rand.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.rand.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.rand.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.rand.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.rand.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.rand.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.rand.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.rand.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.rand.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.rand.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.rand.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.rand.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.rand.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.rand.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.rand.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.rand.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.rand.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.rand.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.rand.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.rand.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.rand.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.rand.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.rand[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.rand.html#numpy-random-randomstate-rand "Link to this heading")

==================================================================================================================================================================================

method

random.RandomState.rand(_d0_, _d1_, _..._, _dn_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.rand.html#numpy.random.RandomState.rand "Link to this definition")

Random values in a given shape.

Note

This is a convenience function for users porting code from Matlab, and wraps [`random_sample`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.random_sample.html#numpy.random.RandomState.random_sample "numpy.random.RandomState.random_sample")
. That function takes a tuple to specify the size of the output, which is consistent with other NumPy functions like [`numpy.zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
 and [`numpy.ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
.

Create an array of the given shape and populate it with random samples from a uniform distribution over `[0, 1)`.\
\
Parameters:\
\
**d0, d1, …, dn**int, optional\
\
The dimensions of the returned array, must be non-negative. If no argument is given a single Python float is returned.\
\
Returns:\
\
**out**ndarray, shape `(d0, d1, ..., dn)`\
\
Random values.\
\
See also\
\
[`random`](https://numpy.org/doc/stable/reference/random/index.html#module-numpy.random "numpy.random")\
\
Examples\
\
Try it in your browser!\
\
\>>> np.random.rand(3,2)\
array(\[\[ 0.14022471,  0.96360618\],  #random\
       \[ 0.37601032,  0.25528411\],  #random\
       \[ 0.49313049,  0.94909878\]\]) #random\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
On this page