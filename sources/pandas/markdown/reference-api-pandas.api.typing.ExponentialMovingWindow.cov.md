[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.cov.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.ExponentialMovingWindow.cov[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.cov.html#pandas-api-typing-exponentialmovingwindow-cov "Link to this heading")

=======================================================================================================================================================================================================================

ExponentialMovingWindow.cov(_other\=None_, _pairwise\=None_, _bias\=False_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/ewm.py#L819-L913)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.cov.html#pandas.api.typing.ExponentialMovingWindow.cov "Link to this definition")

Calculate the ewm (exponential weighted moment) sample covariance.

The weighting is controlled by the `com`, `span`, `halflife`, or `alpha` parameter specified when calling `DataFrame.ewm()` or `Series.ewm()`.

Parameters:

**other**Series or DataFrame , optional

If not supplied then will default to self and produce pairwise output.

**pairwise**bool, default None

If False then only matching columns between self and other will be used and the output will be a DataFrame. If True then all pairwise combinations will be calculated and the output will be a MultiIndex DataFrame in the case of DataFrame inputs. In the case of missing elements, only complete pairwise observations will be used.

**bias**bool, default False

Use a standard estimation bias correction.

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

`Series.ewm`

Calling ewm with Series data.

`DataFrame.ewm`

Calling ewm with DataFrames.

`Series.cov`

Aggregating cov for Series.

`DataFrame.cov`

Aggregating cov for DataFrame.

Examples

\>>> ser1 \= pd.Series(\[1, 2, 3, 4\])
\>>> ser2 \= pd.Series(\[10, 11, 13, 16\])
\>>> ser1.ewm(alpha\=0.2).cov(ser2)
0         NaN
1    0.500000
2    1.524590
3    3.408836
dtype: float64

Copy to clipboard

On this page