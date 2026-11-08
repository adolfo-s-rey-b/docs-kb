[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expression.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Expression.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expression.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Expression.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Expression.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Expression.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Expression.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Expression.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Expression.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Expression.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Expression.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Expression.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Expression.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Expression.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Expression[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expression.html#pandas-api-typing-expression "Link to this heading")

====================================================================================================================================================================

class pandas.api.typing.Expression(_func_, _repr\_str_, _needs\_parenthese\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/col.py#L80-L395)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expression.html#pandas.api.typing.Expression "Link to this definition")

Class representing a deferred expression evaluated against a DataFrame.

Expressions are initially created via `pd.col` and can be composed using arithmetic, comparison, and any method or attribute that the underlying object supports. This includes NumPy ufuncs, indexing, and the boolean operators `&`, `|`, and `~`.

Expressions are solely intended for use in expression-based APIs, such as [`DataFrame.assign`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign "pandas.DataFrame.assign")
 and [`DataFrame.loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc")
, where they are evaluated against the DataFrame they are passed to.

This is not meant to be instantiated directly. Instead, use [`pandas.col()`](https://pandas.pydata.org/docs/reference/api/pandas.col.html#pandas.col "pandas.col")
.

See also

[`pandas.col`](https://pandas.pydata.org/docs/reference/api/pandas.col.html#pandas.col "pandas.col")

Create a deferred column reference.

Notes

The attributes that are available depend on the expression and where it is used. Attribute access is itself deferred: it is applied to the result of evaluating the expression, so an attribute that is not supported by that result raises when the expression is evaluated.

Examples

\>>> df \= pd.DataFrame({"a": \[1, 2\], "b": \[3, 4\]})
\>>> df.assign(c\=pd.col("a") + pd.col("b"))
   a  b  c
0  1  3  4
1  2  4  6

Copy to clipboard

On this page