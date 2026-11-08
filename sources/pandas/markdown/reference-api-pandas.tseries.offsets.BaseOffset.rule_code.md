[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BaseOffset.rule\_code[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html#pandas-tseries-offsets-baseoffset-rule-code "Link to this heading")

==================================================================================================================================================================================================================

BaseOffset.rule\_code[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html#pandas.tseries.offsets.BaseOffset.rule_code "Link to this definition")

Return a string representing the base frequency.

This property provides a short string code that identifies the type of frequency offset, such as ‘h’ for hourly, ‘D’ for daily, or ‘W’ for weekly. This code is used internally for frequency string representations and parsing.

See also

`tseries.offsets.Hour.rule_code`

Returns a string representing the base frequency of ‘h’.

`tseries.offsets.Day.rule_code`

Returns a string representing the base frequency of ‘D’.

Examples

\>>> pd.offsets.Hour().rule\_code
'h'

Copy to clipboard

\>>> pd.offsets.Week(5).rule\_code
'W'

Copy to clipboard

On this page