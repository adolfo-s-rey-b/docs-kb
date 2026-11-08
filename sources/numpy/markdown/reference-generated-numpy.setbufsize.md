[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.setbufsize.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.setbufsize.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.setbufsize.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.setbufsize.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.setbufsize.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.setbufsize.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.setbufsize.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.setbufsize.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.setbufsize.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.setbufsize.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.setbufsize.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.setbufsize.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.setbufsize.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.setbufsize.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.setbufsize.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.setbufsize.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.setbufsize.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.setbufsize.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.setbufsize.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.setbufsize.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.setbufsize.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.setbufsize.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.setbufsize[#](https://numpy.org/doc/stable/reference/generated/numpy.setbufsize.html#numpy-setbufsize "Link to this heading")

====================================================================================================================================

numpy.setbufsize(_size_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/_ufunc_config.py#L161-L204)
[#](https://numpy.org/doc/stable/reference/generated/numpy.setbufsize.html#numpy.setbufsize "Link to this definition")

Set the size of the buffer used in ufuncs.

Changed in version 2.0: The scope of setting the buffer is tied to the [`numpy.errstate`](https://numpy.org/doc/stable/reference/generated/numpy.errstate.html#numpy.errstate "numpy.errstate")
 context. Exiting a `with errstate():` will also restore the bufsize.

Parameters:

**size**int

Size of buffer.

Returns:

**bufsize**int

Previous size of ufunc buffer in bytes.

Notes

**Concurrency note:** see [Floating point error handling](https://numpy.org/doc/stable/reference/routines.err.html)

Examples

Try it in your browser!

When exiting a [`numpy.errstate`](https://numpy.org/doc/stable/reference/generated/numpy.errstate.html#numpy.errstate "numpy.errstate")
 context manager the bufsize is restored:

\>>> import numpy as np
\>>> with np.errstate():
...     np.setbufsize(4096)
...     print(np.getbufsize())
...
8192
4096
\>>> np.getbufsize()
8192

Copy to clipboard

Go BackOpen In Tab

On this page