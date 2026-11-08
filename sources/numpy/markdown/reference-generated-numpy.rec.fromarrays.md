[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromarrays.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.rec.fromarrays.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromarrays.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.rec.fromarrays.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.rec.fromarrays.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.rec.fromarrays.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.rec.fromarrays.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.rec.fromarrays.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.rec.fromarrays.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.rec.fromarrays.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.rec.fromarrays.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.rec.fromarrays.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.rec.fromarrays.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.rec.fromarrays.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.rec.fromarrays.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.rec.fromarrays.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.rec.fromarrays.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.rec.fromarrays.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.rec.fromarrays.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.rec.fromarrays.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.rec.fromarrays.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.rec.fromarrays.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.rec.fromarrays[#](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromarrays.html#numpy-rec-fromarrays "Link to this heading")

================================================================================================================================================

rec.fromarrays(_arrayList_, _dtype\=None_, _shape\=None_, _formats\=None_, _names\=None_, _titles\=None_, _aligned\=False_, _byteorder\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/records.py#L569-L661)
[#](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromarrays.html#numpy.rec.fromarrays "Link to this definition")

Create a record array from a (flat) list of arrays

Parameters:

**arrayList**list or tuple

List of array-like objects (such as lists, tuples, and ndarrays).

**dtype**data-type, optional

valid dtype for all arrays

**shape**int or tuple of ints, optional

Shape of the resulting array. If not provided, inferred from `arrayList[0]`.

**formats, names, titles, aligned, byteorder**

If [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is `None`, these arguments are passed to [`numpy.rec.format_parser`](https://numpy.org/doc/stable/reference/generated/numpy.rec.format_parser.html#numpy.rec.format_parser "numpy.rec.format_parser")
 to construct a dtype. See that function for detailed documentation.

Returns:

np.recarray

Record array consisting of given arrayList columns.

Examples

Try it in your browser!

\>>> x1\=np.array(\[1,2,3,4\])
\>>> x2\=np.array(\['a','dd','xyz','12'\])
\>>> x3\=np.array(\[1.1,2,3,4\])
\>>> r \= np.rec.fromarrays(\[x1,x2,x3\],names\='a,b,c')
\>>> print(r\[1\])
(2, 'dd', 2.0) # may vary
\>>> x1\[1\]\=34
\>>> r.a
array(\[1, 2, 3, 4\])

Copy to clipboard

\>>> x1 \= np.array(\[1, 2, 3, 4\])
\>>> x2 \= np.array(\['a', 'dd', 'xyz', '12'\])
\>>> x3 \= np.array(\[1.1, 2, 3,4\])
\>>> r \= np.rec.fromarrays(
...     \[x1, x2, x3\],
...     dtype\=np.dtype(\[('a', np.int32), ('b', 'S3'), ('c', np.float32)\]))
\>>> r
rec.array(\[(1, b'a', 1.1), (2, b'dd', 2. ), (3, b'xyz', 3. ),\
           (4, b'12', 4. )\],
          dtype=\[('a', '<i4'), ('b', 'S3'), ('c', '<f4')\])

Copy to clipboard

Go BackOpen In Tab

On this page