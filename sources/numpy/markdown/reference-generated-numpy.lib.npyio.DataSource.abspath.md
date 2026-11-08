[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.abspath.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.npyio.DataSource.abspath.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.npyio.DataSource.abspath.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.npyio.DataSource.abspath[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.abspath.html#numpy-lib-npyio-datasource-abspath "Link to this heading")

==========================================================================================================================================================================================

method

lib.npyio.DataSource.abspath(_path_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_datasource.py#L371-L411)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.abspath.html#numpy.lib.npyio.DataSource.abspath "Link to this definition")

Return absolute path of file in the DataSource directory.

If _path_ is a URL, then [`abspath`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.abspath.html#numpy.lib.npyio.DataSource.abspath "numpy.lib.npyio.DataSource.abspath")
 will return either the location the file exists locally or the location it would exist when opened using the [`open`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.open.html#numpy.lib.npyio.DataSource.open "numpy.lib.npyio.DataSource.open")
 method.

Parameters:

**path**str or pathlib.Path

Can be a local file or a remote URL.

Returns:

**out**str

Complete path, including the _DataSource_ destination directory.

Notes

The functionality is based on [`os.path.abspath`](https://docs.python.org/3/library/os.path.html#os.path.abspath "(in Python v3.14)")
.

On this page