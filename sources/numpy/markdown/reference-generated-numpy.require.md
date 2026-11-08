[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.require.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.require.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.require.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.require.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.require.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.require.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.require.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.require.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.require.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.require.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.require.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.require.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.require.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.require.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.require.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.require.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.require.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.require.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.require.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.require.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.require.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.require.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.require[#](https://numpy.org/doc/stable/reference/generated/numpy.require.html#numpy-require "Link to this heading")

===========================================================================================================================

numpy.require(_a_, _dtype\=None_, _requirements\=None_, _\*_, _like\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/_asarray.py#L22-L127)
[#](https://numpy.org/doc/stable/reference/generated/numpy.require.html#numpy.require "Link to this definition")

Return an ndarray of the provided type that satisfies requirements.

This function is useful to be sure that an array with the correct flags is returned for passing to compiled code (perhaps through ctypes).

Parameters:

**a**array\_like

The object to be converted to a type-and-requirement-satisfying array.

**dtype**data-type

The required data-type. If None preserve the current dtype. If your application requires the data to be in native byteorder, include a byteorder specification as a part of the dtype specification.

**requirements**str or sequence of str

The requirements list can be any of the following

*   ‘F\_CONTIGUOUS’ (‘F’) - ensure a Fortran-contiguous array
    
*   ‘C\_CONTIGUOUS’ (‘C’) - ensure a C-contiguous array
    
*   ‘ALIGNED’ (‘A’) - ensure a data-type aligned array
    
*   ‘WRITEABLE’ (‘W’) - ensure a writable array
    
*   ‘OWNDATA’ (‘O’) - ensure an array that owns its own data
    
*   ‘ENSUREARRAY’, (‘E’) - ensure a base array, instead of a subclass
    

**like**array\_like, optional

Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as `like` supports the `__array_function__` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

Returns:

**out**ndarray

Array with specified requirements and type if given.

See also

[`asarray`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")

Convert input to an ndarray.

[`asanyarray`](https://numpy.org/doc/stable/reference/generated/numpy.asanyarray.html#numpy.asanyarray "numpy.asanyarray")

Convert to an ndarray, but pass through ndarray subclasses.

[`ascontiguousarray`](https://numpy.org/doc/stable/reference/generated/numpy.ascontiguousarray.html#numpy.ascontiguousarray "numpy.ascontiguousarray")

Convert input to a contiguous array.

[`asfortranarray`](https://numpy.org/doc/stable/reference/generated/numpy.asfortranarray.html#numpy.asfortranarray "numpy.asfortranarray")

Convert input to an ndarray with column-major memory order.

[`ndarray.flags`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flags.html#numpy.ndarray.flags "numpy.ndarray.flags")

Information about the memory layout of the array.

Notes

The returned array will be guaranteed to have the listed requirements by making a copy if needed.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(6).reshape(2,3)
\>>> x.flags
  C\_CONTIGUOUS : True
  F\_CONTIGUOUS : False
  OWNDATA : False
  WRITEABLE : True
  ALIGNED : True
  WRITEBACKIFCOPY : False

Copy to clipboard

\>>> y \= np.require(x, dtype\=np.float32, requirements\=\['A', 'O', 'W', 'F'\])
\>>> y.flags
  C\_CONTIGUOUS : False
  F\_CONTIGUOUS : True
  OWNDATA : True
  WRITEABLE : True
  ALIGNED : True
  WRITEBACKIFCOPY : False

Copy to clipboard

Go BackOpen In Tab

On this page