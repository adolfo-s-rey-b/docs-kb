[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.kurt.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Expanding.kurt.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.kurt.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Expanding.kurt.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Expanding.kurt.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Expanding.kurt.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Expanding.kurt.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Expanding.kurt.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Expanding.kurt.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Expanding.kurt.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Expanding.kurt.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Expanding.kurt.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Expanding.kurt.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Expanding.kurt.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Expanding.kurt[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.kurt.html#pandas-api-typing-expanding-kurt "Link to this heading")

================================================================================================================================================================================

Expanding.kurt(_numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/expanding.py#L996-L1045)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.kurt.html#pandas.api.typing.Expanding.kurt "Link to this definition")

Calculate the expanding Fisher’s definition of kurtosis without bias.

Measures the tailedness of the distribution over all data points seen so far. A minimum of four periods is required.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

`scipy.stats.kurtosis`

Reference SciPy method.

`Series.expanding`

Calling expanding with Series data.

`DataFrame.expanding`

Calling expanding with DataFrames.

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
\>>> print(f"{scipy.stats.kurtosis(arr, bias\=False):.6f}")
4.999874
\>>> s \= pd.Series(arr)
\>>> s.expanding(4).kurt()
0         NaN
1         NaN
2         NaN
3   -1.200000
4    4.999874
dtype: float64

Copy to clipboard

On this page