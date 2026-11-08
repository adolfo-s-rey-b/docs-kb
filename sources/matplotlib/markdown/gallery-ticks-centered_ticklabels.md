[Skip to main content](https://matplotlib.org/stable/gallery/ticks/centered_ticklabels.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/ticks/centered_ticklabels.html#sphx-glr-download-gallery-ticks-centered-ticklabels-py)
 to download the full example code.

Center labels between ticks[#](https://matplotlib.org/stable/gallery/ticks/centered_ticklabels.html#center-labels-between-ticks "Link to this heading")

========================================================================================================================================================

Tick labels are aligned relative to their associated tick, and are by default centered.

However, there is no direct way to center the labels between ticks. To fake this behavior, one can place a minor tick in between the major ticks. Then label the minor tick, and hide the minor tick lines and the major tick labels.

Here is an example that labels the months, centered between the ticks.

![centered ticklabels](https://matplotlib.org/stable/_images/sphx_glr_centered_ticklabels_001_2_00x.png)

import matplotlib.pyplot as plt

import matplotlib.cbook as cbook
import matplotlib.dates as dates
import matplotlib.ticker as ticker

\# Load some financial data; Google's stock price
[r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
('goog.npz')\['price\_data'\]
[r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[\-250:\]  \# get the last 250 days

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\["date"\], [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\["adj\_close"\])

[ax.xaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([dates.MonthLocator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MonthLocator "matplotlib.dates.MonthLocator")
())
\# 16 is a slight approximation since months differ in number of days.
[ax.xaxis.set\_minor\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html#matplotlib.axis.Axis.set_minor_locator "matplotlib.axis.Axis.set_minor_locator")
([dates.MonthLocator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MonthLocator "matplotlib.dates.MonthLocator")
(bymonthday\=16))

\# The NullFormatter removes the major tick labels
[ax.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
([ticker.NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
[ax.xaxis.set\_minor\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_formatter.html#matplotlib.axis.Axis.set_minor_formatter "matplotlib.axis.Axis.set_minor_formatter")
([dates.DateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
('%b'))

\# Remove the minor tick lines
[ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(axis\='x', which\='minor', tick1On\=False, tick2On\=False)

[imid](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= len([r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) // 2
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
(str([r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\["date"\]\[[imid](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\].item().year))
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: centered_ticklabels.ipynb`](https://matplotlib.org/stable/_downloads/a883dce78e0870655211374a41275631/centered_ticklabels.ipynb)

[`Download Python source code: centered_ticklabels.py`](https://matplotlib.org/stable/_downloads/09364d81fc1cbd08346bd216bcc75656/centered_ticklabels.py)

[`Download zipped: centered_ticklabels.zip`](https://matplotlib.org/stable/_downloads/294462ada4f5afc6763f13e5c3527a36/centered_ticklabels.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)