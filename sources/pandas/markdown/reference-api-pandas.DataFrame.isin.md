[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.isin.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.isin.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.isin.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.isin.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.isin.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.isin.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.isin.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.isin.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.isin.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.isin.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.isin.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.isin.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.isin[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html#pandas-dataframe-isin "Link to this heading")

===============================================================================================================================================

DataFrame.isin(_values_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L19971-L20095)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html#pandas.DataFrame.isin "Link to this definition")

Whether each element in the DataFrame is contained in values.

Returns a DataFrame of the same shape with boolean values: True where the element is in the corresponding structure of `values`, False otherwise. `values` can be a list, dict, Series, or DataFrame; alignment rules depend on its type.

Parameters:

**values**iterable, Series, DataFrame or dict

The result will only be true at a location if all the labels match. If values is a Series, that’s the index. If values is a dict, the keys must be the column names, which must match. If values is a DataFrame, then both the index and column labels must match.

Returns:

DataFrame

DataFrame of booleans showing whether each element in the DataFrame is contained in values.

See also

[`DataFrame.eq`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eq.html#pandas.DataFrame.eq "pandas.DataFrame.eq")

Equality test for DataFrame.

[`Series.isin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html#pandas.Series.isin "pandas.Series.isin")

Equivalent method on Series.

[`Series.str.contains`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html#pandas.Series.str.contains "pandas.Series.str.contains")

Test if pattern or regex is contained within a string of a Series or Index.

Notes

`__iter__` is used (and not `__contains__`) to iterate over values when checking if it contains the elements in DataFrame.

Examples

\>>> df \= pd.DataFrame(
...     {"num\_legs": \[2, 4\], "num\_wings": \[2, 0\]}, index\=\["falcon", "dog"\]
... )
\>>> df
        num\_legs  num\_wings
falcon         2          2
dog            4          0

Copy to clipboard

When `values` is a list check whether every value in the DataFrame is present in the list (which animals have 0 or 2 legs or wings)

\>>> df.isin(\[0, 2\])
        num\_legs  num\_wings
falcon      True       True
dog        False       True

Copy to clipboard

To check if `values` is _not_ in the DataFrame, use the `~` operator:

\>>> ~df.isin(\[0, 2\])
        num\_legs  num\_wings
falcon     False      False
dog         True      False

Copy to clipboard

When `values` is a dict, we can pass values to check for each column separately:

\>>> df.isin({"num\_wings": \[0, 3\]})
        num\_legs  num\_wings
falcon     False      False
dog        False       True

Copy to clipboard

When `values` is a Series or DataFrame the index and column must match. Note that ‘falcon’ does not match based on the number of legs in other.

\>>> other \= pd.DataFrame(
...     {"num\_legs": \[8, 3\], "num\_wings": \[0, 2\]}, index\=\["spider", "falcon"\]
... )
\>>> df.isin(other)
        num\_legs  num\_wings
falcon     False       True
dog        False      False

Copy to clipboard

On this page