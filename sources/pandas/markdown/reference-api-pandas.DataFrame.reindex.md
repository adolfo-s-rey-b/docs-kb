[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.reindex.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.reindex.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.reindex.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.reindex.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.reindex.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.reindex.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.reindex.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.reindex.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.reindex.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.reindex.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.reindex.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.reindex.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.reindex[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html#pandas-dataframe-reindex "Link to this heading")

========================================================================================================================================================

DataFrame.reindex(_labels\=None_, _\*_, _index\=None_, _columns\=None_, _axis\=None_, _method\=None_, _copy\=<no\_default>_, _level\=None_, _fill\_value\=nan_, _limit\=None_, _tolerance\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L6507-L6765)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html#pandas.DataFrame.reindex "Link to this definition")

Conform DataFrame to new index with optional filling logic.

Places NA/NaN in locations having no value in the previous index. A new object is produced unless the new index is equivalent to the current one and `copy=False`.

Parameters:

**labels**array-like, optional

New labels / index to conform the axis specified by ‘axis’ to.

**index**array-like, optional

New labels for the index. Preferably an Index object to avoid duplicating data.

**columns**array-like, optional

New labels for the columns. Preferably an Index object to avoid duplicating data.

**axis**int or str, optional

Axis to target. Can be either the axis name (‘index’, ‘columns’) or number (0, 1).

**method**{None, ‘backfill’/’bfill’, ‘pad’/’ffill’, ‘nearest’}

Method to use for filling holes in reindexed DataFrame. Please note: this is only applicable to DataFrames/Series with a monotonically increasing/decreasing index. Filling is based on the position of each new label relative to the existing labels, and applies to both the index and the columns. For example, with `method='ffill'` and a monotonically increasing index, a new label is filled from the nearest existing label that sorts before it, so a new column whose label falls between two existing columns takes its values from the preceding column.

*   None (default): don’t fill gaps
    
*   pad / ffill: Propagate last valid observation forward to next valid.
    
*   backfill / bfill: Use next valid observation to fill gap.
    
*   nearest: Use nearest valid observations to fill gap.
    

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

**level**int or name

Match index values on the specified level of a MultiIndex. The MultiIndex may be on either the calling object or the target index; using `level` when both are MultiIndexes is ambiguous and raises a `TypeError`. The new labels are aligned against the values of that single level while the other levels are left unchanged; passing a flat index with `level` does not form the Cartesian product of the remaining levels. See [Advanced reindexing and alignment](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-advanced-reindex)
 for the intended use.

**fill\_value**scalar, default np.nan

Value to use for missing values. Defaults to NaN, but can be any “compatible” value.

**limit**int, default None

Maximum number of consecutive elements to forward or backward fill.

**tolerance**optional

Maximum distance between original and new labels for inexact matches. The values of the index at the matching locations most satisfy the equation `abs(index[indexer] - target) <= tolerance`.

Tolerance may be a scalar value, which applies the same tolerance to all values, or list-like, which applies variable tolerance per element. List-like includes list, tuple, array, Series, and must be the same size as the index and its dtype must exactly match the index’s type.

Returns:

DataFrame

DataFrame with changed index.

See also

[`DataFrame.set_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index "pandas.DataFrame.set_index")

Set row labels.

[`DataFrame.reset_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html#pandas.DataFrame.reset_index "pandas.DataFrame.reset_index")

Remove row labels or move them to new columns.

[`DataFrame.reindex_like`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex_like.html#pandas.DataFrame.reindex_like "pandas.DataFrame.reindex_like")

Change to same indices as other DataFrame.

Examples

`DataFrame.reindex` supports two calling conventions

*   `(index=index_labels, columns=column_labels, ...)`
    
*   `(labels, axis={'index', 'columns'}, ...)`
    

We _highly_ recommend using keyword arguments to clarify your intent.

Create a DataFrame with some fictional data.

\>>> index \= \["Firefox", "Chrome", "Safari", "IE10", "Konqueror"\]
\>>> columns \= \["http\_status", "response\_time"\]
\>>> df \= pd.DataFrame(
...     \[\[200, 0.04\], \[200, 0.02\], \[404, 0.07\], \[404, 0.08\], \[301, 1.0\]\],
...     columns\=columns,
...     index\=index,
... )
\>>> df
           http\_status  response\_time
Firefox            200           0.04
Chrome             200           0.02
Safari             404           0.07
IE10               404           0.08
Konqueror          301           1.00

Copy to clipboard

Create a new index and reindex the DataFrame. By default values in the new index that do not have corresponding records in the DataFrame are assigned `NaN`.

\>>> new\_index \= \["Safari", "Iceweasel", "Comodo Dragon", "IE10", "Chrome"\]
\>>> df.reindex(new\_index)
               http\_status  response\_time
Safari               404.0           0.07
Iceweasel              NaN            NaN
Comodo Dragon          NaN            NaN
IE10                 404.0           0.08
Chrome               200.0           0.02

Copy to clipboard

We can fill in the missing values by passing a value to the keyword `fill_value`. Because the index is not monotonically increasing or decreasing, we cannot use arguments to the keyword `method` to fill the `NaN` values.

\>>> df.reindex(new\_index, fill\_value\=0)
               http\_status  response\_time
Safari                 404           0.07
Iceweasel                0           0.00
Comodo Dragon            0           0.00
IE10                   404           0.08
Chrome                 200           0.02

Copy to clipboard

We can also reindex the columns.

\>>> df.reindex(columns\=\["http\_status", "user\_agent"\])
           http\_status  user\_agent
Firefox            200         NaN
Chrome             200         NaN
Safari             404         NaN
IE10               404         NaN
Konqueror          301         NaN

Copy to clipboard

Or we can use “axis-style” keyword arguments

\>>> df.reindex(\["http\_status", "user\_agent"\], axis\="columns")
           http\_status  user\_agent
Firefox            200         NaN
Chrome             200         NaN
Safari             404         NaN
IE10               404         NaN
Konqueror          301         NaN

Copy to clipboard

To further illustrate the filling functionality in `reindex`, we will create a DataFrame with a monotonically increasing index (for example, a sequence of dates).

\>>> date\_index \= pd.date\_range("1/1/2010", periods\=6, freq\="D")
\>>> df2 \= pd.DataFrame(
...     {"prices": \[100, 101, np.nan, 100, 89, 88\]}, index\=date\_index
... )
\>>> df2
            prices
2010-01-01   100.0
2010-01-02   101.0
2010-01-03     NaN
2010-01-04   100.0
2010-01-05    89.0
2010-01-06    88.0

Copy to clipboard

Suppose we decide to expand the DataFrame to cover a wider date range.

\>>> date\_index2 \= pd.date\_range("12/29/2009", periods\=10, freq\="D")
\>>> df2.reindex(date\_index2)
            prices
2009-12-29     NaN
2009-12-30     NaN
2009-12-31     NaN
2010-01-01   100.0
2010-01-02   101.0
2010-01-03     NaN
2010-01-04   100.0
2010-01-05    89.0
2010-01-06    88.0
2010-01-07     NaN

Copy to clipboard

The index entries that did not have a value in the original data frame (for example, ‘2009-12-29’) are by default filled with `NaN`. If desired, we can fill in the missing values using one of several options.

For example, to back-propagate the last valid value to fill the `NaN` values, pass `bfill` as an argument to the `method` keyword.

\>>> df2.reindex(date\_index2, method\="bfill")
            prices
2009-12-29   100.0
2009-12-30   100.0
2009-12-31   100.0
2010-01-01   100.0
2010-01-02   101.0
2010-01-03     NaN
2010-01-04   100.0
2010-01-05    89.0
2010-01-06    88.0
2010-01-07     NaN

Copy to clipboard

Please note that the `NaN` value present in the original DataFrame (at index value 2010-01-03) will not be filled by any of the value propagation schemes. This is because filling while reindexing does not look at DataFrame values, but only compares the original and desired indexes. If you do want to fill in the `NaN` values present in the original DataFrame, use the `fillna()` method.

Because `method="bfill"` fills each new label from the next entry present in the original index, the trailing entry at 2010-01-07 stays `NaN`: there is no original index entry after it. Conversely, `method="ffill"` would leave the leading entries (before the first original index entry) unfilled.

See the [user guide](https://pandas.pydata.org/docs/user_guide/basics.html#basics-reindexing)
 for more.

On this page