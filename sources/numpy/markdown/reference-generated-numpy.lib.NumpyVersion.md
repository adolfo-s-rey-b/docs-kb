[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.NumpyVersion.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.NumpyVersion.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.NumpyVersion.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.NumpyVersion.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.NumpyVersion.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.NumpyVersion.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.NumpyVersion.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.NumpyVersion.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.NumpyVersion.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.NumpyVersion.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.NumpyVersion.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.NumpyVersion.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.NumpyVersion.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.NumpyVersion.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.NumpyVersion.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.NumpyVersion.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.NumpyVersion.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.NumpyVersion.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.NumpyVersion.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.NumpyVersion.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.NumpyVersion.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.NumpyVersion.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.NumpyVersion[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.NumpyVersion.html#numpy-lib-numpyversion "Link to this heading")

======================================================================================================================================================

_class_ numpy.lib.NumpyVersion(_vstring_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/__init__.py)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.NumpyVersion.html#numpy.lib.NumpyVersion "Link to this definition")

Parse and compare numpy version strings.

NumPy has the following versioning scheme (numbers given are examples; they can be > 9 in principle):

*   Released version: ‘1.8.0’, ‘1.8.1’, etc.
    
*   Alpha: ‘1.8.0a1’, ‘1.8.0a2’, etc.
    
*   Beta: ‘1.8.0b1’, ‘1.8.0b2’, etc.
    
*   Release candidates: ‘1.8.0rc1’, ‘1.8.0rc2’, etc.
    
*   Development versions: ‘1.8.0.dev-f1234afa’ (git commit hash appended)
    
*   Development versions after a1: ‘1.8.0a1.dev-f1234afa’, ‘1.8.0b2.dev-f1234afa’, ‘1.8.1rc1.dev-f1234afa’, etc.
    
*   Development versions (no git hash available): ‘1.8.0.dev-Unknown’
    

Comparing needs to be done against a valid version string or other [`NumpyVersion`](https://numpy.org/doc/stable/reference/generated/numpy.lib.NumpyVersion.html#numpy.lib.NumpyVersion "numpy.lib.NumpyVersion")
 instance. Note that all development versions of the same (pre-)release compare equal.

Parameters:

**vstring**str

NumPy version string (`np.__version__`).

Examples

Try it in your browser!

\>>> from numpy.lib import NumpyVersion
\>>> if NumpyVersion(np.\_\_version\_\_) < '1.7.0':
...     print('skip')
\>>> \# skip

Copy to clipboard

\>>> NumpyVersion('1.7')  \# raises ValueError, add ".0"
Traceback (most recent call last):
    ...
ValueError: Not a valid numpy version string

Copy to clipboard

Go BackOpen In Tab

On this page