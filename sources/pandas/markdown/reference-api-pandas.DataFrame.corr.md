[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.corr.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.corr.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.corr.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.corr.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.corr.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.corr.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.corr.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.corr.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.corr.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.corr.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.corr.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.corr.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.corr[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html#pandas-dataframe-corr "Link to this heading")

===============================================================================================================================================

DataFrame.corr(_method\='pearson'_, _min\_periods\=1_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L16485-L16604)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html#pandas.DataFrame.corr "Link to this definition")

Compute pairwise correlation of columns, excluding NA/null values.

The result is a symmetric DataFrame where each element represents the correlation coefficient between two columns. By default, the Pearson correlation is computed, but Kendall and Spearman methods as well as arbitrary callables are also supported.

Parameters:

**method**{‘pearson’, ‘kendall’, ‘spearman’} or callable

Method of correlation:

*   pearson : standard correlation coefficient
    
*   kendall : Kendall Tau correlation coefficient
    
*   spearman : Spearman rank correlation
    
*   callable: callable with input two 1d ndarrays
    
    and returning a float. Note that the returned matrix from corr will have 1 along the diagonals and will be symmetric regardless of the callable’s behavior.
    

**min\_periods**int, optional

Minimum number of observations required per pair of columns to have a valid result.

**numeric\_only**bool, default False

Include only float, int or boolean data.

Changed in version 2.0.0: The default value of `numeric_only` is now `False`.

Returns:

DataFrame

Correlation matrix.

See also

[`DataFrame.corrwith`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corrwith.html#pandas.DataFrame.corrwith "pandas.DataFrame.corrwith")

Compute pairwise correlation with another DataFrame or Series.

[`Series.corr`](https://pandas.pydata.org/docs/reference/api/pandas.Series.corr.html#pandas.Series.corr "pandas.Series.corr")

Compute the correlation between two Series.

Notes

Pearson, Kendall and Spearman correlation are currently computed using pairwise complete observations.

*   [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)
    
*   [Kendall rank correlation coefficient](https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient)
    
*   [Spearman’s rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient)
    

Examples

\>>> def histogram\_intersection(a, b):
...     v \= np.minimum(a, b).sum().round(decimals\=1)
...     return v
\>>> df \= pd.DataFrame(
...     \[(0.2, 0.3), (0.0, 0.6), (0.6, 0.0), (0.2, 0.1)\],
...     columns\=\["dogs", "cats"\],
... )
\>>> df.corr(method\=histogram\_intersection)
      dogs  cats
dogs   1.0   0.3
cats   0.3   1.0

Copy to clipboard

\>>> df \= pd.DataFrame(
...     \[(1, 1), (2, np.nan), (np.nan, 3), (4, 4)\], columns\=\["dogs", "cats"\]
... )
\>>> df.corr(min\_periods\=3)
      dogs  cats
dogs   1.0   NaN
cats   NaN   1.0

Copy to clipboard

On this page