[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.dtype_to_descr.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.format.dtype\_to\_descr[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.dtype_to_descr.html#numpy-lib-format-dtype-to-descr "Link to this heading")

===================================================================================================================================================================================

lib.format.dtype\_to\_descr(_dtype_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_format_impl.py#L250-L307)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.dtype_to_descr.html#numpy.lib.format.dtype_to_descr "Link to this definition")

Get a serializable descriptor from the dtype.

The .descr attribute of a dtype object cannot be round-tripped through the dtype() constructor. Simple types, like dtype(‘float32’), have a descr which looks like a record array with one field with ‘’ as a name. The dtype() constructor interprets this as a request to give a default name. Instead, we construct descriptor that can be passed to dtype().

Parameters:

**dtype**dtype

The dtype of the array that will be written to disk.

Returns:

**descr**object

An object that can be passed to _numpy.dtype()_ in order to replicate the input dtype.

On this page