[Skip to main content](https://numpy.org/doc/stable/reference/routines.datetime.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Datetime support functions[#](https://numpy.org/doc/stable/reference/routines.datetime.html#datetime-support-functions "Link to this heading")

===============================================================================================================================================

|     |     |
| --- | --- |
| [`datetime_as_string`](https://numpy.org/doc/stable/reference/generated/numpy.datetime_as_string.html#numpy.datetime_as_string "numpy.datetime_as_string")<br>(arr\[, unit, timezone, ...\]) | Convert an array of datetimes into an array of strings. |
| [`datetime_data`](https://numpy.org/doc/stable/reference/generated/numpy.datetime_data.html#numpy.datetime_data "numpy.datetime_data")<br>(dtype, /) | Get information about the step size of a date or time type. |

Business day functions[#](https://numpy.org/doc/stable/reference/routines.datetime.html#business-day-functions "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`busdaycalendar`](https://numpy.org/doc/stable/reference/generated/numpy.busdaycalendar.html#numpy.busdaycalendar "numpy.busdaycalendar")<br>(\[weekmask, holidays\]) | A business day calendar object that efficiently stores information defining valid days for the busday family of functions. |
| [`is_busday`](https://numpy.org/doc/stable/reference/generated/numpy.is_busday.html#numpy.is_busday "numpy.is_busday")<br>(dates\[, weekmask, holidays, ...\]) | Calculates which of the given dates are valid days, and which are not. |
| [`busday_offset`](https://numpy.org/doc/stable/reference/generated/numpy.busday_offset.html#numpy.busday_offset "numpy.busday_offset")<br>(dates, offsets\[, roll, ...\]) | First adjusts the date to fall on a valid day according to the `roll` rule, then applies offsets to the given dates counted in valid days. |
| [`busday_count`](https://numpy.org/doc/stable/reference/generated/numpy.busday_count.html#numpy.busday_count "numpy.busday_count")<br>(begindates, enddates\[, ...\]) | Counts the number of valid days between _begindates_ and _enddates_, not including the day of _enddates_. |

On this page