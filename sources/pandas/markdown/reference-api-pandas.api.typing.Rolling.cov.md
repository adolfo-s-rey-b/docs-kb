[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.cov.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Rolling.cov.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.cov.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Rolling.cov.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Rolling.cov.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Rolling.cov.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Rolling.cov.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Rolling.cov.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Rolling.cov.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Rolling.cov.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Rolling.cov.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Rolling.cov.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Rolling.cov.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Rolling.cov.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Rolling.cov[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.cov.html#pandas-api-typing-rolling-cov "Link to this heading")

=======================================================================================================================================================================

Rolling.cov(_other\=None_, _pairwise\=None_, _ddof\=1_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L3344-L3407)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.cov.html#pandas.api.typing.Rolling.cov "Link to this definition")

Calculate the rolling sample covariance.

Compute the sample covariance between the calling object and `other` over each rolling window. If `other` is not supplied, pairwise covariances of the columns are computed.

Parameters:

**other**Series or DataFrame, optional

If not supplied then will default to self and produce pairwise output.

**pairwise**bool, default None

If False then only matching columns between self and other will be used and the output will be a DataFrame. If True then all pairwise combinations will be calculated and the output will be a MultiIndexed DataFrame in the case of DataFrame inputs. In the case of missing elements, only complete pairwise observations will be used.

**ddof**int, default 1

Delta Degrees of Freedom. The divisor used in calculations is `N - ddof`, where `N` represents the number of elements.

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

`Series.rolling`

Calling rolling with Series data.

`DataFrame.rolling`

Calling rolling with DataFrames.

`Series.cov`

Aggregating cov for Series.

`DataFrame.cov`

Aggregating cov for DataFrame.

Examples

\>>> ser1 \= pd.Series(\[1, 2, 3, 4\])
\>>> ser2 \= pd.Series(\[1, 4, 5, 8\])
\>>> ser1.rolling(2).cov(ser2)
0    NaN
1    1.5
2    0.5
3    1.5
dtype: float64

Copy to clipboard

On this page