[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.gradient.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.gradient.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.gradient.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.gradient.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.gradient.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.gradient.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.gradient.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.gradient.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.gradient.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.gradient.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.gradient.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.gradient.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.gradient.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.gradient.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.gradient.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.gradient.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.gradient.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.gradient.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.gradient.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.gradient.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.gradient.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.gradient.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.gradient[#](https://numpy.org/doc/stable/reference/generated/numpy.gradient.html#numpy-gradient "Link to this heading")

==============================================================================================================================

numpy.gradient(_f_, _\*varargs_, _axis\=None_, _edge\_order\=1_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L1013-L1406)
[#](https://numpy.org/doc/stable/reference/generated/numpy.gradient.html#numpy.gradient "Link to this definition")

Return the gradient of an N-dimensional array.

The gradient is computed using second order accurate central differences in the interior points and either first or second order accurate one-sides (forward or backwards) differences at the boundaries. The returned gradient hence has the same shape as the input array.

Parameters:

**f**array\_like

An N-dimensional array containing samples of a scalar function.

**varargs**list of scalar or array, optional

Spacing between f values. Default unitary spacing for all dimensions. Spacing can be specified using:

1.  Single scalar to specify a sample distance for all dimensions.
    
2.  N scalars to specify a constant sample distance for each dimension. i.e. _dx_, _dy_, _dz_, …
    
3.  N arrays to specify the coordinates of the values along each dimension of F. The length of the array must match the size of the corresponding dimension
    
4.  Any combination of N scalars/arrays with the meaning of 2. and 3.
    

If _axis_ is given, the number of varargs must equal the number of axes specified in the axis parameter. Default: 1. (see Examples below).

**edge\_order**{1, 2}, optional

Gradient is calculated using N-th order accurate differences at the boundaries. Default: 1.

**axis**None or int or tuple of ints, optional

Gradient is calculated only along the given axis or axes. The default (axis = None) is to calculate the gradient for all the axes of the input array. axis may be negative, in which case it counts from the last to the first axis.

Returns:

**gradient**ndarray or tuple of ndarray

A tuple of ndarrays (or a single ndarray if there is only one dimension) corresponding to the derivatives of f with respect to each dimension. Each derivative has the same shape as f.

Notes

Assuming that (i.e., f has at least 3 continuous derivatives) and let h\_{\*} be a non-homogeneous stepsize, we minimize the “consistency error” \\eta\_{i} between the true gradient and its estimate from a linear combination of the neighboring grid-points:

\\eta\_{i} = f\_{i}^{\\left(1\\right)} - \\left\[ \\alpha f\\left(x\_{i}\\right) + \\beta f\\left(x\_{i} + h\_{d}\\right) + \\gamma f\\left(x\_{i}-h\_{s}\\right) \\right\]

By substituting f(x\_{i} + h\_{d}) and f(x\_{i} - h\_{s}) with their Taylor series expansion, this translates into solving the following the linear system:

\\begin{split}\\left\\{ \\begin{array}{r} \\alpha+\\beta+\\gamma=0 \\\\ \\beta h\_{d}-\\gamma h\_{s}=1 \\\\ \\beta h\_{d}^{2}+\\gamma h\_{s}^{2}=0 \\end{array} \\right.\\end{split}

The resulting approximation of f\_{i}^{(1)} is the following:

\\hat f\_{i}^{(1)} = \\frac{ h\_{s}^{2}f\\left(x\_{i} + h\_{d}\\right) + \\left(h\_{d}^{2} - h\_{s}^{2}\\right)f\\left(x\_{i}\\right) - h\_{d}^{2}f\\left(x\_{i}-h\_{s}\\right)} { h\_{s}h\_{d}\\left(h\_{d} + h\_{s}\\right)} + \\mathcal{O}\\left(\\frac{h\_{d}h\_{s}^{2} + h\_{s}h\_{d}^{2}}{h\_{d} + h\_{s}}\\right)

It is worth noting that if h\_{s}=h\_{d} (i.e., data are evenly spaced) we find the standard second order approximation:

\\hat f\_{i}^{(1)}= \\frac{f\\left(x\_{i+1}\\right) - f\\left(x\_{i-1}\\right)}{2h} + \\mathcal{O}\\left(h^{2}\\right)

With a similar procedure the forward/backward approximations used for boundaries can be derived.

References

\[1\]

Quarteroni A., Sacco R., Saleri F. (2007) Numerical Mathematics (Texts in Applied Mathematics). New York: Springer.

\[2\]

Durran D. R. (1999) Numerical Methods for Wave Equations in Geophysical Fluid Dynamics. New York: Springer.

\[3\]

Fornberg B. (1988) Generation of Finite Difference Formulas on Arbitrarily Spaced Grids, Mathematics of Computation 51, no. 184 : 699-706. [PDF](https://www.ams.org/journals/mcom/1988-51-184/S0025-5718-1988-0935077-0/S0025-5718-1988-0935077-0.pdf)
.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> f \= np.array(\[1, 2, 4, 7, 11, 16\])
\>>> np.gradient(f)
array(\[1. , 1.5, 2.5, 3.5, 4.5, 5. \])
\>>> np.gradient(f, 2)
array(\[0.5 ,  0.75,  1.25,  1.75,  2.25,  2.5 \])

Copy to clipboard

Spacing can be also specified with an array that represents the coordinates of the values F along the dimensions. For instance a uniform spacing:

\>>> x \= np.arange(f.size)
\>>> np.gradient(f, x)
array(\[1. ,  1.5,  2.5,  3.5,  4.5,  5. \])

Copy to clipboard

Or a non uniform one:

\>>> x \= np.array(\[0., 1., 1.5, 3.5, 4., 6.\])
\>>> np.gradient(f, x)
array(\[1. ,  3. ,  3.5,  6.7,  6.9,  2.5\])

Copy to clipboard

For two dimensional arrays, the return will be two arrays ordered by axis. In this example the first array stands for the gradient in rows and the second one in columns direction:

\>>> np.gradient(np.array(\[\[1, 2, 6\], \[3, 4, 5\]\]))
(array(\[\[ 2.,  2., -1.\],\
        \[ 2.,  2., -1.\]\]),
 array(\[\[1. , 2.5, 4. \],\
        \[1. , 1. , 1. \]\]))

Copy to clipboard

In this example the spacing is also specified: uniform for axis=0 and non uniform for axis=1

\>>> dx \= 2.
\>>> y \= \[1., 1.5, 3.5\]
\>>> np.gradient(np.array(\[\[1, 2, 6\], \[3, 4, 5\]\]), dx, y)
(array(\[\[ 1. ,  1. , -0.5\],\
        \[ 1. ,  1. , -0.5\]\]),
 array(\[\[2. , 2. , 2. \],\
        \[2. , 1.7, 0.5\]\]))

Copy to clipboard

It is possible to specify how boundaries are treated using _edge\_order_

\>>> x \= np.array(\[0, 1, 2, 3, 4\])
\>>> f \= x\*\*2
\>>> np.gradient(f, edge\_order\=1)
array(\[1.,  2.,  4.,  6.,  7.\])
\>>> np.gradient(f, edge\_order\=2)
array(\[0., 2., 4., 6., 8.\])

Copy to clipboard

The _axis_ keyword can be used to specify a subset of axes of which the gradient is calculated

\>>> np.gradient(np.array(\[\[1, 2, 6\], \[3, 4, 5\]\]), axis\=0)
array(\[\[ 2.,  2., -1.\],\
       \[ 2.,  2., -1.\]\])

Copy to clipboard

The _varargs_ argument defines the spacing between sample points in the input array. It can take two forms:

1.  An array, specifying coordinates, which may be unevenly spaced:
    

\>>> x \= np.array(\[0., 2., 3., 6., 8.\])
\>>> y \= x \*\* 2
\>>> np.gradient(y, x, edge\_order\=2)
array(\[ 0.,  4.,  6., 12., 16.\])

Copy to clipboard

2.  A scalar, representing the fixed sample distance:
    

\>>> dx \= 2
\>>> x \= np.array(\[0., 2., 4., 6., 8.\])
\>>> y \= x \*\* 2
\>>> np.gradient(y, dx, edge\_order\=2)
array(\[ 0.,  4.,  8., 12., 16.\])

Copy to clipboard

It’s possible to provide different data for spacing along each dimension. The number of arguments must match the number of dimensions in the input data.

\>>> dx \= 2
\>>> dy \= 3
\>>> x \= np.arange(0, 6, dx)
\>>> y \= np.arange(0, 9, dy)
\>>> xs, ys \= np.meshgrid(x, y)
\>>> zs \= xs + 2 \* ys
\>>> np.gradient(zs, dy, dx)  \# Passing two scalars
(array(\[\[2., 2., 2.\],\
        \[2., 2., 2.\],\
        \[2., 2., 2.\]\]),
 array(\[\[1., 1., 1.\],\
        \[1., 1., 1.\],\
        \[1., 1., 1.\]\]))

Copy to clipboard

Mixing scalars and arrays is also allowed:

\>>> np.gradient(zs, y, dx)  \# Passing one array and one scalar
(array(\[\[2., 2., 2.\],\
        \[2., 2., 2.\],\
        \[2., 2., 2.\]\]),
 array(\[\[1., 1., 1.\],\
        \[1., 1., 1.\],\
        \[1., 1., 1.\]\]))

Copy to clipboard

Go BackOpen In Tab

On this page