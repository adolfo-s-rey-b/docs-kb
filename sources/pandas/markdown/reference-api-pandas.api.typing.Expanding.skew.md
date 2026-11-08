[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.skew.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Expanding.skew.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.skew.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Expanding.skew.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Expanding.skew.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Expanding.skew.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Expanding.skew.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Expanding.skew.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Expanding.skew.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Expanding.skew.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Expanding.skew.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Expanding.skew.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Expanding.skew.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Expanding.skew.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Expanding.skew[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.skew.html#pandas-api-typing-expanding-skew "Link to this heading")

================================================================================================================================================================================

Expanding.skew(_numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/expanding.py#L954-L994)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.skew.html#pandas.api.typing.Expanding.skew "Link to this definition")

Calculate the expanding unbiased skewness.

Computes the third standardized moment over all data points seen so far, measuring the asymmetry of the distribution.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

`scipy.stats.skew`

Third moment of a probability density.

`Series.expanding`

Calling expanding with Series data.

`DataFrame.expanding`

Calling expanding with DataFrames.

`Series.skew`

Aggregating skew for Series.

`DataFrame.skew`

Aggregating skew for DataFrame.

Notes

A minimum of three periods is required for the rolling calculation.

Examples

\>>> ser \= pd.Series(\[\-1, 0, 2, \-1, 2\], index\=\["a", "b", "c", "d", "e"\])
\>>> ser.expanding().skew()
a         NaN
b         NaN
c    0.935220
d    1.414214
e    0.315356
dtype: float64

Copy to clipboard

On this page