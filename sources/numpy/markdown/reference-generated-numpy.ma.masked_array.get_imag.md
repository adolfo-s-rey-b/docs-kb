[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.get_imag.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.get\_imag[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.get_imag.html#numpy-ma-masked-array-get-imag "Link to this heading")

================================================================================================================================================================================

method

ma.masked\_array.get\_imag()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L4538-L4561)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.get_imag.html#numpy.ma.masked_array.get_imag "Link to this definition")

The imaginary part of the masked array.

This property is a view on the imaginary part of this _MaskedArray_.

See also

[`real`](https://numpy.org/doc/stable/reference/generated/numpy.real.html#numpy.real "numpy.real")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(\[1+1.j, \-2j, 3.45+1.6j\], mask\=\[False, True, False\])
\>>> x.imag
masked\_array(data=\[1.0, --, 1.6\],
             mask=\[False,  True, False\],
       fill\_value=1e+20)

Copy to clipboard

Go BackOpen In Tab

On this page