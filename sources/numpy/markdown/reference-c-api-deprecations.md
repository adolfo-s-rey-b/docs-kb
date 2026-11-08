[Skip to main content](https://numpy.org/doc/stable/reference/c-api/deprecations.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/c-api/deprecations.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/c-api/deprecations.html)
[2.4](https://numpy.org/doc/2.4/reference/c-api/deprecations.html)
[2.3](https://numpy.org/doc/2.3/reference/c-api/deprecations.html)
[2.2](https://numpy.org/doc/2.2/reference/c-api/deprecations.html)
[2.1](https://numpy.org/doc/2.1/reference/c-api/deprecations.html)
[2.0](https://numpy.org/doc/2.0/reference/c-api/deprecations.html)
[1.26](https://numpy.org/doc/1.26/reference/c-api/deprecations.html)
[1.25](https://numpy.org/doc/1.25/reference/c-api/deprecations.html)
[1.24](https://numpy.org/doc/1.24/reference/c-api/deprecations.html)
[1.23](https://numpy.org/doc/1.23/reference/c-api/deprecations.html)
[1.22](https://numpy.org/doc/1.22/reference/c-api/deprecations.html)
[1.21](https://numpy.org/doc/1.21/reference/c-api/deprecations.html)
[1.20](https://numpy.org/doc/1.20/reference/c-api/deprecations.html)
[1.19](https://numpy.org/doc/1.19/reference/c-api/deprecations.html)
[1.18](https://numpy.org/doc/1.18/reference/c-api/deprecations.html)
[1.17](https://numpy.org/doc/1.17/reference/c-api/deprecations.html)
[1.16](https://numpy.org/doc/1.16/reference/c-api/deprecations.html)
[1.15](https://numpy.org/doc/1.15/reference/c-api/deprecations.html)
[1.14](https://numpy.org/doc/1.14/reference/c-api/deprecations.html)
[1.13](https://numpy.org/doc/1.13/reference/c-api/deprecations.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

C API deprecations[#](https://numpy.org/doc/stable/reference/c-api/deprecations.html#c-api-deprecations "Link to this heading")

================================================================================================================================

Background[#](https://numpy.org/doc/stable/reference/c-api/deprecations.html#background "Link to this heading")

----------------------------------------------------------------------------------------------------------------

The API exposed by NumPy for third-party extensions has grown over years of releases, and has allowed programmers to directly access NumPy functionality from C. This API can be best described as “organic”. It has emerged from multiple competing desires and from multiple points of view over the years, strongly influenced by the desire to make it easy for users to move to NumPy from Numeric and Numarray. The core API originated with Numeric in 1995 and there are patterns such as the heavy use of macros written to mimic Python’s C-API as well as account for compiler technology of the late 90’s. There is also only a small group of volunteers who have had very little time to spend on improving this API.

There is an ongoing effort to improve the API. It is important in this effort to ensure that code that compiles for NumPy 1.X continues to compile for NumPy 1.X. At the same time, certain API’s will be marked as deprecated so that future-looking code can avoid these API’s and follow better practices.

Another important role played by deprecation markings in the C API is to move towards hiding internal details of the NumPy implementation. For those needing direct, easy, access to the data of ndarrays, this will not remove this ability. Rather, there are many potential performance optimizations which require changing the implementation details, and NumPy developers have been unable to try them because of the high value of preserving ABI compatibility. By deprecating this direct access, we will in the future be able to improve NumPy’s performance in ways we cannot presently.

Deprecation mechanism NPY\_NO\_DEPRECATED\_API[#](https://numpy.org/doc/stable/reference/c-api/deprecations.html#deprecation-mechanism-npy-no-deprecated-api "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In C, there is no equivalent to the deprecation warnings that Python supports. One way to do deprecations is to flag them in the documentation and release notes, then remove or change the deprecated features in a future major version (NumPy 2.0 and beyond). Minor versions of NumPy should not have major C-API changes, however, that prevent code that worked on a previous minor release. For example, we will do our best to ensure that code that compiled and worked on NumPy 1.4 should continue to work on NumPy 1.7 (but perhaps with compiler warnings).

To use the NPY\_NO\_DEPRECATED\_API mechanism, you need to #define it to the target API version of NumPy before #including any NumPy headers. If you want to confirm that your code is clean against 1.7, use:

#define NPY\_NO\_DEPRECATED\_API NPY\_1\_7\_API\_VERSION

Copy to clipboard

On compilers which support a #warning mechanism, NumPy issues a compiler warning if you do not define the symbol NPY\_NO\_DEPRECATED\_API. This way, the fact that there are deprecations will be flagged for third-party developers who may not have read the release notes closely.

Note that defining NPY\_NO\_DEPRECATED\_API is not sufficient to make your extension ABI compatible with a given NumPy version. See [For downstream package authors](https://numpy.org/doc/stable/dev/depending_on_numpy.html#for-downstream-package-authors)
.

On this page