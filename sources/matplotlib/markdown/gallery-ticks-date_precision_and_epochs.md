[Skip to main content](https://matplotlib.org/stable/gallery/ticks/date_precision_and_epochs.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

Note

[Go to the end](https://matplotlib.org/stable/gallery/ticks/date_precision_and_epochs.html#sphx-glr-download-gallery-ticks-date-precision-and-epochs-py)
 to download the full example code.

Date precision and epochs[#](https://matplotlib.org/stable/gallery/ticks/date_precision_and_epochs.html#date-precision-and-epochs "Link to this heading")

==========================================================================================================================================================

Matplotlib can handle [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "(in Python v3.14)")
 objects and [`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")
 objects using a unit converter that recognizes these dates and converts them to floating point numbers.

Before Matplotlib 3.3, the default for this conversion returns a float that was days since "0000-12-31T00:00:00". As of Matplotlib 3.3, the default is days from "1970-01-01T00:00:00". This allows more resolution for modern dates. "2020-01-01" with the old epoch converted to 730120, and a 64-bit floating point number has a resolution of 2^{-52}, or approximately 14 microseconds, so microsecond precision was lost. With the new default epoch "2020-01-01" is 10957.0, so the achievable resolution is 0.21 microseconds.

import datetime

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.dates as mdates

def \_reset\_epoch\_for\_tutorial():
    """
    Users (and downstream libraries) should not use the private method of
    resetting the epoch.
    """
    mdates.\_reset\_epoch\_test\_example()

Datetime[#](https://matplotlib.org/stable/gallery/ticks/date_precision_and_epochs.html#datetime "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

Python [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "(in Python v3.14)")
 objects have microsecond resolution, so with the old default matplotlib dates could not round-trip full-resolution datetime objects.

[old\_epoch](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= '0000-12-31T00:00:00'
[new\_epoch](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= '1970-01-01T00:00:00'

\_reset\_epoch\_for\_tutorial()  \# Don't do this.  Just for this tutorial.
[mdates.set\_epoch](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.set_epoch "matplotlib.dates.set_epoch")
([old\_epoch](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)  \# old epoch (pre MPL 3.3)

[date1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
 \= [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
(2000, 1, 1, 0, 10, 0, 12,
                          tzinfo\=[datetime.timezone.utc](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone")
)
[mdate1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [mdates.date2num](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.date2num "matplotlib.dates.date2num")
([date1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
)
print('Before Roundtrip: ', [date1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
, 'Matplotlib date:', [mdate1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)
[date2](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
 \= [mdates.num2date](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.num2date "matplotlib.dates.num2date")
([mdate1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)
print('After Roundtrip:  ', [date2](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
)

Before Roundtrip:  2000-01-01 00:10:00.000012+00:00 Matplotlib date: 730120.0069444446
After Roundtrip:   2000-01-01 00:10:00.000020+00:00

Note this is only a round-off error, and there is no problem for dates closer to the old epoch:

[date1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
 \= [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
(10, 1, 1, 0, 10, 0, 12,
                          tzinfo\=[datetime.timezone.utc](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone")
)
[mdate1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [mdates.date2num](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.date2num "matplotlib.dates.date2num")
([date1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
)
print('Before Roundtrip: ', [date1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
, 'Matplotlib date:', [mdate1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)
[date2](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
 \= [mdates.num2date](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.num2date "matplotlib.dates.num2date")
([mdate1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)
print('After Roundtrip:  ', [date2](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
)

Before Roundtrip:  0010-01-01 00:10:00.000012+00:00 Matplotlib date: 3288.006944444583
After Roundtrip:   0010-01-01 00:10:00.000012+00:00

If a user wants to use modern dates at microsecond precision, they can change the epoch using [`set_epoch`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.set_epoch "matplotlib.dates.set_epoch")
. However, the epoch has to be set before any date operations to prevent confusion between different epochs. Trying to change the epoch later will raise a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in Python v3.14)")
.

try:
    [mdates.set\_epoch](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.set_epoch "matplotlib.dates.set_epoch")
([new\_epoch](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)  \# this is the new MPL 3.3 default.
except RuntimeError as e:
    print('RuntimeError:', str(e))

RuntimeError: set\_epoch must be called before dates plotted.

For this tutorial, we reset the sentinel using a private method, but users should just set the epoch once, if at all.

\_reset\_epoch\_for\_tutorial()  \# Just being done for this tutorial.
[mdates.set\_epoch](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.set_epoch "matplotlib.dates.set_epoch")
([new\_epoch](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[date1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
 \= [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
(2020, 1, 1, 0, 10, 0, 12,
                          tzinfo\=[datetime.timezone.utc](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone")
)
[mdate1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [mdates.date2num](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.date2num "matplotlib.dates.date2num")
([date1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
)
print('Before Roundtrip: ', [date1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
, 'Matplotlib date:', [mdate1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)
[date2](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
 \= [mdates.num2date](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.num2date "matplotlib.dates.num2date")
([mdate1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)
print('After Roundtrip:  ', [date2](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
)

Before Roundtrip:  2020-01-01 00:10:00.000012+00:00 Matplotlib date: 18262.006944444583
After Roundtrip:   2020-01-01 00:10:00.000012+00:00

datetime64[#](https://matplotlib.org/stable/gallery/ticks/date_precision_and_epochs.html#datetime64 "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

[`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")
 objects have microsecond precision for a much larger timespace than [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "(in Python v3.14)")
 objects. However, currently Matplotlib time is only converted back to datetime objects, which have microsecond resolution, and years that only span 0000 to 9999.

\_reset\_epoch\_for\_tutorial()  \# Don't do this.  Just for this tutorial.
[mdates.set\_epoch](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.set_epoch "matplotlib.dates.set_epoch")
([new\_epoch](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[date1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
 \= [np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
('2000-01-01T00:10:00.000012')
[mdate1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [mdates.date2num](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.date2num "matplotlib.dates.date2num")
([date1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
)
print('Before Roundtrip: ', [date1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
, 'Matplotlib date:', [mdate1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)
[date2](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
 \= [mdates.num2date](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.num2date "matplotlib.dates.num2date")
([mdate1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)
print('After Roundtrip:  ', [date2](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
)

Before Roundtrip:  2000-01-01T00:10:00.000012 Matplotlib date: 10957.006944444583
After Roundtrip:   2000-01-01 00:10:00.000012+00:00

Plotting[#](https://matplotlib.org/stable/gallery/ticks/date_precision_and_epochs.html#plotting "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

This all of course has an effect on plotting. With the old default epoch the times were rounded during the internal `date2num` conversion, leading to jumps in the data:

\_reset\_epoch\_for\_tutorial()  \# Don't do this.  Just for this tutorial.
[mdates.set\_epoch](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.set_epoch "matplotlib.dates.set_epoch")
([old\_epoch](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
('2000-01-01T00:00:00.0', '2000-01-01T00:00:00.000100',
              dtype\='datetime64\[us\]')
\# simulate the plot being made using the old epoch
[xold](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[[mdates.num2date](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.num2date "matplotlib.dates.num2date")\
([mdates.date2num](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.date2num "matplotlib.dates.date2num")\
(d)) for d in [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\])
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, len([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))

\# resetting the Epoch so plots are comparable
\_reset\_epoch\_for\_tutorial()  \# Don't do this.  Just for this tutorial.
[mdates.set\_epoch](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.set_epoch "matplotlib.dates.set_epoch")
([new\_epoch](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\='constrained')
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([xold](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Epoch: ' + [mdates.get\_epoch](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.get_epoch "matplotlib.dates.get_epoch")
())
[ax.xaxis.set\_tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
(rotation\=40)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Epoch: 1970-01-01T00:00:00](https://matplotlib.org/stable/_images/sphx_glr_date_precision_and_epochs_001_2_00x.png)

For dates plotted using the more recent epoch, the plot is smooth:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\='constrained')
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Epoch: ' + [mdates.get\_epoch](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.get_epoch "matplotlib.dates.get_epoch")
())
[ax.xaxis.set\_tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
(rotation\=40)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

\_reset\_epoch\_for\_tutorial()  \# Don't do this.  Just for this tutorial.

![Epoch: 1970-01-01T00:00:00](https://matplotlib.org/stable/_images/sphx_glr_date_precision_and_epochs_002_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.dates.num2date`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.num2date "matplotlib.dates.num2date")
    
*   [`matplotlib.dates.date2num`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.date2num "matplotlib.dates.date2num")
    
*   [`matplotlib.dates.set_epoch`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.set_epoch "matplotlib.dates.set_epoch")
    

**Total running time of the script:** (0 minutes 1.359 seconds)

[`Download Jupyter notebook: date_precision_and_epochs.ipynb`](https://matplotlib.org/stable/_downloads/05b5828bd1a866c387ec6e60c22612f4/date_precision_and_epochs.ipynb)

[`Download Python source code: date_precision_and_epochs.py`](https://matplotlib.org/stable/_downloads/586a88c62e8a2d883ea392b25f0e62a9/date_precision_and_epochs.py)

[`Download zipped: date_precision_and_epochs.zip`](https://matplotlib.org/stable/_downloads/91e0ab6abc7fca732956cf46aa6b2ec6/date_precision_and_epochs.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page