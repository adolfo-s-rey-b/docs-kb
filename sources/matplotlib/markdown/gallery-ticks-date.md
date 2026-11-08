[Skip to main content](https://matplotlib.org/stable/gallery/ticks/date.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/ticks/date.html#sphx-glr-download-gallery-ticks-date-py)
 to download the full example code.

Date tick labels[#](https://matplotlib.org/stable/gallery/ticks/date.html#date-tick-labels "Link to this heading")

===================================================================================================================

Matplotlib date plotting is done by converting date instances into days since an epoch (by default 1970-01-01T00:00:00). The [`matplotlib.dates`](https://matplotlib.org/stable/api/dates_api.html#module-matplotlib.dates "matplotlib.dates")
 module provides the converter functions [`date2num`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.date2num "matplotlib.dates.date2num")
 and [`num2date`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.num2date "matplotlib.dates.num2date")
 that convert [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")
 and [`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")
 objects to and from Matplotlib's internal representation. These data types are registered with the unit conversion mechanism described in [`matplotlib.units`](https://matplotlib.org/stable/api/units_api.html#module-matplotlib.units "matplotlib.units")
, so the conversion happens automatically for the user. The registration process also sets the default tick `locator` and `formatter` for the axis to be [`AutoDateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
 and [`AutoDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateFormatter "matplotlib.dates.AutoDateFormatter")
.

An alternative formatter is the [`ConciseDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")
, used in the second `Axes` below (see [Format date ticks using ConciseDateFormatter](https://matplotlib.org/stable/gallery/ticks/date_concise_formatter.html)
), which often removes the need to rotate the tick labels. The last `Axes` formats the dates manually, using [`DateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
 to format the dates using the format strings documented at [`datetime.date.strftime`](https://docs.python.org/3/library/datetime.html#datetime.date.strftime "(in Python v3.14)")
.

![DefaultFormatter, ConciseFormatter, Manual DateFormatter](https://matplotlib.org/stable/_images/sphx_glr_date_001_2_00x.png)

import matplotlib.pyplot as plt

import matplotlib.cbook as cbook
import matplotlib.dates as mdates

\# Load a numpy record array from yahoo csv data with fields date, open, high,
\# low, close, volume, adj\_close from the mpl-data/sample\_data directory. The
\# record array stores the date as an np.datetime64 with a day unit ('D') in
\# the date column.
[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
('goog.npz')\['price\_data'\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 1, figsize\=(6.4, 7), layout\='constrained')
\# common to all three:
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
('date', 'adj\_close', [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    \# Major ticks every half year, minor ticks every month,
    [ax.xaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([mdates.MonthLocator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MonthLocator "matplotlib.dates.MonthLocator")
(bymonth\=(1, 7)))
    [ax.xaxis.set\_minor\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html#matplotlib.axis.Axis.set_minor_locator "matplotlib.axis.Axis.set_minor_locator")
([mdates.MonthLocator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MonthLocator "matplotlib.dates.MonthLocator")
())
    [ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
(True)
    [ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
(r'Price \[\\$\]')

\# different formats:
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\]
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('DefaultFormatter', loc\='left', y\=0.85, x\=0.02, fontsize\='medium')

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\]
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('ConciseFormatter', loc\='left', y\=0.85, x\=0.02, fontsize\='medium')
[ax.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
(
    [mdates.ConciseDateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")
([ax.xaxis.get\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_locator.html#matplotlib.axis.Axis.get_major_locator "matplotlib.axis.Axis.get_major_locator")
()))

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\]
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Manual DateFormatter', loc\='left', y\=0.85, x\=0.02,
             fontsize\='medium')
\# Text in the x-axis will be displayed in 'YYYY-mm' format.
[ax.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
([mdates.DateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
('%Y-%b'))
\# Rotates and right-aligns the x labels so they don't crowd each other.
[ax.xaxis.set\_tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
(rotation\=30, rotation\_mode\='xtick')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 2.665 seconds)

[`Download Jupyter notebook: date.ipynb`](https://matplotlib.org/stable/_downloads/8aeb247fbe7ba03dc0d33ec44d3b57c4/date.ipynb)

[`Download Python source code: date.py`](https://matplotlib.org/stable/_downloads/d6d4575a26e06f98d4a66040349ca783/date.py)

[`Download zipped: date.zip`](https://matplotlib.org/stable/_downloads/d33ac935e7451f91d63d4949dfcb91f1/date.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)