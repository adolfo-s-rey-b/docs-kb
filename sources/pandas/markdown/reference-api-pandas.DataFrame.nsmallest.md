[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nsmallest.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.nsmallest[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nsmallest.html#pandas-dataframe-nsmallest "Link to this heading")

==============================================================================================================================================================

DataFrame.nsmallest(_n_, _columns_, _keep\='first'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L9833-L9962)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nsmallest.html#pandas.DataFrame.nsmallest "Link to this definition")

Return the first n rows ordered by columns in ascending order.

Return the first n rows with the smallest values in columns, in ascending order. The columns that are not specified are returned as well, but not used for ordering.

This method is equivalent to `df.sort_values(columns, ascending=True).head(n)`, but more performant.

Parameters:

**n**int

Number of items to retrieve.

**columns**list or str

Column name or names to order by.

**keep**{‘first’, ‘last’, ‘all’}, default ‘first’

Where there are duplicate values:

*   `first` : take the first occurrence.
    
*   `last` : take the last occurrence.
    
*   `all` : keep all the ties of the largest item even if it means selecting more than `n` items.
    

Returns:

DataFrame

DataFrame with the first n rows ordered by columns in ascending order.

See also

[`DataFrame.nlargest`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nlargest.html#pandas.DataFrame.nlargest "pandas.DataFrame.nlargest")

Return the first n rows ordered by columns in descending order.

[`DataFrame.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values "pandas.DataFrame.sort_values")

Sort DataFrame by the values.

[`DataFrame.head`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html#pandas.DataFrame.head "pandas.DataFrame.head")

Return the first n rows without re-ordering.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "population": \[\
...             59000000,\
...             65000000,\
...             434000,\
...             434000,\
...             434000,\
...             337000,\
...             337000,\
...             11300,\
...             11300,\
...         \],
...         "GDP": \[1937894, 2583560, 12011, 4520, 12128, 17036, 182, 38, 311\],
...         "alpha-2": \["IT", "FR", "MT", "MV", "BN", "IS", "NR", "TV", "AI"\],
...     },
...     index\=\[\
...         "Italy",\
...         "France",\
...         "Malta",\
...         "Maldives",\
...         "Brunei",\
...         "Iceland",\
...         "Nauru",\
...         "Tuvalu",\
...         "Anguilla",\
...     \],
... )
\>>> df
          population      GDP alpha-2
Italy       59000000  1937894      IT
France      65000000  2583560      FR
Malta         434000    12011      MT
Maldives      434000     4520      MV
Brunei        434000    12128      BN
Iceland       337000    17036      IS
Nauru         337000      182      NR
Tuvalu         11300       38      TV
Anguilla       11300      311      AI

Copy to clipboard

In the following example, we will use `nsmallest` to select the three rows having the smallest values in column “population”.

\>>> df.nsmallest(3, "population")
          population    GDP alpha-2
Tuvalu         11300     38      TV
Anguilla       11300    311      AI
Iceland       337000  17036      IS

Copy to clipboard

When using `keep='last'`, ties are resolved in reverse order:

\>>> df.nsmallest(3, "population", keep\="last")
          population  GDP alpha-2
Anguilla       11300  311      AI
Tuvalu         11300   38      TV
Nauru         337000  182      NR

Copy to clipboard

When using `keep='all'`, the number of element kept can go beyond `n` if there are duplicate values for the largest element, all the ties are kept.

\>>> df.nsmallest(3, "population", keep\="all")
          population    GDP alpha-2
Tuvalu         11300     38      TV
Anguilla       11300    311      AI
Iceland       337000  17036      IS
Nauru         337000    182      NR

Copy to clipboard

However, `nsmallest` does not keep `n` distinct smallest elements:

\>>> df.nsmallest(4, "population", keep\="all")
          population    GDP alpha-2
Tuvalu         11300     38      TV
Anguilla       11300    311      AI
Iceland       337000  17036      IS
Nauru         337000    182      NR

Copy to clipboard

To order by the smallest values in column “population” and then “GDP”, we can specify multiple columns like in the next example.

\>>> df.nsmallest(3, \["population", "GDP"\])
          population  GDP alpha-2
Tuvalu         11300   38      TV
Anguilla       11300  311      AI
Nauru         337000  182      NR

Copy to clipboard

On this page