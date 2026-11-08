[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IntervalDtype.subtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.IntervalDtype.subtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.IntervalDtype.subtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.IntervalDtype.subtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.IntervalDtype.subtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.IntervalDtype.subtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.IntervalDtype.subtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.IntervalDtype.subtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.IntervalDtype.subtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.IntervalDtype.subtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.IntervalDtype.subtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.IntervalDtype.subtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.IntervalDtype.subtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.IntervalDtype.subtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IntervalDtype.subtype[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalDtype.subtype.html#pandas-intervaldtype-subtype "Link to this heading")

====================================================================================================================================================================

property IntervalDtype.subtype[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/dtypes.py#L1365-L1383)
[#](https://pandas.pydata.org/docs/reference/api/pandas.IntervalDtype.subtype.html#pandas.IntervalDtype.subtype "Link to this definition")

The dtype of the Interval bounds.

Each interval in an [`IntervalArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.html#pandas.arrays.IntervalArray "pandas.arrays.IntervalArray")
 has the same data type for its left and right bounds. `subtype` returns that dtype.

See also

[`IntervalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalDtype.html#pandas.IntervalDtype "pandas.IntervalDtype")

An ExtensionDtype for Interval data.

Examples

\>>> dtype \= pd.IntervalDtype(subtype\="int64", closed\="both")
\>>> dtype.subtype
dtype('int64')

Copy to clipboard

On this page