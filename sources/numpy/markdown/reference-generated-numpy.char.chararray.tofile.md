[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.tofile.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.char.chararray.tofile.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.tofile.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.char.chararray.tofile.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.char.chararray.tofile.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.char.chararray.tofile.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.char.chararray.tofile.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.char.chararray.tofile.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.char.chararray.tofile.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.char.chararray.tofile.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.char.chararray.tofile.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.char.chararray.tofile.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.char.chararray.tofile.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.char.chararray.tofile.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.char.chararray.tofile.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.char.chararray.tofile.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.char.chararray.tofile.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.char.chararray.tofile.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.char.chararray.tofile.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.char.chararray.tofile.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.char.chararray.tofile.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.char.chararray.tofile.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.chararray.tofile[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.tofile.html#numpy-char-chararray-tofile "Link to this heading")

=====================================================================================================================================================================

method

char.chararray.tofile(_fid_, _/_, _sep\=''_, _format\='%s'_)[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.tofile.html#numpy.char.chararray.tofile "Link to this definition")

Write array to a file as text or binary (default).

Data is always written in ‘C’ order, independent of the order of _a_. The data produced by this method can be recovered using the function fromfile().

Parameters:

**fid**file or str or Path

An open file object, or a string containing a filename.

**sep**str

Separator between array items for text output. If “” (empty), a binary file is written, equivalent to `file.write(a.tobytes())`.

**format**str

Format string for text file output. Each entry in the array is formatted to text by first converting it to the closest Python type, and then using “format” % item.

Notes

This is a convenience function for quick storage of array data. Information on endianness and precision is lost, so this method is not a good choice for files intended to archive data or transport data between machines with different endianness. Some of these problems can be overcome by outputting the data as text files, at the expense of speed and file size.

When fid is a file object, array contents are directly written to the file, bypassing the file object’s `write` method. As a result, tofile cannot be used with files objects supporting compression (e.g., GzipFile) or file-like objects that do not support `fileno()` (e.g., BytesIO).

On this page