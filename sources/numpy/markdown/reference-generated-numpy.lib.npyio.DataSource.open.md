[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.open.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.npyio.DataSource.open.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.open.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.npyio.DataSource.open.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.npyio.DataSource.open.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.npyio.DataSource.open.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.npyio.DataSource.open.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.npyio.DataSource.open.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.npyio.DataSource.open.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.npyio.DataSource.open.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.npyio.DataSource.open.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.npyio.DataSource.open.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.npyio.DataSource.open.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.npyio.DataSource.open.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.npyio.DataSource.open.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.npyio.DataSource.open.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.npyio.DataSource.open.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.npyio.DataSource.open.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.npyio.DataSource.open.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.npyio.DataSource.open.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.npyio.DataSource.open.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.npyio.DataSource.open.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.npyio.DataSource.open[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.open.html#numpy-lib-npyio-datasource-open "Link to this heading")

=================================================================================================================================================================================

method

lib.npyio.DataSource.open(_path_, _mode\='r'_, _encoding\=None_, _newline\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_datasource.py#L483-L529)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.open.html#numpy.lib.npyio.DataSource.open "Link to this definition")

Open and return file-like object.

If _path_ is a URL, it will be downloaded, stored in the _DataSource_ directory and opened from there.

Parameters:

**path**str or pathlib.Path

Local file path or URL to open.

**mode**{‘r’, ‘w’, ‘a’}, optional

Mode to open _path_. Mode ‘r’ for reading, ‘w’ for writing, ‘a’ to append. Available modes depend on the type of object specified by _path_. Default is ‘r’.

**encoding**{None, str}, optional

Open text file with given encoding. The default encoding will be what [`open`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.open.html#numpy.lib.npyio.DataSource.open "numpy.lib.npyio.DataSource.open")
 uses.

**newline**{None, str}, optional

Newline to use when reading text file.

Returns:

**out**file object

File object.

On this page