[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.resize.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.resize[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.resize.html#numpy-ma-masked-array-resize "Link to this heading")

=========================================================================================================================================================================

method

ma.masked\_array.resize(_newshape_, _refcheck\=True_, _order\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L4819-L4835)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.resize.html#numpy.ma.masked_array.resize "Link to this definition")

Warning

This method does nothing, except raise a ValueError exception. A masked array does not own its data and therefore cannot safely be resized in place. Use the [`numpy.ma.resize`](https://numpy.org/doc/stable/reference/generated/numpy.ma.resize.html#numpy.ma.resize "numpy.ma.resize")
 function instead.

This method is difficult to implement safely and may be deprecated in future releases of NumPy.

On this page