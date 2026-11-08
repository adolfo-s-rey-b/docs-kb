[Skip to main content](https://numpy.org/doc/stable/reference/routines.io.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.io.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.io.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.io.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.io.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.io.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.io.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.io.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.io.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.io.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.io.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.io.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.io.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.io.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.io.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.io.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.io.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.io.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.io.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.io.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.io.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.io.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Input and output[#](https://numpy.org/doc/stable/reference/routines.io.html#input-and-output "Link to this heading")

=====================================================================================================================

NumPy binary files (npy, npz)[#](https://numpy.org/doc/stable/reference/routines.io.html#numpy-binary-files-npy-npz "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy.load "numpy.load")<br>(file\[, mmap\_mode, allow\_pickle, ...\]) | Load arrays or pickled objects from `.npy`, `.npz` or pickled files. |
| [`save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html#numpy.save "numpy.save")<br>(file, arr\[, allow\_pickle\]) | Save an array to a binary file in NumPy `.npy` format. |
| [`savez`](https://numpy.org/doc/stable/reference/generated/numpy.savez.html#numpy.savez "numpy.savez")<br>(file, \*args\[, allow\_pickle\]) | Save several arrays into a single file in uncompressed `.npz` format. |
| [`savez_compressed`](https://numpy.org/doc/stable/reference/generated/numpy.savez_compressed.html#numpy.savez_compressed "numpy.savez_compressed")<br>(file, \*args\[, allow\_pickle\]) | Save several arrays into a single file in compressed `.npz` format. |
| [`lib.npyio.NpzFile`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#numpy.lib.npyio.NpzFile "numpy.lib.npyio.NpzFile")<br>(fid) | A dictionary-like object with lazy-loading of files in the zipped archive provided on construction. |

The format of these binary file types is documented in [`numpy.lib.format`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#module-numpy.lib.format "numpy.lib.format")

Text files[#](https://numpy.org/doc/stable/reference/routines.io.html#text-files "Link to this heading")

---------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt "numpy.loadtxt")<br>(fname\[, dtype, comments, delimiter, ...\]) | Load data from a text file. |
| [`savetxt`](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html#numpy.savetxt "numpy.savetxt")<br>(fname, X\[, fmt, delimiter, newline, ...\]) | Save an array to a text file. |
| [`genfromtxt`](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt")<br>(fname\[, dtype, comments, ...\]) | Load data from a text file, with missing values handled as specified. |
| [`fromregex`](https://numpy.org/doc/stable/reference/generated/numpy.fromregex.html#numpy.fromregex "numpy.fromregex")<br>(file, regexp, dtype\[, encoding\]) | Construct an array from a text file, using regular expression parsing. |
| [`fromstring`](https://numpy.org/doc/stable/reference/generated/numpy.fromstring.html#numpy.fromstring "numpy.fromstring")<br>(string\[, dtype, count, like\]) | A new 1-D array initialized from text data in a string. |
| [`ndarray.tofile`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tofile.html#numpy.ndarray.tofile "numpy.ndarray.tofile")<br>(fid, /\[, sep, format\]) | Write array to a file as text or binary (default). |
| [`ndarray.tolist`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html#numpy.ndarray.tolist "numpy.ndarray.tolist")<br>() | Return the array as an `a.ndim`\-levels deep nested list of Python scalars. |

Raw binary files[#](https://numpy.org/doc/stable/reference/routines.io.html#raw-binary-files "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`fromfile`](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#numpy.fromfile "numpy.fromfile")<br>(file\[, dtype, count, sep, offset, like\]) | Construct an array from data in a text or binary file. |
| [`ndarray.tofile`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tofile.html#numpy.ndarray.tofile "numpy.ndarray.tofile")<br>(fid, /\[, sep, format\]) | Write array to a file as text or binary (default). |

String formatting[#](https://numpy.org/doc/stable/reference/routines.io.html#string-formatting "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`array2string`](https://numpy.org/doc/stable/reference/generated/numpy.array2string.html#numpy.array2string "numpy.array2string")<br>(a\[, max\_line\_width, precision, ...\]) | Return a string representation of an array. |
| [`array_repr`](https://numpy.org/doc/stable/reference/generated/numpy.array_repr.html#numpy.array_repr "numpy.array_repr")<br>(arr\[, max\_line\_width, precision, ...\]) | Return the string representation of an array. |
| [`array_str`](https://numpy.org/doc/stable/reference/generated/numpy.array_str.html#numpy.array_str "numpy.array_str")<br>(a\[, max\_line\_width, precision, ...\]) | Return a string representation of the data in an array. |
| [`format_float_positional`](https://numpy.org/doc/stable/reference/generated/numpy.format_float_positional.html#numpy.format_float_positional "numpy.format_float_positional")<br>(x\[, precision, ...\]) | Format a floating-point scalar as a decimal string in positional notation. |
| [`format_float_scientific`](https://numpy.org/doc/stable/reference/generated/numpy.format_float_scientific.html#numpy.format_float_scientific "numpy.format_float_scientific")<br>(x\[, precision, ...\]) | Format a floating-point scalar as a decimal string in scientific notation. |

Memory mapping files[#](https://numpy.org/doc/stable/reference/routines.io.html#memory-mapping-files "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`memmap`](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html#numpy.memmap "numpy.memmap")<br>(filename\[, dtype, mode, offset, ...\]) | Create a memory-map to an array stored in a _binary_ file on disk. |
| [`lib.format.open_memmap`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.open_memmap.html#numpy.lib.format.open_memmap "numpy.lib.format.open_memmap")<br>(filename\[, mode, ...\]) | Open a .npy file as a memory-mapped array. |

Text formatting options[#](https://numpy.org/doc/stable/reference/routines.io.html#text-formatting-options "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

Text formatting settings are maintained in a [`context variable`](https://docs.python.org/3/library/contextvars.html#module-contextvars "(in Python v3.14)")
, allowing different threads or async tasks to have independent configurations. For more information, see [Thread Safety](https://numpy.org/doc/stable/reference/thread_safety.html#thread-safety)
.

|     |     |
| --- | --- |
| [`set_printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html#numpy.set_printoptions "numpy.set_printoptions")<br>(\[precision, threshold, ...\]) | Set printing options. |
| [`get_printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.get_printoptions.html#numpy.get_printoptions "numpy.get_printoptions")<br>() | Return the current print options. |
| [`printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.printoptions.html#numpy.printoptions "numpy.printoptions")<br>(\*args, \*\*kwargs) | Context manager for setting print options. |

Base-n representations[#](https://numpy.org/doc/stable/reference/routines.io.html#base-n-representations "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`binary_repr`](https://numpy.org/doc/stable/reference/generated/numpy.binary_repr.html#numpy.binary_repr "numpy.binary_repr")<br>(num\[, width\]) | Return the binary representation of the input number as a string. |
| [`base_repr`](https://numpy.org/doc/stable/reference/generated/numpy.base_repr.html#numpy.base_repr "numpy.base_repr")<br>(number\[, base, padding\]) | Return a string representation of a number in the given base system. |

Data sources[#](https://numpy.org/doc/stable/reference/routines.io.html#data-sources "Link to this heading")

-------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`lib.npyio.DataSource`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.html#numpy.lib.npyio.DataSource "numpy.lib.npyio.DataSource")<br>(\[destpath\]) | A generic data source file (file, http, ftp, ...). |

Binary format description[#](https://numpy.org/doc/stable/reference/routines.io.html#binary-format-description "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`lib.format`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#module-numpy.lib.format "numpy.lib.format") | Binary serialization |

On this page