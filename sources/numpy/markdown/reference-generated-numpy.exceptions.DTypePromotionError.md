[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.DTypePromotionError.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.exceptions.DTypePromotionError.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.DTypePromotionError.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.exceptions.DTypePromotionError.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.exceptions.DTypePromotionError.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.exceptions.DTypePromotionError.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.exceptions.DTypePromotionError.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.exceptions.DTypePromotionError.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.exceptions.DTypePromotionError.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.exceptions.DTypePromotionError.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.exceptions.DTypePromotionError.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.exceptions.DTypePromotionError.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.exceptions.DTypePromotionError.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.exceptions.DTypePromotionError.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.exceptions.DTypePromotionError.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.exceptions.DTypePromotionError.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.exceptions.DTypePromotionError.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.exceptions.DTypePromotionError.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.exceptions.DTypePromotionError.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.exceptions.DTypePromotionError.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.exceptions.DTypePromotionError.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.exceptions.DTypePromotionError.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.exceptions.DTypePromotionError[#](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.DTypePromotionError.html#numpy-exceptions-dtypepromotionerror "Link to this heading")

================================================================================================================================================================================================

_exception_ exceptions.DTypePromotionError[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/exceptions.py#L199-L246)
[#](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.DTypePromotionError.html#numpy.exceptions.DTypePromotionError "Link to this definition")

Multiple DTypes could not be converted to a common one.

This exception derives from `TypeError` and is raised whenever dtypes cannot be converted to a single common one. This can be because they are of a different category/class or incompatible instances of the same one (see Examples).

Notes

Many functions will use promotion to find the correct result and implementation. For these functions the error will typically be chained with a more specific error indicating that no implementation was found for the input dtypes.

Typically promotion should be considered “invalid” between the dtypes of two arrays when _arr1 == arr2_ can safely return all `False` because the dtypes are fundamentally different.

Examples

Try it in your browser!

Datetimes and complex numbers are incompatible classes and cannot be promoted:

\>>> import numpy as np
\>>> np.result\_type(np.dtype("M8\[s\]"), np.complex128)  
Traceback (most recent call last):
 ...
DTypePromotionError: The DType <class 'numpy.dtype\[datetime64\]'> could not
be promoted by <class 'numpy.dtype\[complex128\]'>. This means that no common
DType exists for the given inputs. For example they cannot be stored in a
single array unless the dtype is \`object\`. The full list of DTypes is:
(<class 'numpy.dtype\[datetime64\]'>, <class 'numpy.dtype\[complex128\]'>)

Copy to clipboard

For example for structured dtypes, the structure can mismatch and the same `DTypePromotionError` is given when two structured dtypes with a mismatch in their number of fields is given:

\>>> dtype1 \= np.dtype(\[("field1", np.float64), ("field2", np.int64)\])
\>>> dtype2 \= np.dtype(\[("field1", np.float64)\])
\>>> np.promote\_types(dtype1, dtype2)  
Traceback (most recent call last):
 ...
DTypePromotionError: field names \`('field1', 'field2')\` and \`('field1',)\`
mismatch.

Copy to clipboard

Go BackOpen In Tab

On this page