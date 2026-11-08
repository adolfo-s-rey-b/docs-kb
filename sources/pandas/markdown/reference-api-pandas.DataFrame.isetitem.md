[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isetitem.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.isetitem.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isetitem.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.isetitem.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.isetitem.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.isetitem.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.isetitem.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.isetitem.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.isetitem.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.isetitem.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.isetitem.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.isetitem.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.isetitem.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.isetitem.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.isetitem[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isetitem.html#pandas-dataframe-isetitem "Link to this heading")

===========================================================================================================================================================

DataFrame.isetitem(_loc_, _value_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L4484-L4538)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isetitem.html#pandas.DataFrame.isetitem "Link to this definition")

Set the given value in the column with position loc.

This is a positional analogue to `__setitem__`.

Parameters:

**loc**int or sequence of ints

Index position for the column.

**value**scalar or arraylike

Value(s) for the column.

See also

[`DataFrame.iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "pandas.DataFrame.iloc")

Purely integer-location based indexing for selection by position.

Notes

`frame.isetitem(loc, value)` is an in-place method as it will modify the DataFrame in place (not returning a new object). In contrast to `frame.iloc[:, i] = value` which will try to update the existing values in place, `frame.isetitem(loc, value)` will not update the values of the column itself in place, it will instead insert a new array.

In cases where `frame.columns` is unique, this is equivalent to `frame[frame.columns[i]] = value`.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 2\], "B": \[3, 4\]})
\>>> df.isetitem(1, \[5, 6\])
\>>> df
      A  B
0     1  5
1     2  6

Copy to clipboard

On this page