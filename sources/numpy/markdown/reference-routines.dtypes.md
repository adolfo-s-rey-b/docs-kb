[Skip to main content](https://numpy.org/doc/stable/reference/routines.dtypes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.dtypes.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.dtypes.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.dtypes.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.dtypes.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.dtypes.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.dtypes.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.dtypes.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.dtypes.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.dtypes.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.dtypes.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.dtypes.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.dtypes.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.dtypes.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.dtypes.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.dtypes.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.dtypes.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.dtypes.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.dtypes.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.dtypes.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.dtypes.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.dtypes.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Data type classes ([`numpy.dtypes`](https://numpy.org/doc/stable/reference/routines.dtypes.html#module-numpy.dtypes "numpy.dtypes")
)[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#module-numpy.dtypes "Link to this heading")

=================================================================================================================================================================================================================================================

This module is home to specific dtypes related functionality and their classes. For more general information about dtypes, also see [`numpy.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 and [Data type objects (dtype)](https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes)
.

Similar to the builtin `types` module, this submodule defines types (classes) that are not widely used directly.

New in version NumPy: 1.25

The dtypes module is new in NumPy 1.25. Previously DType classes were only accessible indirectly.

DType classes[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#dtype-classes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

The following are the classes of the corresponding NumPy dtype instances and NumPy scalar types. The classes can be used in `isinstance` checks and can also be instantiated or used directly. Direct use of these classes is not typical, since their scalar counterparts (e.g. `np.float64`) or strings like `"float64"` can be used.

Boolean[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#boolean "Link to this heading")

-------------------------------------------------------------------------------------------------------

numpy.dtypes.BoolDType[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/dtypes.py)
[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.BoolDType "Link to this definition")

Bit-sized integers[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#bit-sized-integers "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

numpy.dtypes.Int8DType[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/dtypes.py)
[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.Int8DType "Link to this definition")

numpy.dtypes.UInt8DType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.UInt8DType "Link to this definition")

numpy.dtypes.Int16DType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.Int16DType "Link to this definition")

numpy.dtypes.UInt16DType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.UInt16DType "Link to this definition")

numpy.dtypes.Int32DType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.Int32DType "Link to this definition")

numpy.dtypes.UInt32DType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.UInt32DType "Link to this definition")

numpy.dtypes.Int64DType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.Int64DType "Link to this definition")

numpy.dtypes.UInt64DType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.UInt64DType "Link to this definition")

C-named integers (may be aliases)[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#c-named-integers-may-be-aliases "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

numpy.dtypes.ByteDType[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/dtypes.py)
[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.ByteDType "Link to this definition")

numpy.dtypes.UByteDType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.UByteDType "Link to this definition")

numpy.dtypes.ShortDType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.ShortDType "Link to this definition")

numpy.dtypes.UShortDType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.UShortDType "Link to this definition")

numpy.dtypes.IntDType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.IntDType "Link to this definition")

numpy.dtypes.UIntDType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.UIntDType "Link to this definition")

numpy.dtypes.LongDType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.LongDType "Link to this definition")

numpy.dtypes.ULongDType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.ULongDType "Link to this definition")

numpy.dtypes.LongLongDType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.LongLongDType "Link to this definition")

numpy.dtypes.ULongLongDType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.ULongLongDType "Link to this definition")

Floating point[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#floating-point "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

numpy.dtypes.Float16DType[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/dtypes.py)
[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.Float16DType "Link to this definition")

numpy.dtypes.Float32DType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.Float32DType "Link to this definition")

numpy.dtypes.Float64DType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.Float64DType "Link to this definition")

numpy.dtypes.LongDoubleDType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.LongDoubleDType "Link to this definition")

Complex[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#complex "Link to this heading")

-------------------------------------------------------------------------------------------------------

numpy.dtypes.Complex64DType[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/dtypes.py)
[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.Complex64DType "Link to this definition")

numpy.dtypes.Complex128DType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.Complex128DType "Link to this definition")

numpy.dtypes.CLongDoubleDType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.CLongDoubleDType "Link to this definition")

Strings and Bytestrings[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#strings-and-bytestrings "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

numpy.dtypes.StrDType[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/dtypes.py)
[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.StrDType "Link to this definition")

numpy.dtypes.BytesDType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.BytesDType "Link to this definition")

numpy.dtypes.StringDType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.StringDType "Link to this definition")

Times[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#times "Link to this heading")

---------------------------------------------------------------------------------------------------

numpy.dtypes.DateTime64DType[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/dtypes.py)
[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.DateTime64DType "Link to this definition")

numpy.dtypes.TimeDelta64DType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.TimeDelta64DType "Link to this definition")

Others[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#others "Link to this heading")

-----------------------------------------------------------------------------------------------------

numpy.dtypes.ObjectDType[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/dtypes.py)
[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.ObjectDType "Link to this definition")

numpy.dtypes.VoidDType[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#numpy.dtypes.VoidDType "Link to this definition")

Routines for DType authors[#](https://numpy.org/doc/stable/reference/routines.dtypes.html#routines-for-dtype-authors "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`register_dlpack_dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtypes.register_dlpack_dtype.html#numpy.dtypes.register_dlpack_dtype "numpy.dtypes.register_dlpack_dtype")<br>(dlpack\_key, dtype, /) | Register a NumPy dtype for a DLPack `(code, bits)` pair so that [`numpy.from_dlpack`](https://numpy.org/doc/stable/reference/generated/numpy.from_dlpack.html#numpy.from_dlpack "numpy.from_dlpack")<br> can import it and `ndarray.__dlpack__` can export it. |

On this page