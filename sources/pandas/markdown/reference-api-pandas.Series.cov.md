[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.cov.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.cov.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.cov.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.cov.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.cov.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.cov.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.cov.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.cov.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.cov.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.cov.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.cov.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.cov.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.cov.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.cov.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.cov[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cov.html#pandas-series-cov "Link to this heading")

===================================================================================================================================

Series.cov(_other_, _min\_periods\=None_, _ddof\=1_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L3113-L3161)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cov.html#pandas.Series.cov "Link to this definition")

Compute covariance with Series, excluding missing values.

The two Series objects are not required to be the same length and will be aligned internally before the covariance is calculated.

Parameters:

**other**Series

Series with which to compute the covariance.

**min\_periods**int, optional

Minimum number of observations needed to have a valid result.

**ddof**int, default 1

Delta degrees of freedom. The divisor used in calculations is `N - ddof`, where `N` represents the number of elements.

Returns:

float

Covariance between Series and other normalized by N-1 (unbiased estimator).

See also

[`DataFrame.cov`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cov.html#pandas.DataFrame.cov "pandas.DataFrame.cov")

Compute pairwise covariance of columns.

Examples

\>>> s1 \= pd.Series(\[0.90010907, 0.13484424, 0.62036035\])
\>>> s2 \= pd.Series(\[0.12528585, 0.26962463, 0.51111198\])
\>>> s1.cov(s2)
\-0.01685762652715874

Copy to clipboard

On this page