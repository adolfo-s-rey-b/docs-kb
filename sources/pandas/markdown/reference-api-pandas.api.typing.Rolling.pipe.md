[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.pipe.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Rolling.pipe.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.pipe.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Rolling.pipe.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Rolling.pipe.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Rolling.pipe.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Rolling.pipe.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Rolling.pipe.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Rolling.pipe.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Rolling.pipe.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Rolling.pipe.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Rolling.pipe.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Rolling.pipe.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Rolling.pipe.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Rolling.pipe[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.pipe.html#pandas-api-typing-rolling-pipe "Link to this heading")

==========================================================================================================================================================================

final Rolling.pipe(_func_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L2306-L2391)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.pipe.html#pandas.api.typing.Rolling.pipe "Link to this definition")

Apply a `func` with arguments to this Rolling object and return its result.

Use .pipe when you want to improve readability by chaining together functions that expect Series, DataFrames, GroupBy, Rolling, Expanding or Resampler objects. Instead of writing

\>>> h \= lambda x, arg2, arg3: x + 1 \- arg2 \* arg3
\>>> g \= lambda x, arg1: x \* 5 / arg1
\>>> f \= lambda x: x\*\*4
\>>> df \= pd.DataFrame(
...     {"A": \[1, 2, 3, 4\]}, index\=pd.date\_range("2012-08-02", periods\=4)
... )
\>>> h(g(f(df.rolling("2D")), arg1\=1), arg2\=2, arg3\=3)

Copy to clipboard

You can write

\>>> (
...     df.rolling("2D").pipe(f).pipe(g, arg1\=1).pipe(h, arg2\=2, arg3\=3)
... )

Copy to clipboard

which is much more readable.

Parameters:

**func**callable or tuple of (callable, str)

Function to apply to this Rolling object or, alternatively, a (callable, data\_keyword) tuple where data\_keyword is a string indicating the keyword of callable that expects the Rolling object.

**\*args**iterable, optional

Positional arguments passed into func.

**\*\*kwargs**dict, optional

A dictionary of keyword arguments passed into func.

Returns:

Rolling

The original object with the function func applied.

See also

`Series.pipe`

Apply a function with arguments to a series.

`DataFrame.pipe`

Apply a function with arguments to a dataframe.

[`apply`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.apply.html#pandas.api.typing.Rolling.apply "pandas.api.typing.Rolling.apply")

Apply function to each group instead of to the full Rolling object.

Notes

See more [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#piping-function-calls)
.

Examples

\>>> df \= pd.DataFrame(
...     {"A": \[1, 2, 3, 4\]}, index\=pd.date\_range("2012-08-02", periods\=4)
... )
\>>> df
            A
2012-08-02  1
2012-08-03  2
2012-08-04  3
2012-08-05  4

Copy to clipboard

To get the difference between each rolling 2-day window’s maximum and minimum value in one pass, you can do

\>>> df.rolling("2D").pipe(lambda x: x.max() \- x.min())
            A
2012-08-02  0.0
2012-08-03  1.0
2012-08-04  1.0
2012-08-05  1.0

Copy to clipboard

On this page