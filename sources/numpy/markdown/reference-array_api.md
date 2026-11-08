[Skip to main content](https://numpy.org/doc/stable/reference/array_api.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/array_api.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/array_api.html)
[2.4](https://numpy.org/doc/2.4/reference/array_api.html)
[2.3](https://numpy.org/doc/2.3/reference/array_api.html)
[2.2](https://numpy.org/doc/2.2/reference/array_api.html)
[2.1](https://numpy.org/doc/2.1/reference/array_api.html)
[2.0](https://numpy.org/doc/2.0/reference/array_api.html)
[1.26](https://numpy.org/doc/1.26/reference/array_api.html)
[1.25](https://numpy.org/doc/1.25/reference/array_api.html)
[1.24](https://numpy.org/doc/1.24/reference/array_api.html)
[1.23](https://numpy.org/doc/1.23/reference/array_api.html)
[1.22](https://numpy.org/doc/1.22/reference/array_api.html)
[1.21](https://numpy.org/doc/1.21/reference/array_api.html)
[1.20](https://numpy.org/doc/1.20/reference/array_api.html)
[1.19](https://numpy.org/doc/1.19/reference/array_api.html)
[1.18](https://numpy.org/doc/1.18/reference/array_api.html)
[1.17](https://numpy.org/doc/1.17/reference/array_api.html)
[1.16](https://numpy.org/doc/1.16/reference/array_api.html)
[1.15](https://numpy.org/doc/1.15/reference/array_api.html)
[1.14](https://numpy.org/doc/1.14/reference/array_api.html)
[1.13](https://numpy.org/doc/1.13/reference/array_api.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Array API standard compatibility[#](https://numpy.org/doc/stable/reference/array_api.html#array-api-standard-compatibility "Link to this heading")

===================================================================================================================================================

The NumPy 2.3.0 main namespace as well as the [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
 and [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html#module-numpy.linalg "numpy.linalg")
 namespaces are compatible with the [2024.12 version](https://data-apis.org/array-api/2024.12/index.html)
 of the Python array API standard.

NumPy aims to implement support for the future versions of the standard - assuming that those future versions can be upgraded to given NumPy’s [backwards compatibility policy](https://numpy.org/neps/nep-0023-backwards-compatibility.html#nep23 "(in NumPy Enhancement Proposals)")
.

For usage guidelines for downstream libraries and end users who want to write code that will work with both NumPy and other array libraries, we refer to the documentation of the array API standard itself and to code and developer-focused documentation in SciPy and scikit-learn.

Note that in order to use standard-complaint code with older NumPy versions (< 2.0), the [array-api-compat](https://github.com/data-apis/array-api-compat)
 package may be useful. For testing whether NumPy-using code is only using standard-compliant features rather than anything NumPy-specific, the [array-api-strict](https://github.com/data-apis/array-api-strict)
 package can be used.

History

NumPy 1.22.0 was the first version to include support for the array API standard, via a separate `numpy.array_api` submodule. This module was marked as experimental (it emitted a warning on import) and removed in NumPy 2.0 because full support (2022.12 version [\[1\]](https://numpy.org/doc/stable/reference/array_api.html#id3)
) was included in the main namespace. [NEP 47](https://numpy.org/neps/nep-0047-array-api-standard.html#nep47 "(in NumPy Enhancement Proposals)")
 and [NEP 56](https://numpy.org/neps/nep-0056-array-api-main-namespace.html#nep56 "(in NumPy Enhancement Proposals)")
 describe the motivation and scope for implementing the array API standard in NumPy.

Entry point[#](https://numpy.org/doc/stable/reference/array_api.html#entry-point "Link to this heading")

---------------------------------------------------------------------------------------------------------

NumPy installs an [entry point](https://packaging.python.org/en/latest/specifications/entry-points/)
 that can be used for discovery purposes:

\>>> from importlib.metadata import entry\_points
\>>> entry\_points(group\='array\_api', name\='numpy')
\[EntryPoint(name='numpy', value='numpy', group='array\_api')\]

Copy to clipboard

Note that leaving out `name='numpy'` will cause a list of entry points to be returned for all array API standard compatible implementations that installed an entry point.

Footnotes

Inspection[#](https://numpy.org/doc/stable/reference/array_api.html#inspection "Link to this heading")

-------------------------------------------------------------------------------------------------------

NumPy implements the [array API inspection utilities](https://data-apis.org/array-api/latest/API_specification/inspection.html)
. These functions can be accessed via the `__array_namespace_info__()` function, which returns a namespace containing the inspection utilities.

|     |     |
| --- | --- |
| [`__array_namespace_info__`](https://numpy.org/doc/stable/reference/generated/numpy.__array_namespace_info__.html#numpy.__array_namespace_info__ "numpy.__array_namespace_info__")<br>() | Get the array API inspection namespace for NumPy. |

On this page