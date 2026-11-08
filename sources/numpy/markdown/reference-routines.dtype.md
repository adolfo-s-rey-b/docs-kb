[Skip to main content](https://numpy.org/doc/stable/reference/routines.dtype.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.dtype.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.dtype.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.dtype.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.dtype.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.dtype.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.dtype.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.dtype.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.dtype.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.dtype.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.dtype.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.dtype.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.dtype.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.dtype.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.dtype.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.dtype.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.dtype.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.dtype.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.dtype.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.dtype.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.dtype.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.dtype.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Data type routines[#](https://numpy.org/doc/stable/reference/routines.dtype.html#data-type-routines "Link to this heading")

============================================================================================================================

|     |     |
| --- | --- |
| [`can_cast`](https://numpy.org/doc/stable/reference/generated/numpy.can_cast.html#numpy.can_cast "numpy.can_cast")<br>(from\_, to\[, casting\]) | Returns True if cast between data types can occur according to the casting rule. |
| [`promote_types`](https://numpy.org/doc/stable/reference/generated/numpy.promote_types.html#numpy.promote_types "numpy.promote_types")<br>(type1, type2, /) | Returns the data type with the smallest size and smallest scalar kind to which both `type1` and `type2` may be safely cast. |
| [`min_scalar_type`](https://numpy.org/doc/stable/reference/generated/numpy.min_scalar_type.html#numpy.min_scalar_type "numpy.min_scalar_type")<br>(a, /) | For scalar `a`, returns the data type with the smallest size and smallest scalar kind which can hold its value. |
| [`result_type`](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html#numpy.result_type "numpy.result_type")<br>(\*arrays\_and\_dtypes) | Returns the type that results from applying the NumPy [type promotion](https://numpy.org/doc/stable/reference/arrays.promotion.html#arrays-promotion)<br> rules to the arguments. |
| [`common_type`](https://numpy.org/doc/stable/reference/generated/numpy.common_type.html#numpy.common_type "numpy.common_type")<br>(\*arrays) | Return a scalar type which is common to the input arrays. |

Creating data types[#](https://numpy.org/doc/stable/reference/routines.dtype.html#creating-data-types "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")<br>(dtype\[, align, copy\]) | \-- |
| [`rec.format_parser`](https://numpy.org/doc/stable/reference/generated/numpy.rec.format_parser.html#numpy.rec.format_parser "numpy.rec.format_parser")<br>(formats, names, titles\[, ...\]) | Class to convert formats, names, titles description to a dtype. |

Data type information[#](https://numpy.org/doc/stable/reference/routines.dtype.html#data-type-information "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`finfo`](https://numpy.org/doc/stable/reference/generated/numpy.finfo.html#numpy.finfo "numpy.finfo")<br>(dtype) | Machine limits for floating point types. |
| [`iinfo`](https://numpy.org/doc/stable/reference/generated/numpy.iinfo.html#numpy.iinfo "numpy.iinfo")<br>(type) | Machine limits for integer types. |

Data type testing[#](https://numpy.org/doc/stable/reference/routines.dtype.html#data-type-testing "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`isdtype`](https://numpy.org/doc/stable/reference/generated/numpy.isdtype.html#numpy.isdtype "numpy.isdtype")<br>(dtype, kind) | Determine if a provided dtype is of a specified data type `kind`. |
| [`issubdtype`](https://numpy.org/doc/stable/reference/generated/numpy.issubdtype.html#numpy.issubdtype "numpy.issubdtype")<br>(arg1, arg2) | Returns True if first argument is a typecode lower/equal in type hierarchy. |

Miscellaneous[#](https://numpy.org/doc/stable/reference/routines.dtype.html#miscellaneous "Link to this heading")

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`typename`](https://numpy.org/doc/stable/reference/generated/numpy.typename.html#numpy.typename "numpy.typename")<br>(char) | Return a description for the given data type code. |
| [`mintypecode`](https://numpy.org/doc/stable/reference/generated/numpy.mintypecode.html#numpy.mintypecode "numpy.mintypecode")<br>(typechars\[, typeset, default\]) | Return the character for the minimum-size type to which given types can be safely cast. |

On this page