[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.types.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ufunc.types.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.types.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ufunc.types.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ufunc.types.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ufunc.types.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ufunc.types.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ufunc.types.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ufunc.types.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ufunc.types.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ufunc.types.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ufunc.types.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ufunc.types.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ufunc.types.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ufunc.types.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ufunc.types.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ufunc.types.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ufunc.types.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ufunc.types.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ufunc.types.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ufunc.types.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ufunc.types.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ufunc.types[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.types.html#numpy-ufunc-types "Link to this heading")

=======================================================================================================================================

attribute

ufunc.types[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.types.html#numpy.ufunc.types "Link to this definition")

Returns a list with types grouped input->output.

Data attribute listing the data-type “Domain-Range” groupings the ufunc can deliver. The data-types are given using the character codes.

See also

[`numpy.ufunc.ntypes`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.ntypes.html#numpy.ufunc.ntypes "numpy.ufunc.ntypes")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.add.types
\['??->?', 'bb->b', 'BB->B', 'hh->h', 'HH->H', 'ii->i', 'II->I', ...\
\
Copy to clipboard\
\
\>>> np.power.types\
\['bb->b', 'BB->B', 'hh->h', 'HH->H', 'ii->i', 'II->I', 'll->l', ...\
\
Copy to clipboard\
\
\>>> np.exp.types\
\['e->e', 'f->f', 'd->d', 'f->f', 'd->d', 'g->g', 'F->F', 'D->D', 'G->G', 'O->O'\]\
\
Copy to clipboard\
\
\>>> np.remainder.types\
\['bb->b', 'BB->B', 'hh->h', 'HH->H', 'ii->i', 'II->I', 'll->l', ...\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
On this page