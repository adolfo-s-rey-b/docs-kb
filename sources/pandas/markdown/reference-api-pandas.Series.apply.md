[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.apply.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.apply.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.apply.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.apply.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.apply.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.apply.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.apply.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.apply.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.apply.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.apply.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.apply.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.apply.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.apply[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html#pandas-series-apply "Link to this heading")

=========================================================================================================================================

Series.apply(_func_, _args\=()_, _\*_, _by\_row\='compat'_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L5451-L5575)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html#pandas.Series.apply "Link to this definition")

Invoke function on values of Series.

Can be ufunc (a NumPy function that applies to the entire Series) or a Python function that only works on single values.

Parameters:

**func**function

Python function or NumPy ufunc to apply.

**args**tuple

Positional arguments passed to func after the series value.

**by\_row**False or “compat”, default “compat”

If `"compat"` and func is a callable, func will be passed each element of the Series, like `Series.map`. If func is a list or dict of callables, will first try to translate each func into pandas methods. If that doesn’t work, will try call to apply again with `by_row="compat"` and if that fails, will call apply again with `by_row=False` (backward compatible). If False, the func will be passed the whole Series at once.

`by_row` has no effect when `func` is a string.

Added in version 2.1.0.

**\*\*kwargs**

Additional keyword arguments passed to func.

Returns:

Series or DataFrame

If func returns a Series object the result will be a DataFrame.

See also

[`Series.map`](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html#pandas.Series.map "pandas.Series.map")

For element-wise operations.

[`Series.agg`](https://pandas.pydata.org/docs/reference/api/pandas.Series.agg.html#pandas.Series.agg "pandas.Series.agg")

Only perform aggregating type operations.

[`Series.transform`](https://pandas.pydata.org/docs/reference/api/pandas.Series.transform.html#pandas.Series.transform "pandas.Series.transform")

Only perform transforming type operations.

Notes

Functions that mutate the passed object can produce unexpected behavior or errors and are not supported. See [Mutating with User Defined Function (UDF) methods](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-udf-mutation)
 for more details.

Examples

Create a series with typical summer temperatures for each city.

\>>> s \= pd.Series(\[20, 21, 12\], index\=\["London", "New York", "Helsinki"\])
\>>> s
London      20
New York    21
Helsinki    12
dtype: int64

Copy to clipboard

Square the values by defining a function and passing it as an argument to `apply()`.

\>>> def square(x):
...     return x\*\*2
\>>> s.apply(square)
London      400
New York    441
Helsinki    144
dtype: int64

Copy to clipboard

Square the values by passing an anonymous function as an argument to `apply()`.

\>>> s.apply(lambda x: x\*\*2)
London      400
New York    441
Helsinki    144
dtype: int64

Copy to clipboard

Define a custom function that needs additional positional arguments and pass these additional arguments using the `args` keyword.

\>>> def subtract\_custom\_value(x, custom\_value):
...     return x \- custom\_value

Copy to clipboard

\>>> s.apply(subtract\_custom\_value, args\=(5,))
London      15
New York    16
Helsinki     7
dtype: int64

Copy to clipboard

Define a custom function that takes keyword arguments and pass these arguments to `apply`.

\>>> def add\_custom\_values(x, \*\*kwargs):
...     for month in kwargs:
...         x += kwargs\[month\]
...     return x

Copy to clipboard

\>>> s.apply(add\_custom\_values, june\=30, july\=20, august\=25)
London      95
New York    96
Helsinki    87
dtype: int64

Copy to clipboard

Use a function from the Numpy library.

\>>> s.apply(np.log)
London      2.995732
New York    3.044522
Helsinki    2.484907
dtype: float64

Copy to clipboard

On this page