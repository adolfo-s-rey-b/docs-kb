[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.FY5253.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.FY5253.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.FY5253.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.FY5253.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.FY5253.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.FY5253.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.FY5253.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.FY5253.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.FY5253.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.FY5253.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.FY5253.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.FY5253.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.FY5253[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.html#pandas-tseries-offsets-fy5253 "Link to this heading")

=======================================================================================================================================================================

class pandas.tseries.offsets.FY5253[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.html#pandas.tseries.offsets.FY5253 "Link to this definition")

Describes 52-53 week fiscal year. This is also known as a 4-4-5 calendar.

It is used by companies that desire that their fiscal year always end on the same day of the week.

It is a method of managing accounting periods. It is a common calendar structure for some industries, such as retail, manufacturing and parking industry.

For more information see: [https://en.wikipedia.org/wiki/4-4-5\_calendar](https://en.wikipedia.org/wiki/4-4-5_calendar)

The year may either:

*   end on the last X day of the Y month.
    
*   end on the last X day closest to the last day of the Y month.
    

X is a specific day of the week. Y is a certain month of the year

Parameters:

**n**int

The number of fiscal years represented.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

**weekday**int {0, 1, …, 6}, default 0

A specific integer for the day of the week.

*   0 is Monday
    
*   1 is Tuesday
    
*   2 is Wednesday
    
*   3 is Thursday
    
*   4 is Friday
    
*   5 is Saturday
    
*   6 is Sunday.
    

**startingMonth**int {1, 2, … 12}, default 1

The month in which the fiscal year ends.

**variation**str, default “nearest”

Method of employing 4-4-5 calendar.

There are two options:

*   “nearest” means year end is **weekday** closest to last day of month in year.
    
*   “last” means year end is final **weekday** of the final month in fiscal year.
    

Attributes

|     |     |
| --- | --- |
| [`weekday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.weekday.html#pandas.tseries.offsets.FY5253.weekday "pandas.tseries.offsets.FY5253.weekday") | Return the weekday used by the fiscal year. |
| [`startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.startingMonth.html#pandas.tseries.offsets.FY5253.startingMonth "pandas.tseries.offsets.FY5253.startingMonth") | Return the starting month of the fiscal year. |
| [`variation`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.variation.html#pandas.tseries.offsets.FY5253.variation "pandas.tseries.offsets.FY5253.variation") | Return the variation of the fiscal year. |

Methods

|     |     |
| --- | --- |
| [`get_rule_code_suffix`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.get_rule_code_suffix.html#pandas.tseries.offsets.FY5253.get_rule_code_suffix "pandas.tseries.offsets.FY5253.get_rule_code_suffix")<br>() | Return the suffix component of the rule code. |
| [`get_year_end`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html#pandas.tseries.offsets.FY5253.get_year_end "pandas.tseries.offsets.FY5253.get_year_end")<br>(dt) | Get the fiscal year end date for the given datetime. |

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

In the example below the default parameters give the next 52-53 week fiscal year.

\>>> ts \= pd.Timestamp(2022, 1, 1)
\>>> ts + pd.offsets.FY5253()
Timestamp('2022-01-31 00:00:00')

Copy to clipboard

By the parameter `startingMonth` we can specify the month in which fiscal years end.

\>>> ts \= pd.Timestamp(2022, 1, 1)
\>>> ts + pd.offsets.FY5253(startingMonth\=3)
Timestamp('2022-03-28 00:00:00')

Copy to clipboard

52-53 week fiscal year can be specified by `weekday` and `variation` parameters.

\>>> ts \= pd.Timestamp(2022, 1, 1)
\>>> ts + pd.offsets.FY5253(weekday\=5, startingMonth\=12, variation\="last")
Timestamp('2022-12-31 00:00:00')

Copy to clipboard

On this page