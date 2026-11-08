[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.savez_compressed.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.savez_compressed.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.savez_compressed.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.savez_compressed.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.savez_compressed.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.savez_compressed.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.savez_compressed.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.savez_compressed.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.savez_compressed.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.savez_compressed.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.savez_compressed.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.savez_compressed.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.savez_compressed.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.savez_compressed.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.savez_compressed.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.savez_compressed.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.savez_compressed.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.savez_compressed.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.savez_compressed.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.savez_compressed.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.savez_compressed.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.savez_compressed.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.savez\_compressed[#](https://numpy.org/doc/stable/reference/generated/numpy.savez_compressed.html#numpy-savez-compressed "Link to this heading")

=======================================================================================================================================================

numpy.savez\_compressed(_file_, _\*args_, _allow\_pickle\=True_, _\*\*kwds_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_npyio_impl.py#L681-L753)
[#](https://numpy.org/doc/stable/reference/generated/numpy.savez_compressed.html#numpy.savez_compressed "Link to this definition")

Save several arrays into a single file in compressed `.npz` format.

Provide arrays as keyword arguments to store them under the corresponding name in the output file: `savez_compressed(fn, x=x, y=y)`.

If arrays are specified as positional arguments, i.e., `savez_compressed(fn, x, y)`, their names will be _arr\_0_, _arr\_1_, etc.

Parameters:

**file**file, str, or pathlib.Path

Either the filename (string) or an open file (file-like object) where the data will be saved. If file is a string or a Path, the `.npz` extension will be appended to the filename if it is not already there.

**args**Arguments, optional

Arrays to save to the file. Please use keyword arguments (see _kwds_ below) to assign names to arrays. Arrays specified as args will be named “arr\_0”, “arr\_1”, and so on.

**allow\_pickle**bool, optional

Allow saving object arrays using Python pickles. Reasons for disallowing pickles include security (loading pickled data can execute arbitrary code) and portability (pickled objects may not be loadable on different Python installations, for example if the stored objects require libraries that are not available, and not all pickled data is compatible between different versions of Python). Default: True

**kwds**Keyword arguments, optional

Arrays to save to the file. Each array will be saved to the output file with its corresponding keyword name.

Returns:

None

See also

[`numpy.save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html#numpy.save "numpy.save")

Save a single array to a binary file in NumPy format.

[`numpy.savetxt`](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html#numpy.savetxt "numpy.savetxt")

Save an array to a file as plain text.

[`numpy.savez`](https://numpy.org/doc/stable/reference/generated/numpy.savez.html#numpy.savez "numpy.savez")

Save several arrays into an uncompressed `.npz` file format

[`numpy.load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy.load "numpy.load")

Load the files created by savez\_compressed.

Notes

The `.npz` file format is a zipped archive of files named after the variables they contain. The archive is compressed with `zipfile.ZIP_DEFLATED` and each file in the archive contains one variable in `.npy` format. For a description of the `.npy` format, see [`numpy.lib.format`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#module-numpy.lib.format "numpy.lib.format")
.

When opening the saved `.npz` file with [`load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy.load "numpy.load")
 a [`NpzFile`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#numpy.lib.npyio.NpzFile "numpy.lib.npyio.NpzFile")
 object is returned. This is a dictionary-like object which can be queried for its list of arrays (with the `.files` attribute), and for the arrays themselves.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> test\_array \= np.random.rand(3, 2)
\>>> test\_vector \= np.random.rand(4)
\>>> np.savez\_compressed('/tmp/123', a\=test\_array, b\=test\_vector)
\>>> loaded \= np.load('/tmp/123.npz')
\>>> print(np.array\_equal(test\_array, loaded\['a'\]))
True
\>>> print(np.array\_equal(test\_vector, loaded\['b'\]))
True

Copy to clipboard

Go BackOpen In Tab

On this page