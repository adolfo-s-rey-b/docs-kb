[Skip to main content](https://matplotlib.org/stable/gallery/ticks/date_demo_rrule.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/ticks/date_demo_rrule.html#sphx-glr-download-gallery-ticks-date-demo-rrule-py)
 to download the full example code.

Placing date ticks using recurrence rules[#](https://matplotlib.org/stable/gallery/ticks/date_demo_rrule.html#placing-date-ticks-using-recurrence-rules "Link to this heading")

================================================================================================================================================================================

The [iCalender RFC](https://tools.ietf.org/html/rfc5545)
 specifies _recurrence rules_ (rrules), that define date sequences. You can use rrules in Matplotlib to place date ticks.

This example sets custom date ticks on every 5th easter.

See [https://dateutil.readthedocs.io/en/stable/rrule.html](https://dateutil.readthedocs.io/en/stable/rrule.html)
 for help with rrules.

![date demo rrule](https://matplotlib.org/stable/_images/sphx_glr_date_demo_rrule_001_2_00x.png)

import datetime

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.dates import [YEARLY](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [DateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
, [RRuleLocator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator "matplotlib.dates.RRuleLocator")
, [drange](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.drange "matplotlib.dates.drange")
, [rrulewrapper](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.rrulewrapper "matplotlib.dates.rrulewrapper")

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

\# tick every 5th easter
[rule](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.rrulewrapper "matplotlib.dates.rrulewrapper")
 \= [rrulewrapper](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.rrulewrapper "matplotlib.dates.rrulewrapper")
([YEARLY](https://docs.python.org/3/library/functions.html#int "builtins.int")
, byeaster\=1, interval\=5)
[loc](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator "matplotlib.dates.RRuleLocator")
 \= [RRuleLocator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator "matplotlib.dates.RRuleLocator")
([rule](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.rrulewrapper "matplotlib.dates.rrulewrapper")
)
[formatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
 \= [DateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
('%m/%d/%y')
[date1](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date")
 \= [datetime.date](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date")
(1952, 1, 1)
[date2](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date")
 \= [datetime.date](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date")
(2004, 4, 12)
[delta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta")
 \= [datetime.timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta")
(days\=100)

[dates](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [drange](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.drange "matplotlib.dates.drange")
([date1](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date")
, [date2](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date")
, [delta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta")
)
[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(len([dates](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))  \# make up some random y values

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([dates](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'o')
[ax.xaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([loc](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator "matplotlib.dates.RRuleLocator")
)
[ax.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
([formatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
)
[ax.xaxis.set\_tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
(rotation\=30, labelsize\=10)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: date_demo_rrule.ipynb`](https://matplotlib.org/stable/_downloads/ae36694c76c52f08fd0adc74b46c61c3/date_demo_rrule.ipynb)

[`Download Python source code: date_demo_rrule.py`](https://matplotlib.org/stable/_downloads/8b32dac4f3661c0ab58c25458083690a/date_demo_rrule.py)

[`Download zipped: date_demo_rrule.zip`](https://matplotlib.org/stable/_downloads/efae152dc07eacbe9b313d9885c4e20f/date_demo_rrule.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)