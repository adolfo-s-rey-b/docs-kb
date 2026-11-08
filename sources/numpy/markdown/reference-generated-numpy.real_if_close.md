[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.real_if_close.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.real_if_close.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.real_if_close.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.real_if_close.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.real_if_close.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.real_if_close.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.real_if_close.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.real_if_close.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.real_if_close.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.real_if_close.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.real_if_close.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.real_if_close.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.real_if_close.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.real_if_close.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.real_if_close.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.real_if_close.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.real_if_close.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.real_if_close.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.real_if_close.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.real_if_close.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.real_if_close.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.real_if_close.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.real\_if\_close[#](https://numpy.org/doc/stable/reference/generated/numpy.real_if_close.html#numpy-real-if-close "Link to this heading")

===============================================================================================================================================

numpy.real\_if\_close(_a_, _tol\=100_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_type_check_impl.py#L495-L551)
[#](https://numpy.org/doc/stable/reference/generated/numpy.real_if_close.html#numpy.real_if_close "Link to this definition")

If input is complex with all imaginary parts close to zero, return real parts.

“Close to zero” is defined as _tol_ \* (machine epsilon of the type for _a_).

Parameters:

**a**array\_like

Input array.

**tol**float

Tolerance in machine epsilons for the complex part of the elements in the array. If the tolerance is <=1, then the absolute tolerance is used.

Returns:

**out**ndarray

If _a_ is real, the type of _a_ is used for the output. If _a_ has complex elements, the returned type is float.

See also

[`real`](https://numpy.org/doc/stable/reference/generated/numpy.real.html#numpy.real "numpy.real")
, [`imag`](https://numpy.org/doc/stable/reference/generated/numpy.imag.html#numpy.imag "numpy.imag")
, [`angle`](https://numpy.org/doc/stable/reference/generated/numpy.angle.html#numpy.angle "numpy.angle")

Notes

Machine epsilon varies from machine to machine and between data types but Python floats on most platforms have a machine epsilon equal to 2.2204460492503131e-16. You can use ‘np.finfo(float).eps’ to print out the machine epsilon for floats.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.finfo(float).eps
2.2204460492503131e-16 # may vary

Copy to clipboard

\>>> np.real\_if\_close(\[2.1 + 4e-14j, 5.2 + 3e-15j\], tol\=1000)
array(\[2.1, 5.2\])
\>>> np.real\_if\_close(\[2.1 + 4e-13j, 5.2 + 3e-15j\], tol\=1000)
array(\[2.1+4.e-13j, 5.2 + 3e-15j\])

Copy to clipboard

Go BackOpen In Tab

On this page