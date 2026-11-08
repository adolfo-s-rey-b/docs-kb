[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corrwith.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.corrwith[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corrwith.html#pandas-dataframe-corrwith "Link to this heading")

===========================================================================================================================================================

DataFrame.corrwith(_other_, _axis\=0_, _drop\=False_, _method\='pearson'_, _numeric\_only\=False_, _min\_periods\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L16741-L16884)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corrwith.html#pandas.DataFrame.corrwith "Link to this definition")

Compute pairwise correlation.

Pairwise correlation is computed between rows or columns of DataFrame with rows or columns of Series or DataFrame. DataFrames are first aligned along both axes before computing the correlations.

Parameters:

**other**DataFrame, Series

Object with which to compute correlations.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

The axis to use. 0 or ‘index’ to compute row-wise, 1 or ‘columns’ for column-wise.

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

**min\_periods**int, optional

Minimum number of observations needed to have a valid result.

Changed in version 2.0.0: The default value of `numeric_only` is now `False`.

Returns:

Series

Pairwise correlations.

See also

[`DataFrame.corr`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html#pandas.DataFrame.corr "pandas.DataFrame.corr")

Compute pairwise correlation of columns.

Examples

\>>> index \= \["a", "b", "c", "d", "e"\]
\>>> columns \= \["one", "two", "three", "four"\]
\>>> df1 \= pd.DataFrame(
...     np.arange(20).reshape(5, 4), index\=index, columns\=columns
... )
\>>> df2 \= pd.DataFrame(
...     np.arange(16).reshape(4, 4), index\=index\[:4\], columns\=columns
... )
\>>> df1.corrwith(df2)
one      1.0
two      1.0
three    1.0
four     1.0
dtype: float64

Copy to clipboard

\>>> df2.corrwith(df1, axis\=1)
a    1.0
b    1.0
c    1.0
d    1.0
e    NaN
dtype: float64

Copy to clipboard

On this page