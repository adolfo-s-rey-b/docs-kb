[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fromstring.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fromstring[#](https://numpy.org/doc/stable/reference/generated/numpy.fromstring.html#numpy-fromstring "Link to this heading")

====================================================================================================================================

numpy.fromstring(_string_, _dtype\=np.float64_, _count\=\-1_, _\*_, _sep_, _like\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.fromstring.html#numpy.fromstring "Link to this definition")

A new 1-D array initialized from text data in a string.

Parameters:

**string**str

A string containing the data.

**dtype**data-type, optional

The data type of the array; default: [`numpy.float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
. For binary input data, the data must be in exactly this format. Most builtin numeric types are supported and extension types may be supported.

**count**int, optional

Read this number of [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 elements from the data. If this is negative (the default), the count will be determined from the length of the data.

**sep**str, optional

The string separating numbers in the data; extra whitespace between elements is also ignored.

Deprecated since version 1.14: Passing `sep=''`, the default, is deprecated since it will trigger the deprecated binary mode of this function. This mode interprets [`string`](https://docs.python.org/3/library/string.html#module-string "(in Python v3.14)")
 as binary bytes, rather than ASCII text with decimal numbers, an operation which is better spelt `frombuffer(string, dtype, count)`. If [`string`](https://docs.python.org/3/library/string.html#module-string "(in Python v3.14)")
 contains unicode text, the binary mode of [`fromstring`](https://numpy.org/doc/stable/reference/generated/numpy.fromstring.html#numpy.fromstring "numpy.fromstring")
 will first encode it into bytes using utf-8, which will not produce sane results.

**like**array\_like, optional

Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as `like` supports the `__array_function__` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

Returns:

**arr**ndarray

The constructed array.

Raises:

ValueError

If the string is not the correct size to satisfy the requested [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 and _count_.

See also

[`frombuffer`](https://numpy.org/doc/stable/reference/generated/numpy.frombuffer.html#numpy.frombuffer "numpy.frombuffer")
, [`fromfile`](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#numpy.fromfile "numpy.fromfile")
, [`fromiter`](https://numpy.org/doc/stable/reference/generated/numpy.fromiter.html#numpy.fromiter "numpy.fromiter")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.fromstring('1 2', dtype\=np.int\_, sep\=' ')
array(\[1, 2\])
\>>> np.fromstring('1, 2', dtype\=np.int\_, sep\=',')
array(\[1, 2\])

Copy to clipboard

Go BackOpen In Tab

On this page