[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.duplicated.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.duplicated.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.duplicated.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.duplicated.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.duplicated.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.duplicated.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.duplicated.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.duplicated.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.duplicated.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.duplicated.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.duplicated.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.duplicated.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.duplicated.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.duplicated.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.duplicated[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.duplicated.html#pandas-series-duplicated "Link to this heading")

========================================================================================================================================================

Series.duplicated(_keep\='first'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L2662-L2741)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.duplicated.html#pandas.Series.duplicated "Link to this definition")

Indicate duplicate Series values.

Duplicated values are indicated as `True` values in the resulting Series. Values are considered duplicated when the same value appears more than once. Either all duplicated values, all except the first, or all except the last occurrence of duplicated values can be indicated.

Parameters:

**keep**{‘first’, ‘last’, False}, default ‘first’

Method to handle dropping duplicates:

*   ‘first’ : Mark duplicates as `True` except for the first occurrence.
    
*   ‘last’ : Mark duplicates as `True` except for the last occurrence.
    
*   `False` : Mark all duplicates as `True`.
    

Returns:

Series\[bool\]

Series indicating whether each value is a duplicated value according to `keep`.

See also

[`Index.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.Index.duplicated.html#pandas.Index.duplicated "pandas.Index.duplicated")

Equivalent method on pandas.Index.

[`DataFrame.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html#pandas.DataFrame.duplicated "pandas.DataFrame.duplicated")

Equivalent method on pandas.DataFrame.

[`Series.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop_duplicates.html#pandas.Series.drop_duplicates "pandas.Series.drop_duplicates")

Remove duplicate values from Series.

Examples

By default, for each set of duplicated values, the first occurrence is set on False and all others on True:

\>>> animals \= pd.Series(\["llama", "cow", "llama", "beetle", "llama"\])
\>>> animals.duplicated()
0    False
1    False
2     True
3    False
4     True
dtype: bool

Copy to clipboard

which is equivalent to

\>>> animals.duplicated(keep\="first")
0    False
1    False
2     True
3    False
4     True
dtype: bool

Copy to clipboard

By using ‘last’, the last occurrence of each set of duplicated values is set on False and all others on True:

\>>> animals.duplicated(keep\="last")
0     True
1    False
2     True
3    False
4    False
dtype: bool

Copy to clipboard

By setting keep on `False`, all duplicates are True:

\>>> animals.duplicated(keep\=False)
0     True
1    False
2     True
3    False
4     True
dtype: bool

Copy to clipboard

On this page