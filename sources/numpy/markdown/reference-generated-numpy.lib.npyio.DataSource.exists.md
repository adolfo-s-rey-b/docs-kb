[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.exists.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.npyio.DataSource.exists.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.npyio.DataSource.exists.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.npyio.DataSource.exists[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.exists.html#numpy-lib-npyio-datasource-exists "Link to this heading")

=======================================================================================================================================================================================

method

lib.npyio.DataSource.exists(_path_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_datasource.py#L427-L481)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.exists.html#numpy.lib.npyio.DataSource.exists "Link to this definition")

Test if path exists.

Test if _path_ exists as (and in this order):

*   a local file.
    
*   a remote URL that has been downloaded and stored locally in the _DataSource_ directory.
    
*   a remote URL that has not been downloaded, but is valid and accessible.
    

Parameters:

**path**str or pathlib.Path

Can be a local file or a remote URL.

Returns:

**out**bool

True if _path_ exists.

Notes

When _path_ is a URL, [`exists`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.exists.html#numpy.lib.npyio.DataSource.exists "numpy.lib.npyio.DataSource.exists")
 will return True if it’s either stored locally in the _DataSource_ directory, or is a valid remote URL. _DataSource_ does not discriminate between the two, the file is accessible if it exists in either location.

On this page