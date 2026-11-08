[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.ids.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.ids[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.ids.html#numpy-ma-masked-array-ids "Link to this heading")

================================================================================================================================================================

method

ma.masked\_array.ids()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L4923-L4948)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.ids.html#numpy.ma.masked_array.ids "Link to this definition")

Return the addresses of the data and mask areas.

Parameters:

**None**

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(\[1, 2, 3\], mask\=\[0, 1, 1\])
\>>> x.ids()
(166670640, 166659832) # may vary

Copy to clipboard

If the array has no mask, the address of _nomask_ is returned. This address is typically not close to the data in memory:

\>>> x \= np.ma.array(\[1, 2, 3\])
\>>> x.ids()
(166691080, 3083169284) # may vary

Copy to clipboard

Go BackOpen In Tab

On this page