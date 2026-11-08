[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.ewm.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.ewm.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.ewm.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.ewm.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.ewm.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.ewm.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.ewm.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.ewm.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.ewm.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.ewm.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.ewm.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.ewm.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.ewm.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.ewm.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.ewm[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.ewm.html#pandas-api-typing-dataframegroupby-ewm "Link to this heading")

==================================================================================================================================================================================================

DataFrameGroupBy.ewm(_com\=None_, _span\=None_, _halflife\=None_, _alpha\=None_, _min\_periods\=0_, _adjust\=True_, _ignore\_na\=False_, _times\=None_, _method\='single'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L3908-L4015)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.ewm.html#pandas.api.typing.DataFrameGroupBy.ewm "Link to this definition")

Return an ewm grouper, providing ewm functionality per group.

The decay can be specified in terms of center of mass, span, half-life, or smoothing factor alpha.

Parameters:

**com**float, optional

Specify decay in terms of center of mass. Alternative to `span`, `halflife`, and `alpha`.

**span**float, optional

Specify decay in terms of span.

**halflife**float, str, or Timedelta, optional

Specify decay in terms of half-life.

**alpha**float, optional

Specify smoothing factor directly.

**min\_periods**int, default 0

Minimum number of observations in the window required to have a value; otherwise, result is `np.nan`.

**adjust**bool, default True

Divide by decaying adjustment factor to account for imbalance in relative weights.

**ignore\_na**bool, default False

Ignore missing values when calculating weights.

**times**str or array-like of datetime64, optional

Times corresponding to the observations.

**method**{‘single’, ‘table’}, default ‘single’

Execute the operation per group independently (`'single'`) or over the entire object before regrouping (`'table'`). Only applicable to `mean()`, and only when using `engine='numba'`.

Returns:

pandas.api.typing.ExponentialMovingWindowGroupBy

An object that supports exponentially weighted moving transformations over each group.

See also

`Series.ewm`

EWM transformations for Series.

`DataFrame.ewm`

EWM transformations for DataFrames.

`Series.groupby`

Apply a function groupby to a Series.

`DataFrame.groupby`

Apply a function groupby.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "Class": \["A", "A", "A", "B", "B", "B"\],
...         "Value": \[10, 20, 30, 40, 50, 60\],
...     }
... )
\>>> df
Class  Value
0     A     10
1     A     20
2     A     30
3     B     40
4     B     50
5     B     60

Copy to clipboard

\>>> df.groupby("Class").ewm(com\=0.5).mean()
             Value
Class
A     0  10.000000
      1  17.500000
      2  26.153846
B     3  40.000000
      4  47.500000
      5  56.153846

Copy to clipboard

On this page