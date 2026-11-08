[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.UndefinedVariableError.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.UndefinedVariableError.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.UndefinedVariableError.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.UndefinedVariableError.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.UndefinedVariableError.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.UndefinedVariableError.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.UndefinedVariableError.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.UndefinedVariableError.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.UndefinedVariableError.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.UndefinedVariableError.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.UndefinedVariableError.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.UndefinedVariableError.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.UndefinedVariableError.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.UndefinedVariableError.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.UndefinedVariableError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.UndefinedVariableError.html#pandas-errors-undefinedvariableerror "Link to this heading")

============================================================================================================================================================================================

exception pandas.errors.UndefinedVariableError(_name_, _is\_local\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L738-L775)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.UndefinedVariableError.html#pandas.errors.UndefinedVariableError "Link to this definition")

Exception raised by `query` or `eval` when using an undefined variable name.

It will also specify whether the undefined variable is local or not.

Parameters:

**name**str

The name of the undefined variable.

**is\_local**bool or None, optional

Indicates whether the undefined variable is considered a local variable. If `True`, the error message specifies it as a local variable. If `False` or `None`, the variable is treated as a non-local name.

See also

`DataFrame.query`

Query the columns of a DataFrame with a boolean expression.

`DataFrame.eval`

Evaluate a string describing operations on DataFrame columns.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 1, 1\]})
\>>> df.query("A > x")
... \# UndefinedVariableError: name 'x' is not defined
\>>> df.query("A > @y")
... \# UndefinedVariableError: local variable 'y' is not defined
\>>> pd.eval("x + 1")
... \# UndefinedVariableError: name 'x' is not defined

Copy to clipboard

On this page