[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.FY5253Quarter.get\_rule\_code\_suffix[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html#pandas-tseries-offsets-fy5253quarter-get-rule-code-suffix "Link to this heading")

==============================================================================================================================================================================================================================================================

FY5253Quarter.get\_rule\_code\_suffix()[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html#pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix "Link to this definition")

Return the suffix component of the rule code.

The suffix combines the variation prefix, starting month abbreviation, and weekday abbreviation into a string format.

Returns:

str

Suffix string in the format “{variation}-{month}-{weekday}”. The variation is “N” for nearest or “L” for last.

See also

`FY5253.rule_code`

Return the complete rule code string.

`FY5253Quarter.rule_code`

Return the complete rule code string for FY5253Quarter.

Examples

\>>> offset \= pd.offsets.FY5253(weekday\=4, startingMonth\=12, variation\="nearest")
\>>> offset.get\_rule\_code\_suffix()
'N-DEC-FRI'

Copy to clipboard

\>>> offset \= pd.offsets.FY5253(weekday\=0, startingMonth\=1, variation\="last")
\>>> offset.get\_rule\_code\_suffix()
'L-JAN-MON'

Copy to clipboard

On this page