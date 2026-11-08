[Skip to main content](https://numpy.org/doc/stable/user/basics.dispatch.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Writing custom array containers[#](https://numpy.org/doc/stable/user/basics.dispatch.html#writing-custom-array-containers "Link to this heading")

==================================================================================================================================================

Numpy’s dispatch mechanism, introduced in numpy version v1.16 is the recommended approach for writing custom N-dimensional array containers that are compatible with the numpy API and provide custom implementations of numpy functionality. Applications include [dask](https://docs.dask.org/en/stable/)
 arrays, an N-dimensional array distributed across multiple nodes, and [cupy](https://docs-cupy.chainer.org/en/stable/)
 arrays, an N-dimensional array on a GPU.

For comprehensive documentation on writing custom array containers, please see:

*   [Interoperability with NumPy](https://numpy.org/doc/stable/user/basics.interoperability.html#basics-interoperability)
     - the main guide covering `__array_ufunc__` and `__array_function__` protocols
    
*   [Special attributes and methods](https://numpy.org/doc/stable/reference/arrays.classes.html#special-attributes-and-methods)
     - see `class.__array__()` for documentation and example implementing the `__array__()` method
    

Numpy provides some utilities to aid testing of custom array containers that implement the `__array_ufunc__` and `__array_function__` protocols in the `numpy.testing.overrides` namespace.

To check if a Numpy function can be overridden via `__array_ufunc__`, you can use [`allows_array_ufunc_override`](https://numpy.org/doc/stable/reference/generated/numpy.testing.overrides.allows_array_ufunc_override.html#numpy.testing.overrides.allows_array_ufunc_override "numpy.testing.overrides.allows_array_ufunc_override")
:

\>>> from numpy.testing.overrides import allows\_array\_ufunc\_override
\>>> allows\_array\_ufunc\_override(np.add)
True

Copy to clipboard

Similarly, you can check if a function can be overridden via `__array_function__` using [`allows_array_function_override`](https://numpy.org/doc/stable/reference/generated/numpy.testing.overrides.allows_array_function_override.html#numpy.testing.overrides.allows_array_function_override "numpy.testing.overrides.allows_array_function_override")
.

Lists of every overridable function in the Numpy API are also available via [`get_overridable_numpy_array_functions`](https://numpy.org/doc/stable/reference/generated/numpy.testing.overrides.get_overridable_numpy_array_functions.html#numpy.testing.overrides.get_overridable_numpy_array_functions "numpy.testing.overrides.get_overridable_numpy_array_functions")
 for functions that support the `__array_function__` protocol and [`get_overridable_numpy_ufuncs`](https://numpy.org/doc/stable/reference/generated/numpy.testing.overrides.get_overridable_numpy_ufuncs.html#numpy.testing.overrides.get_overridable_numpy_ufuncs "numpy.testing.overrides.get_overridable_numpy_ufuncs")
 for functions that support the `__array_ufunc__` protocol. Both functions return sets of functions that are present in the Numpy public API. User-defined ufuncs or ufuncs defined in other libraries that depend on Numpy are not present in these sets.

Refer to the [dask source code](https://github.com/dask/dask)
 and [cupy source code](https://github.com/cupy/cupy)
 for more fully-worked examples of custom array containers.

See also [NEP 18](https://numpy.org/neps/nep-0018-array-function-protocol.html "(in NumPy Enhancement Proposals)")
.