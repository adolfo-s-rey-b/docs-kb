[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.pipe.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.pipe[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.pipe.html#pandas-api-typing-resampler-pipe "Link to this heading")

================================================================================================================================================================================

final Resampler.pipe(_func_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L266-L343)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.pipe.html#pandas.api.typing.Resampler.pipe "Link to this definition")

Apply a `func` with arguments to this Resampler object and return its result.

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

Function to apply to this Resampler object or, alternatively, a (callable, data\_keyword) tuple where data\_keyword is a string indicating the keyword of callable that expects the Resampler object.

**\*args**iterable, optional

Positional arguments passed into func.

**\*\*kwargs**dict, optional

A dictionary of keyword arguments passed into func.

Returns:

any

The result of applying `func` to the Resampler object.

See also

`Series.pipe`

Apply a function with arguments to a series.

`DataFrame.pipe`

Apply a function with arguments to a dataframe.

[`apply`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.apply.html#pandas.api.typing.Resampler.apply "pandas.api.typing.Resampler.apply")

Apply function to each group instead of to the full Resampler object.

Notes

See more [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#piping-function-calls)

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

To get the difference between each 2-day period’s maximum and minimum value in one pass, you can do

\>>> df.resample("2D").pipe(lambda x: x.max() \- x.min())
            A
2012-08-02  1
2012-08-04  1

Copy to clipboard

On this page