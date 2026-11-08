[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.sem.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Expanding.sem.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.sem.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Expanding.sem.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Expanding.sem.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Expanding.sem.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Expanding.sem.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Expanding.sem.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Expanding.sem.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Expanding.sem.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Expanding.sem.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Expanding.sem.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Expanding.sem.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Expanding.sem.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Expanding.sem[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.sem.html#pandas-api-typing-expanding-sem "Link to this heading")

=============================================================================================================================================================================

Expanding.sem(_ddof\=1_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/expanding.py#L909-L952)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.sem.html#pandas.api.typing.Expanding.sem "Link to this definition")

Calculate the expanding standard error of mean.

The standard error is computed as `std / sqrt(N)` over all data points seen so far, where `N` is the number of observations.

Parameters:

**ddof**int, default 1

Delta Degrees of Freedom. The divisor used in calculations is `N - ddof`, where `N` represents the number of elements.

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

`Series.expanding`

Calling expanding with Series data.

`DataFrame.expanding`

Calling expanding with DataFrames.

`Series.sem`

Aggregating sem for Series.

`DataFrame.sem`

Aggregating sem for DataFrame.

Notes

A minimum of one period is required for the calculation.

Examples

\>>> s \= pd.Series(\[0, 1, 2, 3\])

Copy to clipboard

\>>> s.expanding().sem()
0         NaN
1    0.500000
2    0.577350
3    0.645497
dtype: float64

Copy to clipboard

On this page