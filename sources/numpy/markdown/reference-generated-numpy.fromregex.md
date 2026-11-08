[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fromregex.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fromregex.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fromregex.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fromregex.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fromregex.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fromregex.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fromregex.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fromregex.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fromregex.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fromregex.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fromregex.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fromregex.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fromregex.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fromregex.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fromregex.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fromregex.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fromregex.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fromregex.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fromregex.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fromregex.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fromregex.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fromregex.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fromregex[#](https://numpy.org/doc/stable/reference/generated/numpy.fromregex.html#numpy-fromregex "Link to this heading")

=================================================================================================================================

numpy.fromregex(_file_, _regexp_, _dtype_, _encoding\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_npyio_impl.py#L1631-L1725)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fromregex.html#numpy.fromregex "Link to this definition")

Construct an array from a text file, using regular expression parsing.

The returned array is always a structured array, and is constructed from all matches of the regular expression in the file. Groups in the regular expression are converted to fields of the structured array.

Parameters:

**file**file, str, or pathlib.Path

Filename or file object to read.

Changed in version 1.22.0: Now accepts [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")
 implementations.

**regexp**str or regexp

Regular expression used to parse the file. Groups in the regular expression correspond to fields in the dtype.

**dtype**dtype or list of dtypes

Dtype for the structured array; must be a structured datatype.

**encoding**str, optional

Encoding used to decode the inputfile. Does not apply to input streams.

Returns:

**output**ndarray

The output array, containing the part of the content of _file_ that was matched by _regexp_. _output_ is always a structured array.

Raises:

TypeError

When [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is not a valid dtype for a structured array.

See also

[`fromstring`](https://numpy.org/doc/stable/reference/generated/numpy.fromstring.html#numpy.fromstring "numpy.fromstring")
, [`loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt "numpy.loadtxt")

Notes

Dtypes for structured arrays can be specified in several forms, but all forms specify at least the data type and field name. For details see _basics.rec_.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from io import StringIO
\>>> text \= StringIO("1312 foo\\n1534  bar\\n444   qux")

Copy to clipboard

\>>> regexp \= r"(\\d+)\\s+(...)"  \# match \[digits, whitespace, anything\]
\>>> output \= np.fromregex(text, regexp,
...                       \[('num', np.int64), ('key', 'S3')\])
\>>> output
array(\[(1312, b'foo'), (1534, b'bar'), ( 444, b'qux')\],
      dtype=\[('num', '<i8'), ('key', 'S3')\])
\>>> output\['num'\]
array(\[1312, 1534,  444\])

Copy to clipboard

Go BackOpen In Tab

On this page