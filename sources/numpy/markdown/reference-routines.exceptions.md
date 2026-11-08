[Skip to main content](https://numpy.org/doc/stable/reference/routines.exceptions.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Exceptions and Warnings[#](https://numpy.org/doc/stable/reference/routines.exceptions.html#exceptions-and-warnings "Link to this heading")

===========================================================================================================================================

General exceptions used by NumPy. Note that some exceptions may be module specific, such as linear algebra errors.

New in version NumPy: 1.25

The exceptions module is new in NumPy 1.25.

Warnings[#](https://numpy.org/doc/stable/reference/routines.exceptions.html#warnings "Link to this heading")

-------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`ComplexWarning`](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.ComplexWarning.html#numpy.exceptions.ComplexWarning "numpy.exceptions.ComplexWarning") | The warning raised when casting a complex dtype to a real dtype. |
| [`VisibleDeprecationWarning`](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.VisibleDeprecationWarning.html#numpy.exceptions.VisibleDeprecationWarning "numpy.exceptions.VisibleDeprecationWarning") | Visible deprecation warning. |
| [`RankWarning`](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.RankWarning.html#numpy.exceptions.RankWarning "numpy.exceptions.RankWarning") | Matrix rank warning. |

Exceptions[#](https://numpy.org/doc/stable/reference/routines.exceptions.html#exceptions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`AxisError`](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.AxisError.html#numpy.exceptions.AxisError "numpy.exceptions.AxisError")<br>(axis\[, ndim, msg\_prefix\]) | Axis supplied was invalid. |
| [`DTypePromotionError`](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.DTypePromotionError.html#numpy.exceptions.DTypePromotionError "numpy.exceptions.DTypePromotionError") | Multiple DTypes could not be converted to a common one. |
| [`TooHardError`](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.TooHardError.html#numpy.exceptions.TooHardError "numpy.exceptions.TooHardError") | `max_work` was exceeded. |

On this page