[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.query.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.query.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.query.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.query.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.query.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.query.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.query.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.query.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.query.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.query.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.query.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.query.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.query[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas-dataframe-query "Link to this heading")

==================================================================================================================================================

DataFrame.query(_expr_, _\*_, _parser\='pandas'_, _engine\=None_, _local\_dict\=None_, _global\_dict\=None_, _resolvers\=None_, _level\=0_, _inplace\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L5027-L5261)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "Link to this definition")

Query the columns of a DataFrame with a boolean expression.

Warning

This method can run arbitrary code which can make you vulnerable to code injection if you pass user input to this function.

Parameters:

**expr**str

The query string to evaluate.

See the documentation for [`eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 for details of supported operations and functions in the query string.

See the documentation for [`DataFrame.eval()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html#pandas.DataFrame.eval "pandas.DataFrame.eval")
 for details on referring to column names and variables in the query string.

**parser**{‘pandas’, ‘python’}, default ‘pandas’

The parser to use to construct the syntax tree from the expression. The default of `'pandas'` parses code slightly different than standard Python. Alternatively, you can parse an expression using the `'python'` parser to retain strict Python semantics. See the [enhancing performance](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#enhancingperf-eval)
 documentation for more details.

**engine**{‘python’, ‘numexpr’}, default ‘numexpr’

The engine used to evaluate the expression. Supported engines are

*   None : tries to use `numexpr`, falls back to `python`
    
*   `'numexpr'` : This default engine evaluates pandas objects using numexpr for large speed ups in complex expressions with large frames.
    
*   `'python'` : Performs operations as if you had `eval`’d in top level python. This engine is generally not that useful.
    

More backends may be available in the future.

**local\_dict**dict or None, optional

A dictionary of local variables, taken from locals() by default.

**global\_dict**dict or None, optional

A dictionary of global variables, taken from globals() by default.

**resolvers**list of dict-like or None, optional

A list of objects implementing the `__getitem__` special method that you can use to inject an additional collection of namespaces to use for variable lookup. For example, this is used in the [`query()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "pandas.DataFrame.query")
 method to inject the `DataFrame.index` and `DataFrame.columns` variables that refer to their respective [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 instance attributes.

**level**int, optional

The number of prior stack frames to traverse and add to the current scope. Most users will **not** need to change this parameter.

**inplace**bool

Whether to modify the DataFrame rather than creating a new one.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

Returns:

DataFrame or None

DataFrame resulting from the provided query expression or None if `inplace=True`.

Raises:

ValueError

If `expr` refers to a column label that is not unique and still evaluates to a DataFrame, since there is then no row mask to select with. Reducing those columns back to one dimension, as in `df.query("a.max(axis=1) > 4")`, is fine.

See also

[`eval`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")

Evaluate a string describing operations on DataFrame columns.

[`DataFrame.eval`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html#pandas.DataFrame.eval "pandas.DataFrame.eval")

Evaluate a string describing operations on DataFrame columns.

Notes

The result of the evaluation of this expression is first passed to [`DataFrame.loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc")
 and if that fails because of a multidimensional key (e.g., a DataFrame) then the result will be passed to `DataFrame.__getitem__()`.

This method uses the top-level [`eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 function to evaluate the passed query.

The [`query()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "pandas.DataFrame.query")
 method uses a slightly modified Python syntax by default. For example, the `&` and `|` (bitwise) operators have the precedence of their boolean cousins, [`and`](https://docs.python.org/3/reference/expressions.html#and "(in Python v3.15)")
 and [`or`](https://docs.python.org/3/reference/expressions.html#or "(in Python v3.15)")
. This _is_ syntactically valid Python, however the semantics are different.

You can change the semantics of the expression by passing the keyword argument `parser='python'`. This enforces the same semantics as evaluation in Python space. Likewise, you can pass `engine='python'` to evaluate an expression using Python itself as a backend. This is not recommended as it is inefficient compared to using `numexpr` as the engine.

The [`DataFrame.index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html#pandas.DataFrame.index "pandas.DataFrame.index")
 and [`DataFrame.columns`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html#pandas.DataFrame.columns "pandas.DataFrame.columns")
 attributes of the [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 instance are placed in the query namespace by default, which allows you to treat both the index and columns of the frame as a column in the frame. The identifier `index` is used for the frame index; you can also use the name of the index to identify it in a query. Please note that Python keywords may not be used as identifiers.

For further details and examples see the `query` documentation in [indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-query)
.

_Backtick quoted variables_

Backtick quoted variables are parsed as literal Python code and are converted internally to a Python valid identifier. This can lead to the following problems.

During parsing a number of disallowed characters inside the backtick quoted string are replaced by strings that are allowed as a Python identifier. These characters include all operators in Python, the space character, the question mark, the exclamation mark, the dollar sign, and the euro sign.

A backtick can be escaped by double backticks.

See also the [Python documentation about lexical analysis](https://docs.python.org/3/reference/lexical_analysis.html)
 in combination with the source code in `pandas.core.computation.parsing`.

Examples

\>>> df \= pd.DataFrame(
...     {"A": range(1, 6), "B": range(10, 0, \-2), "C&C": range(10, 5, \-1)}
... )
\>>> df
   A   B  C&C
0  1  10   10
1  2   8    9
2  3   6    8
3  4   4    7
4  5   2    6
\>>> df.query("A > B")
   A  B  C&C
4  5  2    6

Copy to clipboard

The previous expression is equivalent to

\>>> df\[df.A \> df.B\]
   A  B  C&C
4  5  2    6

Copy to clipboard

For columns with spaces in their name, you can use backtick quoting.

\>>> df.query("B == \`C&C\`")
   A   B  C&C
0  1  10   10

Copy to clipboard

The previous expression is equivalent to

\>>> df\[df.B \== df\["C&C"\]\]
   A   B  C&C
0  1  10   10

Copy to clipboard

Using local variable:

\>>> local\_var \= 2
\>>> df.query("A <= @local\_var")
A   B  C&C
0  1  10   10
1  2   8    9

Copy to clipboard

On this page