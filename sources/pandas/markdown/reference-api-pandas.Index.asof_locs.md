[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.asof_locs.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.asof_locs.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.asof_locs.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.asof_locs.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.asof_locs.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.asof_locs.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.asof_locs.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.asof_locs.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.asof_locs.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.asof_locs.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.asof_locs.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.asof_locs.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.asof_locs.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.asof_locs.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.asof\_locs[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.asof_locs.html#pandas-index-asof-locs "Link to this heading")

===================================================================================================================================================

Index.asof\_locs(_where_, _mask_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L6079-L6144)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.asof_locs.html#pandas.Index.asof_locs "Link to this definition")

Return the locations (indices) of labels in the index.

As in the [`pandas.Index.asof()`](https://pandas.pydata.org/docs/reference/api/pandas.Index.asof.html#pandas.Index.asof "pandas.Index.asof")
, if the label (a particular entry in `where`) is not in the index, the latest index label up to the passed label is chosen and its index returned.

If all of the labels in the index are later than a label in `where`, -1 is returned.

`mask` is used to ignore `NA` values in the index during calculation.

Parameters:

**where**Index

An Index consisting of an array of timestamps.

**mask**np.ndarray\[bool\]

Array of booleans denoting where values in the original data are not `NA`.

Returns:

np.ndarray\[np.intp\]

An array of locations (indices) of the labels from the index which correspond to the return values of [`pandas.Index.asof()`](https://pandas.pydata.org/docs/reference/api/pandas.Index.asof.html#pandas.Index.asof "pandas.Index.asof")
 for every element in `where`.

See also

[`Index.asof`](https://pandas.pydata.org/docs/reference/api/pandas.Index.asof.html#pandas.Index.asof "pandas.Index.asof")

Return the label from the index, or, if not present, the previous one.

Examples

\>>> idx \= pd.date\_range("2023-06-01", periods\=3, freq\="D")
\>>> where \= pd.DatetimeIndex(
...     \["2023-05-30 00:12:00", "2023-06-01 00:00:00", "2023-06-02 23:59:59"\]
... )
\>>> mask \= np.ones(3, dtype\=bool)
\>>> idx.asof\_locs(where, mask)
array(\[-1,  0,  1\])

Copy to clipboard

We can use `mask` to ignore certain values in the index during calculation.

\>>> mask\[1\] \= False
\>>> idx.asof\_locs(where, mask)
array(\[-1,  0,  0\])

Copy to clipboard

On this page