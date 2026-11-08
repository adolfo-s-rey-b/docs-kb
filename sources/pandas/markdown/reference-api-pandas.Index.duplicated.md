[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.duplicated.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.duplicated.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.duplicated.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.duplicated.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.duplicated.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.duplicated.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.duplicated.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.duplicated.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.duplicated.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.duplicated.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.duplicated.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.duplicated.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.duplicated.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.duplicated.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.duplicated[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.duplicated.html#pandas-index-duplicated "Link to this heading")

=====================================================================================================================================================

Index.duplicated(_keep\='first'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L3055-L3113)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.duplicated.html#pandas.Index.duplicated "Link to this definition")

Indicate duplicate index values.

Duplicated values are indicated as `True` values in the resulting array. Either all duplicates, all except the first, or all except the last occurrence of duplicates can be indicated.

Parameters:

**keep**{‘first’, ‘last’, False}, default ‘first’

The value or values in a set of duplicates to mark as missing.

*   ‘first’ : Mark duplicates as `True` except for the first occurrence.
    
*   ‘last’ : Mark duplicates as `True` except for the last occurrence.
    
*   `False` : Mark all duplicates as `True`.
    

Returns:

np.ndarray\[bool\]

A numpy array of boolean values indicating duplicate index values.

See also

[`Series.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.Series.duplicated.html#pandas.Series.duplicated "pandas.Series.duplicated")

Equivalent method on pandas.Series.

[`DataFrame.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html#pandas.DataFrame.duplicated "pandas.DataFrame.duplicated")

Equivalent method on pandas.DataFrame.

[`Index.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Index.drop_duplicates.html#pandas.Index.drop_duplicates "pandas.Index.drop_duplicates")

Remove duplicate values from Index.

Examples

By default, for each set of duplicated values, the first occurrence is set to False and all others to True:

\>>> idx \= pd.Index(\["llama", "cow", "llama", "beetle", "llama"\])
\>>> idx.duplicated()
array(\[False, False,  True, False,  True\])

Copy to clipboard

which is equivalent to

\>>> idx.duplicated(keep\="first")
array(\[False, False,  True, False,  True\])

Copy to clipboard

By using ‘last’, the last occurrence of each set of duplicated values is set on False and all others on True:

\>>> idx.duplicated(keep\="last")
array(\[ True, False,  True, False, False\])

Copy to clipboard

By setting keep on `False`, all duplicates are True:

\>>> idx.duplicated(keep\=False)
array(\[ True, False,  True, False,  True\])

Copy to clipboard

On this page