[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.dtypes.register_dlpack_dtype.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.dtypes.register_dlpack_dtype.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.dtypes.register_dlpack_dtype.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.dtypes.register\_dlpack\_dtype[#](https://numpy.org/doc/stable/reference/generated/numpy.dtypes.register_dlpack_dtype.html#numpy-dtypes-register-dlpack-dtype "Link to this heading")

============================================================================================================================================================================================

dtypes.register\_dlpack\_dtype(_dlpack\_key_, _dtype_, _/_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/dtypes.py#L29-L72)
[#](https://numpy.org/doc/stable/reference/generated/numpy.dtypes.register_dlpack_dtype.html#numpy.dtypes.register_dlpack_dtype "Link to this definition")

Register a NumPy dtype for a DLPack `(code, bits)` pair so that [`numpy.from_dlpack`](https://numpy.org/doc/stable/reference/generated/numpy.from_dlpack.html#numpy.from_dlpack "numpy.from_dlpack")
 can import it and `ndarray.__dlpack__` can export it. Built-in dtype mappings take priority on import.

If you think a conflict is possible but unproblematic you may wrap this into a try/except block as NumPy will raise an error if another DType is already registered for the same (code, bits) pair. While an error is raised, the export is registered even on error.

Registering an identical (not equal) dtype multiple times is allowed but normally registration should happen at import time.

Warning

It is the responsibility of the registering user to ensure that the mapping is valid.

Note

This function was added primarily for `ml_dtypes` and may be replaced with a different mechanism in the future. It is intended to be used by authors of user-defined dtypes and not end-users.

Parameters:

**dlpack\_key**tuple of int

`(dl_dtype_code, dl_bits)` matching the DLPack `DLDataType`, lanes is assumed to be always 1, currently.

**dtype**dtype

A NumPy dtype instance.

Raises:

**ValueError**If a conflicting registration was already done.

See also

[`numpy.from_dlpack`](https://numpy.org/doc/stable/reference/generated/numpy.from_dlpack.html#numpy.from_dlpack "numpy.from_dlpack")

On this page