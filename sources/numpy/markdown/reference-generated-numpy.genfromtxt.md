[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.genfromtxt.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.genfromtxt.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.genfromtxt.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.genfromtxt.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.genfromtxt.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.genfromtxt.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.genfromtxt.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.genfromtxt.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.genfromtxt.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.genfromtxt.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.genfromtxt.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.genfromtxt.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.genfromtxt.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.genfromtxt.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.genfromtxt.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.genfromtxt.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.genfromtxt.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.genfromtxt.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.genfromtxt.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.genfromtxt.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.genfromtxt[#](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html#numpy-genfromtxt "Link to this heading")

====================================================================================================================================

numpy.genfromtxt(_fname_, _dtype=<class 'float'>_, _comments='#'_, _delimiter=None_, _skip\_header=0_, _skip\_footer=0_, _converters=None_, _missing\_values=None_, _filling\_values=None_, _usecols=None_, _names=None_, _excludelist=None_, _deletechars=" !#$%&'()\*+_, _\-./:;<=>?@\[\\\\\]^{|}~"_, _replace\_space='\_'_, _autostrip=False_, _case\_sensitive=True_, _defaultfmt='f%i'_, _unpack=None_, _usemask=False_, _loose=True_, _invalid\_raise=True_, _max\_rows=None_, _encoding=None_, _\*_, _ndmin=0_, _like=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_npyio_impl.py#L1733-L2488)
[#](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "Link to this definition")

Load data from a text file, with missing values handled as specified.

Each line past the first _skip\_header_ lines is split at the _delimiter_ character, and characters following the _comments_ character are discarded.

Parameters:

**fname**file, str, pathlib.Path, list of str, generator

File, filename, list, or generator to read. If the filename extension is `.gz` or `.bz2`, the file is first decompressed. Note that generators must return bytes or strings. The strings in a list or produced by a generator are treated as lines.

**dtype**dtype, optional

Data type of the resulting array. If a structured dtype, the output array will be 1D and structured where each field corresponds to one column. If None, the dtype of each column will be inferred automatically, and the output array will be structured only if either the dtypes are not all the same or if _names_ is not None.

**comments**str, optional

The character used to indicate the start of a comment. All the characters occurring on a line after a comment are discarded.

**delimiter**str, int, or sequence, optional

The string used to separate values. By default, any consecutive whitespaces act as delimiter. An integer or sequence of integers can also be provided as width(s) of each field.

**skiprows**int, optional

_skiprows_ was removed in numpy 1.10. Please use _skip\_header_ instead.

**skip\_header**int, optional

The number of lines to skip at the beginning of the file.

**skip\_footer**int, optional

The number of lines to skip at the end of the file.

**converters**variable, optional

The set of functions that convert the data of a column to a value. The converters can also be used to provide a default value for missing data: `converters = {3: lambda s: float(s or 0)}`.

**missing**variable, optional

_missing_ was removed in numpy 1.10. Please use _missing\_values_ instead.

**missing\_values**variable, optional

The set of strings corresponding to missing data.

**filling\_values**variable, optional

The set of values to be used as default when the data are missing.

**usecols**sequence, optional

Which columns to read, with 0 being the first. For example, `usecols = (1, 4, 5)` will extract the 2nd, 5th and 6th columns.

**names**{None, True, str, sequence}, optional

If _names_ is True, the output will be a structured array whose field names are read from the first line after the first _skip\_header_ lines. This line can optionally be preceded by a comment delimiter. Any content before the comment delimiter is discarded. If _names_ is a sequence or a single string of comma-separated names, the output is a structured array whose field names are taken from _names_. If _names_ is None, the output is structured only if [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is structured, in which case the field names are taken from [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
.

**excludelist**sequence, optional

A list of names to exclude. This list is appended to the default list \[‘return’,’file’,’print’\]. Excluded names are appended with an underscore: for example, _file_ would become _file\__.

**deletechars**str, optional

A string combining invalid characters that must be deleted from the names.

**defaultfmt**str, optional

A format used to define default field names, such as “f%i” or “f\_%02i”.

**autostrip**bool, optional

Whether to automatically strip white spaces from the variables.

**replace\_space**char, optional

Character(s) used in replacement of white spaces in the variable names. By default, use a ‘\_’.

**case\_sensitive**{True, False, ‘upper’, ‘lower’}, optional

If True, field names are case sensitive. If False or ‘upper’, field names are converted to upper case. If ‘lower’, field names are converted to lower case.

**unpack**bool, optional

If True, the returned array is transposed, so that arguments may be unpacked using `x, y, z = genfromtxt(...)`. When used with a structured data-type, arrays are returned for each field. Default is False.

**usemask**bool, optional

If True, return a masked array. If False, return a regular array.

**loose**bool, optional

If True, do not raise errors for invalid values.

**invalid\_raise**bool, optional

If True, an exception is raised if an inconsistency is detected in the number of columns. If False, a warning is emitted and the offending lines are skipped.

**max\_rows**int, optional

The maximum number of rows to read. Must not be used with skip\_footer at the same time. If given, the value must be at least 1. Default is to read the entire file.

**encoding**str, optional

Encoding used to decode the inputfile. Does not apply when _fname_ is a file object. The special value ‘bytes’ enables backward compatibility workarounds that ensure that you receive byte arrays when possible and passes latin1 encoded strings to converters. Override this value to receive unicode arrays and pass strings as input to converters. If set to None the system default is used. The default value is ‘bytes’.

Changed in version 2.0: Before NumPy 2, the default was `'bytes'` for Python 2 compatibility. The default is now `None`.

**ndmin**int, optional

Same parameter as [`loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt "numpy.loadtxt")

New in version 1.23.0.

**like**array\_like, optional

Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as `like` supports the `__array_function__` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

Returns:

**out**ndarray

Data read from the text file. If _usemask_ is True, this is a masked array.

See also

[`numpy.loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt "numpy.loadtxt")

equivalent function when no data is missing.

Notes

*   When spaces are used as delimiters, or when no delimiter has been given as input, there should not be any missing data between two fields.
    
*   When variables are named (either by a flexible dtype or with a _names_ sequence), there must not be any header in the file (else a ValueError exception is raised).
    
*   Individual values are not stripped of spaces by default. When using a custom converter, make sure the function does remove spaces.
    
*   Custom converters may receive unexpected values due to dtype discovery.
    

References

\[1\]

NumPy User Guide, section [I/O with NumPy](https://docs.scipy.org/doc/numpy/user/basics.io.genfromtxt.html)
.

Examples

Try it in your browser!

\>>> from io import StringIO
\>>> import numpy as np

Copy to clipboard

Comma delimited file with mixed dtype

\>>> s \= StringIO("1,1.3,abcde")
\>>> data \= np.genfromtxt(s, dtype\=\[('myint','i8'),('myfloat','f8'),\
... ('mystring','S5')\], delimiter\=",")
\>>> data
array((1, 1.3, b'abcde'),
      dtype=\[('myint', '<i8'), ('myfloat', '<f8'), ('mystring', 'S5')\])

Copy to clipboard

Using dtype = None

\>>> \_ \= s.seek(0) \# needed for StringIO example only
\>>> data \= np.genfromtxt(s, dtype\=None,
... names \= \['myint','myfloat','mystring'\], delimiter\=",")
\>>> data
array((1, 1.3, 'abcde'),
      dtype=\[('myint', '<i8'), ('myfloat', '<f8'), ('mystring', '<U5')\])

Copy to clipboard

Specifying dtype and names

\>>> \_ \= s.seek(0)
\>>> data \= np.genfromtxt(s, dtype\="i8,f8,S5",
... names\=\['myint','myfloat','mystring'\], delimiter\=",")
\>>> data
array((1, 1.3, b'abcde'),
      dtype=\[('myint', '<i8'), ('myfloat', '<f8'), ('mystring', 'S5')\])

Copy to clipboard

An example with fixed-width columns

\>>> s \= StringIO("11.3abcde")
\>>> data \= np.genfromtxt(s, dtype\=None, names\=\['intvar','fltvar','strvar'\],
...     delimiter\=\[1,3,5\])
\>>> data
array((1, 1.3, 'abcde'),
      dtype=\[('intvar', '<i8'), ('fltvar', '<f8'), ('strvar', '<U5')\])

Copy to clipboard

An example to show comments

\>>> f \= StringIO('''
... text,# of chars
... hello world,11
... numpy,5''')
\>>> np.genfromtxt(f, dtype\='S12,S12', delimiter\=',')
array(\[(b'text', b''), (b'hello world', b'11'), (b'numpy', b'5')\],
  dtype=\[('f0', 'S12'), ('f1', 'S12')\])

Copy to clipboard

Go BackOpen In Tab

On this page