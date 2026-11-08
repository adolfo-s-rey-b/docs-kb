[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.asof.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.asof.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.asof.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.asof.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.asof.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.asof.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.asof.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.asof.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.asof.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.asof.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.asof.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.asof.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.asof.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.asof.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.asof[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.asof.html#pandas-index-asof "Link to this heading")

===================================================================================================================================

final Index.asof(_label_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L6004-L6077)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.asof.html#pandas.Index.asof "Link to this definition")

Return the label from the index, or, if not present, the previous one.

Assuming that the index is sorted, return the passed index label if it is in the index, or return the previous index label if the passed one is not in the index.

Parameters:

**label**object

The label up to which the method returns the latest index label.

Returns:

object

The passed label if it is in the index. The previous label if the passed label is not in the sorted index or NaN if there is no such label.

See also

[`Series.asof`](https://pandas.pydata.org/docs/reference/api/pandas.Series.asof.html#pandas.Series.asof "pandas.Series.asof")

Return the latest value in a Series up to the passed index.

[`merge_asof`](https://pandas.pydata.org/docs/reference/api/pandas.merge_asof.html#pandas.merge_asof "pandas.merge_asof")

Perform an asof merge (similar to left join but it matches on nearest key rather than equal key).

[`Index.get_loc`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_loc.html#pandas.Index.get_loc "pandas.Index.get_loc")

An asof is a thin wrapper around get\_loc with method=’pad’.

Examples

Index.asof returns the latest index label up to the passed label.

\>>> idx \= pd.Index(\["2013-12-31", "2014-01-02", "2014-01-03"\])
\>>> idx.asof("2014-01-01")
'2013-12-31'

Copy to clipboard

If the label is in the index, the method returns the passed label.

\>>> idx.asof("2014-01-02")
'2014-01-02'

Copy to clipboard

If all of the labels in the index are later than the passed label, NaN is returned.

\>>> idx.asof("1999-01-02")
nan

Copy to clipboard

If the index is not sorted, an error is raised.

\>>> idx\_not\_sorted \= pd.Index(\["2013-12-31", "2015-01-02", "2014-01-03"\])
\>>> idx\_not\_sorted.asof("2013-12-31")
Traceback (most recent call last):
ValueError: index must be monotonic increasing or decreasing

Copy to clipboard

On this page