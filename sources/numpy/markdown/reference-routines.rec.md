[Skip to main content](https://numpy.org/doc/stable/reference/routines.rec.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.rec.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.rec.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.rec.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.rec.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.rec.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.rec.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.rec.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.rec.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.rec.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.rec.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.rec.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.rec.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.rec.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.rec.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.rec.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.rec.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.rec.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.rec.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.rec.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.rec.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.rec.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Record Arrays ([`numpy.rec`](https://numpy.org/doc/stable/reference/routines.rec.html#module-numpy.rec "numpy.rec")
)[#](https://numpy.org/doc/stable/reference/routines.rec.html#module-numpy.rec "Link to this heading")

===========================================================================================================================================================================================================================

Record arrays expose the fields of structured arrays as properties.

Most commonly, ndarrays contain elements of a single type, e.g. floats, integers, bools etc. However, it is possible for elements to be combinations of these using structured types, such as:

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[(1, 2.0), (1, 2.0)\],
...     dtype\=\[('x', np.int64), ('y', np.float64)\])
\>>> a
array(\[(1, 2.), (1, 2.)\], dtype=\[('x', '<i8'), ('y', '<f8')\])

Copy to clipboard

Here, each element consists of two fields: x (and int), and y (a float). This is known as a structured array. The different fields are analogous to columns in a spread-sheet. The different fields can be accessed as one would a dictionary:

\>>> a\['x'\]
array(\[1, 1\])

Copy to clipboard

\>>> a\['y'\]
array(\[2., 2.\])

Copy to clipboard

Record arrays allow us to access fields as properties:

\>>> ar \= np.rec.array(a)
\>>> ar.x
array(\[1, 1\])
\>>> ar.y
array(\[2., 2.\])

Copy to clipboard

Go BackOpen In Tab

Functions[#](https://numpy.org/doc/stable/reference/routines.rec.html#functions "Link to this heading")

--------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`array`](https://numpy.org/doc/stable/reference/generated/numpy.rec.array.html#numpy.rec.array "numpy.rec.array")<br>(obj\[, dtype, shape, offset, strides, ...\]) | Construct a record array from a wide-variety of objects. |
| [`find_duplicate`](https://numpy.org/doc/stable/reference/generated/numpy.rec.find_duplicate.html#numpy.rec.find_duplicate "numpy.rec.find_duplicate")<br>(list) | Find duplication in a list, return a list of duplicated elements |
| [`format_parser`](https://numpy.org/doc/stable/reference/generated/numpy.rec.format_parser.html#numpy.rec.format_parser "numpy.rec.format_parser")<br>(formats, names, titles\[, ...\]) | Class to convert formats, names, titles description to a dtype. |
| [`fromarrays`](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromarrays.html#numpy.rec.fromarrays "numpy.rec.fromarrays")<br>(arrayList\[, dtype, shape, ...\]) | Create a record array from a (flat) list of arrays |
| [`fromfile`](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromfile.html#numpy.rec.fromfile "numpy.rec.fromfile")<br>(fd\[, dtype, shape, offset, ...\]) | Create an array from binary file data |
| [`fromrecords`](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromrecords.html#numpy.rec.fromrecords "numpy.rec.fromrecords")<br>(recList\[, dtype, shape, ...\]) | Create a recarray from a list of records in text form. |
| [`fromstring`](https://numpy.org/doc/stable/reference/generated/numpy.rec.fromstring.html#numpy.rec.fromstring "numpy.rec.fromstring")<br>(datastring\[, dtype, shape, ...\]) | Create a record array from binary data |

Also, the [`numpy.recarray`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html#numpy.recarray "numpy.recarray")
 class and the [`numpy.record`](https://numpy.org/doc/stable/reference/generated/numpy.record.html#numpy.record "numpy.record")
 scalar dtype are present in this namespace.

On this page