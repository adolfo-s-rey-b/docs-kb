[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.write_array.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.format.write\_array[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.write_array.html#numpy-lib-format-write-array "Link to this heading")

=========================================================================================================================================================================

lib.format.write\_array(_fp_, _array_, _version\=None_, _allow\_pickle\=True_, _pickle\_kwargs\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_format_impl.py#L702-L777)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.write_array.html#numpy.lib.format.write_array "Link to this definition")

Write an array to an NPY file, including a header.

If the array is neither C-contiguous nor Fortran-contiguous AND the file\_like object is not a real file object, this function will have to copy data in memory.

Parameters:

**fp**file\_like object

An open, writable file object, or similar object with a `.write()` method.

**array**ndarray

The array to write to disk.

**version**(int, int) or None, optional

The version number of the format. None means use the oldest supported version that is able to store the data. Default: None

**allow\_pickle**bool, optional

Whether to allow writing pickled data. Default: True

**pickle\_kwargs**dict, optional

Additional keyword arguments to pass to pickle.dump, excluding ‘protocol’. These are only useful when pickling objects in object arrays to Python 2 compatible format.

Raises:

ValueError

If the array cannot be persisted. This includes the case of allow\_pickle=False and array being an object array.

Various other errors

If the array contains Python objects as part of its dtype, the process of pickling them may raise various errors if the objects are not picklable.

On this page