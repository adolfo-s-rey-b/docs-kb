[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.col.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.col.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.col.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.col.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.col.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.col.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.col.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.col.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.col.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.col.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.col.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.col.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.col.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.col.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.col[#](https://pandas.pydata.org/docs/reference/api/pandas.col.html#pandas-col "Link to this heading")

==============================================================================================================

pandas.col(_col\_name_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/col.py#L398-L459)
[#](https://pandas.pydata.org/docs/reference/api/pandas.col.html#pandas.col "Link to this definition")

Generate deferred object representing a column of a DataFrame.

Any place which accepts `lambda df: df[col_name]`, such as [`DataFrame.assign()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign "pandas.DataFrame.assign")
 or [`DataFrame.loc()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc")
, can also accept `pd.col(col_name)`.

Added in version 3.0.0.

Parameters:

**col\_name**Hashable

Column name.

Returns:

[`pandas.api.typing.Expression`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expression.html#pandas.api.typing.Expression "pandas.api.typing.Expression")

A deferred object representing a column of a DataFrame.

See also

[`DataFrame.query`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "pandas.DataFrame.query")

Query columns of a dataframe using string expressions.

[`DataFrame.select`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select.html#pandas.DataFrame.select "pandas.DataFrame.select")

Select a subset of columns from the DataFrame.

Examples

You can use col in assign.

\>>> df \= pd.DataFrame({"name": \["beluga", "narwhal"\], "speed": \[100, 110\]})
\>>> df.assign(name\_titlecase\=pd.col("name").str.title())
      name  speed name\_titlecase
0   beluga    100         Beluga
1  narwhal    110        Narwhal

Copy to clipboard

You can also use it for filtering.

\>>> df.loc\[pd.col("speed") \> 105\]
      name  speed
1  narwhal    110

Copy to clipboard

On this page