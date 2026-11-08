[Skip to main content](https://numpy.org/doc/stable/reference/routines.logic.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Logic functions[#](https://numpy.org/doc/stable/reference/routines.logic.html#logic-functions "Link to this heading")

======================================================================================================================

Truth value testing[#](https://numpy.org/doc/stable/reference/routines.logic.html#truth-value-testing "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`all`](https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy.all "numpy.all")<br>(a\[, axis, out, keepdims, where\]) | Test whether all array elements along a given axis evaluate to True. |
| [`any`](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any "numpy.any")<br>(a\[, axis, out, keepdims, where\]) | Test whether any array element along a given axis evaluates to True. |

Array contents[#](https://numpy.org/doc/stable/reference/routines.logic.html#array-contents "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`isfinite`](https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html#numpy.isfinite "numpy.isfinite")<br>(x, /\[, out, where, casting, order, ...\]) | Test element-wise for finiteness (not infinity and not Not a Number). |
| [`isinf`](https://numpy.org/doc/stable/reference/generated/numpy.isinf.html#numpy.isinf "numpy.isinf")<br>(x, /\[, out, where, casting, order, ...\]) | Test element-wise for positive or negative infinity. |
| [`isnan`](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html#numpy.isnan "numpy.isnan")<br>(x, /\[, out, where, casting, order, ...\]) | Test element-wise for NaN and return result as a boolean array. |
| [`isnat`](https://numpy.org/doc/stable/reference/generated/numpy.isnat.html#numpy.isnat "numpy.isnat")<br>(x, /\[, out, where, casting, order, ...\]) | Test element-wise for NaT (not a time) and return result as a boolean array. |
| [`isneginf`](https://numpy.org/doc/stable/reference/generated/numpy.isneginf.html#numpy.isneginf "numpy.isneginf")<br>(x\[, out\]) | Test element-wise for negative infinity, return result as bool array. |
| [`isposinf`](https://numpy.org/doc/stable/reference/generated/numpy.isposinf.html#numpy.isposinf "numpy.isposinf")<br>(x\[, out\]) | Test element-wise for positive infinity, return result as bool array. |

Array type testing[#](https://numpy.org/doc/stable/reference/routines.logic.html#array-type-testing "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`iscomplex`](https://numpy.org/doc/stable/reference/generated/numpy.iscomplex.html#numpy.iscomplex "numpy.iscomplex")<br>(x) | Returns a bool array, where True if input element is complex. |
| [`iscomplexobj`](https://numpy.org/doc/stable/reference/generated/numpy.iscomplexobj.html#numpy.iscomplexobj "numpy.iscomplexobj")<br>(x) | Check for a complex type or an array of complex numbers. |
| [`isfortran`](https://numpy.org/doc/stable/reference/generated/numpy.isfortran.html#numpy.isfortran "numpy.isfortran")<br>(a) | Check if the array is Fortran contiguous but _not_ C contiguous. |
| [`isreal`](https://numpy.org/doc/stable/reference/generated/numpy.isreal.html#numpy.isreal "numpy.isreal")<br>(x) | Returns a bool array, where True if input element is real. |
| [`isrealobj`](https://numpy.org/doc/stable/reference/generated/numpy.isrealobj.html#numpy.isrealobj "numpy.isrealobj")<br>(x) | Return True if x is a not complex type or an array of complex numbers. |
| [`isscalar`](https://numpy.org/doc/stable/reference/generated/numpy.isscalar.html#numpy.isscalar "numpy.isscalar")<br>(element) | Returns True if the type of _element_ is a scalar type. |

Logical operations[#](https://numpy.org/doc/stable/reference/routines.logic.html#logical-operations "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`logical_and`](https://numpy.org/doc/stable/reference/generated/numpy.logical_and.html#numpy.logical_and "numpy.logical_and")<br>(x1, x2, /\[, out, where, ...\]) | Compute the truth value of x1 AND x2 element-wise. |
| [`logical_or`](https://numpy.org/doc/stable/reference/generated/numpy.logical_or.html#numpy.logical_or "numpy.logical_or")<br>(x1, x2, /\[, out, where, casting, ...\]) | Compute the truth value of x1 OR x2 element-wise. |
| [`logical_not`](https://numpy.org/doc/stable/reference/generated/numpy.logical_not.html#numpy.logical_not "numpy.logical_not")<br>(x, /\[, out, where, casting, ...\]) | Compute the truth value of NOT x element-wise. |
| [`logical_xor`](https://numpy.org/doc/stable/reference/generated/numpy.logical_xor.html#numpy.logical_xor "numpy.logical_xor")<br>(x1, x2, /\[, out, where, ...\]) | Compute the truth value of x1 XOR x2, element-wise. |

Comparison[#](https://numpy.org/doc/stable/reference/routines.logic.html#comparison "Link to this heading")

------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`allclose`](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html#numpy.allclose "numpy.allclose")<br>(a, b\[, rtol, atol, equal\_nan\]) | Returns True if two arrays are element-wise equal within a tolerance. |
| [`isclose`](https://numpy.org/doc/stable/reference/generated/numpy.isclose.html#numpy.isclose "numpy.isclose")<br>(a, b\[, rtol, atol, equal\_nan\]) | Returns a boolean array where two arrays are element-wise equal within a tolerance. |
| [`array_equal`](https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html#numpy.array_equal "numpy.array_equal")<br>(a1, a2\[, equal\_nan\]) | True if two arrays have the same shape and elements, False otherwise. |
| [`array_equiv`](https://numpy.org/doc/stable/reference/generated/numpy.array_equiv.html#numpy.array_equiv "numpy.array_equiv")<br>(a1, a2) | Returns True if input arrays are shape consistent and all elements equal. |

|     |     |
| --- | --- |
| [`greater`](https://numpy.org/doc/stable/reference/generated/numpy.greater.html#numpy.greater "numpy.greater")<br>(x1, x2, /\[, out, where, casting, ...\]) | Return the truth value of (x1 > x2) element-wise. |
| [`greater_equal`](https://numpy.org/doc/stable/reference/generated/numpy.greater_equal.html#numpy.greater_equal "numpy.greater_equal")<br>(x1, x2, /\[, out, where, ...\]) | Return the truth value of (x1 >= x2) element-wise. |
| [`less`](https://numpy.org/doc/stable/reference/generated/numpy.less.html#numpy.less "numpy.less")<br>(x1, x2, /\[, out, where, casting, ...\]) | Return the truth value of (x1 < x2) element-wise. |
| [`less_equal`](https://numpy.org/doc/stable/reference/generated/numpy.less_equal.html#numpy.less_equal "numpy.less_equal")<br>(x1, x2, /\[, out, where, casting, ...\]) | Return the truth value of (x1 <= x2) element-wise. |
| [`equal`](https://numpy.org/doc/stable/reference/generated/numpy.equal.html#numpy.equal "numpy.equal")<br>(x1, x2, /\[, out, where, casting, ...\]) | Return (x1 == x2) element-wise. |
| [`not_equal`](https://numpy.org/doc/stable/reference/generated/numpy.not_equal.html#numpy.not_equal "numpy.not_equal")<br>(x1, x2, /\[, out, where, casting, ...\]) | Return (x1 != x2) element-wise. |

On this page