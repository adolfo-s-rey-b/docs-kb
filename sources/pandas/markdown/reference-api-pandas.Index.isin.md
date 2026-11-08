[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.isin.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.isin.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.isin.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.isin.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.isin.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.isin.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.isin.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.isin.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.isin.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.isin.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.isin.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.isin.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.isin.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.isin.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.isin[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.isin.html#pandas-index-isin "Link to this heading")

===================================================================================================================================

Index.isin(_values_, _level\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L7005-L7078)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.isin.html#pandas.Index.isin "Link to this definition")

Return a boolean array where the index values are in values.

Compute boolean array of whether each index value is found in the passed set of values. The length of the returned boolean array matches the length of the index.

Parameters:

**values**set or list-like

Sought values.

**level**str or int, optional

Name or position of the index level to use (if the index is a MultiIndex).

Returns:

np.ndarray\[bool\]

NumPy array of boolean values.

See also

[`Series.isin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html#pandas.Series.isin "pandas.Series.isin")

Same for Series.

[`DataFrame.isin`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html#pandas.DataFrame.isin "pandas.DataFrame.isin")

Same method for DataFrames.

Notes

In the case of MultiIndex you must either specify values as a list-like object containing tuples that are the same length as the number of levels, or specify level. Otherwise it will raise a `ValueError`.

If level is specified:

*   if it is the name of one _and only one_ index level, use that level;
    
*   otherwise it should be a number indicating level position.
    

Examples

\>>> idx \= pd.Index(\[1, 2, 3\])
\>>> idx
Index(\[1, 2, 3\], dtype='int64')

Copy to clipboard

Check whether each index value in a list of values.

\>>> idx.isin(\[1, 4\])
array(\[ True, False, False\])

Copy to clipboard

\>>> midx \= pd.MultiIndex.from\_arrays(
...     \[\[1, 2, 3\], \["red", "blue", "green"\]\], names\=\["number", "color"\]
... )
\>>> midx
MultiIndex(\[(1,   'red'),\
            (2,  'blue'),\
            (3, 'green')\],
           names=\['number', 'color'\])

Copy to clipboard

Check whether the strings in the ‘color’ level of the MultiIndex are in a list of colors.

\>>> midx.isin(\["red", "orange", "yellow"\], level\="color")
array(\[ True, False, False\])

Copy to clipboard

To check across the levels of a MultiIndex, pass a list of tuples:

\>>> midx.isin(\[(1, "red"), (3, "red")\])
array(\[ True, False, False\])

Copy to clipboard

On this page