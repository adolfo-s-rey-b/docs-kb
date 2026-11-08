[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.frequencies.to_offset.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.frequencies.to\_offset[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.frequencies.to_offset.html#pandas-tseries-frequencies-to-offset "Link to this heading")

=============================================================================================================================================================================================

pandas.tseries.frequencies.to\_offset(_freq_, _is\_period\=False_)[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.frequencies.to_offset.html#pandas.tseries.frequencies.to_offset "Link to this definition")

Return DateOffset object from string or datetime.timedelta object.

This function converts a frequency string (e.g. `"5min"`, `"1D1h"`, `"2W"`) or a `datetime.timedelta` into a pandas `DateOffset` subclass. It can also pass through existing `BaseOffset` instances unchanged.

Parameters:

**freq**str, datetime.timedelta, BaseOffset or None

The frequency represented.

**is\_period**bool, default False

Convert string denoting period frequency to corresponding offsets frequency if is\_period=True.

Returns:

BaseOffset subclass or None

Raises:

ValueError

If freq is an invalid frequency

See also

`BaseOffset`

Standard kind of date increment used for a date range.

Examples

\>>> from pandas.tseries.frequencies import to\_offset
\>>> to\_offset("5min")
<5 \* Minutes>

Copy to clipboard

\>>> to\_offset("1D1h")
<25 \* Hours>

Copy to clipboard

\>>> to\_offset("2W")
<2 \* Weeks: weekday=6>

Copy to clipboard

\>>> to\_offset("2B")
<2 \* BusinessDays>

Copy to clipboard

\>>> to\_offset(pd.Timedelta(days\=1))
<24 \* Hours>

Copy to clipboard

\>>> to\_offset(pd.offsets.Hour())
<Hour>

Copy to clipboard

Passing the parameter `is_period` equal to True, you can use a string denoting period frequency:

\>>> freq \= to\_offset(freq\="ME", is\_period\=False)
\>>> freq.rule\_code
'ME'

Copy to clipboard

\>>> freq \= to\_offset(freq\="M", is\_period\=True)
\>>> freq.rule\_code
'ME'

Copy to clipboard

On this page