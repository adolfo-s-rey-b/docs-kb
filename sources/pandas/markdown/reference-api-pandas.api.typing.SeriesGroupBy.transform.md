[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.transform.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.transform.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.transform.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.transform.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.transform.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.transform.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.transform.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.transform.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.transform.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.transform.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.transform.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.transform.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.transform.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.transform.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.transform[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.transform.html#pandas-api-typing-seriesgroupby-transform "Link to this heading")

===========================================================================================================================================================================================================

SeriesGroupBy.transform(_func_, _\*args_, _engine\=None_, _engine\_kwargs\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L624-L769)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.transform.html#pandas.api.typing.SeriesGroupBy.transform "Link to this definition")

Call function producing a same-indexed Series on each group.

Returns a Series having the same indexes as the original object filled with the transformed values.

Parameters:

**func**function, str

Function to apply to each group. See the Notes section below for requirements.

Accepted inputs are:

*   String
    
*   Python function
    
*   Numba JIT function with `engine='numba'` specified.
    

Only passing a single function is supported with this engine. If the `'numba'` engine is chosen, the function must be a user defined function with `values` and `index` as the first and second arguments respectively in the function signature. Each group’s index will be passed to the user defined function and optionally available for use.

If a string is chosen, then it needs to be the name of the groupby method you want to use.

**\*args**

Positional arguments to pass to func.

**engine**str, default None

*   `'cython'` : Runs the function through C-extensions from cython.
    
*   `'numba'` : Runs the function through JIT compiled code from numba.
    
*   `None` : Defaults to `'cython'` or the global setting `compute.use_numba`
    

**engine\_kwargs**dict, default None

*   For `'cython'` engine, there are no accepted `engine_kwargs`
    
*   For `'numba'` engine, the engine can accept `nogil` and `parallel` dictionary keys. The values must either be `True` or `False`. The default `engine_kwargs` for the `'numba'` engine is `{'nogil': False, 'parallel': False}` and will be applied to the function
    

**\*\*kwargs**

Keyword arguments to be passed into func.

Returns:

Series

Series with the same indexes as the original object filled with transformed values.

See also

`Series.groupby.apply`

Apply function `func` group-wise and combine the results together.

`Series.groupby.aggregate`

Aggregate using one or more operations.

`Series.transform`

Call `func` on self producing a Series with the same axis shape as self.

Notes

See [Transformation](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-transform)
 in the User Guide for more details and examples.

Each group is endowed the attribute ‘name’ in case you need to know which group you are working on.

`func` is passed each group as a whole `Series`. The current implementation imposes two requirements on `func`:

*   `func` must return a value that either has the same shape as the input group or can be broadcast to the shape of the input group. For example, if `func` returns a scalar it will be broadcast to have the same shape as the input group.
    
*   `func` must not mutate groups. Mutation is not supported and may produce unexpected results. See [Mutating with User Defined Function (UDF) methods](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-udf-mutation)
     for more details.
    

When using `engine='numba'`, there will be no “fall back” behavior internally. The group data and group index will be passed as numpy arrays to the JITed user defined function, and no alternative execution attempts will be tried.

The resulting dtype will reflect the return value of the passed `func`, see the examples below.

Changed in version 2.0.0: When using `.transform` on a grouped DataFrame and the transformation function returns a DataFrame, pandas now aligns the result’s index with the input’s index. You can call `.to_numpy()` on the result of the transformation function to avoid alignment.

Examples

\>>> ser \= pd.Series(
...     \[390.0, 350.0, 30.0, 20.0\],
...     index\=\["Falcon", "Falcon", "Parrot", "Parrot"\],
...     name\="Max Speed",
... )
\>>> grouped \= ser.groupby(\[1, 1, 2, 2\])
\>>> grouped.transform(lambda x: (x \- x.mean()) / x.std())
    Falcon    0.707107
    Falcon   -0.707107
    Parrot    0.707107
    Parrot   -0.707107
    Name: Max Speed, dtype: float64

Copy to clipboard

Broadcast result of the transformation

\>>> grouped.transform(lambda x: x.max() \- x.min())
Falcon    40.0
Falcon    40.0
Parrot    10.0
Parrot    10.0
Name: Max Speed, dtype: float64

Copy to clipboard

\>>> grouped.transform("mean")
Falcon    370.0
Falcon    370.0
Parrot     25.0
Parrot     25.0
Name: Max Speed, dtype: float64

Copy to clipboard

The resulting dtype will reflect the return value of the passed `func`, for example:

\>>> grouped.transform(lambda x: x.astype(int).max())
Falcon    390
Falcon    390
Parrot     30
Parrot     30
Name: Max Speed, dtype: int64

Copy to clipboard

On this page