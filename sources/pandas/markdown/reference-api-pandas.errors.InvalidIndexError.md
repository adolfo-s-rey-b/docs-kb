[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.InvalidIndexError.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.InvalidIndexError.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.InvalidIndexError.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.InvalidIndexError.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.InvalidIndexError.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.InvalidIndexError.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.InvalidIndexError.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.InvalidIndexError.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.InvalidIndexError.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.InvalidIndexError.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.InvalidIndexError.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.InvalidIndexError.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.InvalidIndexError.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.InvalidIndexError.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.InvalidIndexError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.InvalidIndexError.html#pandas-errors-invalidindexerror "Link to this heading")

=============================================================================================================================================================================

exception pandas.errors.InvalidIndexError[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L612-L632)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.InvalidIndexError.html#pandas.errors.InvalidIndexError "Link to this definition")

Exception raised when attempting to use an invalid index key.

This exception is triggered when a user attempts to access or manipulate data in a pandas DataFrame or Series using an index key that is not valid for the given object. This may occur in cases such as using a malformed slice, a mismatched key for a `MultiIndex`, or attempting to access an index element that does not exist.

See also

`MultiIndex`

A multi-level, or hierarchical, index object for pandas objects.

Examples

\>>> df \= pd.DataFrame({"a": \[1, 2\], "b": \[3, 4\]})
\>>> df\[("a", slice(None))\]
Traceback (most recent call last):
InvalidIndexError: ('a', slice(None, None, None))

Copy to clipboard

On this page