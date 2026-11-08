[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.descr_to_dtype.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.format.descr_to_dtype.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.descr_to_dtype.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.format.descr_to_dtype.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.format.descr_to_dtype.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.format.descr_to_dtype.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.format.descr_to_dtype.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.format.descr_to_dtype.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.format.descr_to_dtype.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.format.descr_to_dtype.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.format.descr_to_dtype.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.format.descr_to_dtype.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.format.descr_to_dtype.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.format.descr_to_dtype.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.format.descr_to_dtype.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.format.descr_to_dtype.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.format.descr_to_dtype.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.format.descr_to_dtype.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.format.descr_to_dtype.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.format.descr_to_dtype.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.format.descr_to_dtype.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.format.descr_to_dtype.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.format.descr\_to\_dtype[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.descr_to_dtype.html#numpy-lib-format-descr-to-dtype "Link to this heading")

===================================================================================================================================================================================

lib.format.descr\_to\_dtype(_descr_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_format_impl.py#L310-L365)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.descr_to_dtype.html#numpy.lib.format.descr_to_dtype "Link to this definition")

Returns a dtype based off the given description.

This is essentially the reverse of [`dtype_to_descr`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.dtype_to_descr.html#numpy.lib.format.dtype_to_descr "numpy.lib.format.dtype_to_descr")
. It will remove the valueless padding fields created by, i.e. simple fields like dtype(‘float32’), and then convert the description to its corresponding dtype.

Parameters:

**descr**object

The object retrieved by dtype.descr. Can be passed to [`numpy.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 in order to replicate the input dtype.

Returns:

**dtype**dtype

The dtype constructed by the description.

On this page