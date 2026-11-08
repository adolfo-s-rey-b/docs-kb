[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.UnsupportedFunctionCall.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.UnsupportedFunctionCall.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.UnsupportedFunctionCall.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.UnsupportedFunctionCall.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.UnsupportedFunctionCall.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.UnsupportedFunctionCall.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.UnsupportedFunctionCall.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.UnsupportedFunctionCall.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.UnsupportedFunctionCall.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.UnsupportedFunctionCall.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.UnsupportedFunctionCall.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.UnsupportedFunctionCall.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.UnsupportedFunctionCall.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.UnsupportedFunctionCall.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.UnsupportedFunctionCall[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.UnsupportedFunctionCall.html#pandas-errors-unsupportedfunctioncall "Link to this heading")

===============================================================================================================================================================================================

exception pandas.errors.UnsupportedFunctionCall[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L249-L270)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.UnsupportedFunctionCall.html#pandas.errors.UnsupportedFunctionCall "Link to this definition")

Exception raised when attempting to call an unsupported numpy function.

For example, `np.cumsum(groupby_object)`.

See also

`DataFrame.groupby`

Group DataFrame using a mapper or by a Series of columns.

`Series.groupby`

Group Series using a mapper or by a Series of columns.

`core.groupby.GroupBy.cumsum`

Compute cumulative sum for each group.

Examples

\>>> df \= pd.DataFrame(
...     {"A": \[0, 0, 1, 1\], "B": \["x", "x", "z", "y"\], "C": \[1, 2, 3, 4\]}
... )
\>>> np.cumsum(df.groupby(\["A"\]))
Traceback (most recent call last):
UnsupportedFunctionCall: numpy operations are not valid with groupby.
Use .groupby(...).cumsum() instead

Copy to clipboard

On this page