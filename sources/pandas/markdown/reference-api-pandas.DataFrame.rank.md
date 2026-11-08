[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rank.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.rank.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rank.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.rank.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.rank.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.rank.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.rank.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.rank.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.rank.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.rank.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.rank.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.rank.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.rank.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.rank.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.rank[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rank.html#pandas-dataframe-rank "Link to this heading")

===============================================================================================================================================

DataFrame.rank(_axis\=0_, _method\='average'_, _numeric\_only\=False_, _na\_option\='keep'_, _ascending\=True_, _pct\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L9772-L9930)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rank.html#pandas.DataFrame.rank "Link to this definition")

Compute numerical data ranks (1 through n) along axis.

By default, equal values are assigned a rank that is the average of the ranks of those values.

Parameters:

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Index to direct ranking. For Series this parameter is unused and defaults to 0.

**method**{‘average’, ‘min’, ‘max’, ‘first’, ‘dense’}, default ‘average’

How to rank the group of records that have the same value (i.e. ties):

*   average: average rank of the group
    
*   min: lowest rank in the group
    
*   max: highest rank in the group
    
*   first: ranks assigned in order they appear in the array
    
*   dense: like ‘min’, but rank always increases by 1 between groups.
    

**numeric\_only**bool, default False

For DataFrame objects, rank only numeric columns if set to True.

Changed in version 2.0.0: The default value of `numeric_only` is now `False`.

**na\_option**{‘keep’, ‘top’, ‘bottom’}, default ‘keep’

How to rank NaN values:

*   keep: assign NaN rank to NaN values
    
*   top: assign lowest rank to NaN values
    
*   bottom: assign highest rank to NaN values
    

**ascending**bool, default True

Whether or not the elements should be ranked in ascending order.

**pct**bool, default False

Whether or not to display the returned rankings in percentile form.

Returns:

same type as caller

Return a Series or DataFrame with data ranks as values.

See also

`core.groupby.DataFrameGroupBy.rank`

Rank of values within each group.

`core.groupby.SeriesGroupBy.rank`

Rank of values within each group.

Examples

\>>> df \= pd.DataFrame(
...     data\={
...         "Animal": \["cat", "penguin", "dog", "spider", "snake"\],
...         "Number\_legs": \[4, 2, 4, 8, np.nan\],
...     }
... )
\>>> df
    Animal  Number\_legs
0      cat          4.0
1  penguin          2.0
2      dog          4.0
3   spider          8.0
4    snake          NaN

Copy to clipboard

Ties are assigned the mean of the ranks (by default) for the group.

\>>> s \= pd.Series(range(5), index\=list("abcde"))
\>>> s\["d"\] \= s\["b"\]
\>>> s.rank()
a    1.0
b    2.5
c    4.0
d    2.5
e    5.0
dtype: float64

Copy to clipboard

The following example shows how the method behaves with the above parameters:

*   default\_rank: this is the default behaviour obtained without using any parameter.
    
*   max\_rank: setting `method = 'max'` the records that have the same values are ranked using the highest rank (e.g.: since ‘cat’ and ‘dog’ are both in the 2nd and 3rd position, rank 3 is assigned.)
    
*   NA\_bottom: choosing `na_option = 'bottom'`, if there are records with NaN values they are placed at the bottom of the ranking.
    
*   pct\_rank: when setting `pct = True`, the ranking is expressed as percentile rank.
    

\>>> df\["default\_rank"\] \= df\["Number\_legs"\].rank()
\>>> df\["max\_rank"\] \= df\["Number\_legs"\].rank(method\="max")
\>>> df\["NA\_bottom"\] \= df\["Number\_legs"\].rank(na\_option\="bottom")
\>>> df\["pct\_rank"\] \= df\["Number\_legs"\].rank(pct\=True)
\>>> df
    Animal  Number\_legs  default\_rank  max\_rank  NA\_bottom  pct\_rank
0      cat          4.0           2.5       3.0        2.5     0.625
1  penguin          2.0           1.0       1.0        1.0     0.250
2      dog          4.0           2.5       3.0        2.5     0.625
3   spider          8.0           4.0       4.0        4.0     1.000
4    snake          NaN           NaN       NaN        5.0       NaN

Copy to clipboard

On this page