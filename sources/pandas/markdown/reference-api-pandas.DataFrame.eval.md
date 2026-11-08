[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.eval.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.eval.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.eval.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.eval.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.eval.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.eval.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.eval.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.eval.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.eval.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.eval.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.eval.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.eval.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.eval[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html#pandas-dataframe-eval "Link to this heading")

===============================================================================================================================================

DataFrame.eval(_expr_, _\*_, _inplace\=<no\_default>_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L5269-L5437)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html#pandas.DataFrame.eval "Link to this definition")

Evaluate a string describing operations on DataFrame columns.

Warning

This method can run arbitrary code which can make you vulnerable to code injection if you pass user input to this function.

Operates on columns only, not specific rows or elements. This allows eval to run arbitrary code, which can make you vulnerable to code injection if you pass user input to this function.

Parameters:

**expr**str

The expression string to evaluate.

You can refer to variables in the environment by prefixing them with an ‘@’ character like `@a + b`.

You can refer to column names that are not valid Python variable names by surrounding them in backticks. Thus, column names containing spaces or punctuation (besides underscores) or starting with digits must be surrounded by backticks. (For example, a column named “Area (cm^2)” would be referenced as `` `Area (cm^2)` ``). Column names which are Python keywords (like “if”, “for”, “import”, etc) cannot be used.

For example, if one of your columns is called `a a` and you want to sum it with `b`, your query should be `` `a a` + b ``.

See the documentation for [`eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 for full details of supported operations and functions in the expression string.

**inplace**bool, default False

If the expression contains an assignment, whether to perform the operation inplace and mutate the existing DataFrame. Otherwise, a new DataFrame is returned.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

**\*\*kwargs**

See the documentation for [`eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 for complete details on the keyword arguments accepted by [`eval()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html#pandas.DataFrame.eval "pandas.DataFrame.eval")
.

Returns:

ndarray, scalar, pandas object, or None

The result of the evaluation or None if `inplace=True`.

See also

[`DataFrame.query`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "pandas.DataFrame.query")

Evaluates a boolean expression to query the columns of a frame.

[`DataFrame.assign`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign "pandas.DataFrame.assign")

Can evaluate an expression or function to create new values for a column.

[`eval`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")

Evaluate a Python expression as a string using various backends.

Notes

For more details see the API documentation for [`eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
. For detailed examples see [enhancing performance with eval](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#enhancingperf-eval)
.

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
\>>> df.eval("A + B")
0    11
1    10
2     9
3     8
4     7
dtype: int64

Copy to clipboard

Assignment is allowed though by default the original DataFrame is not modified.

\>>> df.eval("D = A + B")
   A   B  C&C   D
0  1  10   10  11
1  2   8    9  10
2  3   6    8   9
3  4   4    7   8
4  5   2    6   7
\>>> df
   A   B  C&C
0  1  10   10
1  2   8    9
2  3   6    8
3  4   4    7
4  5   2    6

Copy to clipboard

Multiple columns can be assigned to using multi-line expressions:

\>>> df.eval(
... '''
... D = A + B
... E = A - B
... '''
... )
   A   B  C&C   D  E
0  1  10   10  11 -9
1  2   8    9  10 -6
2  3   6    8   9 -3
3  4   4    7   8  0
4  5   2    6   7  3

Copy to clipboard

For columns with spaces or other disallowed characters in their name, you can use backtick quoting.

\>>> df.eval("B \* \`C&C\`")
0    100
1     72
2     48
3     28
4     12
dtype: int64

Copy to clipboard

Local variables shall be explicitly referenced using `@` character in front of the name:

\>>> local\_var \= 2
\>>> df.eval("@local\_var \* A")
0     2
1     4
2     6
3     8
4    10
Name: A, dtype: int64

Copy to clipboard

On this page