[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.encode.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.char.encode.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.char.encode.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.char.encode.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.char.encode.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.char.encode.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.char.encode.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.char.encode.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.char.encode.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.char.encode.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.char.encode.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.char.encode.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.char.encode.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.char.encode.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.char.encode.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.char.encode.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.char.encode.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.char.encode.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.char.encode.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.char.encode.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.char.encode.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.char.encode.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.encode[#](https://numpy.org/doc/stable/reference/generated/numpy.char.encode.html#numpy-char-encode "Link to this heading")

=======================================================================================================================================

char.encode(_a_, _encoding\=None_, _errors\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L584-L627)
[#](https://numpy.org/doc/stable/reference/generated/numpy.char.encode.html#numpy.char.encode "Link to this definition")

Calls [`str.encode`](https://docs.python.org/3/library/stdtypes.html#str.encode "(in Python v3.14)")
 element-wise.

The set of available codecs comes from the Python standard library, and may be extended at runtime. For more information, see the [`codecs`](https://docs.python.org/3/library/codecs.html#module-codecs "(in Python v3.14)")
 module.

Parameters:

**a**array\_like, with `StringDType` or `str_` dtype

**encoding**str, optional

The name of an encoding

**errors**str, optional

Specifies how to handle encoding errors

Returns:

**out**ndarray

See also

[`str.encode`](https://docs.python.org/3/library/stdtypes.html#str.encode "(in Python v3.14)")

Notes

The type of the result will depend on the encoding specified.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\['aAaAaA', '  aA  ', 'abBABba'\])
\>>> np.strings.encode(a, encoding\='cp037')
array(\[b'ÁÁÁ', b'@@Á@@',\
   b'ÂÁÂ'\], dtype='|S7')

Copy to clipboard

Go BackOpen In Tab

On this page