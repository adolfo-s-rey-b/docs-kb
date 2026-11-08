[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.suppress_warnings.filter.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.testing.suppress_warnings.filter.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.testing.suppress_warnings.filter.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.testing.suppress_warnings.filter.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.testing.suppress_warnings.filter.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.testing.suppress_warnings.filter.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.testing.suppress_warnings.filter.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.testing.suppress_warnings.filter.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.testing.suppress_warnings.filter.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.testing.suppress_warnings.filter.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.testing.suppress_warnings.filter.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.testing.suppress_warnings.filter.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.testing.suppress_warnings.filter.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.testing.suppress_warnings.filter.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.testing.suppress_warnings.filter.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.testing.suppress_warnings.filter.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.testing.suppress_warnings.filter.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.testing.suppress_warnings.filter.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.testing.suppress_warnings.filter.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.testing.suppress_warnings.filter.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.testing.suppress_warnings.filter.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.testing.suppress_warnings.filter.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.suppress\_warnings.filter[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.suppress_warnings.filter.html#numpy-testing-suppress-warnings-filter "Link to this heading")

=======================================================================================================================================================================================================

method

testing.suppress\_warnings.filter(_category=<class 'Warning'>_, _message=''_, _module=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L2423-L2444)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.suppress_warnings.filter.html#numpy.testing.suppress_warnings.filter "Link to this definition")

Add a new suppressing filter or apply it if the state is entered.

Parameters:

**category**class, optional

Warning class to filter

**message**string, optional

Regular expression matching the warning message.

**module**module, optional

Module to filter for. Note that the module (and its file) must match exactly and cannot be a submodule. This may make it unreliable for external modules.

Notes

When added within a context, filters are only added inside the context and will be forgotten when the context is exited.

On this page