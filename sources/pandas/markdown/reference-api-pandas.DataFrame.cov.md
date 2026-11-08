[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cov.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.cov.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cov.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.cov.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.cov.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.cov.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.cov.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.cov.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.cov.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.cov.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.cov.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.cov.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.cov.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.cov.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.cov[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cov.html#pandas-dataframe-cov "Link to this heading")

============================================================================================================================================

DataFrame.cov(_min\_periods\=None_, _ddof\=1_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L16606-L16739)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cov.html#pandas.DataFrame.cov "Link to this definition")

Compute pairwise covariance of columns, excluding NA/null values.

Compute the pairwise covariance among the series of a DataFrame. The returned data frame is the [covariance matrix](https://en.wikipedia.org/wiki/Covariance_matrix)
 of the columns of the DataFrame.

Both NA and null values are automatically excluded from the calculation. (See the note below about bias from missing values.) A threshold can be set for the minimum number of observations for each value created. Comparisons with observations below this threshold will be returned as `NaN`.

This method is generally used for the analysis of time series data to understand the relationship between different measures across time.

Parameters:

**min\_periods**int, optional

Minimum number of observations required per pair of columns to have a valid result.

**ddof**int, default 1

Delta degrees of freedom. The divisor used in calculations is `N - ddof`, where `N` represents the number of elements. This argument is applicable only when no `nan` is in the dataframe.

**numeric\_only**bool, default False

Include only float, int or boolean data.

Changed in version 2.0.0: The default value of `numeric_only` is now `False`.

Returns:

DataFrame

The covariance matrix of the series of the DataFrame.

See also

[`Series.cov`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cov.html#pandas.Series.cov "pandas.Series.cov")

Compute covariance with another Series.

`core.window.ewm.ExponentialMovingWindow.cov`

Exponential weighted sample covariance.

`core.window.expanding.Expanding.cov`

Expanding sample covariance.

`core.window.rolling.Rolling.cov`

Rolling sample covariance.

Notes

Returns the covariance matrix of the DataFrame’s time series. The covariance is normalized by N-ddof.

For DataFrames that have Series that are missing data (assuming that data is [missing at random](https://en.wikipedia.org/wiki/Missing_data#Missing_at_random)
) the returned covariance matrix will be an unbiased estimate of the variance and covariance between the member Series.

However, for many applications this estimate may not be acceptable because the estimate covariance matrix is not guaranteed to be positive semi-definite. This could lead to estimate correlations having absolute values which are greater than one, and/or a non-invertible covariance matrix. See [Estimation of covariance matrices](https://en.wikipedia.org/w/index.php?title=Estimation_of_covariance_matrices)
 for more details.

Examples

\>>> df \= pd.DataFrame(
...     \[(1, 2), (0, 3), (2, 0), (1, 1)\], columns\=\["dogs", "cats"\]
... )
\>>> df.cov()
          dogs      cats
dogs  0.666667 -1.000000
cats -1.000000  1.666667

Copy to clipboard

\>>> np.random.seed(42)
\>>> df \= pd.DataFrame(
...     np.random.randn(1000, 5), columns\=\["a", "b", "c", "d", "e"\]
... )
\>>> df.cov()
          a         b         c         d         e
a  0.998438 -0.020161  0.059277 -0.008943  0.014144
b -0.020161  1.059352 -0.008543 -0.024738  0.009826
c  0.059277 -0.008543  1.010670 -0.001486 -0.000271
d -0.008943 -0.024738 -0.001486  0.921297 -0.013692
e  0.014144  0.009826 -0.000271 -0.013692  0.977795

Copy to clipboard

**Minimum number of periods**

This method also supports an optional `min_periods` keyword that specifies the required minimum number of non-NA observations for each column pair in order to have a valid result:

\>>> np.random.seed(42)
\>>> df \= pd.DataFrame(np.random.randn(20, 3), columns\=\["a", "b", "c"\])
\>>> df.loc\[df.index\[:5\], "a"\] \= np.nan
\>>> df.loc\[df.index\[5:10\], "b"\] \= np.nan
\>>> df.cov(min\_periods\=12)
          a         b         c
a  0.316741       NaN -0.150812
b       NaN  1.248003  0.191417
c -0.150812  0.191417  0.895202

Copy to clipboard

On this page