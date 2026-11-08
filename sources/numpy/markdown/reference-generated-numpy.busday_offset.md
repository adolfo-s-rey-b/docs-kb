[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.busday_offset.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.busday_offset.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.busday_offset.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.busday_offset.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.busday_offset.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.busday_offset.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.busday_offset.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.busday_offset.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.busday_offset.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.busday_offset.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.busday_offset.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.busday_offset.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.busday_offset.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.busday_offset.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.busday_offset.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.busday_offset.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.busday_offset.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.busday_offset.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.busday_offset.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.busday_offset.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.busday_offset.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.busday_offset.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.busday\_offset[#](https://numpy.org/doc/stable/reference/generated/numpy.busday_offset.html#numpy-busday-offset "Link to this heading")

==============================================================================================================================================

numpy.busday\_offset(_dates_, _offsets_, _roll\='raise'_, _weekmask\='1111100'_, _holidays\=None_, _busdaycal\=None_, _out\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.busday_offset.html#numpy.busday_offset "Link to this definition")

First adjusts the date to fall on a valid day according to the `roll` rule, then applies offsets to the given dates counted in valid days.

Parameters:

**dates**array\_like of datetime64\[D\]

The array of dates to process.

**offsets**array\_like of int

The array of offsets, which is broadcast with `dates`.

**roll**{‘raise’, ‘nat’, ‘forward’, ‘following’, ‘backward’, ‘preceding’, ‘modifiedfollowing’, ‘modifiedpreceding’}, optional

How to treat dates that do not fall on a valid day. The default is ‘raise’.

*   ‘raise’ means to raise an exception for an invalid day.
    
*   ‘nat’ means to return a NaT (not-a-time) for an invalid day.
    
*   ‘forward’ and ‘following’ mean to take the first valid day later in time.
    
*   ‘backward’ and ‘preceding’ mean to take the first valid day earlier in time.
    
*   ‘modifiedfollowing’ means to take the first valid day later in time unless it is across a Month boundary, in which case to take the first valid day earlier in time.
    
*   ‘modifiedpreceding’ means to take the first valid day earlier in time unless it is across a Month boundary, in which case to take the first valid day later in time.
    

**weekmask**str or array\_like of bool, optional

A seven-element array indicating which of Monday through Sunday are valid days. May be specified as a length-seven list or array, like \[1,1,1,1,1,0,0\]; a length-seven string, like ‘1111100’; or a string like “Mon Tue Wed Thu Fri”, made up of 3-character abbreviations for weekdays, optionally separated by white space. Valid abbreviations are: Mon Tue Wed Thu Fri Sat Sun

**holidays**array\_like of datetime64\[D\], optional

An array of dates to consider as invalid dates. They may be specified in any order, and NaT (not-a-time) dates are ignored. This list is saved in a normalized form that is suited for fast calculations of valid days.

**busdaycal**busdaycalendar, optional

A [`busdaycalendar`](https://numpy.org/doc/stable/reference/generated/numpy.busdaycalendar.html#numpy.busdaycalendar "numpy.busdaycalendar")
 object which specifies the valid days. If this parameter is provided, neither weekmask nor holidays may be provided.

**out**array of datetime64\[D\], optional

If provided, this array is filled with the result.

Returns:

**out**array of datetime64\[D\]

An array with a shape from broadcasting `dates` and `offsets` together, containing the dates with offsets applied.

See also

[`busdaycalendar`](https://numpy.org/doc/stable/reference/generated/numpy.busdaycalendar.html#numpy.busdaycalendar "numpy.busdaycalendar")

An object that specifies a custom set of valid days.

[`is_busday`](https://numpy.org/doc/stable/reference/generated/numpy.is_busday.html#numpy.is_busday "numpy.is_busday")

Returns a boolean array indicating valid days.

[`busday_count`](https://numpy.org/doc/stable/reference/generated/numpy.busday_count.html#numpy.busday_count "numpy.busday_count")

Counts how many valid days are in a half-open date range.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> \# First business day in October 2011 (not accounting for holidays)
... np.busday\_offset('2011-10', 0, roll\='forward')
np.datetime64('2011-10-03')
\>>> \# Last business day in February 2012 (not accounting for holidays)
... np.busday\_offset('2012-03', \-1, roll\='forward')
np.datetime64('2012-02-29')
\>>> \# Third Wednesday in January 2011
... np.busday\_offset('2011-01', 2, roll\='forward', weekmask\='Wed')
np.datetime64('2011-01-19')
\>>> \# 2012 Mother's Day in Canada and the U.S.
... np.busday\_offset('2012-05', 1, roll\='forward', weekmask\='Sun')
np.datetime64('2012-05-13')

Copy to clipboard

\>>> \# First business day on or after a date
... np.busday\_offset('2011-03-20', 0, roll\='forward')
np.datetime64('2011-03-21')
\>>> np.busday\_offset('2011-03-22', 0, roll\='forward')
np.datetime64('2011-03-22')
\>>> \# First business day after a date
... np.busday\_offset('2011-03-20', 1, roll\='backward')
np.datetime64('2011-03-21')
\>>> np.busday\_offset('2011-03-22', 1, roll\='backward')
np.datetime64('2011-03-23')

Copy to clipboard

Go BackOpen In Tab

On this page