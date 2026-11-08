[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.crosstab.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.crosstab.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.crosstab.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.crosstab.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.crosstab.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.crosstab.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.crosstab.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.crosstab.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.crosstab.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.crosstab.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.crosstab.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.crosstab.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.crosstab[#](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html#pandas-crosstab "Link to this heading")

=============================================================================================================================

pandas.crosstab(_index_, _columns_, _values\=None_, _rownames\=None_, _colnames\=None_, _aggfunc\=None_, _margins\=False_, _margins\_name\='All'_, _dropna\=True_, _normalize\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/reshape/pivot.py#L982-L1208)
[#](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html#pandas.crosstab "Link to this definition")

Compute a simple cross tabulation of two (or more) factors.

By default, computes a frequency table of the factors unless an array of values and an aggregation function are passed.

Parameters:

**index**array-like, Series, or list of arrays/Series

Values to group by in the rows.

**columns**array-like, Series, or list of arrays/Series

Values to group by in the columns.

**values**array-like, optional

Array of values to aggregate according to the factors. Requires aggfunc be specified.

**rownames**sequence, default None

If passed, must match number of row arrays passed.

**colnames**sequence, default None

If passed, must match number of column arrays passed.

**aggfunc**function, optional

If specified, requires values be specified as well.

**margins**bool, default False

Add row/column margins (subtotals).

**margins\_name**str, default ‘All’

Name of the row/column that will contain the totals when margins is True.

**dropna**bool, default True

Do not include columns whose entries are all NaN.

**normalize**bool, {‘all’, ‘index’, ‘columns’}, or {0,1}, default False

Normalize by dividing all values by the sum of values.

*   If passed ‘all’ or True, will normalize over all values.
    
*   If passed ‘index’ will normalize over each row.
    
*   If passed ‘columns’ will normalize over each column.
    
*   If margins is True, will also normalize margin values.
    

Returns:

DataFrame

Cross tabulation of the data.

See also

[`DataFrame.pivot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html#pandas.DataFrame.pivot "pandas.DataFrame.pivot")

Reshape data based on column values.

[`pivot_table`](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html#pandas.pivot_table "pandas.pivot_table")

Create a pivot table as a DataFrame.

Notes

Any Series passed will have their name attributes used unless row or column names for the cross-tabulation are specified.

With the default `dropna=True`, categories without any observed instances in the input are dropped from the cross-tabulation. When `dropna=False`, all categories of any Categorical input are included, even if the actual data does not contain any instances of a particular category.

Series arguments are aligned on their index before tabulating; rows where any value is missing after alignment (e.g. index labels not present in all Series) are dropped. In the event that there aren’t overlapping indexes an empty DataFrame will be returned.

Reference [the user guide](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-crosstabulations)
 for more examples.

Examples

\>>> a \= np.array(
...     \[\
...         "foo",\
...         "foo",\
...         "foo",\
...         "foo",\
...         "bar",\
...         "bar",\
...         "bar",\
...         "bar",\
...         "foo",\
...         "foo",\
...         "foo",\
...     \],
...     dtype\=object,
... )
\>>> b \= np.array(
...     \[\
...         "one",\
...         "one",\
...         "one",\
...         "two",\
...         "one",\
...         "one",\
...         "one",\
...         "two",\
...         "two",\
...         "two",\
...         "one",\
...     \],
...     dtype\=object,
... )
\>>> c \= np.array(
...     \[\
...         "dull",\
...         "dull",\
...         "shiny",\
...         "dull",\
...         "dull",\
...         "shiny",\
...         "shiny",\
...         "dull",\
...         "shiny",\
...         "shiny",\
...         "shiny",\
...     \],
...     dtype\=object,
... )
\>>> pd.crosstab(a, \[b, c\], rownames\=\["a"\], colnames\=\["b", "c"\])
b   one        two
c   dull shiny dull shiny
a
bar    1     2    1     0
foo    2     2    1     2

Copy to clipboard

When values and aggfunc are passed, the values are aggregated within each group instead of counted:

\>>> vals \= np.array(\[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11\])
\>>> pd.crosstab(a, b, values\=vals, aggfunc\="sum", rownames\=\["a"\], colnames\=\["b"\])
b    one  two
a
bar   18    8
foo   17   23

Copy to clipboard

Here ‘c’ and ‘f’ are not represented in the data and will not be shown in the output because dropna is True by default. Set dropna=False to preserve categories with no data.

\>>> foo \= pd.Categorical(\["a", "b"\], categories\=\["a", "b", "c"\])
\>>> bar \= pd.Categorical(\["d", "e"\], categories\=\["d", "e", "f"\])
\>>> pd.crosstab(foo, bar)
col\_0  d  e
row\_0
a      1  0
b      0  1
\>>> pd.crosstab(foo, bar, dropna\=False)
col\_0  d  e  f
row\_0
a      1  0  0
b      0  1  0
c      0  0  0

Copy to clipboard

On this page