[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fromfile.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fromfile.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fromfile.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fromfile.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fromfile.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fromfile.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fromfile.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fromfile.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fromfile.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fromfile.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fromfile.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fromfile.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fromfile.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fromfile.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fromfile.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fromfile.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fromfile.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fromfile.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fromfile.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fromfile.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fromfile[#](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#numpy-fromfile "Link to this heading")

==============================================================================================================================

numpy.fromfile(_file_, _dtype\=np.float64_, _count\=\-1_, _sep\=''_, _offset\=0_, _\*_, _like\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#numpy.fromfile "Link to this definition")

Construct an array from data in a text or binary file.

A highly efficient way of reading binary data with a known data-type, as well as parsing simply formatted text files. Data written using the _tofile_ method can be read using this function.

Parameters:

**file**file or str or Path

An open file object, a string containing the filename, or a Path object. When reading from a file object it must support random access (i.e. it must have tell and seek methods).

**dtype**data-type

Data type of the returned array. For binary files, it is used to determine the size and byte-order of the items in the file. Most builtin numeric types are supported and extension types may be supported.

**count**int

Number of items to read. `-1` means all items (i.e., the complete file).

**sep**str

Separator between items if file is a text file. Empty (“”) separator means the file should be treated as binary. Spaces (” “) in the separator match zero or more whitespace characters. A separator consisting only of spaces must match at least one whitespace.

**offset**int

The offset (in bytes) from the file’s current position. Defaults to 0. Only permitted for binary files.

**like**array\_like, optional

Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as `like` supports the `__array_function__` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

See also

[`load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy.load "numpy.load")
, [`save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html#numpy.save "numpy.save")

[`ndarray.tofile`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tofile.html#numpy.ndarray.tofile "numpy.ndarray.tofile")

[`loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt "numpy.loadtxt")

More flexible way of loading data from a text file.

Notes

Do not rely on the combination of _tofile_ and [`fromfile`](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#numpy.fromfile "numpy.fromfile")
 for data storage, as the binary files generated are not platform independent. In particular, no byte-order or data-type information is saved. Data can be stored in the platform independent `.npy` format using [`save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html#numpy.save "numpy.save")
 and [`load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy.load "numpy.load")
 instead.

Examples

Try it in your browser!

Construct an ndarray:

\>>> import numpy as np
\>>> dt \= np.dtype(\[('time', \[('min', np.int64), ('sec', np.int64)\]),\
...                ('temp', float)\])
\>>> x \= np.zeros((1,), dtype\=dt)
\>>> x\['time'\]\['min'\] \= 10; x\['temp'\] \= 98.25
\>>> x
array(\[((10, 0), 98.25)\],
      dtype=\[('time', \[('min', '<i8'), ('sec', '<i8')\]), ('temp', '<f8')\])

Copy to clipboard

Save the raw data to disk:

\>>> import tempfile
\>>> fname \= tempfile.mkstemp()\[1\]
\>>> x.tofile(fname)

Copy to clipboard

Read the raw data from disk:

\>>> np.fromfile(fname, dtype\=dt)
array(\[((10, 0), 98.25)\],
      dtype=\[('time', \[('min', '<i8'), ('sec', '<i8')\]), ('temp', '<f8')\])

Copy to clipboard

The recommended way to store and load data:

\>>> np.save(fname, x)
\>>> np.load(fname + '.npy')
array(\[((10, 0), 98.25)\],
      dtype=\[('time', \[('min', '<i8'), ('sec', '<i8')\]), ('temp', '<f8')\])

Copy to clipboard

Go BackOpen In Tab

On this page