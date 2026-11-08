[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.strftime.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.PeriodIndex.strftime.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.strftime.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.PeriodIndex.strftime.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.PeriodIndex.strftime.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.PeriodIndex.strftime.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.PeriodIndex.strftime.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.PeriodIndex.strftime.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.PeriodIndex.strftime.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.PeriodIndex.strftime.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.PeriodIndex.strftime.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.PeriodIndex.strftime.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.PeriodIndex.strftime.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.PeriodIndex.strftime.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.strftime[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.strftime.html#pandas-periodindex-strftime "Link to this heading")

=================================================================================================================================================================

PeriodIndex.strftime(_date\_format_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L278-L311)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.strftime.html#pandas.PeriodIndex.strftime "Link to this definition")

Convert to Index using specified date\_format.

Return an Index of formatted strings specified by date\_format, which supports the same string format as the python standard library. Details of the string format can be found in [python string format doc](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
. [`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")
 objects additionally support several directives not covered there, detailed in [`Period.strftime()`](https://pandas.pydata.org/docs/reference/api/pandas.Period.strftime.html#pandas.Period.strftime "pandas.Period.strftime")
.

Parameters:

**date\_format**str

Date format string (e.g. “%Y-%m-%d”).

Returns:

Index

Index of formatted strings.

See also

[`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")

Convert the given argument to datetime.

[`Period.strftime`](https://pandas.pydata.org/docs/reference/api/pandas.Period.strftime.html#pandas.Period.strftime "pandas.Period.strftime")

Format a single Period.

Examples

\>>> idx \= pd.PeriodIndex(\["2023-01", "2023-02", "2023-03"\], freq\="M")
\>>> idx.strftime("%B %d, %Y")
Index(\['January 31, 2023', 'February 28, 2023', 'March 31, 2023'\], dtype='str')

Copy to clipboard

On this page