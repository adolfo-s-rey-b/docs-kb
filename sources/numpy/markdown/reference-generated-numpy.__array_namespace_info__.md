[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.\_\_array\_namespace\_info\_\_[#](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.html#numpy-array-namespace-info "Link to this heading")

================================================================================================================================================================================

_class_ numpy.\_\_array\_namespace\_info\_\_[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_array_api_info.py#L30-L346)
[#](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.html#numpy.__array_namespace_info__ "Link to this definition")

Get the array API inspection namespace for NumPy.

The array API inspection namespace defines the following functions:

*   capabilities()
    
*   default\_device()
    
*   default\_dtypes()
    
*   dtypes()
    
*   devices()
    

See [https://data-apis.org/array-api/latest/API\_specification/inspection.html](https://data-apis.org/array-api/latest/API_specification/inspection.html)
 for more details.

Methods

|     |     |
| --- | --- |
| [`capabilities`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.capabilities.html#numpy.__array_namespace_info__.capabilities "numpy.__array_namespace_info__.capabilities")<br>() | Return a dictionary of array API library capabilities. |
| [`default_device`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.default_device.html#numpy.__array_namespace_info__.default_device "numpy.__array_namespace_info__.default_device")<br>() | The default device used for new NumPy arrays. |
| [`default_dtypes`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.default_dtypes.html#numpy.__array_namespace_info__.default_dtypes "numpy.__array_namespace_info__.default_dtypes")<br>(\*\[, device\]) | The default data types used for new NumPy arrays. |
| [`devices`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.devices.html#numpy.__array_namespace_info__.devices "numpy.__array_namespace_info__.devices")<br>() | The devices supported by NumPy. |
| [`dtypes`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.dtypes.html#numpy.__array_namespace_info__.dtypes "numpy.__array_namespace_info__.dtypes")<br>(\*\[, device, kind\]) | The array API data types supported by NumPy. |

Returns:

**info**ModuleType

The array API inspection namespace for NumPy.

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