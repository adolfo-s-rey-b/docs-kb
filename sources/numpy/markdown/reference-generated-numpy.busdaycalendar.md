[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.busdaycalendar.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.busdaycalendar.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.busdaycalendar.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.busdaycalendar.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.busdaycalendar.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.busdaycalendar.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.busdaycalendar.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.busdaycalendar.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.busdaycalendar.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.busdaycalendar.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.busdaycalendar.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.busdaycalendar.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.busdaycalendar.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.busdaycalendar.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.busdaycalendar.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.busdaycalendar.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.busdaycalendar.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.busdaycalendar.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.busdaycalendar.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.busdaycalendar.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.busdaycalendar.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.busdaycalendar.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.busdaycalendar[#](https://numpy.org/doc/stable/reference/generated/numpy.busdaycalendar.html#numpy-busdaycalendar "Link to this heading")

================================================================================================================================================

_class_ numpy.busdaycalendar(_weekmask\='1111100'_, _holidays\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/__init__.py)
[#](https://numpy.org/doc/stable/reference/generated/numpy.busdaycalendar.html#numpy.busdaycalendar "Link to this definition")

A business day calendar object that efficiently stores information defining valid days for the busday family of functions.

The default valid days are Monday through Friday (“business days”). A busdaycalendar object can be specified with any set of weekly valid days, plus an optional “holiday” dates that always will be invalid.

Once a busdaycalendar object is created, the weekmask and holidays cannot be modified.

Parameters:

**weekmask**str or array\_like of bool, optional

A seven-element array indicating which of Monday through Sunday are valid days. May be specified as a length-seven list or array, like \[1,1,1,1,1,0,0\]; a length-seven string, like ‘1111100’; or a string like “Mon Tue Wed Thu Fri”, made up of 3-character abbreviations for weekdays, optionally separated by white space. Valid abbreviations are: Mon Tue Wed Thu Fri Sat Sun

**holidays**array\_like of datetime64\[D\], optional

An array of dates to consider as invalid dates, no matter which weekday they fall upon. Holiday dates may be specified in any order, and NaT (not-a-time) dates are ignored. This list is saved in a normalized form that is suited for fast calculations of valid days.

Attributes:

[`weekmask`](https://numpy.org/doc/stable/reference/generated/numpy.busdaycalendar.weekmask.html#numpy.busdaycalendar.weekmask "numpy.busdaycalendar.weekmask")
(copy) seven-element array of bool

A copy of the seven-element boolean mask indicating valid days.

[`holidays`](https://numpy.org/doc/stable/reference/generated/numpy.busdaycalendar.holidays.html#numpy.busdaycalendar.holidays "numpy.busdaycalendar.holidays")
(copy) sorted array of datetime64\[D\]

A copy of the holiday array indicating additional invalid days.

Returns:

**out**busdaycalendar

A business day calendar object containing the specified weekmask and holidays values.

See also

[`is_busday`](https://numpy.org/doc/stable/reference/generated/numpy.is_busday.html#numpy.is_busday "numpy.is_busday")

Returns a boolean array indicating valid days.

[`busday_offset`](https://numpy.org/doc/stable/reference/generated/numpy.busday_offset.html#numpy.busday_offset "numpy.busday_offset")

Applies an offset counted in valid days.

[`busday_count`](https://numpy.org/doc/stable/reference/generated/numpy.busday_count.html#numpy.busday_count "numpy.busday_count")

Counts how many valid days are in a half-open date range.

Notes

Once a busdaycalendar object is created, you cannot modify the weekmask or holidays. The attributes return copies of internal data.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> \# Some important days in July
... bdd \= np.busdaycalendar(
...             holidays\=\['2011-07-01', '2011-07-04', '2011-07-17'\])
\>>> \# Default is Monday to Friday weekdays
... bdd.weekmask
array(\[ True,  True,  True,  True,  True, False, False\])
\>>> \# Any holidays already on the weekend are removed
... bdd.holidays
array(\['2011-07-01', '2011-07-04'\], dtype='datetime64\[D\]')

Copy to clipboard

Go BackOpen In Tab

On this page