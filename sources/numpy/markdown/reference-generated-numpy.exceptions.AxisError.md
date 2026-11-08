[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.AxisError.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.exceptions.AxisError[#](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.AxisError.html#numpy-exceptions-axiserror "Link to this heading")

==================================================================================================================================================================

_exception_ exceptions.AxisError(_axis_, _ndim\=None_, _msg\_prefix\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/exceptions.py#L108-L196)
[#](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.AxisError.html#numpy.exceptions.AxisError "Link to this definition")

Axis supplied was invalid.

This is raised whenever an `axis` parameter is specified that is larger than the number of array dimensions. For compatibility with code written against older numpy versions, which raised a mixture of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
 and [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "(in Python v3.14)")
 for this situation, this exception subclasses both to ensure that `except ValueError` and `except IndexError` statements continue to catch `AxisError`.

Parameters:

**axis**int or str

The out of bounds axis or a custom exception message. If an axis is provided, then [`ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndim.html#numpy.ndim "numpy.ndim")
 should be specified as well.

**ndim**int, optional

The number of array dimensions.

**msg\_prefix**str, optional

A prefix for the exception message.

Attributes:

**axis**int, optional

The out of bounds axis or `None` if a custom exception message was provided. This should be the axis as passed by the user, before any normalization to resolve negative indices.

New in version 1.22.

**ndim**int, optional

The number of array dimensions or `None` if a custom exception message was provided.

New in version 1.22.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> array\_1d \= np.arange(10)
\>>> np.cumsum(array\_1d, axis\=1)
Traceback (most recent call last):
  ...
numpy.exceptions.AxisError: axis 1 is out of bounds for array of dimension 1

Copy to clipboard

Negative axes are preserved:

\>>> np.cumsum(array\_1d, axis\=-2)
Traceback (most recent call last):
  ...
numpy.exceptions.AxisError: axis -2 is out of bounds for array of dimension 1

Copy to clipboard

The class constructor generally takes the axis and arrays’ dimensionality as arguments:

\>>> print(np.exceptions.AxisError(2, 1, msg\_prefix\='error'))
error: axis 2 is out of bounds for array of dimension 1

Copy to clipboard

Alternatively, a custom exception message can be passed:

\>>> print(np.exceptions.AxisError('Custom error message'))
Custom error message

Copy to clipboard

Go BackOpen In Tab

On this page