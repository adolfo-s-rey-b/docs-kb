[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.isoformat.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta.isoformat[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.isoformat.html#pandas-timedelta-isoformat "Link to this heading")

==============================================================================================================================================================

Timedelta.isoformat()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.isoformat.html#pandas.Timedelta.isoformat "Link to this definition")

Format the Timedelta as ISO 8601 Duration.

`P[n]Y[n]M[n]DT[n]H[n]M[n]S`, where the `[n]` s are replaced by the values. See Wikipedia: [ISO 8601 § Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations)
.

Returns:

str

See also

[`Timestamp.isoformat`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoformat.html#pandas.Timestamp.isoformat "pandas.Timestamp.isoformat")

Function is used to convert the given Timestamp object into the ISO format.

Notes

The longest component is days, whose value may be larger than 365. Every component is always included, even if its value is 0. Pandas uses nanosecond precision, so up to 9 decimal places may be included in the seconds component. Trailing 0’s are removed from the seconds component after the decimal. We do not 0 pad components, so it’s …T5H…, not …T05H…

Examples

\>>> td \= pd.Timedelta(days\=6, minutes\=50, seconds\=3,
...                   milliseconds\=10, microseconds\=10, nanoseconds\=12)

Copy to clipboard

\>>> td.isoformat()
'P6DT0H50M3.010010012S'
\>>> pd.Timedelta(hours\=1, seconds\=10).isoformat()
'P0DT1H0M10S'
\>>> pd.Timedelta(days\=500.5).isoformat()
'P500DT12H0M0S'

Copy to clipboard

On this page