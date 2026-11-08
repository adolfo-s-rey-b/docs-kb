[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.magic.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.format.magic.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.magic.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.format.magic.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.format.magic.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.format.magic.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.format.magic.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.format.magic.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.format.magic.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.format.magic.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.format.magic.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.format.magic.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.format.magic.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.format.magic.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.format.magic.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.format.magic.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.format.magic.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.format.magic.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.format.magic.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.format.magic.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.format.magic.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.format.magic.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.format.magic[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.magic.html#numpy-lib-format-magic "Link to this heading")

======================================================================================================================================================

lib.format.magic(_major_, _minor_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_format_impl.py#L205-L226)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.magic.html#numpy.lib.format.magic "Link to this definition")

Return the magic string for the given file format version.

Parameters:

**major**int in \[0, 255\]

**minor**int in \[0, 255\]

Returns:

**magic**str

Raises:

ValueError if the version cannot be formatted.

On this page