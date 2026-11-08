[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.corr.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.corr.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.corr.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.corr.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.corr.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.corr.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.corr.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.corr.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.corr.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.corr.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.corr.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.corr.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.corr.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.corr.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.corr[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.corr.html#pandas-api-typing-dataframegroupby-corr "Link to this heading")

=====================================================================================================================================================================================================

DataFrameGroupBy.corr(_method\='pearson'_, _min\_periods\=1_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L3828-L3912)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.corr.html#pandas.api.typing.DataFrameGroupBy.corr "Link to this definition")

Compute pairwise correlation of columns, excluding NA/null values.

Computes a correlation matrix for each group, measuring the linear or rank-based relationship between columns.

Parameters:

**method**{‘pearson’, ‘kendall’, ‘spearman’} or callable

Method of correlation:

*   pearson : standard correlation coefficient
    
*   kendall : Kendall Tau correlation coefficient
    
*   spearman : Spearman rank correlation
    
*   callable: callable with input two 1d ndarrays
    
    and returning a float. Note that the returned matrix from corr will have 1 along the diagonals and will be symmetric regardless of the callable’s behavior.
    

**min\_periods**int, optional

Minimum number of observations required per pair of columns to have a valid result. Currently only available for Pearson and Spearman correlation.

**numeric\_only**bool, default False

Include only float, int or boolean data.

Changed in version 2.0.0: The default value of `numeric_only` is now `False`.

Returns:

DataFrame

Correlation matrix.

See also

`DataFrame.corrwith`

Compute pairwise correlation with another DataFrame or Series.

`Series.corr`

Compute the correlation between two Series.

Notes

Pearson, Kendall and Spearman correlation are currently computed using pairwise complete observations.

*   [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)
    
*   [Kendall rank correlation coefficient](https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient)
    
*   [Spearman’s rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient)
    

Examples

\>>> df \= pd.DataFrame(
...     {
...         "age": \[2, 3, 4, 6, 6, 1, 2, 1\],
...         "weight": \[2.1, 3.2, 4.1, 6.5, 3.3, 2.1, 4.1, 1.9\],
...         "pet": \["dog", "cat", "dog", "cat", "dog", "cat", "dog", "cat"\],
...     }
... )
\>>> df
   age  weight  pet
0    2     2.1  dog
1    3     3.2  cat
2    4     4.1  dog
3    6     6.5  cat
4    6     3.3  dog
5    1     2.1  cat
6    2     4.1  dog
7    1     1.9  cat
\>>> df.groupby("pet").corr()
                 age    weight
pet
cat age     1.000000  0.989321
    weight  0.989321  1.000000
dog age     1.000000  0.184177
    weight  0.184177  1.000000

Copy to clipboard

On this page