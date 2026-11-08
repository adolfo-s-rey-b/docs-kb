[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodDtype.freq.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.PeriodDtype.freq.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.PeriodDtype.freq.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.PeriodDtype.freq.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.PeriodDtype.freq.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.PeriodDtype.freq.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.PeriodDtype.freq.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.PeriodDtype.freq.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.PeriodDtype.freq.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.PeriodDtype.freq.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.PeriodDtype.freq.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.PeriodDtype.freq.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.PeriodDtype.freq.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.PeriodDtype.freq.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodDtype.freq[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodDtype.freq.html#pandas-perioddtype-freq "Link to this heading")

=====================================================================================================================================================

property PeriodDtype.freq[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/dtypes.py#L1091-L1116)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodDtype.freq.html#pandas.PeriodDtype.freq "Link to this definition")

The frequency object of this PeriodDtype.

The freq property returns the BaseOffset object that represents the frequency of the PeriodDtype. This frequency specifies the interval (e.g., daily, monthly, yearly) associated with the Period type. It is essential for operations that depend on time-based calculations within a period index or series.

See also

[`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")

Represents a period of time.

[`PeriodIndex`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html#pandas.PeriodIndex "pandas.PeriodIndex")

Immutable ndarray holding ordinal values indicating regular periods.

[`PeriodDtype`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodDtype.html#pandas.PeriodDtype "pandas.PeriodDtype")

An ExtensionDtype for Period data.

[`date_range`](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range "pandas.date_range")

Return a fixed frequency range of dates.

Examples

\>>> dtype \= pd.PeriodDtype(freq\="D")
\>>> dtype.freq
<Day>

Copy to clipboard

On this page