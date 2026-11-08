[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.unique.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.unique.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.unique.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.unique.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.unique.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.unique.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.unique.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.unique.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.unique.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.unique.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.unique.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.unique.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.unique[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html#pandas-series-unique "Link to this heading")

============================================================================================================================================

Series.unique()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L2452-L2518)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html#pandas.Series.unique "Link to this definition")

Return unique values of Series object.

Uniques are returned in order of appearance. Hash table-based unique, therefore does NOT sort.

Returns:

ndarray or ExtensionArray

The unique values returned as a NumPy array. See Notes.

See also

[`Series.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop_duplicates.html#pandas.Series.drop_duplicates "pandas.Series.drop_duplicates")

Return Series with duplicate values removed.

[`unique`](https://pandas.pydata.org/docs/reference/api/pandas.unique.html#pandas.unique "pandas.unique")

Top-level unique method for any 1-d array-like object.

[`Index.unique`](https://pandas.pydata.org/docs/reference/api/pandas.Index.unique.html#pandas.Index.unique "pandas.Index.unique")

Return Index with unique values from an Index object.

Notes

Returns the unique values as a NumPy array. In case of an extension-array backed Series, a new [`ExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray "pandas.api.extensions.ExtensionArray")
 of that type with just the unique values is returned. This includes

> *   Categorical
>     
> *   Period
>     
> *   Datetime with Timezone
>     
> *   Datetime without Timezone
>     
> *   Timedelta
>     
> *   Interval
>     
> *   Sparse
>     
> *   IntegerNA
>     
> *   String
>     

See Examples section.

Examples

\>>> pd.Series(\[2, 1, 3, 3\], name\="A").unique()
array(\[2, 1, 3\])

Copy to clipboard

\>>> pd.Series(\[pd.Timestamp("2016-01-01") for \_ in range(3)\]).unique()
<DatetimeArray>
\['2016-01-01 00:00:00'\]
Length: 1, dtype: datetime64\[us\]

Copy to clipboard

\>>> pd.Series(
...     \[pd.Timestamp("2016-01-01", tz\="US/Eastern") for \_ in range(3)\]
... ).unique()
<DatetimeArray>
\['2016-01-01 00:00:00-05:00'\]
Length: 1, dtype: datetime64\[us, US/Eastern\]

Copy to clipboard

A Categorical will return categories in the order of appearance and with the same dtype.

\>>> pd.Series(pd.Categorical(list("baabc"))).unique()
\['b', 'a', 'c'\]
Categories (3, str): \['a', 'b', 'c'\]
\>>> pd.Series(
...     pd.Categorical(list("baabc"), categories\=list("abc"), ordered\=True)
... ).unique()
\['b', 'a', 'c'\]
Categories (3, str): \['a' < 'b' < 'c'\]

Copy to clipboard

On this page