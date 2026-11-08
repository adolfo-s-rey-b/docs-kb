[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.put.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.put.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.put.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.put.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.put.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.put.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.put.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.put.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.put.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.put.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.put.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.put.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.put.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.put.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.put.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.put.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.put.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.put.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.put.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.put.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.put.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.put.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.put[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.put.html#numpy-ma-maskedarray-put "Link to this heading")

============================================================================================================================================================

method

ma.MaskedArray.put(_indices_, _values_, _mode\='raise'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L4837-L4921)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.put.html#numpy.ma.MaskedArray.put "Link to this definition")

Set storage-indexed locations to corresponding values.

Sets self.\_data.flat\[n\] = values\[n\] for each n in indices. If _values_ is shorter than [`indices`](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#numpy.indices "numpy.indices")
 then it will repeat. If _values_ has some masked values, the initial mask is updated in consequence, else the corresponding values are unmasked.

Parameters:

**indices**1-D array\_like

Target indices, interpreted as integers.

**values**array\_like

Values to place in self.\_data copy at target indices.

**mode**{‘raise’, ‘wrap’, ‘clip’}, optional

Specifies how out-of-bounds indices will behave. ‘raise’ : raise an error. ‘wrap’ : wrap around. ‘clip’ : clip to the range.

Notes

_values_ can be a scalar or length 1 array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(\[\[1,2,3\],\[4,5,6\],\[7,8,9\]\], mask\=\[0\] + \[1,0\]\*4)
\>>> x
masked\_array(
  data=\[\[1, --, 3\],\
        \[--, 5, --\],\
        \[7, --, 9\]\],
  mask=\[\[False,  True, False\],\
        \[ True, False,  True\],\
        \[False,  True, False\]\],
  fill\_value=999999)
\>>> x.put(\[0,4,8\],\[10,20,30\])
\>>> x
masked\_array(
  data=\[\[10, --, 3\],\
        \[--, 20, --\],\
        \[7, --, 30\]\],
  mask=\[\[False,  True, False\],\
        \[ True, False,  True\],\
        \[False,  True, False\]\],
  fill\_value=999999)

Copy to clipboard

\>>> x.put(4,999)
\>>> x
masked\_array(
  data=\[\[10, --, 3\],\
        \[--, 999, --\],\
        \[7, --, 30\]\],
  mask=\[\[False,  True, False\],\
        \[ True, False,  True\],\
        \[False,  True, False\]\],
  fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page