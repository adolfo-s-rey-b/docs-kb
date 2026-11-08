[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.index.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.index.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.index.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.index.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.index.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.index.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.index.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.index.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.index.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.index.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.index.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.index.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.index[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html#pandas-series-index "Link to this heading")

=========================================================================================================================================

Series.index[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html#pandas.Series.index "Link to this definition")

The index (axis labels) of the Series.

The index of a Series is used to label and identify each element of the underlying data. The index can be thought of as an immutable ordered set (technically a multi-set, as it may contain duplicate labels), and is used to index and align data in pandas.

Returns:

Index

The index labels of the Series.

See also

[`Series.reindex`](https://pandas.pydata.org/docs/reference/api/pandas.Series.reindex.html#pandas.Series.reindex "pandas.Series.reindex")

Conform Series to new index.

[`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")

The base pandas index type.

Notes

For more information on pandas indexing, see the [indexing user guide](https://pandas.pydata.org/docs/user_guide/indexing.html)
.

Examples

To create a Series with a custom index and view the index labels:

\>>> cities \= \['Kolkata', 'Chicago', 'Toronto', 'Lisbon'\]
\>>> populations \= \[14.85, 2.71, 2.93, 0.51\]
\>>> city\_series \= pd.Series(populations, index\=cities)
\>>> city\_series.index
Index(\['Kolkata', 'Chicago', 'Toronto', 'Lisbon'\], dtype='object')

Copy to clipboard

To change the index labels of an existing Series:

\>>> city\_series.index \= \['KOL', 'CHI', 'TOR', 'LIS'\]
\>>> city\_series.index
Index(\['KOL', 'CHI', 'TOR', 'LIS'\], dtype='object')

Copy to clipboard

On this page