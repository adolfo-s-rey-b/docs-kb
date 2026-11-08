[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.NamedAgg.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.NamedAgg[#](https://pandas.pydata.org/docs/reference/api/pandas.NamedAgg.html#pandas-namedagg "Link to this heading")

=============================================================================================================================

class pandas.NamedAgg(_column_, _aggfunc_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/generic.py#L107-L189)
[#](https://pandas.pydata.org/docs/reference/api/pandas.NamedAgg.html#pandas.NamedAgg "Link to this definition")

Helper for column specific aggregation with control over output column names.

A dataclass used with `DataFrame.groupby().agg()` to specify an aggregation on a particular column and assign a custom name to the resulting column. Additional positional and keyword arguments can be forwarded to the aggregation function.

Parameters:

**column**Hashable

Column label in the DataFrame to apply aggfunc.

**aggfunc**function or str

Function to apply to the provided column. If string, the name of a built-in pandas function.

**\*args, \*\*kwargs**Any

Optional positional and keyword arguments passed to `aggfunc`.

See also

[`DataFrame.groupby`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby "pandas.DataFrame.groupby")

Group DataFrame using a mapper or by a Series of columns.

Examples

\>>> df \= pd.DataFrame({"key": \[1, 1, 2\], "a": \[\-1, 0, 1\], 1: \[10, 11, 12\]})
\>>> agg\_a \= pd.NamedAgg(column\="a", aggfunc\="min")
\>>> agg\_1 \= pd.NamedAgg(column\=1, aggfunc\=lambda x: np.mean(x))
\>>> df.groupby("key").agg(result\_a\=agg\_a, result\_1\=agg\_1)
    result\_a  result\_1
key
1          -1      10.5
2           1      12.0

Copy to clipboard

\>>> def n\_between(ser, low, high, \*\*kwargs):
...     return ser.between(low, high, \*\*kwargs).sum()

Copy to clipboard

\>>> agg\_between \= pd.NamedAgg("a", n\_between, 0, 1)
\>>> df.groupby("key").agg(count\_between\=agg\_between)
    count\_between
key
1               1
2               1

Copy to clipboard

\>>> agg\_between\_kw \= pd.NamedAgg("a", n\_between, 0, 1, inclusive\="both")
\>>> df.groupby("key").agg(count\_between\_kw\=agg\_between\_kw)
    count\_between\_kw
key
1                   1
2                   1

Copy to clipboard

Attributes

|     |     |
| --- | --- |
| `args` |     |

Methods

On this page