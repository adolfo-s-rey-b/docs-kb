[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.replace.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.replace.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.replace.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.replace.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.replace.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.replace.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.replace.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.replace.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.replace.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.replace.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.replace.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.replace.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.replace.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.replace.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.replace[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.replace.html#pandas-index-replace "Link to this heading")

============================================================================================================================================

Index.replace(_to\_replace\=None_, _value\=<no\_default>_, _regex\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L6925-L6969)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.replace.html#pandas.Index.replace "Link to this definition")

Replace values in the Index.

Replace values given in to\_replace with value. Values of the Index that are not in to\_replace are left unchanged.

Parameters:

**to\_replace**str, regex, list, dict, Series, scalar, or None

The value(s) to be replaced. If a dict is provided, value must be omitted.

**value**scalar, dict, list, str, regex, default None

The value to replace occurrences of to\_replace with.

**regex**bool or same types as to\_replace, default False

Whether to interpret to\_replace and/or value as regular expressions.

Returns:

Index

Index with replaced values.

See also

[`Series.replace`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html#pandas.Series.replace "pandas.Series.replace")

Replace values in a Series.

[`DataFrame.replace`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html#pandas.DataFrame.replace "pandas.DataFrame.replace")

Replace values in a DataFrame.

Examples

\>>> idx \= pd.Index(\[1, 2, 3, 4, 5\])
\>>> idx.replace(3, 30)
Index(\[1, 2, 30, 4, 5\], dtype='int64')

Copy to clipboard

On this page