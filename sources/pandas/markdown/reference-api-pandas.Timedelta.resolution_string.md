[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.resolution_string.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta.resolution\_string[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.resolution_string.html#pandas-timedelta-resolution-string "Link to this heading")

=======================================================================================================================================================================================

Timedelta.resolution\_string[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.resolution_string.html#pandas.Timedelta.resolution_string "Link to this definition")

Return a string representing the lowest timedelta resolution.

Each timedelta has a defined resolution that represents the lowest OR most granular level of precision. Each level of resolution is represented by a short string as defined below:

Resolution: Return value

*   Days: ‘D’
    
*   Hours: ‘h’
    
*   Minutes: ‘min’
    
*   Seconds: ‘s’
    
*   Milliseconds: ‘ms’
    
*   Microseconds: ‘us’
    
*   Nanoseconds: ‘ns’
    

Returns:

str

Timedelta resolution.

See also

[`Timedelta.components`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.components.html#pandas.Timedelta.components "pandas.Timedelta.components")

Return all components of the Timedelta as a namedtuple-like.

[`Timedelta.resolution`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.resolution.html#pandas.Timedelta.resolution "pandas.Timedelta.resolution")

Return the smallest possible difference between non-equal Timedelta objects.

Examples

\>>> td \= pd.Timedelta('1 days 2 min 3 us 42 ns')
\>>> td.resolution\_string
'ns'

Copy to clipboard

\>>> td \= pd.Timedelta('1 days 2 min 3 us')
\>>> td.resolution\_string
'us'

Copy to clipboard

\>>> td \= pd.Timedelta('2 min 3 s')
\>>> td.resolution\_string
's'

Copy to clipboard

\>>> td \= pd.Timedelta(36, unit\='us')
\>>> td.resolution\_string
'us'

Copy to clipboard

On this page