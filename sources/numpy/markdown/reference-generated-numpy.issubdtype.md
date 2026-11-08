[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.issubdtype.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.issubdtype.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.issubdtype.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.issubdtype.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.issubdtype.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.issubdtype.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.issubdtype.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.issubdtype.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.issubdtype.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.issubdtype.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.issubdtype.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.issubdtype.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.issubdtype.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.issubdtype.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.issubdtype.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.issubdtype.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.issubdtype.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.issubdtype.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.issubdtype.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.issubdtype.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.issubdtype.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.issubdtype.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.issubdtype[#](https://numpy.org/doc/stable/reference/generated/numpy.issubdtype.html#numpy-issubdtype "Link to this heading")

====================================================================================================================================

numpy.issubdtype(_arg1_, _arg2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numerictypes.py#L411-L474)
[#](https://numpy.org/doc/stable/reference/generated/numpy.issubdtype.html#numpy.issubdtype "Link to this definition")

Returns True if first argument is a typecode lower/equal in type hierarchy.

This is like the builtin [`issubclass`](https://docs.python.org/3/library/functions.html#issubclass "(in Python v3.14)")
, but for [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
s.

Parameters:

**arg1, arg2**dtype\_like

[`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 or object coercible to one

Returns:

**out**bool

See also

[Scalars](https://numpy.org/doc/stable/reference/arrays.scalars.html#arrays-scalars)

Overview of the numpy type hierarchy.

Examples

Try it in your browser!

[`issubdtype`](https://numpy.org/doc/stable/reference/generated/numpy.issubdtype.html#numpy.issubdtype "numpy.issubdtype")
 can be used to check the type of arrays:

\>>> ints \= np.array(\[1, 2, 3\], dtype\=np.int32)
\>>> np.issubdtype(ints.dtype, np.integer)
True
\>>> np.issubdtype(ints.dtype, np.floating)
False

Copy to clipboard

\>>> floats \= np.array(\[1, 2, 3\], dtype\=np.float32)
\>>> np.issubdtype(floats.dtype, np.integer)
False
\>>> np.issubdtype(floats.dtype, np.floating)
True

Copy to clipboard

Similar types of different sizes are not subdtypes of each other:

\>>> np.issubdtype(np.float64, np.float32)
False
\>>> np.issubdtype(np.float32, np.float64)
False

Copy to clipboard

but both are subtypes of [`floating`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.floating "numpy.floating")
:

\>>> np.issubdtype(np.float64, np.floating)
True
\>>> np.issubdtype(np.float32, np.floating)
True

Copy to clipboard

For convenience, dtype-like objects are allowed too:

\>>> np.issubdtype('S1', np.bytes\_)
True
\>>> np.issubdtype('i4', np.signedinteger)
True

Copy to clipboard

Go BackOpen In Tab

On this page