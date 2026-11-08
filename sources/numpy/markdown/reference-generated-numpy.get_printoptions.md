[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.get_printoptions.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.get_printoptions.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.get_printoptions.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.get_printoptions.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.get_printoptions.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.get_printoptions.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.get_printoptions.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.get_printoptions.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.get_printoptions.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.get_printoptions.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.get_printoptions.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.get_printoptions.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.get_printoptions.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.get_printoptions.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.get_printoptions.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.get_printoptions.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.get_printoptions.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.get_printoptions.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.get_printoptions.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.get_printoptions.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.get_printoptions.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.get_printoptions.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.get\_printoptions[#](https://numpy.org/doc/stable/reference/generated/numpy.get_printoptions.html#numpy-get-printoptions "Link to this heading")

=======================================================================================================================================================

numpy.get\_printoptions()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/arrayprint.py#L335-L388)
[#](https://numpy.org/doc/stable/reference/generated/numpy.get_printoptions.html#numpy.get_printoptions "Link to this definition")

Return the current print options.

Returns:

**print\_opts**dict

Dictionary of current print options with keys

*   precision : int
    
*   threshold : int
    
*   edgeitems : int
    
*   linewidth : int
    
*   suppress : bool
    
*   nanstr : str
    
*   infstr : str
    
*   sign : str
    
*   formatter : dict of callables
    
*   floatmode : str
    
*   legacy : str or False
    

For a full description of these options, see [`set_printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html#numpy.set_printoptions "numpy.set_printoptions")
.

See also

[`set_printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html#numpy.set_printoptions "numpy.set_printoptions")
, [`printoptions`](https://numpy.org/doc/stable/reference/generated/numpy.printoptions.html#numpy.printoptions "numpy.printoptions")

Notes

These print options apply only to NumPy ndarrays, not to scalars.

**Concurrency note:** see [Text formatting options](https://numpy.org/doc/stable/reference/routines.io.html#text-formatting-options)

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> np.get\_printoptions()
{'edgeitems': 3, 'threshold': 1000, ..., 'override\_repr': None}

Copy to clipboard

\>>> np.get\_printoptions()\['linewidth'\]
75
\>>> np.set\_printoptions(linewidth\=100)
\>>> np.get\_printoptions()\['linewidth'\]
100

Copy to clipboard

Go BackOpen In Tab

On this page