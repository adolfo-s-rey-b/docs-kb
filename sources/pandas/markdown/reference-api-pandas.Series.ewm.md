[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.ewm.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.ewm.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.ewm.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.ewm.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.ewm.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.ewm.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.ewm.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.ewm.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.ewm.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.ewm.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.ewm.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.ewm.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.ewm.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.ewm.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.ewm[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.ewm.html#pandas-series-ewm "Link to this heading")

===================================================================================================================================

Series.ewm(_com\=None_, _span\=None_, _halflife\=None_, _alpha\=None_, _min\_periods\=0_, _adjust\=True_, _ignore\_na\=False_, _times\=None_, _method\='single'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L12526-L12741)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.ewm.html#pandas.Series.ewm "Link to this definition")

Provide exponentially weighted (EW) calculations.

Exactly one of `com`, `span`, `halflife`, or `alpha` must be provided if `times` is not provided. If `times` is provided and `adjust=True`, `halflife` and one of `com`, `span` or `alpha` may be provided. If `times` is provided and `adjust=False`, `halflife` must be the only provided decay-specification parameter.

Parameters:

**com**float, optional

Specify decay in terms of center of mass

𝛼 \=1/(1 +𝑐⁢𝑜⁢𝑚), for 𝑐⁢𝑜⁢𝑚 ≥0.

**span**float, optional

Specify decay in terms of span

𝛼 \=2/(𝑠⁢𝑝⁢𝑎⁢𝑛 +1), for 𝑠⁢𝑝⁢𝑎⁢𝑛 ≥1.

**halflife**float, str, timedelta, optional

Specify decay in terms of half-life

𝛼 \=1 −exp⁡(−ln⁡(2)/ℎ⁡𝑎⁢𝑙⁢𝑓⁡𝑙⁢𝑖⁢𝑓⁡𝑒), for ℎ⁡𝑎⁢𝑙⁢𝑓⁡𝑙⁢𝑖⁢𝑓⁡𝑒 \>0.

If `times` is specified, a timedelta convertible unit over which an observation decays to half its value. Only applicable to `mean()`, and halflife value will not apply to the other functions.

**alpha**float, optional

Specify smoothing factor 𝛼 directly

0 <𝛼 ≤1.

**min\_periods**int, default 0

Minimum number of observations in window required to have a value; otherwise, result is `np.nan`.

**adjust**bool, default True

Divide by decaying adjustment factor in beginning periods to account for imbalance in relative weightings (viewing EWMA as a moving average).

*   When `adjust=True` (default), the EW function is calculated using weights 𝑤𝑖 \=(1−𝛼)𝑖. For example, the EW moving average of the series \[𝑥0,𝑥1,...,𝑥𝑡\] would be:
    

𝑦𝑡\=𝑥𝑡+(1−𝛼)⁢𝑥𝑡−1+(1−𝛼)2⁢𝑥𝑡−2+...+(1−𝛼)𝑡⁢𝑥01+(1−𝛼)+(1−𝛼)2+...+(1−𝛼)𝑡

*   When `adjust=False`, the exponentially weighted function is calculated recursively:
    

𝑦0\=𝑥0𝑦𝑡\=(1−𝛼)⁢𝑦𝑡−1+𝛼⁢𝑥𝑡,

**ignore\_na**bool, default False

Ignore missing values when calculating weights.

*   When `ignore_na=False` (default), weights are based on absolute positions. For example, the weights of 𝑥0 and 𝑥2 used in calculating the final weighted average of \[𝑥0, None, 𝑥2\] are (1−𝛼)2 and 1 if `adjust=True`, and (1−𝛼)2 and 𝛼 if `adjust=False`.
    
*   When `ignore_na=True`, weights are based on relative positions. For example, the weights of 𝑥0 and 𝑥2 used in calculating the final weighted average of \[𝑥0, None, 𝑥2\] are 1 −𝛼 and 1 if `adjust=True`, and 1 −𝛼 and 𝛼 if `adjust=False`.
    

**times**np.ndarray, Series, default None

Only applicable to `mean()`.

Times corresponding to the observations. Must be monotonically increasing and `datetime64[ns]` dtype.

If 1-D array like, a sequence with the same shape as the observations.

**method**str {‘single’, ‘table’}, default ‘single’

Execute the rolling operation per single column or row (`'single'`) or over the entire object (`'table'`).

This argument is only implemented when specifying `engine='numba'` in the method call.

Only applicable to `mean()`

Returns:

pandas.api.typing.ExponentialMovingWindow

An instance of ExponentialMovingWindow for further exponentially weighted (EW) calculations, e.g. using the `mean` method.

See also

[`rolling`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rolling.html#pandas.Series.rolling "pandas.Series.rolling")

Provides rolling window calculations.

[`expanding`](https://pandas.pydata.org/docs/reference/api/pandas.Series.expanding.html#pandas.Series.expanding "pandas.Series.expanding")

Provides expanding transformations.

Notes

See [Windowing Operations](https://pandas.pydata.org/docs/user_guide/window.html#window-exponentially-weighted)
 for further usage details and examples.

Examples

\>>> df \= pd.DataFrame({'B': \[0, 1, 2, np.nan, 4\]})
\>>> df
     B
0  0.0
1  1.0
2  2.0
3  NaN
4  4.0

Copy to clipboard

\>>> df.ewm(com\=0.5).mean()
          B
0  0.000000
1  0.750000
2  1.615385
3  1.615385
4  3.670213
\>>> df.ewm(alpha\=2 / 3).mean()
          B
0  0.000000
1  0.750000
2  1.615385
3  1.615385
4  3.670213

Copy to clipboard

**adjust**

\>>> df.ewm(com\=0.5, adjust\=True).mean()
          B
0  0.000000
1  0.750000
2  1.615385
3  1.615385
4  3.670213
\>>> df.ewm(com\=0.5, adjust\=False).mean()
          B
0  0.000000
1  0.666667
2  1.555556
3  1.555556
4  3.650794

Copy to clipboard

**ignore\_na**

\>>> df.ewm(com\=0.5, ignore\_na\=True).mean()
          B
0  0.000000
1  0.750000
2  1.615385
3  1.615385
4  3.225000
\>>> df.ewm(com\=0.5, ignore\_na\=False).mean()
          B
0  0.000000
1  0.750000
2  1.615385
3  1.615385
4  3.670213

Copy to clipboard

**times**

Exponentially weighted mean with weights calculated with a timedelta `halflife` relative to `times`.

\>>> times \= \['2020-01-01', '2020-01-03', '2020-01-10', '2020-01-15',\
...         '2020-01-17'\]
\>>> df.ewm(halflife\='4 days', times\=pd.DatetimeIndex(times)).mean()
          B
0  0.000000
1  0.585786
2  1.523889
3  1.523889
4  3.233686

Copy to clipboard

On this page