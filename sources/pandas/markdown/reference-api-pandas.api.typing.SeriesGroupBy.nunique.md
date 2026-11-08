[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.nunique.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.nunique.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.nunique.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.nunique.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.nunique.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.nunique.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.nunique.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.nunique.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.nunique.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.nunique.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.nunique.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.nunique.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.nunique.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.nunique.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.nunique[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.nunique.html#pandas-api-typing-seriesgroupby-nunique "Link to this heading")

=====================================================================================================================================================================================================

SeriesGroupBy.nunique(_dropna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L890-L960)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.nunique.html#pandas.api.typing.SeriesGroupBy.nunique "Link to this definition")

Return number of unique elements in the group.

This method counts the number of distinct values within each group, optionally excluding NaN values.

Parameters:

**dropna**bool, default True

Don’t include NaN in the counts.

Returns:

Series

Number of unique values within each group.

See also

`core.resample.Resampler.nunique`

Method nunique for Resampler.

Examples

\>>> lst \= \["a", "a", "b", "b"\]
\>>> ser \= pd.Series(\[1, 2, 3, 3\], index\=lst)
\>>> ser
a    1
a    2
b    3
b    3
dtype: int64
\>>> ser.groupby(level\=0).nunique()
a    2
b    1
dtype: int64

Copy to clipboard

On this page