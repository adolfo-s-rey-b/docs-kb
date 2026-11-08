[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.corr.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.corr.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.corr.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.corr.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.corr.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.corr.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.corr.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.corr.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.corr.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.corr.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.corr.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.corr.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.corr.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.corr.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.corr[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.corr.html#pandas-series-corr "Link to this heading")

======================================================================================================================================

Series.corr(_other_, _method\='pearson'_, _min\_periods\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L3016-L3111)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.corr.html#pandas.Series.corr "Link to this definition")

Compute correlation with other Series, excluding missing values.

The two Series objects are not required to be the same length and will be aligned internally before the correlation function is applied.

Parameters:

**other**Series

Series with which to compute the correlation.

**method**{‘pearson’, ‘kendall’, ‘spearman’} or callable

Method used to compute correlation:

*   pearson : Standard correlation coefficient
    
*   kendall : Kendall Tau correlation coefficient
    
*   spearman : Spearman rank correlation
    
*   callable: Callable with input two 1d ndarrays and returning a float.
    

Warning

Note that the returned matrix from corr will have 1 along the diagonals and will be symmetric regardless of the callable’s behavior.

**min\_periods**int, optional

Minimum number of observations needed to have a valid result.

Returns:

float

Correlation with other.

See also

[`DataFrame.corr`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html#pandas.DataFrame.corr "pandas.DataFrame.corr")

Compute pairwise correlation between columns.

[`DataFrame.corrwith`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corrwith.html#pandas.DataFrame.corrwith "pandas.DataFrame.corrwith")

Compute pairwise correlation with another DataFrame or Series.

Notes

Pearson, Kendall and Spearman correlation are currently computed using pairwise complete observations.

*   [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)
    
*   [Kendall rank correlation coefficient](https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient)
    
*   [Spearman’s rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient)
    

Automatic data alignment: as with all pandas operations, automatic data alignment is performed for this method. `corr()` automatically considers values with matching indices.

Examples

\>>> def histogram\_intersection(a, b):
...     v \= np.minimum(a, b).sum().round(decimals\=1)
...     return v
\>>> s1 \= pd.Series(\[0.2, 0.0, 0.6, 0.2\])
\>>> s2 \= pd.Series(\[0.3, 0.6, 0.0, 0.1\])
\>>> s1.corr(s2, method\=histogram\_intersection)
0.3

Copy to clipboard

Pandas auto-aligns the values with matching indices

\>>> s1 \= pd.Series(\[1, 2, 3\], index\=\[0, 1, 2\])
\>>> s2 \= pd.Series(\[1, 2, 3\], index\=\[2, 1, 0\])
\>>> s1.corr(s2)
\-1.0

Copy to clipboard

If the input is a constant array, the correlation is not defined in this case, and `np.nan` is returned.

\>>> s1 \= pd.Series(\[0.45, 0.45\])
\>>> s1.corr(s1)
nan

Copy to clipboard

On this page