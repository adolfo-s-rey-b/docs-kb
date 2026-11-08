[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalDtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.IntervalDtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.IntervalDtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.IntervalDtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.IntervalDtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.IntervalDtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.IntervalDtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.IntervalDtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.IntervalDtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.IntervalDtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.IntervalDtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.IntervalDtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.IntervalDtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.IntervalDtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalDtype[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalDtype.html#pandas-intervaldtype "Link to this heading")

============================================================================================================================================

class pandas.IntervalDtype(_subtype\=None_, _closed\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/dtypes.py#L1242-L1532)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalDtype.html#pandas.IntervalDtype "Link to this definition")

An ExtensionDtype for Interval data.

**This is not an actual numpy dtype**, but a duck type.

Parameters:

**subtype**str, np.dtype

The dtype of the Interval bounds.

**closed**{‘right’, ‘left’, ‘both’, ‘neither’}, default ‘right’

Whether the interval is closed on the left-side, right-side, both or neither. See the Notes for more detailed explanation.

Attributes

|     |     |
| --- | --- |
| [`subtype`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalDtype.subtype.html#pandas.IntervalDtype.subtype "pandas.IntervalDtype.subtype") | The dtype of the Interval bounds. |

See also

[`PeriodDtype`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodDtype.html#pandas.PeriodDtype "pandas.PeriodDtype")

An ExtensionDtype for Period data.

Examples

\>>> pd.IntervalDtype(subtype\="int64", closed\="both")
interval\[int64, both\]

Copy to clipboard

On this page