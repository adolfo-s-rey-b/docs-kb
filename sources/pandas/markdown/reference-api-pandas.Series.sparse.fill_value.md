[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.fill_value.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.sparse.fill_value.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.fill_value.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.sparse.fill_value.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.sparse.fill_value.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.sparse.fill_value.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.sparse.fill_value.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.sparse.fill_value.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.sparse.fill_value.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.sparse.fill_value.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.sparse.fill_value.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.sparse.fill_value.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.sparse.fill_value.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.sparse.fill_value.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.sparse.fill\_value[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.fill_value.html#pandas-series-sparse-fill-value "Link to this heading")

==============================================================================================================================================================================

Series.sparse.fill\_value[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.fill_value.html#pandas.Series.sparse.fill_value "Link to this definition")

Elements in data that are fill\_value are not stored.

For memory savings, this should be the most common value in the array.

See also

[`SparseDtype`](https://pandas.pydata.org/docs/reference/api/pandas.SparseDtype.html#pandas.SparseDtype "pandas.SparseDtype")

Dtype for data stored in `SparseArray`.

[`Series.value_counts`](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html#pandas.Series.value_counts "pandas.Series.value_counts")

Return a Series containing counts of unique values.

[`Series.fillna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html#pandas.Series.fillna "pandas.Series.fillna")

Fill NA/NaN in a Series with a specified value.

Examples

\>>> ser \= pd.Series(\[0, 0, 2, 2, 2\], dtype\="Sparse\[int\]")
\>>> ser.sparse.fill\_value
0
\>>> spa\_dtype \= pd.SparseDtype(dtype\=np.int32, fill\_value\=2)
\>>> ser \= pd.Series(\[0, 0, 2, 2, 2\], dtype\=spa\_dtype)
\>>> ser.sparse.fill\_value
2

Copy to clipboard

On this page