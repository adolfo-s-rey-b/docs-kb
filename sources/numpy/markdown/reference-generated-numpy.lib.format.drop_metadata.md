[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.drop_metadata.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.format.drop_metadata.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.drop_metadata.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.format.drop_metadata.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.format.drop_metadata.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.format.drop_metadata.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.format.drop_metadata.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.format.drop_metadata.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.format.drop_metadata.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.format.drop_metadata.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.format.drop_metadata.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.format.drop_metadata.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.format.drop_metadata.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.format.drop_metadata.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.format.drop_metadata.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.format.drop_metadata.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.format.drop_metadata.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.format.drop_metadata.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.format.drop_metadata.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.format.drop_metadata.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.format.drop_metadata.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.format.drop_metadata.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.format.drop\_metadata[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.drop_metadata.html#numpy-lib-format-drop-metadata "Link to this heading")

===============================================================================================================================================================================

lib.format.drop\_metadata(_dtype_, _/_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_utils_impl.py#L481-L541)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.drop_metadata.html#numpy.lib.format.drop_metadata "Link to this definition")

Returns the dtype unchanged if it contained no metadata or a copy of the dtype if it (or any of its structure dtypes) contained metadata.

This utility is used by _np.save_ and _np.savez_ to drop metadata before saving.

Note

Due to its limitation this function may move to a more appropriate home or change in the future and is considered semi-public API only.

Warning

This function does not preserve more strange things like record dtypes and user dtypes may simply return the wrong thing. If you need to be sure about the latter, check the result with: `np.can_cast(new_dtype, dtype, casting="no")`.

On this page