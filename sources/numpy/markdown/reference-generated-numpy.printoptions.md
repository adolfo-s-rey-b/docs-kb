[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.printoptions.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.printoptions.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.printoptions.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.printoptions.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.printoptions.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.printoptions.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.printoptions.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.printoptions.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.printoptions.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.printoptions.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.printoptions.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.printoptions.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.printoptions.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.printoptions.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.printoptions.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.printoptions.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.printoptions.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.printoptions.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.printoptions.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.printoptions.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.printoptions.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.printoptions.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.printoptions[#](https://numpy.org/doc/stable/reference/generated/numpy.printoptions.html#numpy-printoptions "Link to this heading")

==========================================================================================================================================

numpy.printoptions(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/arrayprint.py#L396-L435)
[#](https://numpy.org/doc/stable/reference/generated/numpy.printoptions.html#numpy.printoptions "Link to this definition")

Context manager for setting print options.

Set print options for the scope of the _with_ block, and restore the old options at the end. See [`set_printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html#numpy.set_printoptions "numpy.set_printoptions")
 for the full description of available options.

See also

[`set_printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html#numpy.set_printoptions "numpy.set_printoptions")
, [`get_printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.get_printoptions.html#numpy.get_printoptions "numpy.get_printoptions")

Notes

These print options apply only to NumPy ndarrays, not to scalars.

**Concurrency note:** see [Text formatting options](https://numpy.org/doc/stable/reference/routines.io.html#text-formatting-options)

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> from numpy.testing import assert\_equal
\>>> with np.printoptions(precision\=2):
...     np.array(\[2.0\]) / 3
array(\[0.67\])

Copy to clipboard

The _as_\-clause of the _with_\-statement gives the current print options:

\>>> with np.printoptions(precision\=2) as opts:
...      assert\_equal(opts, np.get\_printoptions())

Copy to clipboard

Go BackOpen In Tab

On this page