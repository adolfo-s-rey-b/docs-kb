[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.select.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.select.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.select.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.select.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.select.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.select.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.select.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.select.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.select.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.select.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.select.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.select.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.select[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select.html#pandas-dataframe-select "Link to this heading")

=====================================================================================================================================================

DataFrame.select(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L6031-L6184)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select.html#pandas.DataFrame.select "Link to this definition")

Select a subset of columns from the DataFrame.

Return a new DataFrame containing the specified columns. Columns can be existing column labels as well as computed columns, expressed via [`pandas.col()`](https://pandas.pydata.org/docs/reference/api/pandas.col.html#pandas.col "pandas.col")
 expressions, or callables passed as keyword arguments.

Added in version 3.1.0.

Parameters:

**\*args**hashable, Expression, or a single list of these

Column labels to select, or expressions evaluated against the DataFrame. Requesting a label twice returns the column twice, and with a `MultiIndex` a non-tuple label selects the entire first level while tuples select from multiple levels. An [`Expression`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expression.html#pandas.api.typing.Expression "pandas.api.typing.Expression")
 evaluating to a Series must be named; use `.rename(...)` to name the result of an unnamed expression. If a single list or other non-tuple sequence (e.g. an `Index` or array) is provided, its elements are the items to select; a sequence cannot be mixed with further positional arguments.

**\*\*kwargs**callable, Expression, Series, scalar, array-like, or dict

Additional computed columns, where each keyword results in a new column with that name and are included in the selection. Values are resolved like the values of [`DataFrame.assign()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign "pandas.DataFrame.assign")
: callables and expressions are evaluated on the DataFrame, and other values are assigned as-is following the alignment and broadcasting rules of `DataFrame.__setitem__()`.

Returns:

DataFrame

A new DataFrame with the selected columns.

See also

[`DataFrame.assign`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign "pandas.DataFrame.assign")

Add new columns to a DataFrame.

[`DataFrame.filter`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html#pandas.DataFrame.filter "pandas.DataFrame.filter")

Subset the DataFrame rows or columns according to labels.

[`DataFrame.select_dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html#pandas.DataFrame.select_dtypes "pandas.DataFrame.select_dtypes")

Select columns based on their dtypes.

[`col`](https://pandas.pydata.org/docs/reference/api/pandas.col.html#pandas.col "pandas.col")

Generate a deferred object representing a column of a DataFrame.

Notes

Items are resolved in order, and computed columns are made available to later items under their name, as in [`DataFrame.assign()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign "pandas.DataFrame.assign")
. A computed column with the same name as an existing column replaces it for later items, but does not replace a column already selected: a name requested more than once is returned more than once.

When the columns are a `MultiIndex`, computed columns must have full-length tuple names so only positional arguments are allowed. Rename expressions with `.rename(...)` when needed.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "first\_name": \["John", "Alice", "Bob"\],
...         "last\_name": \["Smith", "Cooper", "Marley"\],
...         "age": \[61, 22, 35\],
...     }
... )

Copy to clipboard

Select a subset of columns:

\>>> df.select("first\_name", "age")
  first\_name  age
0       John   61
1      Alice   22
2        Bob   35

Copy to clipboard

A single list can also be used to specify the columns to return:

\>>> df.select(\["last\_name", "age"\])
  last\_name  age
0     Smith   61
1    Cooper   22
2    Marley   35

Copy to clipboard

All columns can be selected, but in a different order:

\>>> df.select("last\_name", "first\_name", "age")
  last\_name first\_name  age
0     Smith       John   61
1    Cooper      Alice   22
2    Marley        Bob   35

Copy to clipboard

Note that a DataFrame is always returned. If a single column is requested, a DataFrame with a single column is returned, not a Series:

\>>> df.select("age")
   age
0   61
1   22
2   35

Copy to clipboard

Columns can be computed with [`pandas.col()`](https://pandas.pydata.org/docs/reference/api/pandas.col.html#pandas.col "pandas.col")
 expressions, either positionally (the result keeps the name of the underlying column) or as keyword arguments (the keyword is the resulting column name):

\>>> df.select("first\_name", pd.col("age"), age\_months\=pd.col("age") \* 12)
  first\_name  age  age\_months
0       John   61         732
1      Alice   22         264
2        Bob   35         420

Copy to clipboard

Later items can refer to columns computed earlier in the same call:

\>>> df.select(
...     "first\_name",
...     age\_months\=pd.col("age") \* 12,
...     age\_days\=pd.col("age\_months") \* 30,
... )
  first\_name  age\_months  age\_days
0       John         732     21960
1      Alice         264      7920
2        Bob         420     12600

Copy to clipboard

The `select` method also works when the columns are a `MultiIndex`:

\>>> df \= pd.DataFrame(
...     \[("John", "Smith", 61), ("Alice", "Cooper", 22), ("Bob", "Marley", 35)\],
...     columns\=pd.MultiIndex.from\_tuples(
...         \[("names", "first\_name"), ("names", "last\_name"), ("other", "age")\]
...     ),
... )

Copy to clipboard

If column names are provided, they will select from the first level of the `MultiIndex`:

\>>> df.select("names")
       names
  first\_name last\_name
0       John     Smith
1      Alice    Cooper
2        Bob    Marley

Copy to clipboard

To select from multiple or all levels, tuples can be used:

\>>> df.select(("names", "last\_name"), ("other", "age"))
      names other
  last\_name   age
0     Smith    61
1    Cooper    22
2    Marley    35

Copy to clipboard

On this page