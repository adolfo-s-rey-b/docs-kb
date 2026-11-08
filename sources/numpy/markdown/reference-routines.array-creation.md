[Skip to main content](https://numpy.org/doc/stable/reference/routines.array-creation.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.array-creation.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.array-creation.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.array-creation.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.array-creation.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.array-creation.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.array-creation.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.array-creation.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.array-creation.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.array-creation.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.array-creation.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.array-creation.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.array-creation.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.array-creation.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.array-creation.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.array-creation.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.array-creation.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.array-creation.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.array-creation.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.array-creation.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.array-creation.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.array-creation.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Array creation routines[#](https://numpy.org/doc/stable/reference/routines.array-creation.html#array-creation-routines "Link to this heading")

===============================================================================================================================================

See also

[Array creation](https://numpy.org/doc/stable/user/basics.creation.html#arrays-creation)

From shape or value[#](https://numpy.org/doc/stable/reference/routines.array-creation.html#from-shape-or-value "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`empty`](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")<br>(shape\[, dtype, order, device, like\]) | Return a new array of given shape and type, without initializing entries. |
| [`empty_like`](https://numpy.org/doc/stable/reference/generated/numpy.empty_like.html#numpy.empty_like "numpy.empty_like")<br>(prototype, /\[, dtype, order, ...\]) | Return a new array with the same shape and type as a given array. |
| [`eye`](https://numpy.org/doc/stable/reference/generated/numpy.eye.html#numpy.eye "numpy.eye")<br>(N\[, M, k, dtype, order, device, like\]) | Return a 2-D array with ones on the diagonal and zeros elsewhere. |
| [`identity`](https://numpy.org/doc/stable/reference/generated/numpy.identity.html#numpy.identity "numpy.identity")<br>(n\[, dtype, like\]) | Return the identity array. |
| [`ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")<br>(shape\[, dtype, order, device, like\]) | Return a new array of given shape and type, filled with ones. |
| [`ones_like`](https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html#numpy.ones_like "numpy.ones_like")<br>(a\[, dtype, order, subok, shape, ...\]) | Return an array of ones with the same shape and type as a given array. |
| [`zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")<br>(shape\[, dtype, order, device, like\]) | Return a new array of given shape and type, filled with zeros. |
| [`zeros_like`](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")<br>(a\[, dtype, order, subok, shape, ...\]) | Return an array of zeros with the same shape and type as a given array. |
| [`full`](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")<br>(shape, fill\_value\[, dtype, order, ...\]) | Return a new array of given shape and type, filled with _fill\_value_. |
| [`full_like`](https://numpy.org/doc/stable/reference/generated/numpy.full_like.html#numpy.full_like "numpy.full_like")<br>(a, fill\_value\[, dtype, order, ...\]) | Return a full array with the same shape and type as a given array. |

From existing data[#](https://numpy.org/doc/stable/reference/routines.array-creation.html#from-existing-data "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")<br>(object\[, dtype, copy, order, subok, ...\]) | Create an array. |
| [`asarray`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")<br>(a\[, dtype, order, device, copy, like\]) | Convert the input to an array. |
| [`asanyarray`](https://numpy.org/doc/stable/reference/generated/numpy.asanyarray.html#numpy.asanyarray "numpy.asanyarray")<br>(a\[, dtype, order, device, copy, like\]) | Convert the input to an ndarray, but pass ndarray subclasses through. |
| [`ascontiguousarray`](https://numpy.org/doc/stable/reference/generated/numpy.ascontiguousarray.html#numpy.ascontiguousarray "numpy.ascontiguousarray")<br>(a\[, dtype, like\]) | Return a contiguous array (ndim >= 1) in memory (C order). |
| [`asmatrix`](https://numpy.org/doc/stable/reference/generated/numpy.asmatrix.html#numpy.asmatrix "numpy.asmatrix")<br>(data\[, dtype\]) | Interpret the input as a matrix. |
| [`astype`](https://numpy.org/doc/stable/reference/generated/numpy.astype.html#numpy.astype "numpy.astype")<br>(x, dtype, /, \*\[, copy, device\]) | Copies an array to a specified data type. |
| [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "numpy.copy")<br>(a\[, order, subok\]) | Return an array copy of the given object. |
| [`frombuffer`](https://numpy.org/doc/stable/reference/generated/numpy.frombuffer.html#numpy.frombuffer "numpy.frombuffer")<br>(buffer\[, dtype, count, offset, like\]) | Interpret a buffer as a 1-dimensional array. |
| [`from_dlpack`](https://numpy.org/doc/stable/reference/generated/numpy.from_dlpack.html#numpy.from_dlpack "numpy.from_dlpack")<br>(x, /, \*\[, device, copy\]) | Create a NumPy array from an object implementing the `__dlpack__` protocol. |
| [`fromfile`](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#numpy.fromfile "numpy.fromfile")<br>(file\[, dtype, count, sep, offset, like\]) | Construct an array from data in a text or binary file. |
| [`fromfunction`](https://numpy.org/doc/stable/reference/generated/numpy.fromfunction.html#numpy.fromfunction "numpy.fromfunction")<br>(function, shape, \*\[, dtype, like\]) | Construct an array by executing a function over each coordinate. |
| [`fromiter`](https://numpy.org/doc/stable/reference/generated/numpy.fromiter.html#numpy.fromiter "numpy.fromiter")<br>(iter, dtype\[, count, like\]) | Create a new 1-dimensional array from an iterable object. |
| [`fromstring`](https://numpy.org/doc/stable/reference/generated/numpy.fromstring.html#numpy.fromstring "numpy.fromstring")<br>(string\[, dtype, count, like\]) | A new 1-D array initialized from text data in a string. |
| [`loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt "numpy.loadtxt")<br>(fname\[, dtype, comments, delimiter, ...\]) | Load data from a text file. |

Creating record arrays[#](https://numpy.org/doc/stable/reference/routines.array-creation.html#creating-record-arrays "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

Note

Please refer to [Record arrays](https://numpy.org/doc/stable/reference/arrays.classes.html#arrays-classes-rec)
 for record arrays.

|     |     |
| --- | --- |
| [`rec.array`](https://numpy.org/doc/stable/reference/generated/numpy.rec.array.html#numpy.rec.array "numpy.rec.array")<br>(obj\[, dtype, shape, offset, ...\]) | Construct a record array from a wide-variety of objects. |
| [`rec.fromarrays`](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromarrays.html#numpy.rec.fromarrays "numpy.rec.fromarrays")<br>(arrayList\[, dtype, shape, ...\]) | Create a record array from a (flat) list of arrays |
| [`rec.fromrecords`](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromrecords.html#numpy.rec.fromrecords "numpy.rec.fromrecords")<br>(recList\[, dtype, shape, ...\]) | Create a recarray from a list of records in text form. |
| [`rec.fromstring`](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromstring.html#numpy.rec.fromstring "numpy.rec.fromstring")<br>(datastring\[, dtype, shape, ...\]) | Create a record array from binary data |
| [`rec.fromfile`](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromfile.html#numpy.rec.fromfile "numpy.rec.fromfile")<br>(fd\[, dtype, shape, offset, ...\]) | Create an array from binary file data |

Creating character arrays ([`numpy.char`](https://numpy.org/doc/stable/reference/routines.char.html#module-numpy.char "numpy.char")
)[#](https://numpy.org/doc/stable/reference/routines.array-creation.html#creating-character-arrays-numpy-char "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note

[`numpy.char`](https://numpy.org/doc/stable/reference/routines.char.html#module-numpy.char "numpy.char")
 is used to create character arrays.

|     |     |
| --- | --- |
| [`char.array`](https://numpy.org/doc/stable/reference/generated/numpy.char.array.html#numpy.char.array "numpy.char.array")<br>(obj\[, itemsize, copy, unicode, order\]) | Create a [`chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")<br>. |
| [`char.asarray`](https://numpy.org/doc/stable/reference/generated/numpy.char.asarray.html#numpy.char.asarray "numpy.char.asarray")<br>(obj\[, itemsize, unicode, order\]) | Convert the input to a [`chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")<br>, copying the data only if necessary. |

Numerical ranges[#](https://numpy.org/doc/stable/reference/routines.array-creation.html#numerical-ranges "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")<br>(\[start,\] stop\[, step,\]\[, dtype, ...\]) | Return evenly spaced values within a given interval. |
| [`linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")<br>(start, stop\[, num, endpoint, ...\]) | Return evenly spaced numbers over a specified interval. |
| [`logspace`](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")<br>(start, stop\[, num, endpoint, base, ...\]) | Return numbers spaced evenly on a log scale. |
| [`geomspace`](https://numpy.org/doc/stable/reference/generated/numpy.geomspace.html#numpy.geomspace "numpy.geomspace")<br>(start, stop\[, num, endpoint, ...\]) | Return numbers spaced evenly on a log scale (a geometric progression). |
| [`meshgrid`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")<br>(\*xi\[, copy, sparse, indexing\]) | Return a tuple of coordinate matrices from coordinate vectors. |
| [`mgrid`](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid") | An instance which returns a dense multi-dimensional "meshgrid". |
| [`ogrid`](https://numpy.org/doc/stable/reference/generated/numpy.ogrid.html#numpy.ogrid "numpy.ogrid") | An instance which returns an open multi-dimensional "meshgrid". |

Building matrices[#](https://numpy.org/doc/stable/reference/routines.array-creation.html#building-matrices "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`diag`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")<br>(v\[, k\]) | Extract a diagonal or construct a diagonal array. |
| [`diagflat`](https://numpy.org/doc/stable/reference/generated/numpy.diagflat.html#numpy.diagflat "numpy.diagflat")<br>(v\[, k\]) | Create a two-dimensional array with the flattened input as a diagonal. |
| [`tri`](https://numpy.org/doc/stable/reference/generated/numpy.tri.html#numpy.tri "numpy.tri")<br>(N\[, M, k, dtype, like\]) | An array with ones at and below the given diagonal and zeros elsewhere. |
| [`tril`](https://numpy.org/doc/stable/reference/generated/numpy.tril.html#numpy.tril "numpy.tril")<br>(m\[, k\]) | Lower triangle of an array. |
| [`triu`](https://numpy.org/doc/stable/reference/generated/numpy.triu.html#numpy.triu "numpy.triu")<br>(m\[, k\]) | Upper triangle of an array. |
| [`vander`](https://numpy.org/doc/stable/reference/generated/numpy.vander.html#numpy.vander "numpy.vander")<br>(x\[, N, increasing\]) | Generate a Vandermonde matrix. |

The matrix class[#](https://numpy.org/doc/stable/reference/routines.array-creation.html#the-matrix-class "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`bmat`](https://numpy.org/doc/stable/reference/generated/numpy.bmat.html#numpy.bmat "numpy.bmat")<br>(obj\[, ldict, gdict\]) | Build a matrix object from a string, nested sequence, or array. |

On this page