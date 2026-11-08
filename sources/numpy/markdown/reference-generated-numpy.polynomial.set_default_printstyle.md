[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.set_default_printstyle.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.set_default_printstyle.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.set_default_printstyle.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.set_default_printstyle.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.set_default_printstyle.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.set_default_printstyle.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.set_default_printstyle.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.set_default_printstyle.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.set_default_printstyle.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.set_default_printstyle.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.set_default_printstyle.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.set_default_printstyle.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.set_default_printstyle.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.set_default_printstyle.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.set_default_printstyle.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.set_default_printstyle.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.set_default_printstyle.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.set_default_printstyle.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.set_default_printstyle.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.set_default_printstyle.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.set_default_printstyle.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.set_default_printstyle.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.set\_default\_printstyle[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.set_default_printstyle.html#numpy-polynomial-set-default-printstyle "Link to this heading")

===========================================================================================================================================================================================================

polynomial.set\_default\_printstyle(_style_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/__init__.py#L135-L181)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.set_default_printstyle.html#numpy.polynomial.set_default_printstyle "Link to this definition")

Set the default format for the string representation of polynomials.

Values for `style` must be valid inputs to `__format__`, i.e. ‘ascii’ or ‘unicode’.

Parameters:

**style**str

Format string for default printing style. Must be either ‘ascii’ or ‘unicode’.

Notes

The default format depends on the platform: ‘unicode’ is used on Unix-based systems and ‘ascii’ on Windows. This determination is based on default font support for the unicode superscript and subscript ranges.

Examples

Try it in your browser!

\>>> p \= np.polynomial.Polynomial(\[1, 2, 3\])
\>>> c \= np.polynomial.Chebyshev(\[1, 2, 3\])
\>>> np.polynomial.set\_default\_printstyle('unicode')
\>>> print(p)
1.0 + 2.0·x + 3.0·x²
\>>> print(c)
1.0 + 2.0·T₁(x) + 3.0·T₂(x)
\>>> np.polynomial.set\_default\_printstyle('ascii')
\>>> print(p)
1.0 + 2.0 x + 3.0 x\*\*2
\>>> print(c)
1.0 + 2.0 T\_1(x) + 3.0 T\_2(x)
\>>> \# Formatting supersedes all class/package-level defaults
\>>> print(f"{p:unicode}")
1.0 + 2.0·x + 3.0·x²

Copy to clipboard

Go BackOpen In Tab

On this page