[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.trapezoid.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.trapezoid.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.trapezoid.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.trapezoid.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.trapezoid.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.trapezoid.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.trapezoid.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.trapezoid.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.trapezoid.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.trapezoid.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.trapezoid.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.trapezoid.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.trapezoid.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.trapezoid.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.trapezoid.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.trapezoid.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.trapezoid.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.trapezoid.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.trapezoid.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.trapezoid.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.trapezoid.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.trapezoid.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.trapezoid[#](https://numpy.org/doc/stable/reference/generated/numpy.trapezoid.html#numpy-trapezoid "Link to this heading")

=================================================================================================================================

numpy.trapezoid(_y_, _x\=None_, _dx\=1.0_, _axis\=\-1_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L4922-L5054)
[#](https://numpy.org/doc/stable/reference/generated/numpy.trapezoid.html#numpy.trapezoid "Link to this definition")

Integrate along the given axis using the composite trapezoidal rule.

If _x_ is provided, the integration happens in sequence along its elements - they are not sorted.

Integrate _y_ (_x_) along each 1d slice on the given axis, compute . When _x_ is specified, this integrates along the parametric curve, computing \\int\_t y(t) dt = \\int\_t y(t) \\left.\\frac{dx}{dt}\\right|\_{x=x(t)} dt.

New in version 2.0.0.

Parameters:

**y**array\_like

Input array to integrate.

**x**array\_like, optional

The sample points corresponding to the _y_ values. If _x_ is None, the sample points are assumed to be evenly spaced _dx_ apart. The default is None.

**dx**scalar, optional

The spacing between sample points when _x_ is None. The default is 1.

**axis**int, optional

The axis along which to integrate.

Returns:

**trapezoid**float or ndarray

Definite integral of _y_ = n-dimensional array as approximated along a single axis by the trapezoidal rule. If _y_ is a 1-dimensional array, then the result is a float. If _n_ is greater than 1, then the result is an _n_\-1 dimensional array.

See also

[`sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
, [`cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")

Notes

Image [\[2\]](https://numpy.org/doc/stable/reference/generated/numpy.trapezoid.html#r1ffe72fc1dc5-2)
 illustrates trapezoidal rule – y-axis locations of points will be taken from _y_ array, by default x-axis distances between points will be 1.0, alternatively they can be provided with _x_ array or with _dx_ scalar. Return value will be equal to combined area under the red lines.

References

\[1\]

Wikipedia page: [https://en.wikipedia.org/wiki/Trapezoidal\_rule](https://en.wikipedia.org/wiki/Trapezoidal_rule)

\[[2](https://numpy.org/doc/stable/reference/generated/numpy.trapezoid.html#id1)\
\]

Illustration image: [https://en.wikipedia.org/wiki/File:Composite\_trapezoidal\_rule\_illustration.png](https://en.wikipedia.org/wiki/File:Composite_trapezoidal_rule_illustration.png)

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Use the trapezoidal rule on evenly spaced points:

\>>> np.trapezoid(\[1, 2, 3\])
4.0

Copy to clipboard

The spacing between sample points can be selected by either the `x` or `dx` arguments:

\>>> np.trapezoid(\[1, 2, 3\], x\=\[4, 6, 8\])
8.0
\>>> np.trapezoid(\[1, 2, 3\], dx\=2)
8.0

Copy to clipboard

Using a decreasing `x` corresponds to integrating in reverse:

\>>> np.trapezoid(\[1, 2, 3\], x\=\[8, 6, 4\])
\-8.0

Copy to clipboard

More generally `x` is used to integrate along a parametric curve. We can estimate the integral \\int\_0^1 x^2 = 1/3 using:

\>>> x \= np.linspace(0, 1, num\=50)
\>>> y \= x\*\*2
\>>> np.trapezoid(y, x)
0.33340274885464394

Copy to clipboard

Or estimate the area of a circle, noting we repeat the sample which closes the curve:

\>>> theta \= np.linspace(0, 2 \* np.pi, num\=1000, endpoint\=True)
\>>> np.trapezoid(np.cos(theta), x\=np.sin(theta))
3.141571941375841

Copy to clipboard

`np.trapezoid` can be applied along a specified axis to do multiple computations in one call:

\>>> a \= np.arange(6).reshape(2, 3)
\>>> a
array(\[\[0, 1, 2\],\
       \[3, 4, 5\]\])
\>>> np.trapezoid(a, axis\=0)
array(\[1.5, 2.5, 3.5\])
\>>> np.trapezoid(a, axis\=1)
array(\[2.,  8.\])

Copy to clipboard

Go BackOpen In Tab

On this page