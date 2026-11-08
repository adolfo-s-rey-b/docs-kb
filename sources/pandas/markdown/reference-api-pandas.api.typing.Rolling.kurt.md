[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.kurt.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Rolling.kurt.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.kurt.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Rolling.kurt.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Rolling.kurt.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Rolling.kurt.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Rolling.kurt.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Rolling.kurt.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Rolling.kurt.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Rolling.kurt.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Rolling.kurt.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Rolling.kurt.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Rolling.kurt.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Rolling.kurt.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Rolling.kurt[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.kurt.html#pandas-api-typing-rolling-kurt "Link to this heading")

==========================================================================================================================================================================

Rolling.kurt(_numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L3024-L3074)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.kurt.html#pandas.api.typing.Rolling.kurt "Link to this definition")

Calculate the rolling Fisher’s definition of kurtosis without bias.

This is equivalent to applying `scipy.stats.kurtosis` (with `bias=False`) over each rolling window. A minimum of four periods is required.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

`scipy.stats.kurtosis`

Reference SciPy method.

`Series.rolling`

Calling rolling with Series data.

`DataFrame.rolling`

Calling rolling with DataFrames.

`Series.kurt`

Aggregating kurt for Series.

`DataFrame.kurt`

Aggregating kurt for DataFrame.

Notes

A minimum of four periods is required for the calculation.

Examples

The example below will show a rolling calculation with a window size of four matching the equivalent function call using scipy.stats.

\>>> arr \= \[1, 2, 3, 4, 999\]
\>>> import scipy.stats
\>>> print(f"{scipy.stats.kurtosis(arr\[:\-1\], bias\=False):.6f}")
\-1.200000
\>>> print(f"{scipy.stats.kurtosis(arr\[1:\], bias\=False):.6f}")
3.999946
\>>> s \= pd.Series(arr)
\>>> s.rolling(4).kurt()
0         NaN
1         NaN
2         NaN
3   -1.200000
4    3.999946
dtype: float64

Copy to clipboard

On this page