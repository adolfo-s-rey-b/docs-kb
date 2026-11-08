[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.InvalidVersion.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.InvalidVersion.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.InvalidVersion.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.InvalidVersion.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.InvalidVersion.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.InvalidVersion.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.InvalidVersion.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.InvalidVersion.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.InvalidVersion.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.InvalidVersion.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.InvalidVersion.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.InvalidVersion.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.InvalidVersion.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.InvalidVersion.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.InvalidVersion[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.InvalidVersion.html#pandas-errors-invalidversion "Link to this heading")

====================================================================================================================================================================

exception pandas.errors.InvalidVersion[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.InvalidVersion.html#pandas.errors.InvalidVersion "Link to this definition")

An invalid version was found, users should refer to PEP 440.

The `InvalidVersion` exception is raised when a version string is improperly formatted. Pandas uses this exception to ensure that all version strings are PEP 440 compliant.

See also

`util.version.Version`

Class for handling and parsing version strings.

Examples

\>>> pd.util.version.Version("1.")
Traceback (most recent call last):
InvalidVersion: Invalid version: '1.'

Copy to clipboard

On this page