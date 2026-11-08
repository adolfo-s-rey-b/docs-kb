[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.strings.find.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.strings.find.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.strings.find.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.strings.find.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.strings.find.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.strings.find.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.strings.find.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.strings.find.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.strings.find.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.strings.find.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.strings.find.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.strings.find.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.strings.find.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.strings.find.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.strings.find.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.strings.find.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.strings.find.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.strings.find.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.strings.find.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.strings.find.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.strings.find.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.strings.find.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.strings.find[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.find.html#numpy-strings-find "Link to this heading")

==========================================================================================================================================

strings.find(_a_, _sub_, _start\=0_, _end\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L255-L290)
[#](https://numpy.org/doc/stable/reference/generated/numpy.strings.find.html#numpy.strings.find "Link to this definition")

For each element, return the lowest index in the string where substring `sub` is found, such that `sub` is contained in the range \[`start`, `end`).\
\
Parameters:\
\
**a**array\_like, with `StringDType`, `bytes_` or `str_` dtype\
\
**sub**array\_like, with `bytes_` or `str_` dtype\
\
The substring to search for.\
\
**start, end**array\_like, with any integer dtype\
\
The range to look in, interpreted as in slice notation.\
\
Returns:\
\
**y**ndarray\
\
Output array of ints\
\
See also\
\
[`str.find`](https://docs.python.org/3/library/stdtypes.html#str.find "(in Python v3.14)")\
\
Examples\
\
Try it in your browser!\
\
\>>> import numpy as np\
\>>> a \= np.array(\["NumPy is a Python library"\])\
\>>> np.strings.find(a, "Python")\
array(\[11\])\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
On this page