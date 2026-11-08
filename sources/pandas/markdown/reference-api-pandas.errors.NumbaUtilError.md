[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.NumbaUtilError.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.NumbaUtilError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.NumbaUtilError.html#pandas-errors-numbautilerror "Link to this heading")

====================================================================================================================================================================

exception pandas.errors.NumbaUtilError[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L552-L577)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.NumbaUtilError.html#pandas.errors.NumbaUtilError "Link to this definition")

Error raised for unsupported Numba engine routines.

This exception is raised when attempting to use the Numba engine with a function or operation that is not supported by Numba.

See also

`DataFrame.groupby`

Group DataFrame using a mapper or by a Series of columns.

`Series.groupby`

Group Series using a mapper or by a Series of columns.

`DataFrame.agg`

Aggregate using one or more operations over the specified axis.

`Series.agg`

Aggregate using one or more operations over the specified axis.

Examples

\>>> df \= pd.DataFrame(
...     {"key": \["a", "a", "b", "b"\], "data": \[1, 2, 3, 4\]}, columns\=\["key", "data"\]
... )
\>>> def incorrect\_function(x):
...     return sum(x) \* 2.7
\>>> df.groupby("key").agg(incorrect\_function, engine\="numba")
Traceback (most recent call last):
NumbaUtilError: The first 2 arguments to incorrect\_function
must be \['values', 'index'\]

Copy to clipboard

On this page