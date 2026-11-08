[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.arrays.PeriodArray.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.PeriodArray.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.arrays.PeriodArray.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.arrays.PeriodArray.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.arrays.PeriodArray.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.arrays.PeriodArray.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.arrays.PeriodArray.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.arrays.PeriodArray.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.arrays.PeriodArray.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.arrays.PeriodArray.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.arrays.PeriodArray.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.arrays.PeriodArray.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.arrays.PeriodArray.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.arrays.PeriodArray.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.arrays.PeriodArray[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.PeriodArray.html#pandas-arrays-periodarray "Link to this heading")

===========================================================================================================================================================

class pandas.arrays.PeriodArray(_values_, _dtype\=None_, _copy\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/period.py#L124-L1329)
[#](https://pandas.pydata.org/docs/reference/api/pandas.arrays.PeriodArray.html#pandas.arrays.PeriodArray "Link to this definition")

Pandas ExtensionArray for storing Period data.

Users should use [`array()`](https://pandas.pydata.org/docs/reference/api/pandas.array.html#pandas.array "pandas.array")
 to create new instances.

Parameters:

**values**Union\[PeriodArray, Series\[period\], ndarray\[int\], PeriodIndex\]

The data to store. These should be arrays that can be directly converted to ordinals without inference or copy (PeriodArray, ndarray\[int64\]), or a box around such an array (Series\[period\], PeriodIndex).

**dtype**PeriodDtype, optional

A PeriodDtype instance from which to extract a freq. If both freq and dtype are specified, then the frequencies must match.

**copy**bool, default False

Whether to copy the ordinals before storing.

See also

`Period`

Represents a period of time.

`PeriodIndex`

Immutable Index for period data.

`period_range`

Create a fixed-frequency PeriodArray.

[`array`](https://docs.python.org/3/library/array.html#module-array "(in Python v3.15)")

Construct a pandas array.

Notes

There are two components to a PeriodArray

*   ordinals : integer ndarray
    
*   freq : pd.tseries.offsets.Offset
    

The values are physically stored as a 1-D ndarray of integers. These are called “ordinals” and represent some kind of offset from a base.

The freq indicates the span covered by each element of the array. All elements in the PeriodArray have the same freq.

Examples

\>>> pd.arrays.PeriodArray(pd.PeriodIndex(\["2023-01-01", "2023-01-02"\], freq\="D"))
<PeriodArray>
\['2023-01-01', '2023-01-02'\]
Length: 2, dtype: period\[D\]

Copy to clipboard

On this page