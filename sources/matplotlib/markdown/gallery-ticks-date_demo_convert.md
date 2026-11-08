[Skip to main content](https://matplotlib.org/stable/gallery/ticks/date_demo_convert.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/ticks/date_demo_convert.html#sphx-glr-download-gallery-ticks-date-demo-convert-py)
 to download the full example code.

Date converter demo[#](https://matplotlib.org/stable/gallery/ticks/date_demo_convert.html#date-converter-demo "Link to this heading")

======================================================================================================================================

![date demo convert](https://matplotlib.org/stable/_images/sphx_glr_date_demo_convert_001_2_00x.png)

import datetime

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.dates import [DateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
, [DayLocator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DayLocator "matplotlib.dates.DayLocator")
, [HourLocator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.HourLocator "matplotlib.dates.HourLocator")
, [drange](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.drange "matplotlib.dates.drange")

[date1](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
 \= [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
(2000, 3, 2)
[date2](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
 \= [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
(2000, 3, 6)
[delta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta")
 \= [datetime.timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta")
(hours\=6)
[dates](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [drange](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.drange "matplotlib.dates.drange")
([date1](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
, [date2](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
, [delta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta")
)

[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len([dates](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([dates](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2, 'o')

\# This is superfluous, since the autoscaler should get it right, but
\# use date2num and num2date to convert between dates and floats if
\# you want; both date2num and num2date convert an instance or sequence.
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
([dates](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\], [dates](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[\-1\])

\# The hour locator takes the hour or sequence of hours you want to
\# tick, not the base multiple.
[ax.xaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([DayLocator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DayLocator "matplotlib.dates.DayLocator")
())
[ax.xaxis.set\_minor\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html#matplotlib.axis.Axis.set_minor_locator "matplotlib.axis.Axis.set_minor_locator")
([HourLocator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.HourLocator "matplotlib.dates.HourLocator")
(range(0, 25, 6)))
[ax.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
([DateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
('%Y-%m-%d'))

[ax.fmt\_xdata](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
 \= [DateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
('%Y-%m-%d %H:%M:%S')
[fig.autofmt\_xdate](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.autofmt_xdate.html#matplotlib.figure.Figure.autofmt_xdate "matplotlib.figure.Figure.autofmt_xdate")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: date_demo_convert.ipynb`](https://matplotlib.org/stable/_downloads/3abd560a71cfedb417a54dbdbc713056/date_demo_convert.ipynb)

[`Download Python source code: date_demo_convert.py`](https://matplotlib.org/stable/_downloads/ac73ab64c576ed49d53ad046d22c6af7/date_demo_convert.py)

[`Download zipped: date_demo_convert.zip`](https://matplotlib.org/stable/_downloads/69fe3e9985db2a666c5b9161a457590f/date_demo_convert.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)