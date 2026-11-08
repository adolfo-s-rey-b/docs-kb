[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.capabilities.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.__array_namespace_info__.capabilities.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.__array_namespace_info__.capabilities.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.\_\_array\_namespace\_info\_\_.capabilities[#](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.capabilities.html#numpy-array-namespace-info-capabilities "Link to this heading")

=======================================================================================================================================================================================================================

method

\_\_array\_namespace\_info\_\_.capabilities()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_array_api_info.py#L63-L105)
[#](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.capabilities.html#numpy.__array_namespace_info__.capabilities "Link to this definition")

Return a dictionary of array API library capabilities.

The resulting dictionary has the following keys:

*   **“boolean indexing”**: boolean indicating whether an array library supports boolean indexing. Always `True` for NumPy.
    
*   **“data-dependent shapes”**: boolean indicating whether an array library supports data-dependent output shapes. Always `True` for NumPy.
    

See [https://data-apis.org/array-api/latest/API\_specification/generated/array\_api.info.capabilities.html](https://data-apis.org/array-api/latest/API_specification/generated/array_api.info.capabilities.html)
 for more details.

Returns:

**capabilities**dict

A dictionary of array API library capabilities.

See also

[`__array_namespace_info__.default_device`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.default_device.html#numpy.__array_namespace_info__.default_device "numpy.__array_namespace_info__.default_device")

[`__array_namespace_info__.default_dtypes`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.default_dtypes.html#numpy.__array_namespace_info__.default_dtypes "numpy.__array_namespace_info__.default_dtypes")

[`__array_namespace_info__.dtypes`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.dtypes.html#numpy.__array_namespace_info__.dtypes "numpy.__array_namespace_info__.dtypes")

[`__array_namespace_info__.devices`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.devices.html#numpy.__array_namespace_info__.devices "numpy.__array_namespace_info__.devices")

Examples

Try it in your browser!

\>>> info \= np.\_\_array\_namespace\_info\_\_()
\>>> info.capabilities()
{'boolean indexing': True,
 'data-dependent shapes': True,
 'max dimensions': 64}

Copy to clipboard

Go BackOpen In Tab

On this page