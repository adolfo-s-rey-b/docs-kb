[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.pipe.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.pipe.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.pipe.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.pipe.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.pipe.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.pipe.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.pipe.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.pipe.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.pipe.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.pipe.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.pipe.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.pipe.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.pipe[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html#pandas-dataframe-pipe "Link to this heading")

===============================================================================================================================================

DataFrame.pipe(_func_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L6248-L6354)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html#pandas.DataFrame.pipe "Link to this definition")

Apply chainable functions that expect Series or DataFrames.

Passes the object as the first argument to each function, so that `df.pipe(f).pipe(g)` is equivalent to `g(f(df))`. Improves readability when chaining several transformations.

Parameters:

**func**function

Function to apply to the Series/DataFrame. `args`, and `kwargs` are passed into `func`. Alternatively a `(callable, data_keyword)` tuple where `data_keyword` is a string indicating the keyword of `callable` that expects the Series/DataFrame.

**\*args**iterable, optional

Positional arguments passed into `func`.

**\*\*kwargs**mapping, optional

A dictionary of keyword arguments passed into `func`.

Returns:

The return type of `func`.

The result of applying `func` to the Series or DataFrame.

See also

[`DataFrame.apply`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply "pandas.DataFrame.apply")

Apply a function along input axis of DataFrame.

[`DataFrame.map`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html#pandas.DataFrame.map "pandas.DataFrame.map")

Apply a function elementwise on a whole DataFrame.

[`Series.map`](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html#pandas.Series.map "pandas.Series.map")

Apply a mapping correspondence on a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
.

Notes

Use `.pipe` when chaining together functions that expect Series, DataFrames or GroupBy objects.

Examples

Constructing an income DataFrame from a dictionary.

\>>> data \= \[\[8000, 1000\], \[9500, np.nan\], \[5000, 2000\]\]
\>>> df \= pd.DataFrame(data, columns\=\["Salary", "Others"\])
\>>> df
   Salary  Others
0    8000  1000.0
1    9500     NaN
2    5000  2000.0

Copy to clipboard

Functions that perform tax reductions on an income DataFrame.

\>>> def subtract\_federal\_tax(df):
...     return df \* 0.9
\>>> def subtract\_state\_tax(df, rate):
...     return df \* (1 \- rate)
\>>> def subtract\_national\_insurance(df, rate, rate\_increase):
...     new\_rate \= rate + rate\_increase
...     return df \* (1 \- new\_rate)

Copy to clipboard

Instead of writing

\>>> subtract\_national\_insurance(
...     subtract\_state\_tax(subtract\_federal\_tax(df), rate\=0.12),
...     rate\=0.05,
...     rate\_increase\=0.02,
... )

Copy to clipboard

You can write

\>>> (
...     df.pipe(subtract\_federal\_tax)
...     .pipe(subtract\_state\_tax, rate\=0.12)
...     .pipe(subtract\_national\_insurance, rate\=0.05, rate\_increase\=0.02)
... )
    Salary   Others
0  5892.48   736.56
1  6997.32      NaN
2  3682.80  1473.12

Copy to clipboard

If you have a function that takes the data as (say) the second argument, pass a tuple indicating which keyword expects the data. For example, suppose `national_insurance` takes its data as `df` in the second argument:

\>>> def subtract\_national\_insurance(rate, df, rate\_increase):
...     new\_rate \= rate + rate\_increase
...     return df \* (1 \- new\_rate)
\>>> (
...     df.pipe(subtract\_federal\_tax)
...     .pipe(subtract\_state\_tax, rate\=0.12)
...     .pipe(
...         (subtract\_national\_insurance, "df"), rate\=0.05, rate\_increase\=0.02
...     )
... )
    Salary   Others
0  5892.48   736.56
1  6997.32      NaN
2  3682.80  1473.12

Copy to clipboard

On this page