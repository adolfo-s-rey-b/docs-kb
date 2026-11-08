[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.read_array.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.format.read_array.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.read_array.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.format.read_array.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.format.read_array.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.format.read_array.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.format.read_array.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.format.read_array.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.format.read_array.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.format.read_array.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.format.read_array.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.format.read_array.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.format.read_array.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.format.read_array.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.format.read_array.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.format.read_array.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.format.read_array.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.format.read_array.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.format.read_array.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.format.read_array.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.format.read_array.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.format.read_array.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.format.read\_array[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.read_array.html#numpy-lib-format-read-array "Link to this heading")

======================================================================================================================================================================

lib.format.read\_array(_fp_, _allow\_pickle\=False_, _pickle\_kwargs\=None_, _\*_, _max\_header\_size\=10000_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_format_impl.py#L780-L889)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.read_array.html#numpy.lib.format.read_array "Link to this definition")

Read an array from an NPY file.

Parameters:

**fp**file\_like object

If this is not a real file object, then this may take extra memory and time.

**allow\_pickle**bool, optional

Whether to allow writing pickled data. Default: False

**pickle\_kwargs**dict

Additional keyword arguments to pass to pickle.load. These are only useful when loading object arrays saved on Python 2.

**max\_header\_size**int, optional

Maximum allowed size of the header. Large headers may not be safe to load securely and thus require explicitly passing a larger value. See [`ast.literal_eval`](https://docs.python.org/3/library/ast.html#ast.literal_eval "(in Python v3.14)")
 for details. This option is ignored when _allow\_pickle_ is passed. In that case the file is by definition trusted and the limit is unnecessary.

Returns:

**array**ndarray

The array from the data on disk.

Raises:

ValueError

If the data is invalid, or allow\_pickle=False and the file contains an object array.

On this page