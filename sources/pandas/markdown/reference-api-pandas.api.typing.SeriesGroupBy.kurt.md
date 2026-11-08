[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.kurt.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.kurt.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.kurt.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.kurt.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.kurt.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.kurt.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.kurt.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.kurt.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.kurt.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.kurt.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.kurt.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.kurt.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.kurt.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.kurt.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.kurt[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.kurt.html#pandas-api-typing-seriesgroupby-kurt "Link to this heading")

============================================================================================================================================================================================

SeriesGroupBy.kurt(_skipna\=True_, _numeric\_only\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L1429-L1509)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.kurt.html#pandas.api.typing.SeriesGroupBy.kurt "Link to this definition")

Return unbiased kurtosis within groups.

Kurtosis measures the tailedness of a distribution. This method computes Fisher’s definition of kurtosis (normal distribution has a kurtosis of zero) for each group, using the unbiased estimator.

Parameters:

**skipna**bool, default True

Exclude NA/null values when computing the result.

**numeric\_only**bool, default False

Include only float, int, boolean columns. Not implemented for Series.

**\*\*kwargs**

Additional keyword arguments to be passed to the function.

Returns:

Series

Unbiased kurtosis within groups.

See also

`Series.kurt`

Return unbiased kurtosis over requested axis.

Examples

\>>> ser \= pd.Series(
...     \[390.0, 350.0, 357.0, 333.0, np.nan, 22.0, 20.0, 30.0, 40.0, 41.0\],
...     index\=\[\
...         "Falcon",\
...         "Falcon",\
...         "Falcon",\
...         "Falcon",\
...         "Falcon",\
...         "Parrot",\
...         "Parrot",\
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
Falcon    333.0
Falcon      NaN
Parrot     22.0
Parrot     20.0
Parrot     30.0
Parrot     40.0
Parrot     41.0
Name: Max Speed, dtype: float64
\>>> ser.groupby(level\=0).kurt()
Falcon    1.622109
Parrot   -2.878714
Name: Max Speed, dtype: float64
\>>> ser.groupby(level\=0).kurt(skipna\=False)
Falcon         NaN
Parrot   -2.878714
Name: Max Speed, dtype: float64

Copy to clipboard

On this page