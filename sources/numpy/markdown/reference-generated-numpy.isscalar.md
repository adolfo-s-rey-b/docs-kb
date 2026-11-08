[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.isscalar.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.isscalar.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.isscalar.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.isscalar.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.isscalar.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.isscalar.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.isscalar.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.isscalar.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.isscalar.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.isscalar.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.isscalar.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.isscalar.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.isscalar.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.isscalar.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.isscalar.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.isscalar.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.isscalar.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.isscalar.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.isscalar.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.isscalar.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.isscalar.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.isscalar.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.isscalar[#](https://numpy.org/doc/stable/reference/generated/numpy.isscalar.html#numpy-isscalar "Link to this heading")

==============================================================================================================================

numpy.isscalar(_element_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L1910-L1994)
[#](https://numpy.org/doc/stable/reference/generated/numpy.isscalar.html#numpy.isscalar "Link to this definition")

Returns True if the type of _element_ is a scalar type.

Parameters:

**element**any

Input argument, can be of any type and shape.

Returns:

**val**bool

True if _element_ is a scalar type, False if it is not.

See also

[`ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndim.html#numpy.ndim "numpy.ndim")

Get the number of dimensions of an array

Notes

If you need a stricter way to identify a _numerical_ scalar, use `isinstance(x, numbers.Number)`, as that returns `False` for most non-numerical elements such as strings.

In most cases `np.ndim(x) == 0` should be used instead of this function, as that will also return true for 0d arrays. This is how numpy overloads functions in the style of the `dx` arguments to [`gradient`](https://numpy.org/doc/stable/reference/generated/numpy.gradient.html#numpy.gradient "numpy.gradient")
 and the `bins` argument to [`histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "numpy.histogram")
. Some key differences:

| x   | `isscalar(x)` | `np.ndim(x) == 0` |
| --- | --- | --- |
| PEP 3141 numeric objects (including builtins) | `True` | `True` |
| builtin string and buffer objects | `True` | `True` |
| other builtin objects, like [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")<br>, _Exception_, the result of [`re.compile`](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.14)") | `False` | `True` |
| third-party objects like [`matplotlib.figure.Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "(in Matplotlib v3.11.0)") | `False` | `True` |
| zero-dimensional numpy arrays | `False` | `True` |
| other numpy arrays | `False` | `False` |
| _list_, _tuple_, and other sequence objects | `False` | `False` |

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> np.isscalar(3.1)
True

Copy to clipboard

\>>> np.isscalar(np.array(3.1))
False

Copy to clipboard

\>>> np.isscalar(\[3.1\])
False

Copy to clipboard

\>>> np.isscalar(False)
True

Copy to clipboard

\>>> np.isscalar('numpy')
True

Copy to clipboard

NumPy supports PEP 3141 numbers:

\>>> from fractions import Fraction
\>>> np.isscalar(Fraction(5, 17))
True
\>>> from numbers import Number
\>>> np.isscalar(Number())
True

Copy to clipboard

Go BackOpen In Tab

On this page