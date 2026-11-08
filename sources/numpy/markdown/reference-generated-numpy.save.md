[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.save.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.save.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.save.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.save.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.save.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.save.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.save.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.save.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.save.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.save.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.save.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.save.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.save.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.save.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.save.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.save.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.save.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.save.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.save.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.save.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.save.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.save.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.save[#](https://numpy.org/doc/stable/reference/generated/numpy.save.html#numpy-save "Link to this heading")

==================================================================================================================

numpy.save(_file_, _arr_, _allow\_pickle\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_npyio_impl.py#L504-L572)
[#](https://numpy.org/doc/stable/reference/generated/numpy.save.html#numpy.save "Link to this definition")

Save an array to a binary file in NumPy `.npy` format.

Parameters:

**file**file, str, or pathlib.Path

File or filename to which the data is saved. If file is a file-object, then the filename is unchanged. If file is a string or Path, a `.npy` extension will be appended to the filename if it does not already have one.

**arr**array\_like

Array data to be saved.

**allow\_pickle**bool, optional

Allow saving object arrays using Python pickles. Reasons for disallowing pickles include security (loading pickled data can execute arbitrary code) and portability (pickled objects may not be loadable on different Python installations, for example if the stored objects require libraries that are not available, and not all pickled data is compatible between different versions of Python). Default: True

See also

[`savez`](https://numpy.org/doc/stable/reference/generated/numpy.savez.html#numpy.savez "numpy.savez")

Save several arrays into a `.npz` archive

[`savetxt`](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html#numpy.savetxt "numpy.savetxt")
, [`load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy.load "numpy.load")

Notes

For a description of the `.npy` format, see [`numpy.lib.format`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#module-numpy.lib.format "numpy.lib.format")
.

Any data saved to the file is appended to the end of the file.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> from tempfile import TemporaryFile
\>>> outfile \= TemporaryFile()

Copy to clipboard

\>>> x \= np.arange(10)
\>>> np.save(outfile, x)

Copy to clipboard

\>>> \_ \= outfile.seek(0) \# Only needed to simulate closing & reopening file
\>>> np.load(outfile)
array(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\])

Copy to clipboard

\>>> with open('test.npy', 'wb') as f:
...     np.save(f, np.array(\[1, 2\]))
...     np.save(f, np.array(\[1, 3\]))
\>>> with open('test.npy', 'rb') as f:
...     a \= np.load(f)
...     b \= np.load(f)
\>>> print(a, b)
\# \[1 2\] \[1 3\]

Copy to clipboard

Go BackOpen In Tab

On this page