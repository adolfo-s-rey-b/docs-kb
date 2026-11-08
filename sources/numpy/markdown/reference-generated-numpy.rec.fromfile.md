[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromfile.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.rec.fromfile[#](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromfile.html#numpy-rec-fromfile "Link to this heading")

==========================================================================================================================================

rec.fromfile(_fd_, _dtype\=None_, _shape\=None_, _offset\=0_, _formats\=None_, _names\=None_, _titles\=None_, _aligned\=False_, _byteorder\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/records.py#L837-L939)
[#](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromfile.html#numpy.rec.fromfile "Link to this definition")

Create an array from binary file data

Parameters:

**fd**str or file type

If file is a string or a path-like object then that file is opened, else it is assumed to be a file object. The file object must support random access (i.e. it must have tell and seek methods).

**dtype**data-type, optional

valid dtype for all arrays

**shape**int or tuple of ints, optional

shape of each array.

**offset**int, optional

Position in the file to start reading from.

**formats, names, titles, aligned, byteorder**

If [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is `None`, these arguments are passed to _numpy.format\_parser_ to construct a dtype. See that function for detailed documentation

Returns:

np.recarray

record array consisting of data enclosed in file.

Examples

Try it in your browser!

\>>> from tempfile import TemporaryFile
\>>> a \= np.empty(10,dtype\='f8,i4,S5')
\>>> a\[5\] \= (0.5,10,'abcde')
\>>>
\>>> fd\=TemporaryFile()
\>>> a \= a.view(a.dtype.newbyteorder('<'))
\>>> a.tofile(fd)
\>>>
\>>> \_ \= fd.seek(0)
\>>> r\=np.rec.fromfile(fd, formats\='f8,i4,S5', shape\=10,
... byteorder\='<')
\>>> print(r\[5\])
(0.5, 10, b'abcde')
\>>> r.shape
(10,)

Copy to clipboard

Go BackOpen In Tab

On this page