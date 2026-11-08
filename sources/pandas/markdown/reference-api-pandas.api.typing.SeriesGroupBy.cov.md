[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cov.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.cov.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cov.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.cov.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.cov.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.cov.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.cov.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.cov.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.cov.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.cov.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.cov.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.cov.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.cov.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.cov.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.cov[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cov.html#pandas-api-typing-seriesgroupby-cov "Link to this heading")

=========================================================================================================================================================================================

SeriesGroupBy.cov(_other_, _min\_periods\=None_, _ddof\=1_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L1838-L1875)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cov.html#pandas.api.typing.SeriesGroupBy.cov "Link to this definition")

Compute covariance between each group and another Series.

This method computes the sample covariance between each group’s values and the corresponding values in `other`.

Parameters:

**other**Series

Series to compute covariance with.

**min\_periods**int, optional

Minimum number of observations required per pair of columns to have a valid result.

**ddof**int, optional

Delta degrees of freedom for variance calculation.

Returns:

Series

Covariance value for each group.

See also

`Series.cov`

Equivalent method on `Series`.

Examples

\>>> s \= pd.Series(\[1, 2, 3, 4\], index\=\[0, 0, 1, 1\])
\>>> g \= s.groupby(\[0, 0, 1, 1\])
\>>> g.cov()

Copy to clipboard

On this page