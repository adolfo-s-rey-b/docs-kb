[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.testing.suppress_warnings.record.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.testing.suppress\_warnings.record[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.suppress_warnings.record.html#numpy-testing-suppress-warnings-record "Link to this heading")

=======================================================================================================================================================================================================

method

testing.suppress\_warnings.record(_category=<class 'Warning'>_, _message=''_, _module=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/testing/_private/utils.py#L2446-L2474)
[#](https://numpy.org/doc/stable/reference/generated/numpy.testing.suppress_warnings.record.html#numpy.testing.suppress_warnings.record "Link to this definition")

Append a new recording filter or apply it if the state is entered.

All warnings matching will be appended to the `log` attribute.

Parameters:

**category**class, optional

Warning class to filter

**message**string, optional

Regular expression matching the warning message.

**module**module, optional

Module to filter for. Note that the module (and its file) must match exactly and cannot be a submodule. This may make it unreliable for external modules.

Returns:

**log**list

A list which will be filled with all matched warnings.

Notes

When added within a context, filters are only added inside the context and will be forgotten when the context is exited.

On this page