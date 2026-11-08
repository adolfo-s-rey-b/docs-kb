[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.common_type.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.common_type.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.common_type.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.common_type.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.common_type.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.common_type.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.common_type.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.common_type.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.common_type.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.common_type.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.common_type.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.common_type.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.common_type.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.common_type.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.common_type.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.common_type.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.common_type.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.common_type.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.common_type.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.common_type.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.common_type.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.common_type.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.common\_type[#](https://numpy.org/doc/stable/reference/generated/numpy.common_type.html#numpy-common-type "Link to this heading")

========================================================================================================================================

numpy.common\_type(_\*arrays_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_type_check_impl.py#L661-L714)
[#](https://numpy.org/doc/stable/reference/generated/numpy.common_type.html#numpy.common_type "Link to this definition")

Return a scalar type which is common to the input arrays.

The return type will always be an inexact (i.e. floating point) scalar type, even if all the arrays are integer arrays. If one of the inputs is an integer array, the minimum precision type that is returned is a 64-bit floating point dtype.

All input arrays except int64 and uint64 can be safely cast to the returned dtype without loss of information.

Parameters:

**array1, array2, …**ndarrays

Input arrays.

Returns:

**out**data type code

Data type code.

See also

[`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
, [`mintypecode`](https://numpy.org/doc/stable/reference/generated/numpy.mintypecode.html#numpy.mintypecode "numpy.mintypecode")

Examples

Try it in your browser!

\>>> np.common\_type(np.arange(2, dtype\=np.float32))
<class 'numpy.float32'>
\>>> np.common\_type(np.arange(2, dtype\=np.float32), np.arange(2))
<class 'numpy.float64'>
\>>> np.common\_type(np.arange(4), np.array(\[45, 6.j\]), np.array(\[45.0\]))
<class 'numpy.complex128'>

Copy to clipboard

Go BackOpen In Tab

On this page