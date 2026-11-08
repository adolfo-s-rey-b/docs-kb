[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.open_memmap.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.format.open_memmap.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.open_memmap.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.format.open_memmap.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.format.open_memmap.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.format.open_memmap.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.format.open_memmap.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.format.open_memmap.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.format.open_memmap.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.format.open_memmap.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.format.open_memmap.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.format.open_memmap.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.format.open_memmap.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.format.open_memmap.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.format.open_memmap.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.format.open_memmap.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.format.open_memmap.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.format.open_memmap.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.format.open_memmap.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.format.open_memmap.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.format.open_memmap.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.format.open_memmap.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.format.open\_memmap[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.open_memmap.html#numpy-lib-format-open-memmap "Link to this heading")

=========================================================================================================================================================================

lib.format.open\_memmap(_filename_, _mode\='r+'_, _dtype\=None_, _shape\=None_, _fortran\_order\=False_, _version\=None_, _\*_, _max\_header\_size\=10000_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_format_impl.py#L892-L997)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.open_memmap.html#numpy.lib.format.open_memmap "Link to this definition")

Open a .npy file as a memory-mapped array.

This may be used to read an existing file or create a new one.

Parameters:

**filename**str or path-like

The name of the file on disk. This may _not_ be a file-like object.

**mode**str, optional

The mode in which to open the file; the default is ‘r+’. In addition to the standard file modes, ‘c’ is also accepted to mean “copy on write.” See [`memmap`](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html#numpy.memmap "numpy.memmap")
 for the available mode strings.

**dtype**data-type, optional

The data type of the array if we are creating a new file in “write” mode, if not, [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is ignored. The default value is None, which results in a data-type of [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
.

**shape**tuple of int

The shape of the array if we are creating a new file in “write” mode, in which case this parameter is required. Otherwise, this parameter is ignored and is thus optional.

**fortran\_order**bool, optional

Whether the array should be Fortran-contiguous (True) or C-contiguous (False, the default) if we are creating a new file in “write” mode.

**version**tuple of int (major, minor) or None

If the mode is a “write” mode, then this is the version of the file format used to create the file. None means use the oldest supported version that is able to store the data. Default: None

**max\_header\_size**int, optional

Maximum allowed size of the header. Large headers may not be safe to load securely and thus require explicitly passing a larger value. See [`ast.literal_eval`](https://docs.python.org/3/library/ast.html#ast.literal_eval "(in Python v3.14)")
 for details.

Returns:

**marray**memmap

The memory-mapped array.

Raises:

ValueError

If the data or the mode is invalid.

OSError

If the file is not found or cannot be opened correctly.

See also

[`numpy.memmap`](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html#numpy.memmap "numpy.memmap")

On this page