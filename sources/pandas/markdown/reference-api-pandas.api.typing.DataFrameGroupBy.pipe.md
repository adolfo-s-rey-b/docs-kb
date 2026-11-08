[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.pipe[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html#pandas-api-typing-dataframegroupby-pipe "Link to this heading")

=====================================================================================================================================================================================================

DataFrameGroupBy.pipe(_func_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L471-L546)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html#pandas.api.typing.DataFrameGroupBy.pipe "Link to this definition")

Apply a `func` with arguments to this GroupBy object and return its result.

Use .pipe when you want to improve readability by chaining together functions that expect Series, DataFrames, GroupBy or Resampler objects. Instead of writing

\>>> h \= lambda x, arg2, arg3: x + 1 \- arg2 \* arg3
\>>> g \= lambda x, arg1: x \* 5 / arg1
\>>> f \= lambda x: x\*\*4
\>>> df \= pd.DataFrame(\[\["a", 4\], \["b", 5\]\], columns\=\["group", "value"\])
\>>> h(g(f(df.groupby("group")), arg1\=1), arg2\=2, arg3\=3)

Copy to clipboard

You can write

\>>> (
...     df.groupby("group").pipe(f).pipe(g, arg1\=1).pipe(h, arg2\=2, arg3\=3)
... )

Copy to clipboard

which is much more readable.

Parameters:

**func**callable or tuple of (callable, str)

Function to apply to this GroupBy object or, alternatively, a (callable, data\_keyword) tuple where data\_keyword is a string indicating the keyword of callable that expects the GroupBy object.

**\*args**iterable, optional

Positional arguments passed into func.

**\*\*kwargs**dict, optional

A dictionary of keyword arguments passed into func.

Returns:

GroupBy

The return type of func.

See also

`Series.pipe`

Apply a function with arguments to a series.

`DataFrame.pipe`

Apply a function with arguments to a dataframe.

[`apply`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html#pandas.api.typing.DataFrameGroupBy.apply "pandas.api.typing.DataFrameGroupBy.apply")

Apply function to each group instead of to the full GroupBy object.

Notes

See more [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#piping-function-calls)

Examples

\>>> df \= pd.DataFrame({"A": "a b a b".split(), "B": \[1, 2, 3, 4\]})
\>>> df
   A  B
0  a  1
1  b  2
2  a  3
3  b  4

Copy to clipboard

To get the difference between each groups maximum and minimum value in one pass, you can do

\>>> df.groupby("A").pipe(lambda x: x.max() \- x.min())
   B
A
a  2
b  2

Copy to clipboard

On this page