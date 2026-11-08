[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.npyio.DataSource.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.npyio.DataSource.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.npyio.DataSource.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.npyio.DataSource.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.npyio.DataSource.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.npyio.DataSource.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.npyio.DataSource.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.npyio.DataSource.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.npyio.DataSource.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.npyio.DataSource.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.npyio.DataSource.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.npyio.DataSource.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.npyio.DataSource.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.npyio.DataSource.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.npyio.DataSource.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.npyio.DataSource.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.npyio.DataSource.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.npyio.DataSource.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.npyio.DataSource.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.npyio.DataSource.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.npyio.DataSource[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.html#numpy-lib-npyio-datasource "Link to this heading")

==================================================================================================================================================================

_class_ numpy.lib.npyio.DataSource(_destpath\='.'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_datasource.py#L195-L529)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.html#numpy.lib.npyio.DataSource "Link to this definition")

A generic data source file (file, http, ftp, …).

DataSources can be local files or remote files/URLs. The files may also be compressed or uncompressed. DataSource hides some of the low-level details of downloading the file, allowing you to simply pass in a valid file path (or URL) and obtain a file object.

Parameters:

**destpath**str or None, optional

Path to the directory where the source file gets downloaded to for use. If _destpath_ is None, a temporary directory will be created. The default path is the current directory.

Methods

|     |     |
| --- | --- |
| [`abspath`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.abspath.html#numpy.lib.npyio.DataSource.abspath "numpy.lib.npyio.DataSource.abspath")<br>(path) | Return absolute path of file in the DataSource directory. |
| [`exists`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.exists.html#numpy.lib.npyio.DataSource.exists "numpy.lib.npyio.DataSource.exists")<br>(path) | Test if path exists. |
| [`open`](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.DataSource.open.html#numpy.lib.npyio.DataSource.open "numpy.lib.npyio.DataSource.open")<br>(path\[, mode, encoding, newline\]) | Open and return file-like object. |

Notes

URLs require a scheme string (`http://`) to be used, without it they will fail:

\>>> repos \= np.lib.npyio.DataSource()
\>>> repos.exists('www.google.com/index.html')
False
\>>> repos.exists('http://www.google.com/index.html')
True

Copy to clipboard

Temporary directories are deleted when the DataSource is deleted.

Examples

Try it in your browser!

\>>> ds \= np.lib.npyio.DataSource('/home/guido')
\>>> urlname \= 'http://www.google.com/'
\>>> gfile \= ds.open('http://www.google.com/')
\>>> ds.abspath(urlname)
'/home/guido/www.google.com/index.html'

\>>> ds \= np.lib.npyio.DataSource(None)  \# use with temporary file
\>>> ds.open('/home/guido/foobar.txt')
<open file '/home/guido.foobar.txt', mode 'r' at 0x91d4430>
\>>> ds.abspath('/home/guido/foobar.txt')
'/tmp/.../home/guido/foobar.txt'

Copy to clipboard

Go BackOpen In Tab

On this page