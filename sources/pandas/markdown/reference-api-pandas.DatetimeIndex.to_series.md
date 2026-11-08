[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_series.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeIndex.to_series.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_series.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeIndex.to_series.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeIndex.to_series.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeIndex.to_series.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeIndex.to_series.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeIndex.to_series.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeIndex.to_series.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeIndex.to_series.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeIndex.to_series.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeIndex.to_series.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeIndex.to_series.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeIndex.to_series.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.to\_series[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_series.html#pandas-datetimeindex-to-series "Link to this heading")

===========================================================================================================================================================================

DatetimeIndex.to\_series(_index\=None_, _name\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L1700-L1764)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_series.html#pandas.DatetimeIndex.to_series "Link to this definition")

Create a Series with both index and values equal to the index keys.

Useful with map for returning an indexer based on an index.

Parameters:

**index**Index or array-like, optional

Index of resulting Series. If None, defaults to original index.

**name**str, optional

Name of resulting Series. If None, defaults to name of original index.

Returns:

Series

The dtype will be based on the type of the Index values.

See also

[`Index.to_frame`](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_frame.html#pandas.Index.to_frame "pandas.Index.to_frame")

Convert an Index to a DataFrame.

[`Series.to_frame`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html#pandas.Series.to_frame "pandas.Series.to_frame")

Convert Series to DataFrame.

Examples

\>>> idx \= pd.Index(\["Ant", "Bear", "Cow"\], name\="animal")

Copy to clipboard

By default, the original index and original name is reused.

\>>> idx.to\_series()
animal
Ant      Ant
Bear    Bear
Cow      Cow
Name: animal, dtype: str

Copy to clipboard

To enforce a new index, specify new labels to `index`:

\>>> idx.to\_series(index\=\[0, 1, 2\])
0     Ant
1    Bear
2     Cow
Name: animal, dtype: str

Copy to clipboard

To override the name of the resulting column, specify `name`:

\>>> idx.to\_series(name\="zoo")
animal
Ant      Ant
Bear    Bear
Cow      Cow
Name: zoo, dtype: str

Copy to clipboard

On this page