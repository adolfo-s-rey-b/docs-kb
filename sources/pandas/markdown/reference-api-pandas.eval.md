[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.eval.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.eval.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.eval.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.eval.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.eval.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.eval.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.eval.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.eval.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.eval.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.eval.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.eval.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.eval.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.eval.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.eval[#](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas-eval "Link to this heading")

=================================================================================================================

pandas.eval(_expr_, _parser\='pandas'_, _engine\=None_, _local\_dict\=None_, _global\_dict\=None_, _resolvers\=()_, _level\=0_, _target\=None_, _inplace\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/computation/eval.py#L200-L500)
[#](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "Link to this definition")

Evaluate a Python expression as a string using various backends.

Warning

This function can run arbitrary code which can make you vulnerable to code injection if you pass user input to this function.

Parameters:

**expr**str

The expression to evaluate. This string cannot contain any Python [statements](https://docs.python.org/3/reference/simple_stmts.html#simple-statements)
, only Python [expressions](https://docs.python.org/3/reference/simple_stmts.html#expression-statements)
.

By default, with the numexpr engine, the following operations are supported:

*   Arithmetic operations: `+`, `-`, `*`, `/`, `**`, `%`
    
*   Boolean operations: `|` (or), `&` (and), and `~` (not)
    
*   Comparison operators: `<`, `<=`, `==`, `!=`, `>=`, `>`
    

Furthermore, the following mathematical functions are supported:

*   Trigonometric: `sin`, `cos`, `tan`, `arcsin`, `arccos`, `arctan`, `arctan2`, `sinh`, `cosh`, `tanh`, `arcsinh`, `arccosh` and `arctanh`
    
*   Logarithms: `log` natural, `log10` base 10, `log1p` log(1+x)
    
*   Absolute Value `abs`
    
*   Square root `sqrt`
    
*   Exponential `exp` and Exponential minus one `expm1`
    

See the numexpr engine [documentation](https://numexpr.readthedocs.io/en/latest/user_guide.html#supported-functions)
 for further function support details.

Using the `'python'` engine allows the use of native Python operators such as floor division `//`, in addition to built-in and user-defined Python functions.

Additionally, the `'pandas'` parser allows the use of [`and`](https://docs.python.org/3/reference/expressions.html#and "(in Python v3.15)")
, [`or`](https://docs.python.org/3/reference/expressions.html#or "(in Python v3.15)")
, and [`not`](https://docs.python.org/3/reference/expressions.html#not "(in Python v3.15)")
 with the same semantics as the corresponding bitwise operators.

**parser**{‘pandas’, ‘python’}, default ‘pandas’

The parser to use to construct the syntax tree from the expression. The default of `'pandas'` parses code slightly different than standard Python. Alternatively, you can parse an expression using the `'python'` parser to retain strict Python semantics. See the [enhancing performance](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#enhancingperf-eval)
 documentation for more details.

**engine**{‘python’, ‘numexpr’}, optional, default None

The engine used to evaluate the expression. Supported engines are

*   None : tries to use `numexpr`, falls back to `python`
    
*   `'numexpr'` : This is the default engine when `numexpr` is installed. Evaluates pandas objects using numexpr for large speed ups in complex expressions with large frames.
    
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

**target**object, optional, default None

This is the target object for assignment. It is used when there is variable assignment in the expression. If so, then target must support item assignment with string keys, and if a copy is being returned, it must also support .copy().

**inplace**bool, default False

If target is provided, and the expression mutates target, whether to modify target inplace. Otherwise, return a copy of target with the mutation.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

Returns:

ndarray, numeric scalar, DataFrame, Series, or None

The completion value of evaluating the given code or None if `inplace=True`.

Raises:

ValueError

There are many instances where such an error can be raised:

*   target=None, but the expression is multiline.
    
*   The expression is multiline, but not all them have item assignment. An example of such an arrangement is this:
    
    a = b + 1 a + 2
    
    Here, there are expressions on different lines, making it multiline, but the last line has no variable assigned to the output of a + 2.
    
*   inplace=True, but the expression is missing item assignment.
    
*   Item assignment is provided, but the target does not support string item assignment.
    
*   Item assignment is provided and inplace=False, but the target does not support the .copy() method
    

See also

[`DataFrame.query`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "pandas.DataFrame.query")

Evaluates a boolean expression to query the columns of a frame.

[`DataFrame.eval`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html#pandas.DataFrame.eval "pandas.DataFrame.eval")

Evaluate a string describing operations on DataFrame columns.

Notes

The `dtype` of any objects involved in an arithmetic `%` operation are recursively cast to `float64`.

See the [enhancing performance](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#enhancingperf-eval)
 documentation for more details.

Examples

\>>> df \= pd.DataFrame({"animal": \["dog", "pig"\], "age": \[10, 20\]})
\>>> df
  animal  age
0    dog   10
1    pig   20

Copy to clipboard

We can add a new column using `pd.eval`:

\>>> pd.eval("double\_age = df.age \* 2", target\=df)
  animal  age  double\_age
0    dog   10          20
1    pig   20          40

Copy to clipboard

On this page