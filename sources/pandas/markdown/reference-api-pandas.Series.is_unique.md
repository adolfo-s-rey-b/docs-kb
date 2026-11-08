[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_unique.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.is_unique.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_unique.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.is_unique.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.is_unique.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.is_unique.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.is_unique.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.is_unique.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.is_unique.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.is_unique.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.is_unique.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.is_unique.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.is_unique.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.is_unique.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.is\_unique[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_unique.html#pandas-series-is-unique "Link to this heading")

======================================================================================================================================================

property Series.is\_unique[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L1259-L1287)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_unique.html#pandas.Series.is_unique "Link to this definition")

Return True if values in the object are unique.

This property checks whether all values in the Series or Index are distinct, including missing values.

Returns:

bool

See also

[`Series.unique`](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html#pandas.Series.unique "pandas.Series.unique")

Return unique values of Series object.

[`Series.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop_duplicates.html#pandas.Series.drop_duplicates "pandas.Series.drop_duplicates")

Return Series with duplicate values removed.

[`Series.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.Series.duplicated.html#pandas.Series.duplicated "pandas.Series.duplicated")

Indicate duplicate Series values.

Examples

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> s.is\_unique
True

Copy to clipboard

\>>> s \= pd.Series(\[1, 2, 3, 1\])
\>>> s.is\_unique
False

Copy to clipboard

On this page