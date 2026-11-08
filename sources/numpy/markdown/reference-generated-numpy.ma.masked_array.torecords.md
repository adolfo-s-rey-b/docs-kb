[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.torecords.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.torecords[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.torecords.html#numpy-ma-masked-array-torecords "Link to this heading")

==================================================================================================================================================================================

method

ma.masked\_array.torecords()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L6421-L6479)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.torecords.html#numpy.ma.masked_array.torecords "Link to this definition")

Transforms a masked array into a flexible-type array.

The flexible type array that is returned will have two fields:

*   the `_data` field stores the `_data` part of the array.
    
*   the `_mask` field stores the `_mask` part of the array.
    

Parameters:

**None**

Returns:

**record**ndarray

A new flexible-type [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 with two fields: the first element containing a value, the second element containing the corresponding mask boolean. The returned record shape matches self.shape.

Notes

A side-effect of transforming a masked array into a flexible [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 is that meta information (`fill_value`, …) will be lost.

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
\>>> x.toflex()
array(\[\[(1, False), (2,  True), (3, False)\],\
       \[(4,  True), (5, False), (6,  True)\],\
       \[(7, False), (8,  True), (9, False)\]\],
      dtype=\[('\_data', '<i8'), ('\_mask', '?')\])

Copy to clipboard

Go BackOpen In Tab

On this page