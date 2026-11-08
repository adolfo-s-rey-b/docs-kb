[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__array__.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ndarray.\_\_array\_\_[#](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__array__.html#numpy-ndarray-array "Link to this heading")

=========================================================================================================================================================

method

ndarray.\_\_array\_\_(\[_dtype_, \]_\*_, _copy=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__array__.html#numpy.ndarray.__array__ "Link to this definition")

For `dtype` parameter it returns a new reference to self if `dtype` is not given or it matches array’s data type. A new array of provided data type is returned if `dtype` is different from the current data type of the array. For `copy` parameter it returns a new reference to self if `copy=False` or `copy=None` and copying isn’t enforced by `dtype` parameter. The method returns a new array for `copy=True`, regardless of `dtype` parameter.

A more detailed explanation of the `__array__` interface can be found in [The \_\_array\_\_() method](https://numpy.org/doc/stable/user/basics.interoperability.html#dunder-array-interface)
.

On this page