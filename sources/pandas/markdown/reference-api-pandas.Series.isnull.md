[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.isnull.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.isnull.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.isnull.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.isnull.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.isnull.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.isnull.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.isnull.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.isnull.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.isnull.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.isnull.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.isnull.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.isnull.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.isnull.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.isnull.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.isnull[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.isnull.html#pandas-series-isnull "Link to this heading")

============================================================================================================================================

Series.isnull()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L6881-L6924)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.isnull.html#pandas.Series.isnull "Link to this definition")

Series.isnull is an alias for Series.isna.

Detect missing values.

Return a boolean same-sized object indicating if the values are NA. NA values, such as None or `numpy.NaN`, gets mapped to True values. Everything else gets mapped to False values. Characters such as empty strings `''` or `numpy.inf` are not considered NA values.

Returns:

Series

Mask of bool values for each element in Series that indicates whether an element is an NA value.

See also

[`Series.isnull`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isnull.html#pandas.Series.isnull "pandas.Series.isnull")

Alias of isna.

[`DataFrame.isnull`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html#pandas.DataFrame.isnull "pandas.DataFrame.isnull")

Alias of isna.

[`Series.notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html#pandas.Series.notna "pandas.Series.notna")

Boolean inverse of isna.

[`DataFrame.notna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notna.html#pandas.DataFrame.notna "pandas.DataFrame.notna")

Boolean inverse of isna.

[`Series.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dropna.html#pandas.Series.dropna "pandas.Series.dropna")

Omit axes labels with missing values.

[`DataFrame.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna "pandas.DataFrame.dropna")

Omit axes labels with missing values.

[`isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html#pandas.isna "pandas.isna")

Top-level isna.

Examples

\>>> ser \= pd.Series(\[5, 6, np.nan\])
\>>> ser
0    5.0
1    6.0
2    NaN
dtype: float64

Copy to clipboard

\>>> ser.isnull()
0    False
1    False
2     True
dtype: bool

Copy to clipboard

On this page