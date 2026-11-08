[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.skew.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.skew.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.skew.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.skew.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.skew.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.skew.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.skew.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.skew.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.skew.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.skew.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.skew.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.skew.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.skew.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.skew.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.skew[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.skew.html#pandas-api-typing-seriesgroupby-skew "Link to this heading")

============================================================================================================================================================================================

SeriesGroupBy.skew(_skipna\=True_, _numeric\_only\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L1349-L1427)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.skew.html#pandas.api.typing.SeriesGroupBy.skew "Link to this definition")

Return unbiased skew within groups.

Normalized by N-1.

Parameters:

**skipna**bool, default True

Exclude NA/null values when computing the result.

**numeric\_only**bool, default False

Include only float, int, boolean columns. Not implemented for Series.

**\*\*kwargs**

Additional keyword arguments to be passed to the function.

Deprecated since version 3.1.0: Passing `**kwargs` to SeriesGroupBy.skew is deprecated and will be removed in a future version of pandas.

Returns:

Series

Unbiased skew within groups.

See also

`Series.skew`

Return unbiased skew over requested axis.

Examples

\>>> ser \= pd.Series(
...     \[390.0, 350.0, 357.0, np.nan, 22.0, 20.0, 30.0\],
...     index\=\[\
...         "Falcon",\
...         "Falcon",\
...         "Falcon",\
...         "Falcon",\
...         "Parrot",\
...         "Parrot",\
...         "Parrot",\
...     \],
...     name\="Max Speed",
... )
\>>> ser
Falcon    390.0
Falcon    350.0
Falcon    357.0
Falcon      NaN
Parrot     22.0
Parrot     20.0
Parrot     30.0
Name: Max Speed, dtype: float64
\>>> ser.groupby(level\=0).skew()
Falcon    1.525174
Parrot    1.457863
Name: Max Speed, dtype: float64
\>>> ser.groupby(level\=0).skew(skipna\=False)
Falcon         NaN
Parrot    1.457863
Name: Max Speed, dtype: float64

Copy to clipboard

On this page