[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.npyio.NpzFile.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.npyio.NpzFile.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.npyio.NpzFile.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.npyio.NpzFile.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.npyio.NpzFile.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.npyio.NpzFile.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.npyio.NpzFile.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.npyio.NpzFile.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.npyio.NpzFile.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.npyio.NpzFile.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.npyio.NpzFile.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.npyio.NpzFile.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.npyio.NpzFile.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.npyio.NpzFile.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.npyio.NpzFile.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.npyio.NpzFile.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.npyio.NpzFile.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.npyio.NpzFile.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.npyio.NpzFile.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.npyio.NpzFile.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.npyio.NpzFile[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#numpy-lib-npyio-npzfile "Link to this heading")

=========================================================================================================================================================

_class_ numpy.lib.npyio.NpzFile(_fid_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_npyio_impl.py#L115-L308)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#numpy.lib.npyio.NpzFile "Link to this definition")

A dictionary-like object with lazy-loading of files in the zipped archive provided on construction.

[`NpzFile`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#numpy.lib.npyio.NpzFile "numpy.lib.npyio.NpzFile")
 is used to load files in the NumPy `.npz` data archive format. It assumes that files in the archive have a `.npy` extension, other files are ignored.

The arrays and file strings are lazily loaded on either getitem access using `obj['key']` or attribute lookup using `obj.f.key`. A list of all files (without `.npy` extensions) can be obtained with `obj.files` and the ZipFile object itself using `obj.zip`.

Parameters:

**fid**file, str, or pathlib.Path

The zipped archive to open. This is either a file-like object or a string containing the path to the archive.

**own\_fid**bool, optional

Whether NpzFile should close the file handle. Requires that [`fid`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.fid.html#numpy.lib.npyio.NpzFile.fid "numpy.lib.npyio.NpzFile.fid")
 is a file-like object.

Attributes:

**files**list of str

List of all files in the archive with a `.npy` extension.

**zip**ZipFile instance

The ZipFile object initialized with the zipped archive.

**f**BagObj instance

An object on which attribute can be performed as an alternative to getitem access on the [`NpzFile`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#numpy.lib.npyio.NpzFile "numpy.lib.npyio.NpzFile")
 instance itself.

**allow\_pickle**bool, optional

Allow loading pickled data. Default: False

**pickle\_kwargs**dict, optional

Additional keyword arguments to pass on to pickle.load. These are only useful when loading object arrays saved on Python 2.

**max\_header\_size**int, optional

Maximum allowed size of the header. Large headers may not be safe to load securely and thus require explicitly passing a larger value. See [`ast.literal_eval`](https://docs.python.org/3/library/ast.html#ast.literal_eval "(in Python v3.14)")
 for details. This option is ignored when _allow\_pickle_ is passed. In that case the file is by definition trusted and the limit is unnecessary.

Methods

|     |     |
| --- | --- |
| [`close`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.close.html#numpy.lib.npyio.NpzFile.close "numpy.lib.npyio.NpzFile.close")<br>() | Close the file. |
| [`get`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.get.html#numpy.lib.npyio.NpzFile.get "numpy.lib.npyio.NpzFile.get")<br>(key\[, default\]) | D.get(k,\[,d\]) returns D\[k\] if k in D, else d. |
| [`items`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.items.html#numpy.lib.npyio.NpzFile.items "numpy.lib.npyio.NpzFile.items")<br>() | D.items() returns a set-like object providing a view on the items |
| [`keys`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.keys.html#numpy.lib.npyio.NpzFile.keys "numpy.lib.npyio.NpzFile.keys")<br>() | D.keys() returns a set-like object providing a view on the keys |
| [`values`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.values.html#numpy.lib.npyio.NpzFile.values "numpy.lib.npyio.NpzFile.values")<br>() | D.values() returns a set-like object providing a view on the values |

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from tempfile import TemporaryFile
\>>> outfile \= TemporaryFile()
\>>> x \= np.arange(10)
\>>> y \= np.sin(x)
\>>> np.savez(outfile, x\=x, y\=y)
\>>> \_ \= outfile.seek(0)

Copy to clipboard

\>>> npz \= np.load(outfile)
\>>> isinstance(npz, np.lib.npyio.NpzFile)
True
\>>> npz
NpzFile 'object' with keys: x, y
\>>> sorted(npz.files)
\['x', 'y'\]
\>>> npz\['x'\]  \# getitem access
array(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\])
\>>> npz.f.x  \# attribute lookup
array(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\])

Copy to clipboard

Go BackOpen In Tab

On this page