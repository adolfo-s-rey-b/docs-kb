[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.dtypes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.__array_namespace_info__.dtypes.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.__array_namespace_info__.dtypes.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.\_\_array\_namespace\_info\_\_.dtypes[#](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.dtypes.html#numpy-array-namespace-info-dtypes "Link to this heading")

=====================================================================================================================================================================================================

method

\_\_array\_namespace\_info\_\_.dtypes(_\*_, _device\=None_, _kind\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_array_api_info.py#L186-L319)
[#](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.dtypes.html#numpy.__array_namespace_info__.dtypes "Link to this definition")

The array API data types supported by NumPy.

Note that this function only returns data types that are defined by the array API.

Parameters:

**device**str, optional

The device to get the data types for. For NumPy, only `'cpu'` is allowed.

**kind**str or tuple of str, optional

The kind of data types to return. If `None`, all data types are returned. If a string, only data types of that kind are returned. If a tuple, a dictionary containing the union of the given kinds is returned. The following kinds are supported:

*   `'bool'`: boolean data types (i.e., `bool`).
    
*   `'signed integer'`: signed integer data types (i.e., `int8`, `int16`, `int32`, `int64`).
    
*   `'unsigned integer'`: unsigned integer data types (i.e., `uint8`, `uint16`, `uint32`, `uint64`).
    
*   `'integral'`: integer data types. Shorthand for `('signed integer', 'unsigned integer')`.
    
*   `'real floating'`: real-valued floating-point data types (i.e., `float32`, `float64`).
    
*   `'complex floating'`: complex floating-point data types (i.e., `complex64`, `complex128`).
    
*   `'numeric'`: numeric data types. Shorthand for `('integral', 'real floating', 'complex floating')`.
    

Returns:

**dtypes**dict

A dictionary mapping the names of data types to the corresponding NumPy data types.

See also

[`__array_namespace_info__.capabilities`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.capabilities.html#numpy.__array_namespace_info__.capabilities "numpy.__array_namespace_info__.capabilities")

[`__array_namespace_info__.default_device`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.default_device.html#numpy.__array_namespace_info__.default_device "numpy.__array_namespace_info__.default_device")

[`__array_namespace_info__.default_dtypes`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.default_dtypes.html#numpy.__array_namespace_info__.default_dtypes "numpy.__array_namespace_info__.default_dtypes")

[`__array_namespace_info__.devices`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.devices.html#numpy.__array_namespace_info__.devices "numpy.__array_namespace_info__.devices")

Examples

Try it in your browser!

\>>> info \= np.\_\_array\_namespace\_info\_\_()
\>>> info.dtypes(kind\='signed integer')
{'int8': numpy.int8,
 'int16': numpy.int16,
 'int32': numpy.int32,
 'int64': numpy.int64}

Copy to clipboard

Go BackOpen In Tab

On this page