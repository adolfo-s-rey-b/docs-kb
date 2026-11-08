[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.mintypecode.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.mintypecode.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.mintypecode.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.mintypecode.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.mintypecode.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.mintypecode.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.mintypecode.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.mintypecode.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.mintypecode.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.mintypecode.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.mintypecode.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.mintypecode.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.mintypecode.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.mintypecode.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.mintypecode.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.mintypecode.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.mintypecode.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.mintypecode.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.mintypecode.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.mintypecode.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.mintypecode.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.mintypecode.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.mintypecode[#](https://numpy.org/doc/stable/reference/generated/numpy.mintypecode.html#numpy-mintypecode "Link to this heading")

=======================================================================================================================================

numpy.mintypecode(_typechars_, _typeset\='GDFgdf'_, _default\='d'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_type_check_impl.py#L26-L78)
[#](https://numpy.org/doc/stable/reference/generated/numpy.mintypecode.html#numpy.mintypecode "Link to this definition")

Return the character for the minimum-size type to which given types can be safely cast.

The returned type character must represent the smallest size dtype such that an array of the returned type can handle the data from an array of all types in _typechars_ (or if _typechars_ is an array, then its dtype.char).

Parameters:

**typechars**list of str or array\_like

If a list of strings, each string should represent a dtype. If array\_like, the character representation of the array dtype is used.

**typeset**str or list of str, optional

The set of characters that the returned character is chosen from. The default set is ‘GDFgdf’.

**default**str, optional

The default character, this is returned if none of the characters in _typechars_ matches a character in _typeset_.

Returns:

**typechar**str

The character representing the minimum-size type that was found.

See also

[`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.mintypecode(\['d', 'f', 'S'\])
'd'
\>>> x \= np.array(\[1.1, 2\-3.j\])
\>>> np.mintypecode(x)
'D'

Copy to clipboard

\>>> np.mintypecode('abceh', default\='G')
'G'

Copy to clipboard

Go BackOpen In Tab

On this page