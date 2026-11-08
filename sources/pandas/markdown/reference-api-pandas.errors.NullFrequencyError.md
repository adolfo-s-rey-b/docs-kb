[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.NullFrequencyError.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.NullFrequencyError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.NullFrequencyError.html#pandas-errors-nullfrequencyerror "Link to this heading")

================================================================================================================================================================================

exception pandas.errors.NullFrequencyError[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L43-L61)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.NullFrequencyError.html#pandas.errors.NullFrequencyError "Link to this definition")

Exception raised when a `freq` cannot be null.

Particularly `DatetimeIndex.shift`, `TimedeltaIndex.shift`, `PeriodIndex.shift`.

See also

`Index.shift`

Shift values of Index.

`Series.shift`

Shift values of Series.

Examples

\>>> df \= pd.DatetimeIndex(\["2011-01-01 10:00", "2011-01-01"\], freq\=None)
\>>> df.shift(2)
Traceback (most recent call last):
NullFrequencyError: Cannot shift with no freq

Copy to clipboard

On this page