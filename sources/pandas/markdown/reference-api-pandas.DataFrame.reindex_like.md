[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex_like.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.reindex_like.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex_like.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.reindex_like.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.reindex_like.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.reindex_like.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.reindex_like.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.reindex_like.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.reindex_like.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.reindex_like.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.reindex_like.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.reindex_like.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.reindex_like.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.reindex_like.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.reindex\_like[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex_like.html#pandas-dataframe-reindex-like "Link to this heading")

========================================================================================================================================================================

DataFrame.reindex\_like(_other_, _method\=None_, _copy\=<no\_default>_, _limit\=None_, _tolerance\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L4522-L4647)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex_like.html#pandas.DataFrame.reindex_like "Link to this definition")

Return an object with matching indices as other object.

Conform the object to the same index on all axes. Optional filling logic, placing NaN in locations having no value in the previous index. A new object is produced unless the new index is equivalent to the current one and copy=False.

Parameters:

**other**Object of the same data type

Its row and column indices are used to define the new indices of this object.

**method**{None, ‘backfill’/’bfill’, ‘pad’/’ffill’, ‘nearest’}

Method to use for filling holes in reindexed DataFrame. Please note: this is only applicable to DataFrames/Series with a monotonically increasing/decreasing index.

Deprecated since version 3.0.0.

*   None (default): don’t fill gaps
    
*   pad / ffill: propagate last valid observation forward to next valid
    
*   backfill / bfill: use next valid observation to fill gap
    
*   nearest: use nearest valid observations to fill gap.
    

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

**limit**int, default None

Maximum number of consecutive labels to fill for inexact matches.

**tolerance**optional

Maximum distance between original and new labels for inexact matches. The values of the index at the matching locations must satisfy the equation `abs(index[indexer] - target) <= tolerance`.

Tolerance may be a scalar value, which applies the same tolerance to all values, or list-like, which applies variable tolerance per element. List-like includes list, tuple, array, Series, and must be the same size as the index and its dtype must exactly match the index’s type.

Returns:

Series or DataFrame

Same type as caller, but with changed indices on each axis.

See also

[`DataFrame.set_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index "pandas.DataFrame.set_index")

Set row labels.

[`DataFrame.reset_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html#pandas.DataFrame.reset_index "pandas.DataFrame.reset_index")

Remove row labels or move them to new columns.

[`DataFrame.reindex`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html#pandas.DataFrame.reindex "pandas.DataFrame.reindex")

Change to new indices or expand indices.

Notes

Same as calling `.reindex(index=other.index, columns=other.columns,...)`.

Examples

\>>> df1 \= pd.DataFrame(
...     \[\
...         \[24.3, 75.7, "high"\],\
...         \[31, 87.8, "high"\],\
...         \[22, 71.6, "medium"\],\
...         \[35, 95, "medium"\],\
...     \],
...     columns\=\["temp\_celsius", "temp\_fahrenheit", "windspeed"\],
...     index\=pd.date\_range(start\="2014-02-12", end\="2014-02-15", freq\="D"),
... )

Copy to clipboard

\>>> df1
            temp\_celsius  temp\_fahrenheit windspeed
2014-02-12          24.3             75.7      high
2014-02-13          31.0             87.8      high
2014-02-14          22.0             71.6    medium
2014-02-15          35.0             95.0    medium

Copy to clipboard

\>>> df2 \= pd.DataFrame(
...     \[\[28, "low"\], \[30, "low"\], \[35.1, "medium"\]\],
...     columns\=\["temp\_celsius", "windspeed"\],
...     index\=pd.DatetimeIndex(\["2014-02-12", "2014-02-13", "2014-02-15"\]),
... )

Copy to clipboard

\>>> df2
            temp\_celsius windspeed
2014-02-12          28.0       low
2014-02-13          30.0       low
2014-02-15          35.1    medium

Copy to clipboard

\>>> df2.reindex\_like(df1)
            temp\_celsius  temp\_fahrenheit windspeed
2014-02-12          28.0              NaN       low
2014-02-13          30.0              NaN       low
2014-02-14           NaN              NaN       NaN
2014-02-15          35.1              NaN    medium

Copy to clipboard

On this page