[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.NumExprClobberingError.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.NumExprClobberingError.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.NumExprClobberingError.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.NumExprClobberingError.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.NumExprClobberingError.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.NumExprClobberingError.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.NumExprClobberingError.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.NumExprClobberingError.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.NumExprClobberingError.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.NumExprClobberingError.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.NumExprClobberingError.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.NumExprClobberingError.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.NumExprClobberingError.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.NumExprClobberingError.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.NumExprClobberingError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.NumExprClobberingError.html#pandas-errors-numexprclobberingerror "Link to this heading")

============================================================================================================================================================================================

exception pandas.errors.NumExprClobberingError[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L714-L735)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.NumExprClobberingError.html#pandas.errors.NumExprClobberingError "Link to this definition")

Exception raised when trying to use a built-in numexpr name as a variable name.

`eval` or `query` will throw the error if the engine is set to ‘numexpr’. ‘numexpr’ is the default engine value for these methods if the numexpr package is installed.

See also

[`eval`](https://docs.python.org/3/builtins/functions.html#eval "(in Python v3.15)")

Evaluate a Python expression as a string using various backends.

`DataFrame.query`

Query the columns of a DataFrame with a boolean expression.

Examples

\>>> df \= pd.DataFrame({"abs": \[1, 1, 1\]})
\>>> df.query("abs > 2")
... \# NumExprClobberingError: Variables in expression "(abs) > (2)" overlap...
\>>> sin, a \= 1, 2
\>>> pd.eval("sin + a", engine\="numexpr")
... \# NumExprClobberingError: Variables in expression "(sin) + (a)" overlap...

Copy to clipboard

On this page