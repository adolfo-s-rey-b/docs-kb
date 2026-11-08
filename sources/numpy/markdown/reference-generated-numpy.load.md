[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.load.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.load.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.load.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.load.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.load.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.load.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.load.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.load.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.load.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.load.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.load.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.load.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.load.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.load.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.load.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.load.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.load.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.load.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.load.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.load.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.load.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.load.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.load[#](https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy-load "Link to this heading")

==================================================================================================================

numpy.load(_file_, _mmap\_mode\=None_, _allow\_pickle\=False_, _fix\_imports\=True_, _encoding\='ASCII'_, _\*_, _max\_header\_size\=10000_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_npyio_impl.py#L311-L497)
[#](https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy.load "Link to this definition")

Load arrays or pickled objects from `.npy`, `.npz` or pickled files.

Warning

Loading files that contain object arrays uses the `pickle` module, which is not secure against erroneous or maliciously constructed data. Consider passing `allow_pickle=False` to load data that is known not to contain object arrays for the safer handling of untrusted sources.

Parameters:

**file**file-like object, string, or pathlib.Path

The file to read. File-like objects must support the `seek()` and `read()` methods and must always be opened in binary mode. Pickled files require that the file-like object support the `readline()` method as well.

**mmap\_mode**{None, ‘r+’, ‘r’, ‘w+’, ‘c’}, optional

If not None, then memory-map the file, using the given mode (see [`numpy.memmap`](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html#numpy.memmap "numpy.memmap")
 for a detailed description of the modes). A memory-mapped array is kept on disk. However, it can be accessed and sliced like any ndarray. Memory mapping is especially useful for accessing small fragments of large files without reading the entire file into memory.

**allow\_pickle**bool, optional

Allow loading pickled object arrays stored in npy files. Reasons for disallowing pickles include security, as loading pickled data can execute arbitrary code. If pickles are disallowed, loading object arrays will fail. Default: False

**fix\_imports**bool, optional

Only useful when loading Python 2 generated pickled files, which includes npy/npz files containing object arrays. If _fix\_imports_ is True, pickle will try to map the old Python 2 names to the new names used in Python 3.

**encoding**str, optional

What encoding to use when reading Python 2 strings. Only useful when loading Python 2 generated pickled files, which includes npy/npz files containing object arrays. Values other than ‘latin1’, ‘ASCII’, and ‘bytes’ are not allowed, as they can corrupt numerical data. Default: ‘ASCII’

**max\_header\_size**int, optional

Maximum allowed size of the header. Large headers may not be safe to load securely and thus require explicitly passing a larger value. See [`ast.literal_eval`](https://docs.python.org/3/library/ast.html#ast.literal_eval "(in Python v3.14)")
 for details. This option is ignored when _allow\_pickle_ is passed. In that case the file is by definition trusted and the limit is unnecessary.

Returns:

**result**array, tuple, dict, etc.

Data stored in the file. For `.npz` files, the returned instance of NpzFile class must be closed to avoid leaking file descriptors.

Raises:

OSError

If the input file does not exist or cannot be read.

UnpicklingError

If `allow_pickle=True`, but the file cannot be loaded as a pickle.

ValueError

The file contains an object array, but `allow_pickle=False` given.

EOFError

When calling `np.load` multiple times on the same file handle, if all data has already been read

See also

[`save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html#numpy.save "numpy.save")
, [`savez`](https://numpy.org/doc/stable/reference/generated/numpy.savez.html#numpy.savez "numpy.savez")
, [`savez_compressed`](https://numpy.org/doc/stable/reference/generated/numpy.savez_compressed.html#numpy.savez_compressed "numpy.savez_compressed")
, [`loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt "numpy.loadtxt")

[`memmap`](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html#numpy.memmap "numpy.memmap")

Create a memory-map to an array stored in a file on disk.

[`lib.format.open_memmap`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.open_memmap.html#numpy.lib.format.open_memmap "numpy.lib.format.open_memmap")

Create or load a memory-mapped `.npy` file.

Notes

*   If the file contains pickle data, then whatever object is stored in the pickle is returned.
    
*   If the file is a `.npy` file, then a single array is returned.
    
*   If the file is a `.npz` file, then a dictionary-like object is returned, containing `{filename: array}` key-value pairs, one for each file in the archive.
    
*   If the file is a `.npz` file, the returned value supports the context manager protocol in a similar fashion to the open function:
    
    with load('foo.npz') as data:
        a \= data\['a'\]
    
    Copy to clipboard
    
    The underlying file descriptor is closed when exiting the ‘with’ block.
    

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Store data to disk, and load it again:

\>>> np.save('/tmp/123', np.array(\[\[1, 2, 3\], \[4, 5, 6\]\]))
\>>> np.load('/tmp/123.npy')
array(\[\[1, 2, 3\],\
       \[4, 5, 6\]\])

Copy to clipboard

Store compressed data to disk, and load it again:

\>>> a\=np.array(\[\[1, 2, 3\], \[4, 5, 6\]\])
\>>> b\=np.array(\[1, 2\])
\>>> np.savez('/tmp/123.npz', a\=a, b\=b)
\>>> data \= np.load('/tmp/123.npz')
\>>> data\['a'\]
array(\[\[1, 2, 3\],\
       \[4, 5, 6\]\])
\>>> data\['b'\]
array(\[1, 2\])
\>>> data.close()

Copy to clipboard

Mem-map the stored array, and then access the second row directly from disk:

\>>> X \= np.load('/tmp/123.npy', mmap\_mode\='r')
\>>> X\[1, :\]
memmap(\[4, 5, 6\])

Copy to clipboard

Go BackOpen In Tab

On this page