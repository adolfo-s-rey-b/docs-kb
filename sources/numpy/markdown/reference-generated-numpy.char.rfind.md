[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.rfind.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.rfind[#](https://numpy.org/doc/stable/reference/generated/numpy.char.rfind.html#numpy-char-rfind "Link to this heading")

====================================================================================================================================

char.rfind(_a_, _sub_, _start\=0_, _end\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/strings.py#L293-L333)
[#](https://numpy.org/doc/stable/reference/generated/numpy.char.rfind.html#numpy.char.rfind "Link to this definition")

For each element, return the highest index in the string where substring `sub` is found, such that `sub` is contained in the range \[`start`, `end`).\
\
Parameters:\
\
**a**array-like, with `StringDType`, `bytes_`, or `str_` dtype\
\
**sub**array-like, with `StringDType`, `bytes_`, or `str_` dtype\
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
[`str.rfind`](https://docs.python.org/3/library/stdtypes.html#str.rfind "(in Python v3.14)")\
\
Examples\
\
Try it in your browser!\
\
\>>> import numpy as np\
\>>> a \= np.array(\["Computer Science"\])\
\>>> np.strings.rfind(a, "Science", start\=0, end\=None)\
array(\[9\])\
\>>> np.strings.rfind(a, "Science", start\=0, end\=8)\
array(\[-1\])\
\>>> b \= np.array(\["Computer Science", "Science"\])\
\>>> np.strings.rfind(b, "Science", start\=0, end\=None)\
array(\[9, 0\])\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
On this page