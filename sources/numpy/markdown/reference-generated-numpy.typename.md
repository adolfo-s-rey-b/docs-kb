[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.typename.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.typename.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.typename.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.typename.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.typename.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.typename.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.typename.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.typename.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.typename.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.typename.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.typename.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.typename.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.typename.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.typename.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.typename.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.typename.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.typename.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.typename.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.typename.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.typename.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.typename.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.typename.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.typename[#](https://numpy.org/doc/stable/reference/generated/numpy.typename.html#numpy-typename "Link to this heading")

==============================================================================================================================

numpy.typename(_char_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_type_check_impl.py#L580-L640)
[#](https://numpy.org/doc/stable/reference/generated/numpy.typename.html#numpy.typename "Link to this definition")

Return a description for the given data type code.

Deprecated since version 2.5: [`numpy.typename`](https://numpy.org/doc/stable/reference/generated/numpy.typename.html#numpy.typename "numpy.typename")
 is deprecated. Use [`numpy.dtype.name`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.name.html#numpy.dtype.name "numpy.dtype.name")
 instead.

Parameters:

**char**str

Data type code.

Returns:

**out**str

Description of the input data type code.

See also

[`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> typechars \= \['S1', '?', 'B', 'D', 'G', 'F', 'I', 'H', 'L', 'O', 'Q',\
...              'S', 'U', 'V', 'b', 'd', 'g', 'f', 'i', 'h', 'l', 'q'\]
\>>> for typechar in typechars:
...     print(typechar, ' : ', np.typename(typechar))
...
S1  :  character
?  :  bool
B  :  unsigned char
D  :  complex double precision
G  :  complex long double precision
F  :  complex single precision
I  :  unsigned integer
H  :  unsigned short
L  :  unsigned long integer
O  :  object
Q  :  unsigned long long integer
S  :  string
U  :  unicode
V  :  void
b  :  signed char
d  :  double precision
g  :  long precision
f  :  single precision
i  :  integer
h  :  short
l  :  long integer
q  :  long long integer

Copy to clipboard

Go BackOpen In Tab

On this page