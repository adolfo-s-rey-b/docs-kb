[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.set\_index[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html#pandas-dataframe-set-index "Link to this heading")

===============================================================================================================================================================

DataFrame.set\_index(_keys_, _\*_, _drop\=True_, _append\=False_, _inplace\=<no\_default>_, _verify\_integrity\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L7702-L7963)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index "Link to this definition")

Set the DataFrame index using existing columns.

Set the DataFrame index (row labels) using one or more existing columns or arrays (of the correct length). The index can replace the existing index or expand on it.

Parameters:

**keys**label or array-like or list of labels/arrays

This parameter can be either a single column key, a single array of the same length as the calling DataFrame, or a list containing an arbitrary combination of column keys and arrays. Here, “array” encompasses [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
, [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
, `np.ndarray`, and instances of [`Iterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.15)")
.

**drop**bool, default True

Delete columns to be used as the new index.

**append**bool, default False

Whether to append columns to existing index. Setting to True will add the new columns to existing index. When set to False, the current index will be dropped from the DataFrame.

**inplace**bool, default False

Whether to modify the DataFrame rather than creating a new one.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

**verify\_integrity**bool, default False

Check the new index for duplicates. Otherwise defer the check until necessary. Setting to False will improve the performance of this method.

Deprecated since version 3.0.0: The `verify_integrity` keyword is deprecated and will be removed in a future version. Check `result.index.is_unique` directly instead.

Returns:

DataFrame or None

Changed row labels or None if `inplace=True`.

See also

[`DataFrame.reset_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html#pandas.DataFrame.reset_index "pandas.DataFrame.reset_index")

Opposite of set\_index.

[`DataFrame.reindex`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html#pandas.DataFrame.reindex "pandas.DataFrame.reindex")

Change to new indices or expand indices.

[`DataFrame.reindex_like`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex_like.html#pandas.DataFrame.reindex_like "pandas.DataFrame.reindex_like")

Change to same indices as other DataFrame.

Notes

Columns and Series do not store a `freq`, so a [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
 or [`TimedeltaIndex`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html#pandas.TimedeltaIndex "pandas.TimedeltaIndex")
 created from a column has `freq=None`; set `.index.freq` on the result to restore it. Passing the index directly as `keys` keeps its `freq`.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "month": \[1, 4, 7, 10\],
...         "year": \[2012, 2014, 2013, 2014\],
...         "sale": \[55, 40, 84, 31\],
...     }
... )
\>>> df
   month  year  sale
0      1  2012    55
1      4  2014    40
2      7  2013    84
3     10  2014    31

Copy to clipboard

Set the index to become the ‘month’ column:

\>>> df.set\_index("month")
       year  sale
month
1      2012    55
4      2014    40
7      2013    84
10     2014    31

Copy to clipboard

Create a MultiIndex using columns ‘year’ and ‘month’:

\>>> df.set\_index(\["year", "month"\])
            sale
year  month
2012  1     55
2014  4     40
2013  7     84
2014  10    31

Copy to clipboard

Create a MultiIndex using an Index and a column:

\>>> df.set\_index(\[pd.Index(\[1, 2, 3, 4\]), "year"\])
         month  sale
   year
1  2012  1      55
2  2014  4      40
3  2013  7      84
4  2014  10     31

Copy to clipboard

Create a MultiIndex using two Series:

\>>> s \= pd.Series(\[1, 2, 3, 4\])
\>>> df.set\_index(\[s, s\*\*2\])
      month  year  sale
1 1       1  2012    55
2 4       4  2014    40
3 9       7  2013    84
4 16     10  2014    31

Copy to clipboard

Append a column to the existing index:

\>>> df \= df.set\_index("month")
\>>> df.set\_index("year", append\=True)
              sale
month  year
1      2012    55
4      2014    40
7      2013    84
10     2014    31

Copy to clipboard

\>>> df.set\_index("year", append\=False)
       sale
year
2012    55
2014    40
2013    84
2014    31

Copy to clipboard

On this page