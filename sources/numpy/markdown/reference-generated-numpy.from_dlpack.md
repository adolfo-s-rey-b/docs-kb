[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.from_dlpack.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.from_dlpack.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.from_dlpack.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.from_dlpack.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.from_dlpack.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.from_dlpack.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.from_dlpack.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.from_dlpack.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.from_dlpack.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.from_dlpack.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.from_dlpack.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.from_dlpack.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.from_dlpack.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.from_dlpack.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.from_dlpack.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.from_dlpack.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.from_dlpack.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.from_dlpack.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.from_dlpack.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.from_dlpack.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.from_dlpack.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.from_dlpack.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.from\_dlpack[#](https://numpy.org/doc/stable/reference/generated/numpy.from_dlpack.html#numpy-from-dlpack "Link to this heading")

========================================================================================================================================

numpy.from\_dlpack(_x_, _/_, _\*_, _device\=None_, _copy\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.from_dlpack.html#numpy.from_dlpack "Link to this definition")

Create a NumPy array from an object implementing the `__dlpack__` protocol. Generally, the returned NumPy array is a view of the input object. See [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.from_dlpack.html#re9eadf7a166b-1)
 and [\[2\]](https://numpy.org/doc/stable/reference/generated/numpy.from_dlpack.html#re9eadf7a166b-2)
 for more details.

Parameters:

**x**object

A Python object that implements the `__dlpack__` and `__dlpack_device__` methods.

**device**device, optional

Device on which to place the created array. Default: `None`. Must be `"cpu"` if passed which may allow importing an array that is not already CPU available.

**copy**bool, optional

Boolean indicating whether or not to copy the input. If `True`, the copy will be made. If `False`, the function will never copy, and will raise `BufferError` in case a copy is deemed necessary. Passing it requests a copy from the exporter who may or may not implement the capability. If `None`, the function will reuse the existing memory buffer if possible and copy otherwise. Default: `None`.

Returns:

**out**ndarray

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.from_dlpack.html#id1)\
\]

Array API documentation, [https://data-apis.org/array-api/latest/design\_topics/data\_interchange.html#syntax-for-data-interchange-with-dlpack](https://data-apis.org/array-api/latest/design_topics/data_interchange.html#syntax-for-data-interchange-with-dlpack)

\[[2](https://numpy.org/doc/stable/reference/generated/numpy.from_dlpack.html#id2)\
\]

Python specification for DLPack, [https://dmlc.github.io/dlpack/latest/python\_spec.html](https://dmlc.github.io/dlpack/latest/python_spec.html)

Examples

Try it in your browser!

\>>> import torch  
\>>> x \= torch.arange(10)  
\>>> \# create a view of the torch tensor "x" in NumPy
\>>> y \= np.from\_dlpack(x)  

Copy to clipboard

Go BackOpen In Tab

On this page