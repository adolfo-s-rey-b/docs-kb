[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.dot.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.dot[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.dot.html#numpy-ma-masked-array-dot "Link to this heading")

================================================================================================================================================================

method

ma.masked\_array.dot(_b_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L5163-L5196)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.dot.html#numpy.ma.masked_array.dot "Link to this definition")

Masked dot product of two arrays. Note that _out_ and _strict_ are located in different positions than in [`ma.dot`](https://numpy.org/doc/stable/reference/generated/numpy.ma.dot.html#numpy.ma.dot "numpy.ma.dot")
. In order to maintain compatibility with the functional version, it is recommended that the optional arguments be treated as keyword only. At some point that may be mandatory.

Parameters:

**b**masked\_array\_like

Inputs array.

**out**masked\_array, optional

Output argument. This must have the exact kind that would be returned if it was not used. In particular, it must have the right type, must be C-contiguous, and its dtype must be the dtype that would be returned for _ma.dot(a,b)_. This is a performance feature. Therefore, if these conditions are not met, an exception is raised, instead of attempting to be flexible.

**strict**bool, optional

Whether masked data are propagated (True) or set to 0 (False) for the computation. Default is False. Propagating the mask means that if a masked value appears in a row or column, the whole row or column is considered masked.

See also

[`numpy.ma.dot`](https://numpy.org/doc/stable/reference/generated/numpy.ma.dot.html#numpy.ma.dot "numpy.ma.dot")

equivalent function

On this page