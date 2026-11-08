[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__new__.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.\_\_new\_\_[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__new__.html#numpy-ma-maskedarray-new "Link to this heading")

========================================================================================================================================================================

method

_static_ ma.MaskedArray.\_\_new\_\_(_cls_, _data\=None_, _mask\=np.False\__, _dtype\=None_, _copy\=False_, _subok\=True_, _ndmin\=0_, _fill\_value\=None_, _keep\_mask\=True_, _hard\_mask\=None_, _shrink\=True_, _order\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L2882-L3023)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__new__.html#numpy.ma.MaskedArray.__new__ "Link to this definition")

Create a new masked array from scratch.

Notes

A masked array can also be created by taking a .view(MaskedArray).

On this page