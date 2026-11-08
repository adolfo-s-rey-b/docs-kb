[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.fromfunction.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.fromfunction.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.fromfunction.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.fromfunction.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.fromfunction.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.fromfunction.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.fromfunction.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.fromfunction.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.fromfunction.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.fromfunction.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.fromfunction.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.fromfunction.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.fromfunction.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.fromfunction.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.fromfunction.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.fromfunction.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.fromfunction.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.fromfunction.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.fromfunction.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.fromfunction.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.fromfunction.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.fromfunction.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.fromfunction[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.fromfunction.html#numpy-ma-fromfunction "Link to this heading")

===================================================================================================================================================

ma.fromfunction(_function_, _shape_, _\*_, _dtype=<class 'float'>_, _like=None_, _\*\*kwargs_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L8820-L8832)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.fromfunction.html#numpy.ma.fromfunction "Link to this definition")

Construct an array by executing a function over each coordinate.

The resulting array therefore has a value `fn(x, y, z)` at coordinate `(x, y, z)`.

Parameters:

**function**callable

The function is called with N parameters, where N is the rank of [`shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")
. Each parameter represents the coordinates of the array varying along a specific axis. For example, if [`shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")
 were `(2, 2)`, then the parameters would be `array([[0, 0], [1, 1]])` and `array([[0, 1], [0, 1]])`

**shape**(N,) tuple of ints

Shape of the output array, which also determines the shape of the coordinate arrays passed to _function_.

**dtype**data-type, optional

Data-type of the coordinate arrays passed to _function_. By default, [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is float.

**like**array\_like, optional

Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as `like` supports the `__array_function__` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

Returns:

fromfunction: MaskedArray

The result of the call to _function_ is passed back directly. Therefore the shape of [`fromfunction`](https://numpy.org/doc/stable/reference/generated/numpy.fromfunction.html#numpy.fromfunction "numpy.fromfunction")
 is completely determined by _function_. If _function_ returns a scalar value, the shape of [`fromfunction`](https://numpy.org/doc/stable/reference/generated/numpy.fromfunction.html#numpy.fromfunction "numpy.fromfunction")
 would not match the [`shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")
 parameter.

See also

[`indices`](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#numpy.indices "numpy.indices")
, [`meshgrid`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")

Notes

Keywords other than [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 and _like_ are passed to _function_.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.fromfunction(lambda i, j: i, (2, 2), dtype\=np.float64)
array(\[\[0., 0.\],\
       \[1., 1.\]\])

Copy to clipboard

\>>> np.fromfunction(lambda i, j: j, (2, 2), dtype\=np.float64)
array(\[\[0., 1.\],\
       \[0., 1.\]\])

Copy to clipboard

\>>> np.fromfunction(lambda i, j: i \== j, (3, 3), dtype\=np.int\_)
array(\[\[ True, False, False\],\
       \[False,  True, False\],\
       \[False, False,  True\]\])

Copy to clipboard

\>>> np.fromfunction(lambda i, j: i + j, (3, 3), dtype\=np.int\_)
array(\[\[0, 1, 2\],\
       \[1, 2, 3\],\
       \[2, 3, 4\]\])

Copy to clipboard

Go BackOpen In Tab

On this page