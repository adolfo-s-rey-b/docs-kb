[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.components.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.components.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.components.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.components.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.components.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.components.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.components.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.components.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.components.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.components.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.components.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.components.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.components.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.components.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.components[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.components.html#pandas-series-dt-components "Link to this heading")

=================================================================================================================================================================

Series.dt.components[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/accessors.py#L594-L635)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.components.html#pandas.Series.dt.components "Link to this definition")

Return a Dataframe of the components of the Timedeltas.

Each row of the DataFrame corresponds to a Timedelta in the original Series and contains the individual components (days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds) of the Timedelta.

Returns:

DataFrame

See also

[`TimedeltaIndex.components`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.components.html#pandas.TimedeltaIndex.components "pandas.TimedeltaIndex.components")

Return a DataFrame of the individual resolution components of the Timedeltas.

[`Series.dt.total_seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.total_seconds.html#pandas.Series.dt.total_seconds "pandas.Series.dt.total_seconds")

Return the total number of seconds in the duration.

Examples

\>>> s \= pd.Series(pd.to\_timedelta(np.arange(5), unit\="s"))
\>>> s
0   0 days 00:00:00
1   0 days 00:00:01
2   0 days 00:00:02
3   0 days 00:00:03
4   0 days 00:00:04
dtype: timedelta64\[us\]
\>>> s.dt.components
   days  hours  minutes  seconds  milliseconds  microseconds  nanoseconds
0     0      0        0        0             0             0            0
1     0      0        0        1             0             0            0
2     0      0        0        2             0             0            0
3     0      0        0        3             0             0            0
4     0      0        0        4             0             0            0

Copy to clipboard

On this page