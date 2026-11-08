[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.datetime_data.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.datetime\_data[#](https://numpy.org/doc/stable/reference/generated/numpy.datetime_data.html#numpy-datetime-data "Link to this heading")

==============================================================================================================================================

numpy.datetime\_data(_dtype_, _/_)[#](https://numpy.org/doc/stable/reference/generated/numpy.datetime_data.html#numpy.datetime_data "Link to this definition")

Get information about the step size of a date or time type.

The returned tuple can be passed as the second argument of [`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
 and [`numpy.timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
.

Parameters:

**dtype**dtype

The dtype object, which must be a [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
 or [`timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
 type.

Returns:

**unit**str

The [datetime unit](https://numpy.org/doc/stable/reference/arrays.datetime.html#arrays-dtypes-dateunits)
 on which this dtype is based.

**count**int

The number of base units in a step.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> dt\_25s \= np.dtype('timedelta64\[25s\]')
\>>> np.datetime\_data(dt\_25s)
('s', 25)
\>>> np.array(10, dt\_25s).astype('timedelta64\[s\]')
array(250, dtype='timedelta64\[s\]')

Copy to clipboard

The result can be used to construct a datetime that uses the same units as a timedelta

\>>> np.datetime64('2010', np.datetime\_data(dt\_25s))
np.datetime64('2010-01-01T00:00:00','25s')

Copy to clipboard

Go BackOpen In Tab

On this page