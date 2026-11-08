[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.unit.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.unit[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.unit.html#pandas-timestamp-unit "Link to this heading")

===============================================================================================================================================

Timestamp.unit[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.unit.html#pandas.Timestamp.unit "Link to this definition")

The abbreviation associated with self.\_creso.

This property returns a string representing the time unit of the Timestamp’s resolution. It corresponds to the smallest time unit that can be represented by this Timestamp object. The possible values are: - ‘s’ (second) - ‘ms’ (millisecond) - ‘us’ (microsecond) - ‘ns’ (nanosecond)

Returns:

str

A string abbreviation of the Timestamp’s resolution unit: - ‘s’ for second - ‘ms’ for millisecond - ‘us’ for microsecond - ‘ns’ for nanosecond

See also

[`Timestamp.resolution`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.resolution.html#pandas.Timestamp.resolution "pandas.Timestamp.resolution")

Return resolution of the Timestamp.

[`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")

A duration expressing the difference between two dates or times.

Examples

\>>> pd.Timestamp("2020-01-01 12:34:56").unit
'us'

Copy to clipboard

\>>> pd.Timestamp("2020-01-01 12:34:56.123").unit
'us'

Copy to clipboard

\>>> pd.Timestamp("2020-01-01 12:34:56.123456").unit
'us'

Copy to clipboard

\>>> pd.Timestamp("2020-01-01 12:34:56.123456789").unit
'ns'

Copy to clipboard

On this page