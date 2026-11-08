[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.filter.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.filter.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.filter.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.filter.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.filter.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.filter.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.filter.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.filter.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.filter.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.filter.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.filter.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.filter.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.filter[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html#pandas-dataframe-filter "Link to this heading")

=====================================================================================================================================================

DataFrame.filter(_arg\=None_, _/_, _like\=None_, _regex\=None_, _axis\=None_, _\*_, _items\=None_, _cond\=None_, _na\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L5630-L5896)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html#pandas.DataFrame.filter "Link to this definition")

Subset the rows or columns according to a boolean mask or the labels.

Rows (or columns with `axis=1`) are kept where a boolean mask is True, or selected by their labels with `items`, `like`, or `regex`.

Parameters:

**arg**callable, expression, or list-like, optional

Positional-only. A callable or an expression created with [`pandas.col()`](https://pandas.pydata.org/docs/reference/api/pandas.col.html#pandas.col "pandas.col")
 is a boolean mask, see `cond`. Any other list-like selects labels, see `items`. A list-like of booleans also selects labels, but since it is likely intended as a mask a warning is issued; pass `items` or `cond` instead to be explicit.

**like**str

Keep labels from axis for which “like in label == True”. This will be deprecated in a future version; use `obj.filter(lambda obj: obj.columns.astype(str).str.contains(like, regex=False), axis=1)` instead.

**regex**str (regular expression)

Keep labels from axis for which re.search(regex, label) == True. This will be deprecated in a future version; use `obj.filter(lambda obj: obj.columns.astype(str).str.contains(regex), axis=1)` instead.

**axis**{0 or ‘index’, 1 or ‘columns’, None}, default None

The axis to filter on, expressed either as an index (int) or axis name (str). Defaults to the index for a boolean mask, and to the info axis (‘columns’ for `DataFrame`) when selecting labels. An expression only supports the index. For `Series` this parameter is unused and defaults to `None`.

**items**list-like, optional

Keep labels from axis which are in `items`. This will be deprecated in a future version; use [`DataFrame.select()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select.html#pandas.DataFrame.select "pandas.DataFrame.select")
 when all of `items` are present in the columns, or `obj.loc[:, pd.Index(items).intersection(obj.columns)]` (or the equivalent for the index) otherwise.

**cond**array-like of bool, callable, or expression, optional

A boolean mask selecting the entries to keep. A [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 is aligned with the labels of the filtered axis; any other array-like must have the same length as that axis. A callable is called with the object and must return a boolean mask. An expression such as `pd.col("a") > 1` is evaluated against the DataFrame and is only supported with `axis=0`.

Added in version 3.1.0.

**na**{“raise”, True, False}, default False

How to treat missing values in a boolean mask. `True` or `False` treats missing values as that value, matching `obj[mask]` for a mask with nullable boolean dtype; `"raise"` raises a `ValueError`. Ignored when selecting labels.

Added in version 3.1.0.

Returns:

Same type as caller

The filtered subset of the DataFrame or Series.

Raises:

TypeError

If none or more than one of the positional argument, `items`, `cond`, `like`, and `regex` is passed, or if `cond` is not a one-dimensional boolean mask.

ValueError

If a mask contains missing values and `na="raise"`, if a boolean array is not one-dimensional, or if an expression is passed with `axis=1`.

IndexError

If a mask that is not a Series has a different length than the filtered axis.

IndexingError

If a Series mask cannot be aligned with the filtered axis.

Warns:

UserWarning

If a list-like of booleans is passed positionally.

See also

[`DataFrame.loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc")

Access a group of rows and columns by label(s) or a boolean array.

[`DataFrame.where`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.where.html#pandas.DataFrame.where "pandas.DataFrame.where")

Replace values where the condition is False.

Notes

The positional argument is a boolean mask only when it is a callable or an expression; any other value, including a list-like of booleans, selects labels. Use `cond` to filter with a boolean array or [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
.

Selecting labels with `items`, `like`, or `regex` will be deprecated in a future version.

Examples

\>>> df \= pd.DataFrame(
...     {"one": \[1, 4\], "two": \[2, 5\], "three": \[3, 6\]},
...     index\=\["mouse", "rabbit"\],
... )
\>>> df
        one  two  three
mouse     1    2      3
rabbit    4    5      6

Copy to clipboard

Filter rows with a boolean Series.

\>>> df.filter(cond\=df\["two"\] \> 2)
        one  two  three
rabbit    4    5      6

Copy to clipboard

The same using an expression or a callable, which are convenient in method chains and may be passed positionally.

\>>> df.filter(pd.col("two") \> 2)
        one  two  three
rabbit    4    5      6
\>>> df.filter(lambda df: df\["two"\] \> 2)
        one  two  three
rabbit    4    5      6

Copy to clipboard

Filter columns with a boolean array.

\>>> df.filter(cond\=df.columns.str.endswith("e"), axis\=1)
        one  three
mouse     1      3
rabbit    4      6

Copy to clipboard

Missing values in the mask are treated as False by default; pass `na="raise"` to raise instead, or `na=True` to keep them.

\>>> mask \= pd.array(\[True, None\], dtype\="boolean")
\>>> df.filter(cond\=mask)
       one  two  three
mouse    1    2      3
\>>> df.filter(cond\=mask, na\=True)
        one  two  three
mouse     1    2      3
rabbit    4    5      6

Copy to clipboard

Select columns by their labels.

\>>> df.filter(items\=\["one", "three"\])
        one  three
mouse     1      3
rabbit    4      6
\>>> df.filter(regex\="e$", axis\=1)
        one  three
mouse     1      3
rabbit    4      6
\>>> df.filter(like\="bbi", axis\=0)
        one  two  three
rabbit    4    5      6

Copy to clipboard

On this page