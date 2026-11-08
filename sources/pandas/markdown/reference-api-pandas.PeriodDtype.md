[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodDtype.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodDtype[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodDtype.html#pandas-perioddtype "Link to this heading")

======================================================================================================================================

class pandas.PeriodDtype(_freq_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/dtypes.py#L1000-L1239)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodDtype.html#pandas.PeriodDtype "Link to this definition")

An ExtensionDtype for Period data.

**This is not an actual numpy dtype**, but a duck type.

Parameters:

**freq**str or DateOffset

The frequency of this PeriodDtype.

Attributes

|     |     |
| --- | --- |
| [`freq`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodDtype.freq.html#pandas.PeriodDtype.freq "pandas.PeriodDtype.freq") | The frequency object of this PeriodDtype. |

See also

[`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")

Represents a single time period.

[`PeriodIndex`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html#pandas.PeriodIndex "pandas.PeriodIndex")

Immutable index for period data.

[`date_range`](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range "pandas.date_range")

Return a fixed frequency DatetimeIndex.

[`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")

One-dimensional array with axis labels.

[`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")

Two-dimensional, size-mutable, potentially heterogeneous tabular data.

Examples

\>>> pd.PeriodDtype(freq\="D")
period\[D\]

Copy to clipboard

\>>> pd.PeriodDtype(freq\=pd.offsets.MonthEnd())
period\[M\]

Copy to clipboard

On this page