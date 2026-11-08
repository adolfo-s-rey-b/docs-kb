[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.default_dtypes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.\_\_array\_namespace\_info\_\_.default\_dtypes[#](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.default_dtypes.html#numpy-array-namespace-info-default-dtypes "Link to this heading")

==============================================================================================================================================================================================================================

method

\_\_array\_namespace\_info\_\_.default\_dtypes(_\*_, _device\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_array_api_info.py#L134-L184)
[#](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.default_dtypes.html#numpy.__array_namespace_info__.default_dtypes "Link to this definition")

The default data types used for new NumPy arrays.

For NumPy, this always returns the following dictionary:

*   **“real floating”**: `numpy.float64`
    
*   **“complex floating”**: `numpy.complex128`
    
*   **“integral”**: `numpy.intp`
    
*   **“indexing”**: `numpy.intp`
    

Parameters:

**device**str, optional

The device to get the default data types for. For NumPy, only `'cpu'` is allowed.

Returns:

**dtypes**dict

A dictionary describing the default data types used for new NumPy arrays.

See also

[`__array_namespace_info__.capabilities`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.capabilities.html#numpy.__array_namespace_info__.capabilities "numpy.__array_namespace_info__.capabilities")

[`__array_namespace_info__.default_device`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.default_device.html#numpy.__array_namespace_info__.default_device "numpy.__array_namespace_info__.default_device")

[`__array_namespace_info__.dtypes`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.dtypes.html#numpy.__array_namespace_info__.dtypes "numpy.__array_namespace_info__.dtypes")

[`__array_namespace_info__.devices`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.devices.html#numpy.__array_namespace_info__.devices "numpy.__array_namespace_info__.devices")

Examples

Try it in your browser!

\>>> info \= np.\_\_array\_namespace\_info\_\_()
\>>> info.default\_dtypes()
{'real floating': numpy.float64,
 'complex floating': numpy.complex128,
 'integral': numpy.int64,
 'indexing': numpy.int64}

Copy to clipboard

Go BackOpen In Tab

On this page