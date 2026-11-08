[Skip to main content](https://numpy.org/doc/stable/user/how-to-partition.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/user/how-to-partition.html)
[2.5 (stable)](https://numpy.org/doc/stable/user/how-to-partition.html)
[2.4](https://numpy.org/doc/2.4/user/how-to-partition.html)
[2.3](https://numpy.org/doc/2.3/user/how-to-partition.html)
[2.2](https://numpy.org/doc/2.2/user/how-to-partition.html)
[2.1](https://numpy.org/doc/2.1/user/how-to-partition.html)
[2.0](https://numpy.org/doc/2.0/user/how-to-partition.html)
[1.26](https://numpy.org/doc/1.26/user/how-to-partition.html)
[1.25](https://numpy.org/doc/1.25/user/how-to-partition.html)
[1.24](https://numpy.org/doc/1.24/user/how-to-partition.html)
[1.23](https://numpy.org/doc/1.23/user/how-to-partition.html)
[1.22](https://numpy.org/doc/1.22/user/how-to-partition.html)
[1.21](https://numpy.org/doc/1.21/user/how-to-partition.html)
[1.20](https://numpy.org/doc/1.20/user/how-to-partition.html)
[1.19](https://numpy.org/doc/1.19/user/how-to-partition.html)
[1.18](https://numpy.org/doc/1.18/user/how-to-partition.html)
[1.17](https://numpy.org/doc/1.17/user/how-to-partition.html)
[1.16](https://numpy.org/doc/1.16/user/how-to-partition.html)
[1.15](https://numpy.org/doc/1.15/user/how-to-partition.html)
[1.14](https://numpy.org/doc/1.14/user/how-to-partition.html)
[1.13](https://numpy.org/doc/1.13/user/how-to-partition.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

How to create arrays with regularly-spaced values[#](https://numpy.org/doc/stable/user/how-to-partition.html#how-to-create-arrays-with-regularly-spaced-values "Link to this heading")

=======================================================================================================================================================================================

There are a few NumPy functions that are similar in application, but which provide slightly different results, which may cause confusion if one is not sure when and how to use them. The following guide aims to list these functions and describe their recommended usage.

The functions mentioned here are

*   [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
    
*   [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
    
*   [`numpy.geomspace`](https://numpy.org/doc/stable/reference/generated/numpy.geomspace.html#numpy.geomspace "numpy.geomspace")
    
*   [`numpy.logspace`](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
    
*   [`numpy.meshgrid`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
    
*   [`numpy.mgrid`](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
    
*   [`numpy.ogrid`](https://numpy.org/doc/stable/reference/generated/numpy.ogrid.html#numpy.ogrid "numpy.ogrid")
    

1D domains (intervals)[#](https://numpy.org/doc/stable/user/how-to-partition.html#d-domains-intervals "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

### `linspace` vs. `arange`[#](https://numpy.org/doc/stable/user/how-to-partition.html#linspace-vs-arange "Link to this heading")

Both [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
 and [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
 provide ways to partition an interval (a 1D domain) into equal-length subintervals. These partitions will vary depending on the chosen starting and ending points, and the **step** (the length of the subintervals).

*   **Use** [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
     **if you want integer steps.**
    
    [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
     relies on step size to determine how many elements are in the returned array, which excludes the endpoint. This is determined through the `step` argument to `arange`.
    
    Example:
    
    \>>> np.arange(0, 10, 2)  \# np.arange(start, stop, step)
    array(\[0, 2, 4, 6, 8\])
    
    Copy to clipboard
    
    The arguments `start` and `stop` should be integer or real, but not complex numbers. [`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
     is similar to the Python built-in [`range`](https://docs.python.org/3/library/stdtypes.html#range "(in Python v3.14)")
    .
    
    Floating-point inaccuracies can make `arange` results with floating-point numbers confusing. In this case, you should use [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
     instead.
    
*   **Use** [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
     **if you want the endpoint to be included in the result, or if you are using a non-integer step size.**
    
    [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
     _can_ include the endpoint and determines step size from the _num_ argument, which specifies the number of elements in the returned array.
    
    The inclusion of the endpoint is determined by an optional boolean argument `endpoint`, which defaults to `True`. Note that selecting `endpoint=False` will change the step size computation, and the subsequent output for the function.
    
    Example:
    
    \>>> np.linspace(0.1, 0.2, num\=5)  \# np.linspace(start, stop, num)
    array(\[0.1  , 0.125, 0.15 , 0.175, 0.2  \])
    \>>> np.linspace(0.1, 0.2, num\=5, endpoint\=False)
    array(\[0.1, 0.12, 0.14, 0.16, 0.18\])
    
    Copy to clipboard
    
    [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
     can also be used with complex arguments:
    
    \>>> np.linspace(1+1.j, 4, 5, dtype\=np.complex64)
    array(\[1.  +1.j  , 1.75+0.75j, 2.5 +0.5j , 3.25+0.25j, 4.  +0.j  \],
          dtype=complex64)
    
    Copy to clipboard
    

### Other examples[#](https://numpy.org/doc/stable/user/how-to-partition.html#other-examples "Link to this heading")

1.  Unexpected results may happen if floating point values are used as `step` in `numpy.arange`. To avoid this, make sure all floating point conversion happens after the computation of results. For example, replace
    
    \>>> list(np.arange(0.1,0.4,0.1).round(1))
    \[0.1, 0.2, 0.3, 0.4\]  # endpoint should not be included!
    
    Copy to clipboard
    
    with
    
    \>>> list(np.arange(1, 4, 1) / 10.0)
    \[0.1, 0.2, 0.3\]  # expected result
    
    Copy to clipboard
    
2.  Note that
    
    \>>> np.arange(0, 1.12, 0.04)
    array(\[0.  , 0.04, 0.08, 0.12, 0.16, 0.2 , 0.24, 0.28, 0.32, 0.36, 0.4 ,\
           0.44, 0.48, 0.52, 0.56, 0.6 , 0.64, 0.68, 0.72, 0.76, 0.8 , 0.84,\
           0.88, 0.92, 0.96, 1.  , 1.04, 1.08, 1.12\])
    
    Copy to clipboard
    
    and
    
    \>>> np.arange(0, 1.08, 0.04)
    array(\[0.  , 0.04, 0.08, 0.12, 0.16, 0.2 , 0.24, 0.28, 0.32, 0.36, 0.4 ,\
           0.44, 0.48, 0.52, 0.56, 0.6 , 0.64, 0.68, 0.72, 0.76, 0.8 , 0.84,\
           0.88, 0.92, 0.96, 1.  , 1.04\])
    
    Copy to clipboard
    
    These differ because of numeric noise. When using floating point values, it is possible that `0 + 0.04 * 28 < 1.12`, and so `1.12` is in the interval. In fact, this is exactly the case:
    
    \>>> 1.12/0.04
    28.000000000000004
    
    Copy to clipboard
    
    But `0 + 0.04 * 27 >= 1.08` so that 1.08 is excluded:
    
    \>>> 1.08/0.04
    27.0
    
    Copy to clipboard
    
    Alternatively, you could use `np.arange(0, 28)*0.04` which would always give you precise control of the end point since it is integral:
    
    \>>> np.arange(0, 28)\*0.04
    array(\[0.  , 0.04, 0.08, 0.12, 0.16, 0.2 , 0.24, 0.28, 0.32, 0.36, 0.4 ,\
           0.44, 0.48, 0.52, 0.56, 0.6 , 0.64, 0.68, 0.72, 0.76, 0.8 , 0.84,\
           0.88, 0.92, 0.96, 1.  , 1.04, 1.08\])
    
    Copy to clipboard
    

### `geomspace` and `logspace`[#](https://numpy.org/doc/stable/user/how-to-partition.html#geomspace-and-logspace "Link to this heading")

`numpy.geomspace` is similar to `numpy.linspace`, but with numbers spaced evenly on a log scale (a geometric progression). The endpoint is included in the result.

Example:

\>>> np.geomspace(2, 3, num\=5)
array(\[2.        , 2.21336384, 2.44948974, 2.71080601, 3.        \])

Copy to clipboard

`numpy.logspace` is similar to `numpy.geomspace`, but with the start and end points specified as logarithms (with base 10 as default):

\>>> np.logspace(2, 3, num\=5)
array(\[ 100.        ,  177.827941  ,  316.22776602,  562.34132519, 1000.        \])

Copy to clipboard

In linear space, the sequence starts at `base ** start` (`base` to the power of `start`) and ends with `base ** stop`:

\>>> np.logspace(2, 3, num\=5, base\=2)
array(\[4.        , 4.75682846, 5.65685425, 6.72717132, 8.        \])

Copy to clipboard

N-D domains[#](https://numpy.org/doc/stable/user/how-to-partition.html#n-d-domains "Link to this heading")

-----------------------------------------------------------------------------------------------------------

N-D domains can be partitioned into _grids_. This can be done using one of the following functions.

### `meshgrid`[#](https://numpy.org/doc/stable/user/how-to-partition.html#meshgrid "Link to this heading")

The purpose of `numpy.meshgrid` is to create a rectangular grid out of a set of one-dimensional coordinate arrays.

Given arrays:

\>>> x \= np.array(\[0, 1, 2, 3\])
\>>> y \= np.array(\[0, 1, 2, 3, 4, 5\])

Copy to clipboard

`meshgrid` will create two coordinate arrays, which can be used to generate the coordinate pairs determining this grid.:

\>>> xx, yy \= np.meshgrid(x, y)
\>>> xx
array(\[\[0, 1, 2, 3\],\
       \[0, 1, 2, 3\],\
       \[0, 1, 2, 3\],\
       \[0, 1, 2, 3\],\
       \[0, 1, 2, 3\],\
       \[0, 1, 2, 3\]\])
\>>> yy
array(\[\[0, 0, 0, 0\],\
       \[1, 1, 1, 1\],\
       \[2, 2, 2, 2\],\
       \[3, 3, 3, 3\],\
       \[4, 4, 4, 4\],\
       \[5, 5, 5, 5\]\])

\>>> import matplotlib.pyplot as plt
\>>> plt.plot(xx, yy, marker\='.', color\='k', linestyle\='none')

Copy to clipboard

![../_images/meshgrid_plot.png](https://numpy.org/doc/stable/_images/meshgrid_plot.png)

### `mgrid`[#](https://numpy.org/doc/stable/user/how-to-partition.html#mgrid "Link to this heading")

`numpy.mgrid` can be used as a shortcut for creating meshgrids. It is not a function, but when indexed, returns a multidimensional meshgrid.

\>>> xx, yy \= np.meshgrid(np.array(\[0, 1, 2, 3\]), np.array(\[0, 1, 2, 3, 4, 5\]))
\>>> xx.T, yy.T
(array(\[\[0, 0, 0, 0, 0, 0\],\
        \[1, 1, 1, 1, 1, 1\],\
        \[2, 2, 2, 2, 2, 2\],\
        \[3, 3, 3, 3, 3, 3\]\]),
 array(\[\[0, 1, 2, 3, 4, 5\],\
        \[0, 1, 2, 3, 4, 5\],\
        \[0, 1, 2, 3, 4, 5\],\
        \[0, 1, 2, 3, 4, 5\]\]))

\>>> np.mgrid\[0:4, 0:6\]
array(\[\[\[0, 0, 0, 0, 0, 0\],\
        \[1, 1, 1, 1, 1, 1\],\
        \[2, 2, 2, 2, 2, 2\],\
        \[3, 3, 3, 3, 3, 3\]\],\
\
       \[\[0, 1, 2, 3, 4, 5\],\
        \[0, 1, 2, 3, 4, 5\],\
        \[0, 1, 2, 3, 4, 5\],\
        \[0, 1, 2, 3, 4, 5\]\]\])

Copy to clipboard

### `ogrid`[#](https://numpy.org/doc/stable/user/how-to-partition.html#ogrid "Link to this heading")

Similar to `numpy.mgrid`, `numpy.ogrid` returns an _open_ multidimensional meshgrid. This means that when it is indexed, only one dimension of each returned array is greater than 1. This avoids repeating the data and thus saves memory, which is often desirable.

These sparse coordinate grids are intended to be used with [Broadcasting](https://scipy-lectures.org/intro/numpy/operations.html#broadcasting "(in Scipy lecture notes v2022.1)")
. When all coordinates are used in an expression, broadcasting still leads to a fully-dimensional result array.

\>>> np.ogrid\[0:4, 0:6\]
(array(\[\[0\],\
        \[1\],\
        \[2\],\
        \[3\]\]), array(\[\[0, 1, 2, 3, 4, 5\]\]))

Copy to clipboard

All three methods described here can be used to evaluate function values on a grid.

\>>> g \= np.ogrid\[0:4, 0:6\]
\>>> zg \= np.sqrt(g\[0\]\*\*2 + g\[1\]\*\*2)
\>>> g\[0\].shape, g\[1\].shape, zg.shape
((4, 1), (1, 6), (4, 6))
\>>> m \= np.mgrid\[0:4, 0:6\]
\>>> zm \= np.sqrt(m\[0\]\*\*2 + m\[1\]\*\*2)
\>>> np.array\_equal(zm, zg)
True

Copy to clipboard

On this page