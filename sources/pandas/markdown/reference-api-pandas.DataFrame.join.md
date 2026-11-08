[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.join.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.join.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.join.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.join.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.join.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.join.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.join.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.join.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.join.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.join.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.join.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.join.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.join[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html#pandas-dataframe-join "Link to this heading")

===============================================================================================================================================

DataFrame.join(_other_, _on\=None_, _how\='left'_, _lsuffix\=<no\_default>_, _rsuffix\=<no\_default>_, _sort\=False_, _validate\=None_, _\*_, _suffixes\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L15676-L15961)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html#pandas.DataFrame.join "Link to this definition")

Join columns of another DataFrame.

Join columns with other DataFrame either on index or on a key column. Efficiently join multiple DataFrame objects by index at once by passing a list.

Parameters:

**other**DataFrame, Series, or a list containing any combination of them

Index should be similar to one of the columns in the caller. If a Series is passed, its name attribute must be set, and that will be used as the column name in the resulting joined DataFrame.

**on**str, list of str, or array-like, optional

Column or index level name(s) in the caller to join on the index in other, otherwise joins index-on-index. If multiple values given, the other DataFrame must have a MultiIndex. Can pass an array as the join key if it is not already contained in the calling DataFrame. Like an Excel VLOOKUP operation.

**how**{‘left’, ‘right’, ‘outer’, ‘inner’, ‘cross’, ‘left\_anti’, ‘right\_anti’},

default ‘left’ How to handle the operation of the two objects.

*   left: use calling frame’s index (or column if on is specified)
    
*   right: use other’s index.
    
*   outer: form union of calling frame’s index (or column if on is specified) with other’s index, and sort it lexicographically.
    
*   inner: form intersection of calling frame’s index (or column if on is specified) with other’s index, preserving the order of the calling’s one.
    
*   cross: creates the cartesian product from both frames, preserves the order of the left keys.
    
*   left\_anti: use set difference of calling frame’s index and other’s index.
    
*   right\_anti: use set difference of other’s index and calling frame’s index.
    

**lsuffix**str, default ‘’

Suffix to use from left frame’s overlapping columns.

Deprecated since version 3.1.0: Use `suffixes` instead.

**rsuffix**str, default ‘’

Suffix to use from right frame’s overlapping columns.

Deprecated since version 3.1.0: Use `suffixes` instead.

**sort**bool, default False

Order result DataFrame lexicographically by the join key. If False, the order of the join key depends on the join type (how keyword).

**validate**str, optional

If specified, checks if join is of specified type.

*   “one\_to\_one” or “1:1”: check if join keys are unique in both left and right datasets.
    
*   “one\_to\_many” or “1:m”: check if join keys are unique in left dataset.
    
*   “many\_to\_one” or “m:1”: check if join keys are unique in right dataset.
    
*   “many\_to\_many” or “m:m”: allowed, but does not result in checks.
    

**suffixes**tuple of (str, str), default (“”, “”)

A length-2 sequence where each element is optionally a string indicating the suffix to add to overlapping column names in the caller and `other` respectively. Pass a value of `None` instead of a string to indicate that the column name from the caller or `other` should be left as-is, with no suffix. At least one of the values must not be None.

Returns:

DataFrame

A dataframe containing columns from both the caller and other.

See also

[`DataFrame.merge`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html#pandas.DataFrame.merge "pandas.DataFrame.merge")

For column(s)-on-column(s) operations.

Notes

Parameters on and suffixes are not supported when passing a list of DataFrame objects.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "key": \["K0", "K1", "K2", "K3", "K4", "K5"\],
...         "A": \["A0", "A1", "A2", "A3", "A4", "A5"\],
...     }
... )

Copy to clipboard

\>>> df
  key   A
0  K0  A0
1  K1  A1
2  K2  A2
3  K3  A3
4  K4  A4
5  K5  A5

Copy to clipboard

\>>> other \= pd.DataFrame({"key": \["K0", "K1", "K2"\], "B": \["B0", "B1", "B2"\]})

Copy to clipboard

\>>> other
  key   B
0  K0  B0
1  K1  B1
2  K2  B2

Copy to clipboard

Join DataFrames using their indexes.

\>>> df.join(other, suffixes\=("\_caller", "\_other"))
  key\_caller   A key\_other    B
0         K0  A0        K0   B0
1         K1  A1        K1   B1
2         K2  A2        K2   B2
3         K3  A3       NaN  NaN
4         K4  A4       NaN  NaN
5         K5  A5       NaN  NaN

Copy to clipboard

If we want to join using the key columns, we need to set key to be the index in both df and other. The joined DataFrame will have key as its index.

\>>> df.set\_index("key").join(other.set\_index("key"))
      A    B
key
K0   A0   B0
K1   A1   B1
K2   A2   B2
K3   A3  NaN
K4   A4  NaN
K5   A5  NaN

Copy to clipboard

Another option to join using the key columns is to use the on parameter. DataFrame.join always uses other’s index but we can use any column in df. This method preserves the original DataFrame’s index in the result.

\>>> df.join(other.set\_index("key"), on\="key")
  key   A    B
0  K0  A0   B0
1  K1  A1   B1
2  K2  A2   B2
3  K3  A3  NaN
4  K4  A4  NaN
5  K5  A5  NaN

Copy to clipboard

Using non-unique key values shows how they are matched.

\>>> df \= pd.DataFrame(
...     {
...         "key": \["K0", "K1", "K1", "K3", "K0", "K1"\],
...         "A": \["A0", "A1", "A2", "A3", "A4", "A5"\],
...     }
... )

Copy to clipboard

\>>> df
  key   A
0  K0  A0
1  K1  A1
2  K1  A2
3  K3  A3
4  K0  A4
5  K1  A5

Copy to clipboard

\>>> df.join(other.set\_index("key"), on\="key", validate\="m:1")
  key   A    B
0  K0  A0   B0
1  K1  A1   B1
2  K1  A2   B1
3  K3  A3  NaN
4  K0  A4   B0
5  K1  A5   B1

Copy to clipboard

On this page