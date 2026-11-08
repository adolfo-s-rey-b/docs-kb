[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.recarray.tofile.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.recarray.tofile[#](https://numpy.org/doc/stable/reference/generated/numpy.recarray.tofile.html#numpy-recarray-tofile "Link to this heading")

===================================================================================================================================================

method

recarray.tofile(_fid_, _/_, _sep\=''_, _format\='%s'_)[#](https://numpy.org/doc/stable/reference/generated/numpy.recarray.tofile.html#numpy.recarray.tofile "Link to this definition")

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