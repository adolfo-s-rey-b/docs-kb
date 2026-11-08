[Skip to main content](https://pandas.pydata.org/docs/reference/offset_frequency.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/offset_frequency.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/offset_frequency.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/offset_frequency.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/offset_frequency.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/offset_frequency.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/offset_frequency.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/offset_frequency.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/offset_frequency.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/offset_frequency.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/offset_frequency.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/offset_frequency.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/offset_frequency.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/offset_frequency.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Date offsets[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#date-offsets "Link to this heading")

====================================================================================================================

BaseOffset[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#baseoffset "Link to this heading")

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`BaseOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.html#pandas.tseries.offsets.BaseOffset "pandas.tseries.offsets.BaseOffset") | Base class for all pandas date offsets. |

### Properties[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#properties "Link to this heading")

|     |     |
| --- | --- |
| [`BaseOffset.freqstr`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html#pandas.tseries.offsets.BaseOffset.freqstr "pandas.tseries.offsets.BaseOffset.freqstr") | Return a string representing the frequency. |
| [`BaseOffset.kwds`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.kwds.html#pandas.tseries.offsets.BaseOffset.kwds "pandas.tseries.offsets.BaseOffset.kwds") | Return a dict of extra parameters for the offset. |
| [`BaseOffset.name`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.name.html#pandas.tseries.offsets.BaseOffset.name "pandas.tseries.offsets.BaseOffset.name") | (DEPRECATED) Return a string representing the base frequency. |
| [`BaseOffset.nanos`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.nanos.html#pandas.tseries.offsets.BaseOffset.nanos "pandas.tseries.offsets.BaseOffset.nanos") | Return an integer of the total number of nanoseconds. |
| [`BaseOffset.normalize`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.normalize.html#pandas.tseries.offsets.BaseOffset.normalize "pandas.tseries.offsets.BaseOffset.normalize") | Return boolean whether the frequency can align with midnight. |
| [`BaseOffset.rule_code`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.rule_code.html#pandas.tseries.offsets.BaseOffset.rule_code "pandas.tseries.offsets.BaseOffset.rule_code") | Return a string representing the base frequency. |
| [`BaseOffset.n`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.n.html#pandas.tseries.offsets.BaseOffset.n "pandas.tseries.offsets.BaseOffset.n") | Return the count of the number of periods. |

### Methods[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#methods "Link to this heading")

|     |     |
| --- | --- |
| [`BaseOffset.copy`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.copy.html#pandas.tseries.offsets.BaseOffset.copy "pandas.tseries.offsets.BaseOffset.copy")<br>() | Return a copy of the frequency. |
| [`BaseOffset.is_on_offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_on_offset.html#pandas.tseries.offsets.BaseOffset.is_on_offset "pandas.tseries.offsets.BaseOffset.is_on_offset")<br>(dt) | Return boolean whether a timestamp intersects with this frequency. |
| [`BaseOffset.is_month_start`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_month_start.html#pandas.tseries.offsets.BaseOffset.is_month_start "pandas.tseries.offsets.BaseOffset.is_month_start")<br>(ts) | Return boolean whether a timestamp occurs on the month start. |
| [`BaseOffset.is_month_end`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_month_end.html#pandas.tseries.offsets.BaseOffset.is_month_end "pandas.tseries.offsets.BaseOffset.is_month_end")<br>(ts) | Return boolean whether a timestamp occurs on the month end. |
| [`BaseOffset.is_quarter_start`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_start.html#pandas.tseries.offsets.BaseOffset.is_quarter_start "pandas.tseries.offsets.BaseOffset.is_quarter_start")<br>(ts) | Return boolean whether a timestamp occurs on the quarter start. |
| [`BaseOffset.is_quarter_end`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_quarter_end.html#pandas.tseries.offsets.BaseOffset.is_quarter_end "pandas.tseries.offsets.BaseOffset.is_quarter_end")<br>(ts) | Return boolean whether a timestamp occurs on the quarter end. |
| [`BaseOffset.is_year_start`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_year_start.html#pandas.tseries.offsets.BaseOffset.is_year_start "pandas.tseries.offsets.BaseOffset.is_year_start")<br>(ts) | Return boolean whether a timestamp occurs on the year start. |
| [`BaseOffset.is_year_end`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.is_year_end.html#pandas.tseries.offsets.BaseOffset.is_year_end "pandas.tseries.offsets.BaseOffset.is_year_end")<br>(ts) | Return boolean whether a timestamp occurs on the year end. |
| [`BaseOffset.rollback`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.rollback.html#pandas.tseries.offsets.BaseOffset.rollback "pandas.tseries.offsets.BaseOffset.rollback")<br>(dt) | Roll provided date backward to next offset only if not on offset. |
| [`BaseOffset.rollforward`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.rollforward.html#pandas.tseries.offsets.BaseOffset.rollforward "pandas.tseries.offsets.BaseOffset.rollforward")<br>(dt) | Roll provided date forward to next offset only if not on offset. |

DateOffset[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#dateoffset "Link to this heading")

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset") | Standard kind of date increment used for a date range. |

BusinessDay[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#businessday "Link to this heading")

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`BusinessDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.html#pandas.tseries.offsets.BusinessDay "pandas.tseries.offsets.BusinessDay")<br>(\[n, normalize, offset\]) | DateOffset subclass representing possibly n business days. |
| [`BDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BDay.html#pandas.tseries.offsets.BDay "pandas.tseries.offsets.BDay") |     |

Custom properties:

|     |     |
| --- | --- |
| [`BusinessDay.offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.offset.html#pandas.tseries.offsets.BusinessDay.offset "pandas.tseries.offsets.BusinessDay.offset") | Return the time offset applied to the business day. |
| [`BusinessDay.weekmask`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.weekmask.html#pandas.tseries.offsets.BusinessDay.weekmask "pandas.tseries.offsets.BusinessDay.weekmask") | Return the weekmask used for custom business day calculations. |
| [`BusinessDay.holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html#pandas.tseries.offsets.BusinessDay.holidays "pandas.tseries.offsets.BusinessDay.holidays") | Return the holidays used for custom business day calculations. |
| [`BusinessDay.calendar`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.calendar.html#pandas.tseries.offsets.BusinessDay.calendar "pandas.tseries.offsets.BusinessDay.calendar") | Return the calendar used for business day calculations. |

BusinessHour[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#businesshour "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`BusinessHour`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.html#pandas.tseries.offsets.BusinessHour "pandas.tseries.offsets.BusinessHour") | DateOffset subclass representing possibly n business hours. |

Custom properties:

|     |     |
| --- | --- |
| [`BusinessHour.offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.offset.html#pandas.tseries.offsets.BusinessHour.offset "pandas.tseries.offsets.BusinessHour.offset") | Return the time offset applied to the business day. |
| [`BusinessHour.start`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.start.html#pandas.tseries.offsets.BusinessHour.start "pandas.tseries.offsets.BusinessHour.start") | Return the start time(s) of the business hour. |
| [`BusinessHour.end`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.end.html#pandas.tseries.offsets.BusinessHour.end "pandas.tseries.offsets.BusinessHour.end") | Return the end time(s) of the business hour. |
| [`BusinessHour.weekmask`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.weekmask.html#pandas.tseries.offsets.BusinessHour.weekmask "pandas.tseries.offsets.BusinessHour.weekmask") | Return the weekmask used for custom business day calculations. |
| [`BusinessHour.holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.holidays.html#pandas.tseries.offsets.BusinessHour.holidays "pandas.tseries.offsets.BusinessHour.holidays") | Return the holidays used for custom business day calculations. |
| [`BusinessHour.calendar`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.calendar.html#pandas.tseries.offsets.BusinessHour.calendar "pandas.tseries.offsets.BusinessHour.calendar") | Return the calendar used for business day calculations. |

CustomBusinessDay[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#custombusinessday "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`CustomBusinessDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.html#pandas.tseries.offsets.CustomBusinessDay "pandas.tseries.offsets.CustomBusinessDay")<br>(\[n, normalize, weekmask, ...\]) | DateOffset subclass representing possibly n custom business days. |
| [`CDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CDay.html#pandas.tseries.offsets.CDay "pandas.tseries.offsets.CDay") |     |

Custom properties:

|     |     |
| --- | --- |
| [`CustomBusinessDay.weekmask`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.weekmask.html#pandas.tseries.offsets.CustomBusinessDay.weekmask "pandas.tseries.offsets.CustomBusinessDay.weekmask") | Return the weekmask used for custom business day calculations. |
| [`CustomBusinessDay.calendar`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.calendar.html#pandas.tseries.offsets.CustomBusinessDay.calendar "pandas.tseries.offsets.CustomBusinessDay.calendar") | Return the calendar used for business day calculations. |
| [`CustomBusinessDay.holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.holidays.html#pandas.tseries.offsets.CustomBusinessDay.holidays "pandas.tseries.offsets.CustomBusinessDay.holidays") | Return the holidays used for custom business day calculations. |
| [`CustomBusinessDay.offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.offset.html#pandas.tseries.offsets.CustomBusinessDay.offset "pandas.tseries.offsets.CustomBusinessDay.offset") | Return the time offset applied to the business day. |

CustomBusinessHour[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#custombusinesshour "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`CustomBusinessHour`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.html#pandas.tseries.offsets.CustomBusinessHour "pandas.tseries.offsets.CustomBusinessHour") | DateOffset subclass representing possibly n custom business days. |

Custom properties:

|     |     |
| --- | --- |
| [`CustomBusinessHour.weekmask`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.weekmask.html#pandas.tseries.offsets.CustomBusinessHour.weekmask "pandas.tseries.offsets.CustomBusinessHour.weekmask") | Return the weekmask used for custom business day calculations. |
| [`CustomBusinessHour.calendar`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.calendar.html#pandas.tseries.offsets.CustomBusinessHour.calendar "pandas.tseries.offsets.CustomBusinessHour.calendar") | Return the calendar used for business day calculations. |
| [`CustomBusinessHour.holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.holidays.html#pandas.tseries.offsets.CustomBusinessHour.holidays "pandas.tseries.offsets.CustomBusinessHour.holidays") | Return the holidays used for custom business day calculations. |
| [`CustomBusinessHour.start`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.start.html#pandas.tseries.offsets.CustomBusinessHour.start "pandas.tseries.offsets.CustomBusinessHour.start") | Return the start time(s) of the business hour. |
| [`CustomBusinessHour.end`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.end.html#pandas.tseries.offsets.CustomBusinessHour.end "pandas.tseries.offsets.CustomBusinessHour.end") | Return the end time(s) of the business hour. |
| [`CustomBusinessHour.offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.offset.html#pandas.tseries.offsets.CustomBusinessHour.offset "pandas.tseries.offsets.CustomBusinessHour.offset") | Return the time offset applied to the business day. |

Month offsets[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#month-offsets "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`MonthEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.MonthEnd.html#pandas.tseries.offsets.MonthEnd "pandas.tseries.offsets.MonthEnd") | DateOffset of one month end. |
| [`MonthBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.MonthBegin.html#pandas.tseries.offsets.MonthBegin "pandas.tseries.offsets.MonthBegin") | DateOffset of one month at beginning. |

Business variants:

|     |     |
| --- | --- |
| [`BusinessMonthEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessMonthEnd.html#pandas.tseries.offsets.BusinessMonthEnd "pandas.tseries.offsets.BusinessMonthEnd") | DateOffset increments between the last business day of the month. |
| [`BMonthEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BMonthEnd.html#pandas.tseries.offsets.BMonthEnd "pandas.tseries.offsets.BMonthEnd") |     |
| [`BusinessMonthBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessMonthBegin.html#pandas.tseries.offsets.BusinessMonthBegin "pandas.tseries.offsets.BusinessMonthBegin") | DateOffset of one month at the first business day. |
| [`BMonthBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BMonthBegin.html#pandas.tseries.offsets.BMonthBegin "pandas.tseries.offsets.BMonthBegin") |     |

CustomBusinessMonthEnd[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#custombusinessmonthend "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`CustomBusinessMonthEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.html#pandas.tseries.offsets.CustomBusinessMonthEnd "pandas.tseries.offsets.CustomBusinessMonthEnd")<br>(\[n, normalize, ...\]) | DateOffset subclass representing custom business month(s). |
| [`CBMonthEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CBMonthEnd.html#pandas.tseries.offsets.CBMonthEnd "pandas.tseries.offsets.CBMonthEnd") |     |

Custom properties:

|     |     |
| --- | --- |
| [`CustomBusinessMonthEnd.m_offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.m_offset.html#pandas.tseries.offsets.CustomBusinessMonthEnd.m_offset "pandas.tseries.offsets.CustomBusinessMonthEnd.m_offset") | Return a MonthBegin or MonthEnd offset. |
| [`CustomBusinessMonthEnd.weekmask`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask.html#pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask "pandas.tseries.offsets.CustomBusinessMonthEnd.weekmask") | Return the weekmask used for custom business day calculations. |
| [`CustomBusinessMonthEnd.calendar`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.calendar.html#pandas.tseries.offsets.CustomBusinessMonthEnd.calendar "pandas.tseries.offsets.CustomBusinessMonthEnd.calendar") | Return the calendar used for business day calculations. |
| [`CustomBusinessMonthEnd.holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.holidays.html#pandas.tseries.offsets.CustomBusinessMonthEnd.holidays "pandas.tseries.offsets.CustomBusinessMonthEnd.holidays") | Return the holidays used for custom business day calculations. |
| [`CustomBusinessMonthEnd.offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthEnd.offset.html#pandas.tseries.offsets.CustomBusinessMonthEnd.offset "pandas.tseries.offsets.CustomBusinessMonthEnd.offset") | Return the time offset applied to the business day. |

CustomBusinessMonthBegin[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#custombusinessmonthbegin "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`CustomBusinessMonthBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html#pandas.tseries.offsets.CustomBusinessMonthBegin "pandas.tseries.offsets.CustomBusinessMonthBegin")<br>(\[n, normalize, ...\]) | DateOffset subclass representing custom business month(s). |
| [`CBMonthBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CBMonthBegin.html#pandas.tseries.offsets.CBMonthBegin "pandas.tseries.offsets.CBMonthBegin") |     |

Custom properties:

|     |     |
| --- | --- |
| [`CustomBusinessMonthBegin.m_offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html#pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset "pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset") | Return a MonthBegin or MonthEnd offset. |
| [`CustomBusinessMonthBegin.weekmask`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.weekmask.html#pandas.tseries.offsets.CustomBusinessMonthBegin.weekmask "pandas.tseries.offsets.CustomBusinessMonthBegin.weekmask") | Return the weekmask used for custom business day calculations. |
| [`CustomBusinessMonthBegin.calendar`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html#pandas.tseries.offsets.CustomBusinessMonthBegin.calendar "pandas.tseries.offsets.CustomBusinessMonthBegin.calendar") | Return the calendar used for business day calculations. |
| [`CustomBusinessMonthBegin.holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.holidays.html#pandas.tseries.offsets.CustomBusinessMonthBegin.holidays "pandas.tseries.offsets.CustomBusinessMonthBegin.holidays") | Return the holidays used for custom business day calculations. |
| [`CustomBusinessMonthBegin.offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.offset.html#pandas.tseries.offsets.CustomBusinessMonthBegin.offset "pandas.tseries.offsets.CustomBusinessMonthBegin.offset") | Return the time offset applied to the business day. |

SemiMonthEnd[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#semimonthend "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`SemiMonthEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthEnd.html#pandas.tseries.offsets.SemiMonthEnd "pandas.tseries.offsets.SemiMonthEnd") | Two DateOffset's per month repeating on the last day of the month & day\_of\_month. |
| [`SemiMonthBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthBegin.html#pandas.tseries.offsets.SemiMonthBegin "pandas.tseries.offsets.SemiMonthBegin") | Two DateOffset's per month repeating on the first day of the month & day\_of\_month. |

Custom properties:

|     |     |
| --- | --- |
| [`SemiMonthEnd.day_of_month`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthEnd.day_of_month.html#pandas.tseries.offsets.SemiMonthEnd.day_of_month "pandas.tseries.offsets.SemiMonthEnd.day_of_month") | Return the day of the month for the semi-monthly offset. |
| [`SemiMonthBegin.day_of_month`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html#pandas.tseries.offsets.SemiMonthBegin.day_of_month "pandas.tseries.offsets.SemiMonthBegin.day_of_month") | Return the day of the month for the semi-monthly offset. |

Week[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#week "Link to this heading")

----------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Week`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Week.html#pandas.tseries.offsets.Week "pandas.tseries.offsets.Week") | Weekly offset. |

Custom properties:

|     |     |
| --- | --- |
| [`Week.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Week.weekday.html#pandas.tseries.offsets.Week.weekday "pandas.tseries.offsets.Week.weekday") | Return the day of the week on which the offset is applied. |

WeekOfMonth[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#weekofmonth "Link to this heading")

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`WeekOfMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.WeekOfMonth.html#pandas.tseries.offsets.WeekOfMonth "pandas.tseries.offsets.WeekOfMonth") | Describes monthly dates like "the Tuesday of the 2nd week of each month". |

Custom properties:

|     |     |
| --- | --- |
| [`WeekOfMonth.week`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.WeekOfMonth.week.html#pandas.tseries.offsets.WeekOfMonth.week "pandas.tseries.offsets.WeekOfMonth.week") | Return the week of the month on which this offset applies. |
| [`WeekOfMonth.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.WeekOfMonth.weekday.html#pandas.tseries.offsets.WeekOfMonth.weekday "pandas.tseries.offsets.WeekOfMonth.weekday") | Return the day of the week on which this offset applies. |

LastWeekOfMonth[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#lastweekofmonth "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`LastWeekOfMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.LastWeekOfMonth.html#pandas.tseries.offsets.LastWeekOfMonth "pandas.tseries.offsets.LastWeekOfMonth") | Describes monthly dates in last week of month. |

Custom properties:

|     |     |
| --- | --- |
| [`LastWeekOfMonth.week`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.LastWeekOfMonth.week.html#pandas.tseries.offsets.LastWeekOfMonth.week "pandas.tseries.offsets.LastWeekOfMonth.week") | Return the week of the month on which this offset applies. |
| [`LastWeekOfMonth.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.LastWeekOfMonth.weekday.html#pandas.tseries.offsets.LastWeekOfMonth.weekday "pandas.tseries.offsets.LastWeekOfMonth.weekday") | Return the day of the week on which this offset applies. |

Quarter offsets[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#quarter-offsets "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`QuarterEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.QuarterEnd.html#pandas.tseries.offsets.QuarterEnd "pandas.tseries.offsets.QuarterEnd") | DateOffset increments between Quarter end dates. |
| [`QuarterBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.QuarterBegin.html#pandas.tseries.offsets.QuarterBegin "pandas.tseries.offsets.QuarterBegin") | DateOffset increments between Quarter start dates. |
| [`BQuarterEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterEnd.html#pandas.tseries.offsets.BQuarterEnd "pandas.tseries.offsets.BQuarterEnd") | DateOffset increments between the last business day of each Quarter. |
| [`BQuarterBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterBegin.html#pandas.tseries.offsets.BQuarterBegin "pandas.tseries.offsets.BQuarterBegin") | DateOffset increments between the first business day of each Quarter. |

Custom properties:

|     |     |
| --- | --- |
| [`BQuarterEnd.startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterEnd.startingMonth.html#pandas.tseries.offsets.BQuarterEnd.startingMonth "pandas.tseries.offsets.BQuarterEnd.startingMonth") | Return the month of the year that anchors the quarters. |
| [`BQuarterBegin.startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html#pandas.tseries.offsets.BQuarterBegin.startingMonth "pandas.tseries.offsets.BQuarterBegin.startingMonth") | Return the month of the year that anchors the quarters. |
| [`QuarterEnd.startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.QuarterEnd.startingMonth.html#pandas.tseries.offsets.QuarterEnd.startingMonth "pandas.tseries.offsets.QuarterEnd.startingMonth") | Return the month of the year that anchors the quarters. |
| [`QuarterBegin.startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.QuarterBegin.startingMonth.html#pandas.tseries.offsets.QuarterBegin.startingMonth "pandas.tseries.offsets.QuarterBegin.startingMonth") | Return the month of the year that anchors the quarters. |

HalfYear offsets[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#halfyear-offsets "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`HalfYearEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.HalfYearEnd.html#pandas.tseries.offsets.HalfYearEnd "pandas.tseries.offsets.HalfYearEnd") | DateOffset increments between half-year end dates. |
| [`HalfYearBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.HalfYearBegin.html#pandas.tseries.offsets.HalfYearBegin "pandas.tseries.offsets.HalfYearBegin") | DateOffset increments between half-year start dates. |
| [`BHalfYearEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BHalfYearEnd.html#pandas.tseries.offsets.BHalfYearEnd "pandas.tseries.offsets.BHalfYearEnd") | DateOffset increments between the last business day of each half-year. |
| [`BHalfYearBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BHalfYearBegin.html#pandas.tseries.offsets.BHalfYearBegin "pandas.tseries.offsets.BHalfYearBegin") | DateOffset increments between the first business day of each half-year. |

Custom properties:

|     |     |
| --- | --- |
| [`BHalfYearEnd.startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BHalfYearEnd.startingMonth.html#pandas.tseries.offsets.BHalfYearEnd.startingMonth "pandas.tseries.offsets.BHalfYearEnd.startingMonth") | Return the month of the year that anchors the half-years. |
| [`BHalfYearBegin.startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BHalfYearBegin.startingMonth.html#pandas.tseries.offsets.BHalfYearBegin.startingMonth "pandas.tseries.offsets.BHalfYearBegin.startingMonth") | Return the month of the year that anchors the half-years. |
| [`HalfYearEnd.startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.HalfYearEnd.startingMonth.html#pandas.tseries.offsets.HalfYearEnd.startingMonth "pandas.tseries.offsets.HalfYearEnd.startingMonth") | Return the month of the year that anchors the half-years. |
| [`HalfYearBegin.startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.HalfYearBegin.startingMonth.html#pandas.tseries.offsets.HalfYearBegin.startingMonth "pandas.tseries.offsets.HalfYearBegin.startingMonth") | Return the month of the year that anchors the half-years. |

Year offsets[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#year-offsets "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`YearEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.YearEnd.html#pandas.tseries.offsets.YearEnd "pandas.tseries.offsets.YearEnd")<br>(\[n, normalize, month\]) | DateOffset increments between calendar year end dates. |
| [`YearBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.YearBegin.html#pandas.tseries.offsets.YearBegin "pandas.tseries.offsets.YearBegin") | DateOffset increments between calendar year begin dates. |
| [`BYearEnd`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearEnd.html#pandas.tseries.offsets.BYearEnd "pandas.tseries.offsets.BYearEnd") | DateOffset increments between the last business day of the year. |
| [`BYearBegin`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearBegin.html#pandas.tseries.offsets.BYearBegin "pandas.tseries.offsets.BYearBegin") | DateOffset increments between the first business day of the year. |

Custom properties:

|     |     |
| --- | --- |
| [`YearEnd.month`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.YearEnd.month.html#pandas.tseries.offsets.YearEnd.month "pandas.tseries.offsets.YearEnd.month") | Return the month of the year on which this offset applies. |
| [`YearBegin.month`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.YearBegin.month.html#pandas.tseries.offsets.YearBegin.month "pandas.tseries.offsets.YearBegin.month") | Return the month of the year on which this offset applies. |
| [`BYearEnd.month`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearEnd.month.html#pandas.tseries.offsets.BYearEnd.month "pandas.tseries.offsets.BYearEnd.month") | Return the month of the year on which this offset applies. |
| [`BYearBegin.month`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearBegin.month.html#pandas.tseries.offsets.BYearBegin.month "pandas.tseries.offsets.BYearBegin.month") | Return the month of the year on which this offset applies. |

FY5253[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#fy5253 "Link to this heading")

--------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`FY5253`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.html#pandas.tseries.offsets.FY5253 "pandas.tseries.offsets.FY5253") | Describes 52-53 week fiscal year. |

Custom properties:

|     |     |
| --- | --- |
| [`FY5253.startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.startingMonth.html#pandas.tseries.offsets.FY5253.startingMonth "pandas.tseries.offsets.FY5253.startingMonth") | Return the starting month of the fiscal year. |
| [`FY5253.variation`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.variation.html#pandas.tseries.offsets.FY5253.variation "pandas.tseries.offsets.FY5253.variation") | Return the variation of the fiscal year. |
| [`FY5253.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.weekday.html#pandas.tseries.offsets.FY5253.weekday "pandas.tseries.offsets.FY5253.weekday") | Return the weekday used by the fiscal year. |

Custom methods:

|     |     |
| --- | --- |
| [`FY5253.get_rule_code_suffix`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.get_rule_code_suffix.html#pandas.tseries.offsets.FY5253.get_rule_code_suffix "pandas.tseries.offsets.FY5253.get_rule_code_suffix")<br>() | Return the suffix component of the rule code. |
| [`FY5253.get_year_end`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html#pandas.tseries.offsets.FY5253.get_year_end "pandas.tseries.offsets.FY5253.get_year_end")<br>(dt) | Get the fiscal year end date for the given datetime. |

FY5253Quarter[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#fy5253quarter "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`FY5253Quarter`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.html#pandas.tseries.offsets.FY5253Quarter "pandas.tseries.offsets.FY5253Quarter") | DateOffset increments between business quarter dates for 52-53 week fiscal year. |

Custom properties:

|     |     |
| --- | --- |
| [`FY5253Quarter.qtr_with_extra_week`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html#pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week "pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week") | Return the quarter number that has the leap or 14 week when needed. |
| [`FY5253Quarter.startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.startingMonth.html#pandas.tseries.offsets.FY5253Quarter.startingMonth "pandas.tseries.offsets.FY5253Quarter.startingMonth") | Return the starting month of the fiscal year. |
| [`FY5253Quarter.variation`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.variation.html#pandas.tseries.offsets.FY5253Quarter.variation "pandas.tseries.offsets.FY5253Quarter.variation") | Return the variation of the fiscal year. |
| [`FY5253Quarter.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.weekday.html#pandas.tseries.offsets.FY5253Quarter.weekday "pandas.tseries.offsets.FY5253Quarter.weekday") | Return the weekday used by the fiscal year. |

Custom methods:

|     |     |
| --- | --- |
| [`FY5253Quarter.get_rule_code_suffix`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix.html#pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix "pandas.tseries.offsets.FY5253Quarter.get_rule_code_suffix")<br>() | Return the suffix component of the rule code. |
| [`FY5253Quarter.get_weeks`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html#pandas.tseries.offsets.FY5253Quarter.get_weeks "pandas.tseries.offsets.FY5253Quarter.get_weeks")<br>(dt) | Get the number of weeks in each quarter for the fiscal year containing dt. |
| [`FY5253Quarter.year_has_extra_week`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html#pandas.tseries.offsets.FY5253Quarter.year_has_extra_week "pandas.tseries.offsets.FY5253Quarter.year_has_extra_week")<br>(dt) | Return whether the fiscal year containing the given date has 53 weeks. |

Easter[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#easter "Link to this heading")

--------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Easter`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Easter.html#pandas.tseries.offsets.Easter "pandas.tseries.offsets.Easter") | DateOffset for the Easter holiday using logic defined in dateutil. |

Ticks[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#ticks "Link to this heading")

------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Tick`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Tick.html#pandas.tseries.offsets.Tick "pandas.tseries.offsets.Tick") | Base class for fixed frequency offsets (Milli, Micro, Second, Minute, Hour). |
| [`Day`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Day.html#pandas.tseries.offsets.Day "pandas.tseries.offsets.Day") | Offset `n` days. |
| [`Hour`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Hour.html#pandas.tseries.offsets.Hour "pandas.tseries.offsets.Hour") | Offset `n` hours. |
| [`Minute`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Minute.html#pandas.tseries.offsets.Minute "pandas.tseries.offsets.Minute") | Offset `n` minutes. |
| [`Second`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Second.html#pandas.tseries.offsets.Second "pandas.tseries.offsets.Second") | Offset `n` seconds. |
| [`Milli`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Milli.html#pandas.tseries.offsets.Milli "pandas.tseries.offsets.Milli") | Offset `n` milliseconds. |
| [`Micro`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Micro.html#pandas.tseries.offsets.Micro "pandas.tseries.offsets.Micro") | Offset `n` microseconds. |
| [`Nano`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Nano.html#pandas.tseries.offsets.Nano "pandas.tseries.offsets.Nano") | Offset `n` nanoseconds. |

Frequencies[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#frequencies "Link to this heading")

==================================================================================================================

|     |     |
| --- | --- |
| [`to_offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.frequencies.to_offset.html#pandas.tseries.frequencies.to_offset "pandas.tseries.frequencies.to_offset")<br>(freq\[, is\_period\]) | Return DateOffset object from string or datetime.timedelta object. |

Holiday calendars[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#holiday-calendars "Link to this heading")

==============================================================================================================================

Holiday[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#holiday "Link to this heading")

----------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Holiday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.Holiday.html#pandas.tseries.holiday.Holiday "pandas.tseries.holiday.Holiday")<br>(name\[, year, month, day, offset, ...\]) | Class that defines a holiday with start/end dates and rules for observance. |

### Methods[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#id1 "Link to this heading")

|     |     |
| --- | --- |
| [`Holiday.dates`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.Holiday.dates.html#pandas.tseries.holiday.Holiday.dates "pandas.tseries.holiday.Holiday.dates")<br>(start\_date, end\_date\[, ...\]) | Calculate holidays observed between start date and end date. |

Calendars[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#calendars "Link to this heading")

--------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`AbstractHolidayCalendar`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html#pandas.tseries.holiday.AbstractHolidayCalendar "pandas.tseries.holiday.AbstractHolidayCalendar")<br>(\[name, rules\]) | Abstract interface to create holidays following certain rules. |
| [`USFederalHolidayCalendar`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.USFederalHolidayCalendar.html#pandas.tseries.holiday.USFederalHolidayCalendar "pandas.tseries.holiday.USFederalHolidayCalendar")<br>(\[name, rules\]) | US Federal Government holiday calendar. |

### Methods[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#id2 "Link to this heading")

|     |     |
| --- | --- |
| [`AbstractHolidayCalendar.holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.holidays.html#pandas.tseries.holiday.AbstractHolidayCalendar.holidays "pandas.tseries.holiday.AbstractHolidayCalendar.holidays")<br>(\[start, ...\]) | Return a curve with holidays between start\_date and end\_date. |
| [`AbstractHolidayCalendar.merge`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge.html#pandas.tseries.holiday.AbstractHolidayCalendar.merge "pandas.tseries.holiday.AbstractHolidayCalendar.merge")<br>(other\[, inplace\]) | Merge holiday calendars together. |
| [`AbstractHolidayCalendar.merge_class`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.merge_class.html#pandas.tseries.holiday.AbstractHolidayCalendar.merge_class "pandas.tseries.holiday.AbstractHolidayCalendar.merge_class")<br>(base, other) | Merge holiday calendars together. |
| [`AbstractHolidayCalendar.rule_from_name`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name.html#pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name "pandas.tseries.holiday.AbstractHolidayCalendar.rule_from_name")<br>(name) | Return the rule for the holiday with the given name. |

Observance rules[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#observance-rules "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`after_nearest_workday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.after_nearest_workday.html#pandas.tseries.holiday.after_nearest_workday "pandas.tseries.holiday.after_nearest_workday")<br>(dt) | Move to the workday after the nearest workday. |
| [`before_nearest_workday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.before_nearest_workday.html#pandas.tseries.holiday.before_nearest_workday "pandas.tseries.holiday.before_nearest_workday")<br>(dt) | Move to the workday before the nearest workday. |
| [`nearest_workday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.nearest_workday.html#pandas.tseries.holiday.nearest_workday "pandas.tseries.holiday.nearest_workday")<br>(dt) | Move Saturday to Friday and Sunday to Monday. |
| [`next_monday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.next_monday.html#pandas.tseries.holiday.next_monday "pandas.tseries.holiday.next_monday")<br>(dt) | Move Saturday and Sunday to the following Monday. |
| [`next_monday_or_tuesday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.next_monday_or_tuesday.html#pandas.tseries.holiday.next_monday_or_tuesday "pandas.tseries.holiday.next_monday_or_tuesday")<br>(dt) | Move Saturday to Monday, and Sunday or Monday to Tuesday. |
| [`next_workday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.next_workday.html#pandas.tseries.holiday.next_workday "pandas.tseries.holiday.next_workday")<br>(dt) | Move to the next weekday. |
| [`previous_friday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.previous_friday.html#pandas.tseries.holiday.previous_friday "pandas.tseries.holiday.previous_friday")<br>(dt) | Move Saturday and Sunday back to the previous Friday. |
| [`previous_workday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.previous_workday.html#pandas.tseries.holiday.previous_workday "pandas.tseries.holiday.previous_workday")<br>(dt) | Move to the previous weekday. |
| [`sunday_to_monday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.sunday_to_monday.html#pandas.tseries.holiday.sunday_to_monday "pandas.tseries.holiday.sunday_to_monday")<br>(dt) | Move Sunday to the following Monday. |
| [`weekend_to_monday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.weekend_to_monday.html#pandas.tseries.holiday.weekend_to_monday "pandas.tseries.holiday.weekend_to_monday")<br>(dt) | Move Saturday and Sunday to the following Monday. |

Calendar utilities[#](https://pandas.pydata.org/docs/reference/offset_frequency.html#calendar-utilities "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`HolidayCalendarFactory`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.HolidayCalendarFactory.html#pandas.tseries.holiday.HolidayCalendarFactory "pandas.tseries.holiday.HolidayCalendarFactory")<br>(name, base, other\[, ...\]) | Create a holiday calendar class from two sets of rules. |
| [`get_calendar`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.get_calendar.html#pandas.tseries.holiday.get_calendar "pandas.tseries.holiday.get_calendar")<br>(name) | Return an instance of a calendar based on its name. |
| [`register`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.register.html#pandas.tseries.holiday.register "pandas.tseries.holiday.register")<br>(cls) | Add a holiday calendar class to the registry of named calendars. |

On this page