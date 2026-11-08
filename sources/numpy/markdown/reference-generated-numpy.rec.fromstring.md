[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromstring.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.rec.fromstring.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromstring.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.rec.fromstring.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.rec.fromstring.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.rec.fromstring.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.rec.fromstring.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.rec.fromstring.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.rec.fromstring.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.rec.fromstring.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.rec.fromstring.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.rec.fromstring.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.rec.fromstring.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.rec.fromstring.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.rec.fromstring.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.rec.fromstring.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.rec.fromstring.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.rec.fromstring.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.rec.fromstring.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.rec.fromstring.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.rec.fromstring.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.rec.fromstring.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.rec.fromstring[#](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromstring.html#numpy-rec-fromstring "Link to this heading")

================================================================================================================================================

rec.fromstring(_datastring_, _dtype\=None_, _shape\=None_, _offset\=0_, _formats\=None_, _names\=None_, _titles\=None_, _aligned\=False_, _byteorder\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/records.py#L753-L826)
[#](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromstring.html#numpy.rec.fromstring "Link to this definition")

Create a record array from binary data

Note that despite the name of this function it does not accept _str_ instances.

Parameters:

**datastring**bytes-like

Buffer of binary data

**dtype**data-type, optional

Valid dtype for all arrays

**shape**int or tuple of ints, optional

Shape of each array.

**offset**int, optional

Position in the buffer to start reading from.

**formats, names, titles, aligned, byteorder**

If [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is `None`, these arguments are passed to _numpy.format\_parser_ to construct a dtype. See that function for detailed documentation.

Returns:

np.recarray

Record array view into the data in datastring. This will be readonly if _datastring_ is readonly.

See also

[`numpy.frombuffer`](https://numpy.org/doc/stable/reference/generated/numpy.frombuffer.html#numpy.frombuffer "numpy.frombuffer")

Examples

Try it in your browser!

\>>> a \= b'\\x01\\x02\\x03abc'
\>>> np.rec.fromstring(a, dtype\='u1,u1,u1,S3')
rec.array(\[(1, 2, 3, b'abc')\],
        dtype=\[('f0', 'u1'), ('f1', 'u1'), ('f2', 'u1'), ('f3', 'S3')\])

Copy to clipboard

\>>> grades\_dtype \= \[('Name', (np.str\_, 10)), ('Marks', np.float64),\
...                 ('GradeLevel', np.int32)\]
\>>> grades\_array \= np.array(\[('Sam', 33.3, 3), ('Mike', 44.4, 5),\
...                         ('Aadi', 66.6, 6)\], dtype\=grades\_dtype)
\>>> np.rec.fromstring(grades\_array.tobytes(), dtype\=grades\_dtype)
rec.array(\[('Sam', 33.3, 3), ('Mike', 44.4, 5), ('Aadi', 66.6, 6)\],
        dtype=\[('Name', '<U10'), ('Marks', '<f8'), ('GradeLevel', '<i4')\])

Copy to clipboard

\>>> s \= '\\x01\\x02\\x03abc'
\>>> np.rec.fromstring(s, dtype\='u1,u1,u1,S3')
Traceback (most recent call last):
   ...
TypeError: a bytes-like object is required, not 'str'

Copy to clipboard

Go BackOpen In Tab

On this page