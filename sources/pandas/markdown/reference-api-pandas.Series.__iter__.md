[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.__iter__.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.__iter__.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.__iter__.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.__iter__.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.__iter__.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.__iter__.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.__iter__.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.__iter__.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.__iter__.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.__iter__.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.__iter__.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.__iter__.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.__iter__.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.__iter__.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.\_\_iter\_\_[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.__iter__.html#pandas-series-iter "Link to this heading")

==================================================================================================================================================

Series.\_\_iter\_\_()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L987-L1018)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.__iter__.html#pandas.Series.__iter__ "Link to this definition")

Return an iterator of the values.

These are each a scalar type, which is a Python scalar (for str, int, float) or a pandas scalar (for Timestamp/Timedelta/Interval/Period)

Returns:

iterator

An iterator yielding scalar values from the Series.

See also

[`Series.items`](https://pandas.pydata.org/docs/reference/api/pandas.Series.items.html#pandas.Series.items "pandas.Series.items")

Lazily iterate over (index, value) tuples.

Examples

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> for x in s:
...     print(x)
1
2
3

Copy to clipboard

On this page