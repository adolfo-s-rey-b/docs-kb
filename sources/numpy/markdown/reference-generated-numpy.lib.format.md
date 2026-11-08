[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.format[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#module-numpy.lib.format "Link to this heading")

===========================================================================================================================================

Binary serialization

NPY format[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#npy-format "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

A simple format for saving numpy arrays to disk with the full information about them.

The `.npy` format is the standard binary file format in NumPy for persisting a _single_ arbitrary NumPy array on disk. The format stores all of the shape and dtype information necessary to reconstruct the array correctly even on another machine with a different architecture. The format is designed to be as simple as possible while achieving its limited goals.

The `.npz` format is the standard format for persisting _multiple_ NumPy arrays on disk. A `.npz` file is a zip file containing multiple `.npy` files, one for each array.

### Capabilities[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#capabilities "Link to this heading")

*   Can represent all NumPy arrays including nested record arrays and object arrays.
    
*   Represents the data in its native binary form.
    
*   Supports Fortran-contiguous arrays directly.
    
*   Stores all of the necessary information to reconstruct the array including shape and dtype on a machine of a different architecture. Both little-endian and big-endian arrays are supported, and a file with little-endian numbers will yield a little-endian array on any machine reading the file. The types are described in terms of their actual sizes. For example, if a machine with a 64-bit C “long int” writes out an array with “long ints”, a reading machine with 32-bit C “long ints” will yield an array with 64-bit integers.
    
*   Is straightforward to reverse engineer. Datasets often live longer than the programs that created them. A competent developer should be able to create a solution in their preferred programming language to read most `.npy` files that they have been given without much documentation.
    
*   Allows memory-mapping of the data. See [`open_memmap`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.open_memmap.html#numpy.lib.format.open_memmap "numpy.lib.format.open_memmap")
    .
    
*   Can be read from a filelike stream object instead of an actual file.
    
*   Stores object arrays, i.e. arrays containing elements that are arbitrary Python objects. Files with object arrays are not to be mmapable, but can be read and written to disk.
    

### Limitations[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#limitations "Link to this heading")

*   Arbitrary subclasses of numpy.ndarray are not completely preserved. Subclasses will be accepted for writing, but only the array data will be written out. A regular numpy.ndarray object will be created upon reading the file.
    

Warning

Due to limitations in the interpretation of structured dtypes, dtypes with fields with empty names will have the names replaced by ‘f0’, ‘f1’, etc. Such arrays will not round-trip through the format entirely accurately. The data is intact; only the field names will differ. We are working on a fix for this. This fix will not require a change in the file format. The arrays with such structures can still be saved and restored, and the correct dtype may be restored by using the `loadedarray.view(correct_dtype)` method.

### File extensions[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#file-extensions "Link to this heading")

We recommend using the `.npy` and `.npz` extensions for files saved in this format. This is by no means a requirement; applications may wish to use these file formats but use an extension specific to the application. In the absence of an obvious alternative, however, we suggest using `.npy` and `.npz`.

### Version numbering[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#version-numbering "Link to this heading")

The version numbering of these formats is independent of NumPy version numbering. If the format is upgraded, the code in _numpy.io_ will still be able to read and write Version 1.0 files.

### Format Version 1.0[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#format-version-1-0 "Link to this heading")

The first 6 bytes are a magic string: exactly `\x93NUMPY`.

The next 1 byte is an unsigned byte: the major version number of the file format, e.g. `\x01`.

The next 1 byte is an unsigned byte: the minor version number of the file format, e.g. `\x00`. Note: the version of the file format is not tied to the version of the numpy package.

The next 2 bytes form a little-endian unsigned short int: the length of the header data HEADER\_LEN.

The next HEADER\_LEN bytes form the header data describing the array’s format. It is an ASCII string which contains a Python literal expression of a dictionary. It is terminated by a newline (`\n`) and padded with spaces (`\x20`) to make the total of `len(magic string) + 2 + len(length) + HEADER_LEN` be evenly divisible by 64 for alignment purposes.

The dictionary contains three keys:

> “descr”dtype.descr
> 
> An object that can be passed as an argument to the [`numpy.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
>  constructor to create the array’s dtype.
> 
> “fortran\_order”bool
> 
> Whether the array data is Fortran-contiguous or not. Since Fortran-contiguous arrays are a common form of non-C-contiguity, we allow them to be written directly to disk for efficiency.
> 
> “shape”tuple of int
> 
> The shape of the array.

For repeatability and readability, the dictionary keys are sorted in alphabetic order. This is for convenience only. A writer SHOULD implement this if possible. A reader MUST NOT depend on this.

Following the header comes the array data. If the dtype contains Python objects (i.e. `dtype.hasobject is True`), then the data is a Python pickle of the array. Otherwise the data is the contiguous (either C- or Fortran-, depending on `fortran_order`) bytes of the array. Consumers can figure out the number of bytes by multiplying the number of elements given by the shape (noting that `shape=()` means there is 1 element) by `dtype.itemsize`.

### Format Version 2.0[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#format-version-2-0 "Link to this heading")

The version 1.0 format only allowed the array header to have a total size of 65535 bytes. This can be exceeded by structured arrays with a large number of columns. The version 2.0 format extends the header size to 4 GiB. [`numpy.save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html#numpy.save "numpy.save")
 will automatically save in 2.0 format if the data requires it, else it will always use the more compatible 1.0 format.

The description of the fourth element of the header therefore has become: “The next 4 bytes form a little-endian unsigned int: the length of the header data HEADER\_LEN.”

### Format Version 3.0[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#format-version-3-0 "Link to this heading")

This version replaces the ASCII string (which in practice was latin1) with a utf8-encoded string, so supports structured types with any unicode field names.

### Notes[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#notes "Link to this heading")

The `.npy` format, including motivation for creating it and a comparison of alternatives, is described in the [“npy-format” NEP](https://numpy.org/neps/nep-0001-npy-format.html "(in NumPy Enhancement Proposals)")
, however details have evolved with time and this document is more current.

Functions

|     |     |
| --- | --- |
| [`descr_to_dtype`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.descr_to_dtype.html#numpy.lib.format.descr_to_dtype "numpy.lib.format.descr_to_dtype")<br>(descr) | Returns a dtype based off the given description. |
| [`drop_metadata`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.drop_metadata.html#numpy.lib.format.drop_metadata "numpy.lib.format.drop_metadata")<br>(dtype, /) | Returns the dtype unchanged if it contained no metadata or a copy of the dtype if it (or any of its structure dtypes) contained metadata. |
| [`dtype_to_descr`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.dtype_to_descr.html#numpy.lib.format.dtype_to_descr "numpy.lib.format.dtype_to_descr")<br>(dtype) | Get a serializable descriptor from the dtype. |
| [`header_data_from_array_1_0`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.header_data_from_array_1_0.html#numpy.lib.format.header_data_from_array_1_0 "numpy.lib.format.header_data_from_array_1_0")<br>(array) | Get the dictionary of header metadata from a numpy.ndarray. |
| [`isfileobj`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.isfileobj.html#numpy.lib.format.isfileobj "numpy.lib.format.isfileobj")<br>(f) |     |
| [`magic`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.magic.html#numpy.lib.format.magic "numpy.lib.format.magic")<br>(major, minor) | Return the magic string for the given file format version. |
| [`open_memmap`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.open_memmap.html#numpy.lib.format.open_memmap "numpy.lib.format.open_memmap")<br>(filename\[, mode, dtype, shape, ...\]) | Open a .npy file as a memory-mapped array. |
| [`read_array`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.read_array.html#numpy.lib.format.read_array "numpy.lib.format.read_array")<br>(fp\[, allow\_pickle, ...\]) | Read an array from an NPY file. |
| [`read_array_header_1_0`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.read_array_header_1_0.html#numpy.lib.format.read_array_header_1_0 "numpy.lib.format.read_array_header_1_0")<br>(fp\[, max\_header\_size\]) | Read an array header from a filelike object using the 1.0 file format version. |
| [`read_array_header_2_0`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.read_array_header_2_0.html#numpy.lib.format.read_array_header_2_0 "numpy.lib.format.read_array_header_2_0")<br>(fp\[, max\_header\_size\]) | Read an array header from a filelike object using the 2.0 file format version. |
| [`read_magic`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.read_magic.html#numpy.lib.format.read_magic "numpy.lib.format.read_magic")<br>(fp) | Read the magic string to get the version of the file format. |
| [`write_array`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.write_array.html#numpy.lib.format.write_array "numpy.lib.format.write_array")<br>(fp, array\[, version, ...\]) | Write an array to an NPY file, including a header. |
| [`write_array_header_1_0`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.write_array_header_1_0.html#numpy.lib.format.write_array_header_1_0 "numpy.lib.format.write_array_header_1_0")<br>(fp, d) | Write the header for an array using the 1.0 format. |
| [`write_array_header_2_0`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.write_array_header_2_0.html#numpy.lib.format.write_array_header_2_0 "numpy.lib.format.write_array_header_2_0")<br>(fp, d) | Write the header for an array using the 2.0 format. |

On this page