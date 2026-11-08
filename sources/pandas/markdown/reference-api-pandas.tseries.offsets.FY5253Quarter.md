[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.FY5253Quarter.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.FY5253Quarter.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.FY5253Quarter.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.FY5253Quarter.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.FY5253Quarter.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.FY5253Quarter.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.FY5253Quarter.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.FY5253Quarter.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.FY5253Quarter.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.FY5253Quarter.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.FY5253Quarter.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.FY5253Quarter.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.FY5253Quarter[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.html#pandas-tseries-offsets-fy5253quarter "Link to this heading")

============================================================================================================================================================================================

class pandas.tseries.offsets.FY5253Quarter[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.html#pandas.tseries.offsets.FY5253Quarter "Link to this definition")

DateOffset increments between business quarter dates for 52-53 week fiscal year.

Also known as a 4-4-5 calendar.

It is used by companies that desire that their fiscal year always end on the same day of the week.

It is a method of managing accounting periods. It is a common calendar structure for some industries, such as retail, manufacturing and parking industry.

For more information see: [https://en.wikipedia.org/wiki/4-4-5\_calendar](https://en.wikipedia.org/wiki/4-4-5_calendar)

The year may either:

*   end on the last X day of the Y month.
    
*   end on the last X day closest to the last day of the Y month.
    

X is a specific day of the week. Y is a certain month of the year

startingMonth = 1 corresponds to dates like 1/31/2007, 4/30/2007, … startingMonth = 2 corresponds to dates like 2/28/2007, 5/31/2007, … startingMonth = 3 corresponds to dates like 3/30/2007, 6/29/2007, …

Parameters:

**n**int

The number of business quarters represented.

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
    

**startingMonth**int {1, 2, …, 12}, default 1

The month in which fiscal years end.

**qtr\_with\_extra\_week**int {1, 2, 3, 4}, default 1

The quarter number that has the leap or 14 week when needed.

**variation**str, default “nearest”

Method of employing 4-4-5 calendar.

There are two options:

*   “nearest” means year end is **weekday** closest to last day of month in year.
    
*   “last” means year end is final **weekday** of the final month in fiscal year.
    

Attributes

|     |     |
| --- | --- |
| [`weekday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html#pandas.tseries.offsets.FY5253Quarter.weekday "pandas.tseries.offsets.FY5253Quarter.weekday") | Return the weekday used by the fiscal year. |
| [`startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.startingMonth.html#pandas.tseries.offsets.FY5253Quarter.startingMonth "pandas.tseries.offsets.FY5253Quarter.startingMonth") | Return the starting month of the fiscal year. |
| [`qtr_with_extra_week`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html#pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week "pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week") | Return the quarter number that has the leap or 14 week when needed. |
| [`variation`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html#pandas.tseries.offsets.FY5253Quarter.variation "pandas.tseries.offsets.FY5253Quarter.variation") | Return the variation of the fiscal year. |

Methods

|     |     |
| --- | --- |
| [`get_rule_code_suffix`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html#pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix "pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix")<br>() | Return the suffix component of the rule code. |
| [`get_weeks`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html#pandas.tseries.offsets.FY5253Quarter.get_weeks "pandas.tseries.offsets.FY5253Quarter.get_weeks")<br>(dt) | Get the number of weeks in each quarter for the fiscal year containing dt. |
| [`year_has_extra_week`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html#pandas.tseries.offsets.FY5253Quarter.year_has_extra_week "pandas.tseries.offsets.FY5253Quarter.year_has_extra_week")<br>(dt) | Return whether the fiscal year containing the given date has 53 weeks. |

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

In the example below the default parameters give the next business quarter for 52-53 week fiscal year.

\>>> ts \= pd.Timestamp(2022, 1, 1)
\>>> ts + pd.offsets.FY5253Quarter()
Timestamp('2022-01-31 00:00:00')

Copy to clipboard

By the parameter `startingMonth` we can specify the month in which fiscal years end.

\>>> ts \= pd.Timestamp(2022, 1, 1)
\>>> ts + pd.offsets.FY5253Quarter(startingMonth\=3)
Timestamp('2022-03-28 00:00:00')

Copy to clipboard

Business quarters for 52-53 week fiscal year can be specified by `weekday` and `variation` parameters.

\>>> ts \= pd.Timestamp(2022, 1, 1)
\>>> ts + pd.offsets.FY5253Quarter(weekday\=5, startingMonth\=12, variation\="last")
Timestamp('2022-04-02 00:00:00')

Copy to clipboard

On this page