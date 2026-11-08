[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.loadtxt.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.loadtxt.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.loadtxt.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.loadtxt.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.loadtxt.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.loadtxt.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.loadtxt.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.loadtxt.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.loadtxt.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.loadtxt.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.loadtxt.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.loadtxt.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.loadtxt.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.loadtxt.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.loadtxt.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.loadtxt.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.loadtxt.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.loadtxt.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.loadtxt.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.loadtxt.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.loadtxt[#](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy-loadtxt "Link to this heading")

===========================================================================================================================

numpy.loadtxt(_fname_, _dtype=<class 'float'>_, _comments='#'_, _delimiter=None_, _converters=None_, _skiprows=0_, _usecols=None_, _unpack=False_, _ndmin=0_, _encoding=None_, _max\_rows=None_, _\*_, _quotechar=None_, _like=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_npyio_impl.py#L1118-L1386)
[#](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt "Link to this definition")

Load data from a text file.

Parameters:

**fname**file, str, pathlib.Path, list of str, generator

File, filename, list, or generator to read. If the filename extension is `.gz` or `.bz2`, the file is first decompressed. Note that generators must return bytes or strings. The strings in a list or produced by a generator are treated as lines.

**dtype**data-type, optional

Data-type of the resulting array; default: float. If this is a structured data-type, the resulting array will be 1-dimensional, and each row will be interpreted as an element of the array. In this case, the number of columns used must match the number of fields in the data-type.

**comments**str or sequence of str or None, optional

The characters or list of characters used to indicate the start of a comment. None implies no comments. For backwards compatibility, byte strings will be decoded as ‘latin1’. The default is ‘#’.

**delimiter**str, optional

The character used to separate the values. For backwards compatibility, byte strings will be decoded as ‘latin1’. The default is whitespace.

Changed in version 1.23.0: Only single character delimiters are supported. Newline characters cannot be used as the delimiter.

**converters**dict or callable, optional

Converter functions to customize value parsing. If _converters_ is callable, the function is applied to all columns, else it must be a dict that maps column number to a parser function. See examples for further details. Default: None.

Changed in version 1.23.0: The ability to pass a single callable to be applied to all columns was added.

**skiprows**int, optional

Skip the first _skiprows_ lines, including comments; default: 0.

**usecols**int or sequence, optional

Which columns to read, with 0 being the first. For example, `usecols = (1,4,5)` will extract the 2nd, 5th and 6th columns. The default, None, results in all columns being read.

**unpack**bool, optional

If True, the returned array is transposed, so that arguments may be unpacked using `x, y, z = loadtxt(...)`. When used with a structured data-type, arrays are returned for each field. Default is False.

**ndmin**int, optional

The returned array will have at least _ndmin_ dimensions. Otherwise mono-dimensional axes will be squeezed. Legal values: 0 (default), 1 or 2.

**encoding**str, optional

Encoding used to decode the inputfile. Does not apply to input streams. The special value ‘bytes’ enables backward compatibility workarounds that ensures you receive byte arrays as results if possible and passes ‘latin1’ encoded strings to converters. Override this value to receive unicode arrays and pass strings as input to converters. If set to None the system default is used. The default value is None.

Changed in version 2.0: Before NumPy 2, the default was `'bytes'` for Python 2 compatibility. The default is now `None`.

**max\_rows**int, optional

Read _max\_rows_ rows of content after _skiprows_ lines. The default is to read all the rows. Note that empty rows containing no data such as empty lines and comment lines are not counted towards _max\_rows_, while such lines are counted in _skiprows_.

Changed in version 1.23.0: Lines containing no data, including comment lines (e.g., lines starting with ‘#’ or as specified via _comments_) are not counted towards _max\_rows_.

**quotechar**unicode character or None, optional

The character used to denote the start and end of a quoted item. Occurrences of the delimiter or comment characters are ignored within a quoted item. The default value is `quotechar=None`, which means quoting support is disabled.

If two consecutive instances of _quotechar_ are found within a quoted field, the first is treated as an escape character. See examples.

New in version 1.23.0.

**like**array\_like, optional

Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as `like` supports the `__array_function__` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

Returns:

**out**ndarray

Data read from the text file.

See also

[`load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy.load "numpy.load")
, [`fromstring`](https://numpy.org/doc/stable/reference/generated/numpy.fromstring.html#numpy.fromstring "numpy.fromstring")
, [`fromregex`](https://numpy.org/doc/stable/reference/generated/numpy.fromregex.html#numpy.fromregex "numpy.fromregex")

[`genfromtxt`](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt")

Load data with missing values handled as specified.

[`scipy.io.loadmat`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.loadmat.html#scipy.io.loadmat "(in SciPy v1.18.0)")

reads MATLAB data files

Notes

This function aims to be a fast reader for simply formatted files. The [`genfromtxt`](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt")
 function provides more sophisticated handling of, e.g., lines with missing values.

Each row in the input text file must have the same number of values to be able to read all values. If all rows do not have same number of values, a subset of up to n columns (where n is the least number of values present in all rows) can be read by specifying the columns via _usecols_.

The strings produced by the Python float.hex method can be used as input for floats.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from io import StringIO   \# StringIO behaves like a file object
\>>> c \= StringIO("0 1\\n2 3")
\>>> np.loadtxt(c)
array(\[\[0., 1.\],\
       \[2., 3.\]\])

Copy to clipboard

\>>> d \= StringIO("M 21 72\\nF 35 58")
\>>> np.loadtxt(d, dtype\={'names': ('gender', 'age', 'weight'),
...                      'formats': ('S1', 'i4', 'f4')})
array(\[(b'M', 21, 72.), (b'F', 35, 58.)\],
      dtype=\[('gender', 'S1'), ('age', '<i4'), ('weight', '<f4')\])

Copy to clipboard

\>>> c \= StringIO("1,0,2\\n3,0,4")
\>>> x, y \= np.loadtxt(c, delimiter\=',', usecols\=(0, 2), unpack\=True)
\>>> x
array(\[1., 3.\])
\>>> y
array(\[2., 4.\])

Copy to clipboard

The _converters_ argument is used to specify functions to preprocess the text prior to parsing. _converters_ can be a dictionary that maps preprocessing functions to each column:

\>>> s \= StringIO("1.618, 2.296\\n3.141, 4.669\\n")
\>>> conv \= {
...     0: lambda x: np.floor(float(x)),  \# conversion fn for column 0
...     1: lambda x: np.ceil(float(x)),  \# conversion fn for column 1
... }
\>>> np.loadtxt(s, delimiter\=",", converters\=conv)
array(\[\[1., 3.\],\
       \[3., 5.\]\])

Copy to clipboard

_converters_ can be a callable instead of a dictionary, in which case it is applied to all columns:

\>>> s \= StringIO("0xDE 0xAD\\n0xC0 0xDE")
\>>> import functools
\>>> conv \= functools.partial(int, base\=16)
\>>> np.loadtxt(s, converters\=conv)
array(\[\[222., 173.\],\
       \[192., 222.\]\])

Copy to clipboard

This example shows how _converters_ can be used to convert a field with a trailing minus sign into a negative number.

\>>> s \= StringIO("10.01 31.25-\\n19.22 64.31\\n17.57- 63.94")
\>>> def conv(fld):
...     return \-float(fld\[:\-1\]) if fld.endswith("-") else float(fld)
...
\>>> np.loadtxt(s, converters\=conv)
array(\[\[ 10.01, -31.25\],\
       \[ 19.22,  64.31\],\
       \[-17.57,  63.94\]\])

Copy to clipboard

Using a callable as the converter can be particularly useful for handling values with different formatting, e.g. floats with underscores:

\>>> s \= StringIO("1 2.7 100\_000")
\>>> np.loadtxt(s, converters\=float)
array(\[1.e+00, 2.7e+00, 1.e+05\])

Copy to clipboard

This idea can be extended to automatically handle values specified in many different formats, such as hex values:

\>>> def conv(val):
...     try:
...         return float(val)
...     except ValueError:
...         return float.fromhex(val)
\>>> s \= StringIO("1, 2.5, 3\_000, 0b4, 0x1.4000000000000p+2")
\>>> np.loadtxt(s, delimiter\=",", converters\=conv)
array(\[1.0e+00, 2.5e+00, 3.0e+03, 1.8e+02, 5.0e+00\])

Copy to clipboard

Or a format where the `-` sign comes after the number:

\>>> s \= StringIO("10.01 31.25-\\n19.22 64.31\\n17.57- 63.94")
\>>> conv \= lambda x: \-float(x\[:\-1\]) if x.endswith("-") else float(x)
\>>> np.loadtxt(s, converters\=conv)
array(\[\[ 10.01, -31.25\],\
       \[ 19.22,  64.31\],\
       \[-17.57,  63.94\]\])

Copy to clipboard

Support for quoted fields is enabled with the _quotechar_ parameter. Comment and delimiter characters are ignored when they appear within a quoted item delineated by _quotechar_:

\>>> s \= StringIO('"alpha, #42", 10.0\\n"beta, #64", 2.0\\n')
\>>> dtype \= np.dtype(\[("label", "U12"), ("value", float)\])
\>>> np.loadtxt(s, dtype\=dtype, delimiter\=",", quotechar\='"')
array(\[('alpha, #42', 10.), ('beta, #64',  2.)\],
      dtype=\[('label', '<U12'), ('value', '<f8')\])

Copy to clipboard

Quoted fields can be separated by multiple whitespace characters:

\>>> s \= StringIO('"alpha, #42"       10.0\\n"beta, #64" 2.0\\n')
\>>> dtype \= np.dtype(\[("label", "U12"), ("value", float)\])
\>>> np.loadtxt(s, dtype\=dtype, delimiter\=None, quotechar\='"')
array(\[('alpha, #42', 10.), ('beta, #64',  2.)\],
      dtype=\[('label', '<U12'), ('value', '<f8')\])

Copy to clipboard

Two consecutive quote characters within a quoted field are treated as a single escaped character:

\>>> s \= StringIO('"Hello, my name is ""Monty""!"')
\>>> np.loadtxt(s, dtype\=np.str\_, delimiter\=",", quotechar\='"')
array('Hello, my name is "Monty"!', dtype='<U26')

Copy to clipboard

Read subset of columns when all rows do not contain equal number of values:

\>>> d \= StringIO("1 2\\n2 4\\n3 9 12\\n4 16 20")
\>>> np.loadtxt(d, usecols\=(0, 1))
array(\[\[ 1.,  2.\],\
       \[ 2.,  4.\],\
       \[ 3.,  9.\],\
       \[ 4., 16.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page