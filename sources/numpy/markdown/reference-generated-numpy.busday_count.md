[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.busday_count.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.busday_count.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.busday_count.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.busday_count.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.busday_count.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.busday_count.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.busday_count.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.busday_count.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.busday_count.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.busday_count.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.busday_count.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.busday_count.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.busday_count.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.busday_count.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.busday_count.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.busday_count.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.busday_count.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.busday_count.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.busday_count.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.busday_count.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.busday_count.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.busday_count.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.busday\_count[#](https://numpy.org/doc/stable/reference/generated/numpy.busday_count.html#numpy-busday-count "Link to this heading")

===========================================================================================================================================

numpy.busday\_count(_begindates_, _enddates_, _weekmask\='1111100'_, _holidays\=\[\]_, _busdaycal\=None_, _out\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.busday_count.html#numpy.busday_count "Link to this definition")

Counts the number of valid days between _begindates_ and _enddates_, not including the day of _enddates_.

If `enddates` specifies a date value that is earlier than the corresponding `begindates` date value, the count will be negative.

Parameters:

**begindates**array\_like of datetime64\[D\]

The array of the first dates for counting.

**enddates**array\_like of datetime64\[D\]

The array of the end dates for counting, which are excluded from the count themselves.

**weekmask**str or array\_like of bool, optional

A seven-element array indicating which of Monday through Sunday are valid days. May be specified as a length-seven list or array, like \[1,1,1,1,1,0,0\]; a length-seven string, like ‘1111100’; or a string like “Mon Tue Wed Thu Fri”, made up of 3-character abbreviations for weekdays, optionally separated by white space. Valid abbreviations are: Mon Tue Wed Thu Fri Sat Sun

**holidays**array\_like of datetime64\[D\], optional

An array of dates to consider as invalid dates. They may be specified in any order, and NaT (not-a-time) dates are ignored. This list is saved in a normalized form that is suited for fast calculations of valid days.

**busdaycal**busdaycalendar, optional

A [`busdaycalendar`](https://numpy.org/doc/stable/reference/generated/numpy.busdaycalendar.html#numpy.busdaycalendar "numpy.busdaycalendar")
 object which specifies the valid days. If this parameter is provided, neither weekmask nor holidays may be provided.

**out**array of int, optional

If provided, this array is filled with the result.

Returns:

**out**array of int

An array with a shape from broadcasting `begindates` and `enddates` together, containing the number of valid days between the begin and end dates.

See also

[`busdaycalendar`](https://numpy.org/doc/stable/reference/generated/numpy.busdaycalendar.html#numpy.busdaycalendar "numpy.busdaycalendar")

An object that specifies a custom set of valid days.

[`is_busday`](https://numpy.org/doc/stable/reference/generated/numpy.is_busday.html#numpy.is_busday "numpy.is_busday")

Returns a boolean array indicating valid days.

[`busday_offset`](https://numpy.org/doc/stable/reference/generated/numpy.busday_offset.html#numpy.busday_offset "numpy.busday_offset")

Applies an offset counted in valid days.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> \# Number of weekdays in January 2011
... np.busday\_count('2011-01', '2011-02')
21
\>>> \# Number of weekdays in 2011
\>>> np.busday\_count('2011', '2012')
260
\>>> \# Number of Saturdays in 2011
... np.busday\_count('2011', '2012', weekmask\='Sat')
53

Copy to clipboard

Go BackOpen In Tab

On this page