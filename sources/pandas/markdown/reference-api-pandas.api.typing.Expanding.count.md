[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.count.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Expanding.count[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.count.html#pandas-api-typing-expanding-count "Link to this heading")

===================================================================================================================================================================================

Expanding.count(_numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/expanding.py#L217-L252)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.count.html#pandas.api.typing.Expanding.count "Link to this definition")

Calculate the expanding count of non NaN observations.

At each point in time, returns the number of non-NaN values seen so far. This is useful for tracking data availability across an expanding window.

Parameters:

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

`Series.count`

Aggregating count for Series.

`DataFrame.count`

Aggregating count for DataFrame.

Examples

\>>> ser \= pd.Series(\[1, 2, 3, 4\], index\=\["a", "b", "c", "d"\])
\>>> ser.expanding().count()
a    1.0
b    2.0
c    3.0
d    4.0
dtype: float64

Copy to clipboard

On this page