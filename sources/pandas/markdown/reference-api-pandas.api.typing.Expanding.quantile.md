[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.quantile.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Expanding.quantile[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.quantile.html#pandas-api-typing-expanding-quantile "Link to this heading")

============================================================================================================================================================================================

Expanding.quantile(_q_, _interpolation\='linear'_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/expanding.py#L1123-L1183)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.quantile.html#pandas.api.typing.Expanding.quantile "Link to this definition")

Calculate the expanding quantile.

At each step the specified quantile is computed from all prior observations, using the given interpolation method for values between data points.

Parameters:

**q**float

Quantile to compute. 0 <= quantile <= 1.

**interpolation**{‘linear’, ‘lower’, ‘higher’, ‘midpoint’, ‘nearest’}

This optional parameter specifies the interpolation method to use, when the desired quantile lies between two data points i and j:

> *   linear: i + (j - i) \* fraction, where fraction is the fractional part of the index surrounded by i and j.
>     
> *   lower: i.
>     
> *   higher: j.
>     
> *   nearest: i or j whichever is nearest.
>     
> *   midpoint: (i + j) / 2.
>     

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

`Series.quantile`

Aggregating quantile for Series.

`DataFrame.quantile`

Aggregating quantile for DataFrame.

Examples

\>>> ser \= pd.Series(\[1, 2, 3, 4, 5, 6\], index\=\["a", "b", "c", "d", "e", "f"\])
\>>> ser.expanding(min\_periods\=4).quantile(0.25)
a     NaN
b     NaN
c     NaN
d    1.75
e    2.00
f    2.25
dtype: float64

Copy to clipboard

On this page