[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.corr.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Expanding.corr.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.corr.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Expanding.corr.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Expanding.corr.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Expanding.corr.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Expanding.corr.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Expanding.corr.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Expanding.corr.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Expanding.corr.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Expanding.corr.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Expanding.corr.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Expanding.corr.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Expanding.corr.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Expanding.corr[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.corr.html#pandas-api-typing-expanding-corr "Link to this heading")

================================================================================================================================================================================

Expanding.corr(_other\=None_, _pairwise\=None_, _ddof\=1_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/expanding.py#L1368-L1452)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.corr.html#pandas.api.typing.Expanding.corr "Link to this definition")

Calculate the expanding correlation.

Uses Pearson’s correlation over all data points seen so far.

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

[`cov`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.cov.html#pandas.api.typing.Expanding.cov "pandas.api.typing.Expanding.cov")

Similar method to calculate covariance.

[`numpy.corrcoef`](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "(in NumPy v2.5)")

NumPy Pearson’s correlation calculation.

`Series.expanding`

Calling expanding with Series data.

`DataFrame.expanding`

Calling expanding with DataFrames.

`Series.corr`

Aggregating corr for Series.

`DataFrame.corr`

Aggregating corr for DataFrame.

Notes

This function uses Pearson’s definition of correlation ([https://en.wikipedia.org/wiki/Pearson\_correlation\_coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)
).

When other is not specified, the output will be self correlation (e.g. all 1’s), except for [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 inputs with pairwise set to True.

Function will return `NaN` for correlations of equal valued sequences; this is the result of a 0/0 division error.

When pairwise is set to False, only matching columns between self and other will be used.

When pairwise is set to True, the output will be a MultiIndex DataFrame with the original index on the first level, and the other DataFrame columns on the second level.

In the case of missing elements, only complete pairwise observations will be used.

Examples

\>>> ser1 \= pd.Series(\[1, 2, 3, 4\], index\=\["a", "b", "c", "d"\])
\>>> ser2 \= pd.Series(\[10, 11, 13, 16\], index\=\["a", "b", "c", "d"\])
\>>> ser1.expanding().corr(ser2)
a         NaN
b    1.000000
c    0.981981
d    0.975900
dtype: float64

Copy to clipboard

On this page