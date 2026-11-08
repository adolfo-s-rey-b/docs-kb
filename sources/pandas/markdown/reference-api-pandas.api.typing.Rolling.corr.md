[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.corr.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Rolling.corr.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.corr.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Rolling.corr.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Rolling.corr.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Rolling.corr.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Rolling.corr.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Rolling.corr.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Rolling.corr.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Rolling.corr.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Rolling.corr.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Rolling.corr.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Rolling.corr.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Rolling.corr.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Rolling.corr[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.corr.html#pandas-api-typing-rolling-corr "Link to this heading")

==========================================================================================================================================================================

Rolling.corr(_other\=None_, _pairwise\=None_, _ddof\=1_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L3409-L3541)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.corr.html#pandas.api.typing.Rolling.corr "Link to this definition")

Calculate the rolling correlation.

Compute the Pearson correlation coefficient between the calling object and `other` over each rolling window. If `other` is not supplied, pairwise correlations of the columns are computed.

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

[`cov`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.cov.html#pandas.api.typing.Rolling.cov "pandas.api.typing.Rolling.cov")

Similar method to calculate covariance.

[`numpy.corrcoef`](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "(in NumPy v2.5)")

NumPy Pearson’s correlation calculation.

`Series.rolling`

Calling rolling with Series data.

`DataFrame.rolling`

Calling rolling with DataFrames.

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

The below example shows a rolling calculation with a window size of four matching the equivalent function call using `numpy.corrcoef()`.

\>>> v1 \= \[3, 3, 3, 5, 8\]
\>>> v2 \= \[3, 4, 4, 4, 8\]
\>>> np.corrcoef(v1\[:\-1\], v2\[:\-1\])
array(\[\[1.        , 0.33333333\],\
    \[0.33333333, 1.        \]\])
\>>> np.corrcoef(v1\[1:\], v2\[1:\])
array(\[\[1.       , 0.9169493\],\
    \[0.9169493, 1.       \]\])
\>>> s1 \= pd.Series(v1)
\>>> s2 \= pd.Series(v2)
\>>> s1.rolling(4).corr(s2)
0         NaN
1         NaN
2         NaN
3    0.333333
4    0.916949
dtype: float64

Copy to clipboard

The below example shows a similar rolling calculation on a DataFrame using the pairwise option.

\>>> matrix \= np.array(
...     \[\[51.0, 35.0\], \[49.0, 30.0\], \[47.0, 32.0\], \[46.0, 31.0\], \[50.0, 36.0\]\]
... )
\>>> np.corrcoef(matrix\[:\-1, 0\], matrix\[:\-1, 1\])
array(\[\[1.       , 0.6263001\],\
    \[0.6263001, 1.       \]\])
\>>> np.corrcoef(matrix\[1:, 0\], matrix\[1:, 1\])
array(\[\[1.        , 0.55536811\],\
    \[0.55536811, 1.        \]\])
\>>> df \= pd.DataFrame(matrix, columns\=\["X", "Y"\])
\>>> df
      X     Y
0  51.0  35.0
1  49.0  30.0
2  47.0  32.0
3  46.0  31.0
4  50.0  36.0
\>>> df.rolling(4).corr(pairwise\=True)
            X         Y
0 X        NaN       NaN
  Y        NaN       NaN
1 X        NaN       NaN
  Y        NaN       NaN
2 X        NaN       NaN
  Y        NaN       NaN
3 X   1.000000  0.626300
  Y   0.626300  1.000000
4 X   1.000000  0.555368
  Y   0.555368  1.000000

Copy to clipboard

On this page