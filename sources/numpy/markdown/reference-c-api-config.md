[Skip to main content](https://numpy.org/doc/stable/reference/c-api/config.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

System configuration[#](https://numpy.org/doc/stable/reference/c-api/config.html#system-configuration "Link to this heading")

==============================================================================================================================

When NumPy is built, information about system configuration is recorded, and is made available for extension modules using NumPy’s C API. These are mostly defined in `numpyconfig.h` (included in `ndarrayobject.h`). The public symbols are prefixed by `NPY_*`. NumPy also offers some functions for querying information about the platform in use.

For private use, NumPy also constructs a `config.h` in the NumPy include directory, which is not exported by NumPy (that is a python extension which use the numpy C API will not see those symbols), to avoid namespace pollution.

Data type sizes[#](https://numpy.org/doc/stable/reference/c-api/config.html#data-type-sizes "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

The `NPY_SIZEOF_{CTYPE}` constants are defined so that sizeof information is available to the pre-processor.

NPY\_SIZEOF\_SHORT[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_SIZEOF_SHORT "Link to this definition")
  

sizeof(short)

NPY\_SIZEOF\_INT[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_SIZEOF_INT "Link to this definition")
  

sizeof(int)

NPY\_SIZEOF\_LONG[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_SIZEOF_LONG "Link to this definition")
  

sizeof(long)

NPY\_SIZEOF\_LONGLONG[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_SIZEOF_LONGLONG "Link to this definition")
  

sizeof(longlong) where longlong is defined appropriately on the platform.

NPY\_SIZEOF\_PY\_LONG\_LONG[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_SIZEOF_PY_LONG_LONG "Link to this definition")
  

NPY\_SIZEOF\_FLOAT[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_SIZEOF_FLOAT "Link to this definition")
  

sizeof(float)

NPY\_SIZEOF\_DOUBLE[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_SIZEOF_DOUBLE "Link to this definition")
  

sizeof(double)

NPY\_SIZEOF\_LONG\_DOUBLE[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_SIZEOF_LONG_DOUBLE "Link to this definition")
  

NPY\_SIZEOF\_LONGDOUBLE[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_SIZEOF_LONGDOUBLE "Link to this definition")
  

sizeof(longdouble)

NPY\_SIZEOF\_PY\_INTPTR\_T[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_SIZEOF_PY_INTPTR_T "Link to this definition")
  

Size of a pointer `void *` and `intptr_t`/`Py_intptr_t`.

NPY\_SIZEOF\_INTP[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_SIZEOF_INTP "Link to this definition")
  

Size of a `size_t` on this platform (`sizeof(size_t)`)

Platform information[#](https://numpy.org/doc/stable/reference/c-api/config.html#platform-information "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

NPY\_CPU\_X86[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_CPU_X86 "Link to this definition")
  

NPY\_CPU\_AMD64[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_CPU_AMD64 "Link to this definition")
  

NPY\_CPU\_IA64[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_CPU_IA64 "Link to this definition")
  

NPY\_CPU\_PPC[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_CPU_PPC "Link to this definition")
  

NPY\_CPU\_PPC64[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_CPU_PPC64 "Link to this definition")
  

NPY\_CPU\_SPARC[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_CPU_SPARC "Link to this definition")
  

NPY\_CPU\_SPARC64[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_CPU_SPARC64 "Link to this definition")
  

NPY\_CPU\_S390[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_CPU_S390 "Link to this definition")
  

NPY\_CPU\_PARISC[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_CPU_PARISC "Link to this definition")
  

CPU architecture of the platform; only one of the above is defined.

Defined in `numpy/npy_cpu.h`

NPY\_LITTLE\_ENDIAN[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_LITTLE_ENDIAN "Link to this definition")
  

NPY\_BIG\_ENDIAN[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_BIG_ENDIAN "Link to this definition")
  

NPY\_BYTE\_ORDER[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_BYTE_ORDER "Link to this definition")
  

Portable alternatives to the `endian.h` macros of GNU Libc. If big endian, [`NPY_BYTE_ORDER`](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_BYTE_ORDER "NPY_BYTE_ORDER")
 == [`NPY_BIG_ENDIAN`](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_BIG_ENDIAN "NPY_BIG_ENDIAN")
, and similarly for little endian architectures.

Defined in `numpy/npy_endian.h`.

int PyArray\_GetEndianness()[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.PyArray_GetEndianness "Link to this definition")
  

Returns the endianness of the current platform. One of [`NPY_CPU_BIG`](https://numpy.org/doc/stable/reference/c-api/config.html#c.PyArray_GetEndianness.NPY_CPU_BIG "NPY_CPU_BIG")
, [`NPY_CPU_LITTLE`](https://numpy.org/doc/stable/reference/c-api/config.html#c.PyArray_GetEndianness.NPY_CPU_LITTLE "NPY_CPU_LITTLE")
, or [`NPY_CPU_UNKNOWN_ENDIAN`](https://numpy.org/doc/stable/reference/c-api/config.html#c.PyArray_GetEndianness.NPY_CPU_UNKNOWN_ENDIAN "NPY_CPU_UNKNOWN_ENDIAN")
.

NPY\_CPU\_BIG[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.PyArray_GetEndianness.NPY_CPU_BIG "Link to this definition")
  

NPY\_CPU\_LITTLE[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.PyArray_GetEndianness.NPY_CPU_LITTLE "Link to this definition")
  

NPY\_CPU\_UNKNOWN\_ENDIAN[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.PyArray_GetEndianness.NPY_CPU_UNKNOWN_ENDIAN "Link to this definition")
  

Compiler directives[#](https://numpy.org/doc/stable/reference/c-api/config.html#compiler-directives "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

NPY\_LIKELY[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_LIKELY "Link to this definition")
  

NPY\_UNLIKELY[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_UNLIKELY "Link to this definition")
  

NPY\_UNUSED[#](https://numpy.org/doc/stable/reference/c-api/config.html#c.NPY_UNUSED "Link to this definition")
  

On this page