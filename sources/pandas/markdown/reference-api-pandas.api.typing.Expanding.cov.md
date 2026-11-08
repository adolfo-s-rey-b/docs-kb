[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.cov.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Expanding.cov.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.cov.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Expanding.cov.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Expanding.cov.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Expanding.cov.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Expanding.cov.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Expanding.cov.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Expanding.cov.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Expanding.cov.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Expanding.cov.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Expanding.cov.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Expanding.cov.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Expanding.cov.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Expanding.cov[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.cov.html#pandas-api-typing-expanding-cov "Link to this heading")

=============================================================================================================================================================================

Expanding.cov(_other\=None_, _pairwise\=None_, _ddof\=1_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/expanding.py#L1306-L1366)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.cov.html#pandas.api.typing.Expanding.cov "Link to this definition")

Calculate the expanding sample covariance.

When `other` is provided, computes pairwise covariance between `self` and `other`; otherwise computes all pairwise covariances of the columns.

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

`Series.expanding`

Calling expanding with Series data.

`DataFrame.expanding`

Calling expanding with DataFrames.

`Series.cov`

Aggregating cov for Series.

`DataFrame.cov`

Aggregating cov for DataFrame.

Examples

\>>> ser1 \= pd.Series(\[1, 2, 3, 4\], index\=\["a", "b", "c", "d"\])
\>>> ser2 \= pd.Series(\[10, 11, 13, 16\], index\=\["a", "b", "c", "d"\])
\>>> ser1.expanding().cov(ser2)
a         NaN
b    0.500000
c    1.500000
d    3.333333
dtype: float64

Copy to clipboard

On this page