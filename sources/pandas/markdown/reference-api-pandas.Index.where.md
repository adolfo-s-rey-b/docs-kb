[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.where.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.where.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.where.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.where.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.where.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.where.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.where.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.where.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.where.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.where.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.where.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.where.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.where.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.where.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.where[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.where.html#pandas-index-where "Link to this heading")

======================================================================================================================================

final Index.where(_cond_, _other\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L5507-L5560)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.where.html#pandas.Index.where "Link to this definition")

Replace values where the condition is False.

The replacement is taken from other.

Parameters:

**cond**bool array-like with the same length as self

Condition to select the values on.

**other**scalar, or array-like, default None

Replacement if the condition is False.

Returns:

pandas.Index

A copy of self with values replaced from other where the condition is False.

See also

[`Series.where`](https://pandas.pydata.org/docs/reference/api/pandas.Series.where.html#pandas.Series.where "pandas.Series.where")

Same method for Series.

[`DataFrame.where`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.where.html#pandas.DataFrame.where "pandas.DataFrame.where")

Same method for DataFrame.

Examples

\>>> idx \= pd.Index(\["car", "bike", "train", "tractor"\])
\>>> idx
Index(\['car', 'bike', 'train', 'tractor'\], dtype='str')
\>>> idx.where(idx.isin(\["car", "train"\]), "other")
Index(\['car', 'other', 'train', 'other'\], dtype='str')

Copy to clipboard

On this page