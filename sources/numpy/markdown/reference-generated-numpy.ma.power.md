[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.power.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.power[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.power.html#numpy-ma-power "Link to this heading")

==============================================================================================================================

ma.power(_a_, _b_, _third\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7134-L7210)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.power.html#numpy.ma.power "Link to this definition")

Returns element-wise base array raised to power from second array.

This is the masked array version of [`numpy.power`](https://numpy.org/doc/stable/reference/generated/numpy.power.html#numpy.power "numpy.power")
. For details see [`numpy.power`](https://numpy.org/doc/stable/reference/generated/numpy.power.html#numpy.power "numpy.power")
.

See also

[`numpy.power`](https://numpy.org/doc/stable/reference/generated/numpy.power.html#numpy.power "numpy.power")

Notes

The _out_ argument to [`numpy.power`](https://numpy.org/doc/stable/reference/generated/numpy.power.html#numpy.power "numpy.power")
 is not supported, _third_ has to be None.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> x \= \[11.2, \-3.973, 0.801, \-1.41\]
\>>> mask \= \[0, 0, 0, 1\]
\>>> masked\_x \= ma.masked\_array(x, mask)
\>>> masked\_x
masked\_array(data=\[11.2, -3.973, 0.801, --\],
         mask=\[False, False, False,  True\],
   fill\_value=1e+20)
\>>> ma.power(masked\_x, 2)
masked\_array(data=\[125.43999999999998, 15.784728999999999,\
               0.6416010000000001, --\],
         mask=\[False, False, False,  True\],
   fill\_value=1e+20)
\>>> y \= \[\-0.5, 2, 0, 17\]
\>>> masked\_y \= ma.masked\_array(y, mask)
\>>> masked\_y
masked\_array(data=\[-0.5, 2.0, 0.0, --\],
         mask=\[False, False, False,  True\],
   fill\_value=1e+20)
\>>> ma.power(masked\_x, masked\_y)
masked\_array(data=\[0.2988071523335984, 15.784728999999999, 1.0, --\],
         mask=\[False, False, False,  True\],
   fill\_value=1e+20)

Copy to clipboard

Go BackOpen In Tab

On this page