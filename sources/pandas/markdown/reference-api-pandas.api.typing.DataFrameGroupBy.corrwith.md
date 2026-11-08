[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.corrwith.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.corrwith.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.corrwith.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.corrwith.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.corrwith.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.corrwith.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.corrwith.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.corrwith.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.corrwith.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.corrwith.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.corrwith.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.corrwith.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.corrwith.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.corrwith.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.corrwith[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.corrwith.html#pandas-api-typing-dataframegroupby-corrwith "Link to this heading")

=================================================================================================================================================================================================================

DataFrameGroupBy.corrwith(_other_, _drop\=False_, _method\='pearson'_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L4149-L4230)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.corrwith.html#pandas.api.typing.DataFrameGroupBy.corrwith "Link to this definition")

Compute pairwise correlation.

Deprecated since version 3.0.0.

Pairwise correlation is computed between rows or columns of DataFrame with rows or columns of Series or DataFrame. DataFrames are first aligned along both axes before computing the correlations.

Parameters:

**other**DataFrame, Series

Object with which to compute correlations.

**drop**bool, default False

Drop missing indices from result.

**method**{‘pearson’, ‘kendall’, ‘spearman’} or callable

Method of correlation:

*   pearson : standard correlation coefficient
    
*   kendall : Kendall Tau correlation coefficient
    
*   spearman : Spearman rank correlation
    
*   callable: callable with input two 1d ndarrays
    
    and returning a float.
    

**numeric\_only**bool, default False

Include only float, int or boolean data.

Changed in version 2.0.0: The default value of `numeric_only` is now `False`.

Returns:

Series

Pairwise correlations.

See also

`DataFrame.corr`

Compute pairwise correlation of columns.

Examples

\>>> df1 \= pd.DataFrame(
...     {
...         "Day": \[1, 1, 1, 2, 2, 2, 3, 3, 3\],
...         "Data": \[6, 6, 8, 5, 4, 2, 7, 3, 9\],
...     }
... )
\>>> df2 \= pd.DataFrame(
...     {
...         "Day": \[1, 1, 1, 2, 2, 2, 3, 3, 3\],
...         "Data": \[5, 3, 8, 3, 1, 1, 2, 3, 6\],
...     }
... )

Copy to clipboard

\>>> df1.groupby("Day").corrwith(df2)
         Data  Day
Day
1    0.917663  NaN
2    0.755929  NaN
3    0.576557  NaN

Copy to clipboard

On this page