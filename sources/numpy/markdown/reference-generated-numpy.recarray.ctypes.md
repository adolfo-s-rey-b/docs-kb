[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.recarray.ctypes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.recarray.ctypes.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.recarray.ctypes.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.recarray.ctypes.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.recarray.ctypes.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.recarray.ctypes.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.recarray.ctypes.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.recarray.ctypes.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.recarray.ctypes.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.recarray.ctypes.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.recarray.ctypes.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.recarray.ctypes.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.recarray.ctypes.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.recarray.ctypes.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.recarray.ctypes.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.recarray.ctypes.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.recarray.ctypes.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.recarray.ctypes.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.recarray.ctypes.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.recarray.ctypes.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.recarray.ctypes.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.recarray.ctypes.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.recarray.ctypes[#](https://numpy.org/doc/stable/reference/generated/numpy.recarray.ctypes.html#numpy-recarray-ctypes "Link to this heading")

===================================================================================================================================================

attribute

recarray.ctypes[#](https://numpy.org/doc/stable/reference/generated/numpy.recarray.ctypes.html#numpy.recarray.ctypes "Link to this definition")

An object to simplify the interaction of the array with the ctypes module.

This attribute creates an object that makes it easier to use arrays when calling shared libraries with the ctypes module. The returned object has, among others, data, shape, and strides attributes (see Notes below) which themselves return ctypes objects that can be used as arguments to a shared library.

Parameters:

**None**

Returns:

**c**Python object

Possessing attributes data, shape, strides, etc.

See also

[`numpy.ctypeslib`](https://numpy.org/doc/stable/reference/routines.ctypeslib.html#module-numpy.ctypeslib "numpy.ctypeslib")

Notes

Below are the public attributes of this object which were documented in “Guide to NumPy” (we have omitted undocumented public attributes, as well as documented private attributes):

\_ctypes.data

A pointer to the memory area of the array as a Python integer. This memory area may contain data that is not aligned, or not in correct byte-order. The memory area may not even be writeable. The array flags and data-type of this array should be respected when passing this attribute to arbitrary C-code to avoid trouble that can include Python crashing. User Beware! The value of this attribute is exactly the same as: `self._array_interface_['data'][0]`.

Note that unlike `data_as`, a reference won’t be kept to the array: code like `ctypes.c_void_p((a + b).ctypes.data)` will result in a pointer to a deallocated array, and should be spelt `(a + b).ctypes.data_as(ctypes.c_void_p)`

\_ctypes.shape

(c\_intp\*self.ndim): A ctypes array of length self.ndim where the basetype is the C-integer corresponding to `dtype('p')` on this platform (see [`c_intp`](https://numpy.org/doc/stable/reference/routines.ctypeslib.html#numpy.ctypeslib.c_intp "numpy.ctypeslib.c_intp")
). This base-type could be [`ctypes.c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "(in Python v3.14)")
, [`ctypes.c_long`](https://docs.python.org/3/library/ctypes.html#ctypes.c_long "(in Python v3.14)")
, or [`ctypes.c_longlong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_longlong "(in Python v3.14)")
 depending on the platform. The ctypes array contains the shape of the underlying array.

\_ctypes.strides

(c\_intp\*self.ndim): A ctypes array of length self.ndim where the basetype is the same as for the shape attribute. This ctypes array contains the strides information from the underlying array. This strides information is important for showing how many bytes must be jumped to get to the next element in the array.

\_ctypes.data\_as(_obj_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/_internal.py#L279-L296)

Return the data pointer cast to a particular c-types object. For example, calling `self._as_parameter_` is equivalent to `self.data_as(ctypes.c_void_p)`. Perhaps you want to use the data as a pointer to a ctypes array of floating-point data: `self.data_as(ctypes.POINTER(ctypes.c_double))`.

The returned pointer will keep a reference to the array.

\_ctypes.shape\_as(_obj_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/_internal.py#L298-L305)

Return the shape tuple as an array of some other c-types type. For example: `self.shape_as(ctypes.c_short)`.

\_ctypes.strides\_as(_obj_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/_internal.py#L307-L314)

Return the strides tuple as an array of some other c-types type. For example: `self.strides_as(ctypes.c_longlong)`.

If the ctypes module is not available, then the ctypes attribute of array objects still returns something useful, but ctypes objects are not returned and errors may be raised instead. In particular, the object will still have the `as_parameter` attribute which will return an integer equal to the data attribute.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import ctypes
\>>> x \= np.array(\[\[0, 1\], \[2, 3\]\], dtype\=np.int32)
\>>> x
array(\[\[0, 1\],\
       \[2, 3\]\], dtype=int32)
\>>> x.ctypes.data
31962608 # may vary
\>>> x.ctypes.data\_as(ctypes.POINTER(ctypes.c\_uint32))
<\_\_main\_\_.LP\_c\_uint object at 0x7ff2fc1fc200> # may vary
\>>> x.ctypes.data\_as(ctypes.POINTER(ctypes.c\_uint32)).contents
c\_uint(0)
\>>> x.ctypes.data\_as(ctypes.POINTER(ctypes.c\_uint64)).contents
c\_ulong(4294967296)
\>>> x.ctypes.shape
<numpy.\_core.\_internal.c\_long\_Array\_2 object at 0x7ff2fc1fce60> # may vary
\>>> x.ctypes.strides
<numpy.\_core.\_internal.c\_long\_Array\_2 object at 0x7ff2fc1ff320> # may vary

Copy to clipboard

Go BackOpen In Tab

On this page