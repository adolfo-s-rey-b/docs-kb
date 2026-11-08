[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.rec.format_parser.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.rec.format_parser.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.rec.format_parser.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.rec.format_parser.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.rec.format_parser.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.rec.format_parser.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.rec.format_parser.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.rec.format_parser.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.rec.format_parser.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.rec.format_parser.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.rec.format_parser.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.rec.format_parser.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.rec.format_parser.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.rec.format_parser.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.rec.format_parser.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.rec.format_parser.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.rec.format_parser.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.rec.format_parser.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.rec.format_parser.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.rec.format_parser.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.rec.format_parser.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.rec.format_parser.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.rec.format\_parser[#](https://numpy.org/doc/stable/reference/generated/numpy.rec.format_parser.html#numpy-rec-format-parser "Link to this heading")

==========================================================================================================================================================

_class_ numpy.rec.format\_parser(_formats_, _names_, _titles_, _aligned\=False_, _byteorder\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/records.py#L56-L193)
[#](https://numpy.org/doc/stable/reference/generated/numpy.rec.format_parser.html#numpy.rec.format_parser "Link to this definition")

Class to convert formats, names, titles description to a dtype.

After constructing the format\_parser object, the dtype attribute is the converted data-type: `dtype = format_parser(formats, names, titles).dtype`

Parameters:

**formats**str or list of str

The format description, either specified as a string with comma-separated format descriptions in the form `'f8, i4, S5'`, or a list of format description strings in the form `['f8', 'i4', 'S5']`.

**names**str or list/tuple of str

The field names, either specified as a comma-separated string in the form `'col1, col2, col3'`, or as a list or tuple of strings in the form `['col1', 'col2', 'col3']`. An empty list can be used, in that case default field names (‘f0’, ‘f1’, …) are used.

**titles**sequence

Sequence of title strings. An empty list can be used to leave titles out.

**aligned**bool, optional

If True, align the fields by padding as the C-compiler would. Default is False.

**byteorder**str, optional

If specified, all the fields will be changed to the provided byte-order. Otherwise, the default byte-order is used. For all available string specifiers, see _dtype.newbyteorder_.

Attributes:

**dtype**dtype

The converted data-type.

See also

[`numpy.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
, [`numpy.typename`](https://numpy.org/doc/stable/reference/generated/numpy.typename.html#numpy.typename "numpy.typename")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.rec.format\_parser(\['<f8', '<i4'\], \['col1', 'col2'\],
...                      \['T1', 'T2'\]).dtype
dtype(\[(('T1', 'col1'), '<f8'), (('T2', 'col2'), '<i4')\])

Copy to clipboard

_names_ and/or _titles_ can be empty lists. If _titles_ is an empty list, titles will simply not appear. If _names_ is empty, default field names will be used.

\>>> np.rec.format\_parser(\['f8', 'i4', 'S5'\], \['col1', 'col2', 'col3'\],
...                      \[\]).dtype
dtype(\[('col1', '<f8'), ('col2', '<i4'), ('col3', '<S5')\])
\>>> np.rec.format\_parser(\['<f8', '<i4', '<S5'\], \[\], \[\]).dtype
dtype(\[('f0', '<f8'), ('f1', '<i4'), ('f2', 'S5')\])

Copy to clipboard

Go BackOpen In Tab

On this page