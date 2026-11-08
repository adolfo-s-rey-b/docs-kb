[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.transform.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.transform[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.transform.html#pandas-api-typing-resampler-transform "Link to this heading")

===============================================================================================================================================================================================

final Resampler.transform(_arg_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L457-L499)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.transform.html#pandas.api.typing.Resampler.transform "Link to this definition")

Call function producing a like-indexed Series on each group.

Return a Series with the transformed values.

Parameters:

**arg**function

To apply to each group. Should return a Series with the same index.

**\*args, \*\*kwargs**

Additional arguments and keywords.

Returns:

Series

A Series with the transformed values, maintaining the same index as the original object.

See also

`core.resample.Resampler.apply`

Apply a function along each group.

`core.resample.Resampler.aggregate`

Aggregate using one or more operations over the specified axis.

Examples

\>>> s \= pd.Series(\[1, 2\], index\=pd.date\_range("20180101", periods\=2, freq\="1h"))
\>>> s
2018-01-01 00:00:00    1
2018-01-01 01:00:00    2
Freq: h, dtype: int64

Copy to clipboard

\>>> resampled \= s.resample("15min")
\>>> resampled.transform(lambda x: (x \- x.mean()) / x.std())
2018-01-01 00:00:00   NaN
2018-01-01 01:00:00   NaN
Freq: h, dtype: float64

Copy to clipboard

On this page