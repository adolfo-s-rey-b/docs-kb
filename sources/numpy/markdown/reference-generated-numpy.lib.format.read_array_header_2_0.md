[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.read_array_header_2_0.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.format.read_array_header_2_0.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.format.read_array_header_2_0.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.format.read\_array\_header\_2\_0[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.read_array_header_2_0.html#numpy-lib-format-read-array-header-2-0 "Link to this heading")

==========================================================================================================================================================================================================

lib.format.read\_array\_header\_2\_0(_fp_, _max\_header\_size\=10000_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_format_impl.py#L548-L583)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.read_array_header_2_0.html#numpy.lib.format.read_array_header_2_0 "Link to this definition")

Read an array header from a filelike object using the 2.0 file format version.

This will leave the file object located just after the header.

Parameters:

**fp**filelike object

A file object or something with a _read()_ method like a file.

**max\_header\_size**int, optional

Maximum allowed size of the header. Large headers may not be safe to load securely and thus require explicitly passing a larger value. See [`ast.literal_eval`](https://docs.python.org/3/library/ast.html#ast.literal_eval "(in Python v3.14)")
 for details.

Returns:

**shape**tuple of int

The shape of the array.

**fortran\_order**bool

The array data will be written out directly if it is either C-contiguous or Fortran-contiguous. Otherwise, it will be made contiguous before writing it out.

**dtype**dtype

The dtype of the file’s data.

Raises:

ValueError

If the data is invalid.

On this page