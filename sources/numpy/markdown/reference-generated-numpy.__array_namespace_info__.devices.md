[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.devices.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.__array_namespace_info__.devices.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.devices.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.__array_namespace_info__.devices.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.__array_namespace_info__.devices.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.__array_namespace_info__.devices.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.__array_namespace_info__.devices.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.__array_namespace_info__.devices.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.__array_namespace_info__.devices.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.__array_namespace_info__.devices.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.__array_namespace_info__.devices.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.__array_namespace_info__.devices.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.__array_namespace_info__.devices.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.__array_namespace_info__.devices.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.__array_namespace_info__.devices.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.__array_namespace_info__.devices.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.__array_namespace_info__.devices.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.__array_namespace_info__.devices.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.__array_namespace_info__.devices.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.__array_namespace_info__.devices.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.__array_namespace_info__.devices.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.__array_namespace_info__.devices.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.\_\_array\_namespace\_info\_\_.devices[#](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.devices.html#numpy-array-namespace-info-devices "Link to this heading")

========================================================================================================================================================================================================

method

\_\_array\_namespace\_info\_\_.devices()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_array_api_info.py#L321-L346)
[#](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.devices.html#numpy.__array_namespace_info__.devices "Link to this definition")

The devices supported by NumPy.

For NumPy, this always returns `('cpu',)`.

Returns:

**devices**list of str

The devices supported by NumPy.

See also

[`__array_namespace_info__.capabilities`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.capabilities.html#numpy.__array_namespace_info__.capabilities "numpy.__array_namespace_info__.capabilities")

[`__array_namespace_info__.default_device`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.default_device.html#numpy.__array_namespace_info__.default_device "numpy.__array_namespace_info__.default_device")

[`__array_namespace_info__.default_dtypes`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.default_dtypes.html#numpy.__array_namespace_info__.default_dtypes "numpy.__array_namespace_info__.default_dtypes")

[`__array_namespace_info__.dtypes`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.dtypes.html#numpy.__array_namespace_info__.dtypes "numpy.__array_namespace_info__.dtypes")

Examples

Try it in your browser!

\>>> info \= np.\_\_array\_namespace\_info\_\_()
\>>> info.devices()
('cpu',)

Copy to clipboard

Go BackOpen In Tab

On this page