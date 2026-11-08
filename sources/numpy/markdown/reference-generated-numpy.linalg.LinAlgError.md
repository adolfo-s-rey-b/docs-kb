[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.LinAlgError.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.LinAlgError.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.LinAlgError.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.LinAlgError.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.LinAlgError.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.LinAlgError.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.LinAlgError.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.LinAlgError.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.LinAlgError.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.LinAlgError.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.LinAlgError.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.LinAlgError.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.LinAlgError.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.LinAlgError.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.LinAlgError.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.LinAlgError.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.LinAlgError.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.LinAlgError.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.LinAlgError.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.LinAlgError.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.LinAlgError.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.LinAlgError.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.LinAlgError[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.LinAlgError.html#numpy-linalg-linalgerror "Link to this heading")

============================================================================================================================================================

_exception_ linalg.LinAlgError[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L113-L140)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.LinAlgError.html#numpy.linalg.LinAlgError "Link to this definition")

Generic Python-exception-derived object raised by linalg functions.

General purpose exception class, derived from Python’s ValueError class, programmatically raised in linalg functions when a Linear Algebra-related condition would prevent further correct execution of the function.

Parameters:

**None**

Examples

Try it in your browser!

\>>> from numpy import linalg as LA
\>>> LA.inv(np.zeros((2,2)))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "...linalg.py", line 350,
    in inv return wrap(solve(a, identity(a.shape\[0\], dtype=a.dtype)))
  File "...linalg.py", line 249,
    in solve
    raise LinAlgError('Singular matrix')
numpy.linalg.LinAlgError: Singular matrix

Copy to clipboard

Go BackOpen In Tab

On this page