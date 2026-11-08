[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromrecords.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.rec.fromrecords.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromrecords.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.rec.fromrecords.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.rec.fromrecords.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.rec.fromrecords.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.rec.fromrecords.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.rec.fromrecords.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.rec.fromrecords.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.rec.fromrecords.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.rec.fromrecords.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.rec.fromrecords.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.rec.fromrecords.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.rec.fromrecords.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.rec.fromrecords.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.rec.fromrecords.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.rec.fromrecords.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.rec.fromrecords.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.rec.fromrecords.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.rec.fromrecords.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.rec.fromrecords.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.rec.fromrecords.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.rec.fromrecords[#](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromrecords.html#numpy-rec-fromrecords "Link to this heading")

===================================================================================================================================================

rec.fromrecords(_recList_, _dtype\=None_, _shape\=None_, _formats\=None_, _names\=None_, _titles\=None_, _aligned\=False_, _byteorder\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/records.py#L664-L750)
[#](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromrecords.html#numpy.rec.fromrecords "Link to this definition")

Create a recarray from a list of records in text form.

Parameters:

**recList**sequence

data in the same field may be heterogeneous - they will be promoted to the highest data type.

**dtype**data-type, optional

valid dtype for all arrays

**shape**int or tuple of ints, optional

shape of each array.

**formats, names, titles, aligned, byteorder**

If [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is `None`, these arguments are passed to _numpy.format\_parser_ to construct a dtype. See that function for detailed documentation.

If both _formats_ and [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 are None, then this will auto-detect formats. Use list of tuples rather than list of lists for faster processing.

Returns:

np.recarray

record array consisting of given recList rows.

Examples

Try it in your browser!

\>>> r\=np.rec.fromrecords(\[(456,'dbe',1.2),(2,'de',1.3)\],
... names\='col1,col2,col3')
\>>> print(r\[0\])
(456, 'dbe', 1.2)
\>>> r.col1
array(\[456,   2\])
\>>> r.col2
array(\['dbe', 'de'\], dtype='<U3')
\>>> import pickle
\>>> pickle.loads(pickle.dumps(r))
rec.array(\[(456, 'dbe', 1.2), (  2, 'de', 1.3)\],
          dtype=\[('col1', '<i8'), ('col2', '<U3'), ('col3', '<f8')\])

Copy to clipboard

Go BackOpen In Tab

On this page