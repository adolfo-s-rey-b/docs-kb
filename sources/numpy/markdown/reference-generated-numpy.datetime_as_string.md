[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.datetime_as_string.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.datetime_as_string.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.datetime_as_string.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.datetime_as_string.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.datetime_as_string.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.datetime_as_string.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.datetime_as_string.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.datetime_as_string.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.datetime_as_string.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.datetime_as_string.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.datetime_as_string.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.datetime_as_string.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.datetime_as_string.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.datetime_as_string.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.datetime_as_string.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.datetime_as_string.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.datetime_as_string.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.datetime_as_string.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.datetime_as_string.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.datetime_as_string.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.datetime_as_string.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.datetime_as_string.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.datetime\_as\_string[#](https://numpy.org/doc/stable/reference/generated/numpy.datetime_as_string.html#numpy-datetime-as-string "Link to this heading")

==============================================================================================================================================================

numpy.datetime\_as\_string(_arr_, _unit\=None_, _timezone\='naive'_, _casting\='same\_kind'_)[#](https://numpy.org/doc/stable/reference/generated/numpy.datetime_as_string.html#numpy.datetime_as_string "Link to this definition")

Convert an array of datetimes into an array of strings.

Parameters:

**arr**array\_like of datetime64

The array of UTC timestamps to format.

**unit**str

One of None, ‘auto’, or a [datetime unit](https://numpy.org/doc/stable/reference/arrays.datetime.html#arrays-dtypes-dateunits)
.

**timezone**{‘naive’, ‘UTC’, ‘local’} or tzinfo

Timezone information to use when displaying the datetime. If ‘UTC’, end with a Z to indicate UTC time. If ‘local’, convert to the local timezone first, and suffix with a +-#### timezone offset. If a tzinfo object, then do as with ‘local’, but use the specified timezone.

**casting**{‘no’, ‘equiv’, ‘safe’, ‘same\_kind’, ‘unsafe’}

Casting to allow when changing between datetime units.

Returns:

**str\_arr**ndarray

An array of strings the same shape as _arr_.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from zoneinfo import ZoneInfo
\>>> d \= np.arange('2002-10-27T04:30', 4\*60, 60, dtype\='M8\[m\]')
\>>> d
array(\['2002-10-27T04:30', '2002-10-27T05:30', '2002-10-27T06:30',\
       '2002-10-27T07:30'\], dtype='datetime64\[m\]')

Copy to clipboard

Setting the timezone to UTC shows the same information, but with a Z suffix

\>>> np.datetime\_as\_string(d, timezone\='UTC')
array(\['2002-10-27T04:30Z', '2002-10-27T05:30Z', '2002-10-27T06:30Z',\
       '2002-10-27T07:30Z'\], dtype='<U35')

Copy to clipboard

Note that we picked datetimes that cross a DST boundary. Passing in a `ZoneInfo` object will print the appropriate offset

\>>> np.datetime\_as\_string(d, timezone\=ZoneInfo('US/Eastern'))
array(\['2002-10-27T00:30-0400', '2002-10-27T01:30-0400',\
       '2002-10-27T01:30-0500', '2002-10-27T02:30-0500'\], dtype='<U39')

Copy to clipboard

Passing in a unit will change the precision

\>>> np.datetime\_as\_string(d, unit\='h')
array(\['2002-10-27T04', '2002-10-27T05', '2002-10-27T06', '2002-10-27T07'\],
      dtype='<U32')
\>>> np.datetime\_as\_string(d, unit\='s')
array(\['2002-10-27T04:30:00', '2002-10-27T05:30:00', '2002-10-27T06:30:00',\
       '2002-10-27T07:30:00'\], dtype='<U38')

Copy to clipboard

‘casting’ can be used to specify whether precision can be changed

\>>> np.datetime\_as\_string(d, unit\='h', casting\='safe')
Traceback (most recent call last):
    ...
TypeError: Cannot create a datetime string as units 'h' from a NumPy
datetime with units 'm' according to the rule 'safe'

Copy to clipboard

Go BackOpen In Tab

On this page