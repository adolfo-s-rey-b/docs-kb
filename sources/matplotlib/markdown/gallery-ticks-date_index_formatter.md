[Skip to main content](https://matplotlib.org/stable/gallery/ticks/date_index_formatter.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/ticks/date_index_formatter.html#sphx-glr-download-gallery-ticks-date-index-formatter-py)
 to download the full example code.

Custom tick formatter for time series[#](https://matplotlib.org/stable/gallery/ticks/date_index_formatter.html#custom-tick-formatter-for-time-series "Link to this heading")

=============================================================================================================================================================================

When plotting daily data, e.g., financial time series, one often wants to leave out days on which there is no data, for instance weekends, so that the data are plotted at regular intervals without extra spaces for the days with no data. The example shows how to use an 'index formatter' to achieve the desired plot.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook
from matplotlib.dates import [DateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
, [DayLocator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DayLocator "matplotlib.dates.DayLocator")
import matplotlib.lines as ml
from matplotlib.ticker import [Formatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")

\# Load a structured numpy array from yahoo csv data with fields date, open, high,
\# low, close, volume, adj\_close from the mpl-data/sample\_data directory. The
\# record array stores the date as an np.datetime64 with a day unit ('D') in
\# the date column (\`\`r\['date'\]\`\`).
[r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
('goog.npz')\['price\_data'\]
[r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:9\]  \# get the first 9 days

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, figsize\=(6, 6), layout\='constrained')
[fig.get\_layout\_engine](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_layout_engine.html#matplotlib.figure.Figure.get_layout_engine "matplotlib.figure.Figure.get_layout_engine")
().set(hspace\=0.15)

\# First we'll do it the default way, with gaps on weekends
[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\["date"\], [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\["adj\_close"\], 'o-')

\# Highlight gaps in daily data
[gaps](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.flatnonzero](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html#numpy.flatnonzero "numpy.flatnonzero")
([np.diff](https://numpy.org/doc/stable/reference/generated/numpy.diff.html#numpy.diff "numpy.diff")
([r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\["date"\]) \> [np.timedelta64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
(1, 'D'))
for [gap](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 in [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[\['date', 'adj\_close'\]\]\[[np.stack](https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack "numpy.stack")\
(([gaps](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [gaps](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
 + 1)).T\]:
    [ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([gap](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['date'\], [gap](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['adj\_close'\], 'w--', lw\=2)
[ax1.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(handles\=\[[ml.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
(\[\], \[\], ls\='--', label\='Gaps in daily data')\])

[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Plot y at x Coordinates")
[ax1.xaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([DayLocator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DayLocator "matplotlib.dates.DayLocator")
())
[ax1.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
([DateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
('%a'))

\# Next we'll write a custom index formatter. Below we will plot
\# the data against an index that goes from 0, 1,  ... len(data).  Instead of
\# formatting the tick marks as integers, we format as times.
def format\_date(x, \_):
    try:
        \# convert datetime64 to datetime, and use datetime's strftime:
        return [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\["date"\]\[round(x)\].item().strftime('%a')
    except IndexError:
        pass

\# Create an index plot (x defaults to range(len(y)) if omitted)
[ax2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\["adj\_close"\], 'o-')

[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Plot y at Index Coordinates Using Custom Formatter")
[ax2.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
(format\_date)  \# internally creates FuncFormatter

![Plot y at x Coordinates, Plot y at Index Coordinates Using Custom Formatter](https://matplotlib.org/stable/_images/sphx_glr_date_index_formatter_001_2_00x.png)

Instead of passing a function into [`Axis.set_major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
 you can use any other callable, e.g. an instance of a class that implements \_\_call\_\_:

class MyFormatter([Formatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
):
    def \_\_init\_\_(self, dates, fmt\='%a'):
        self.dates \= dates
        self.fmt \= fmt

    def \_\_call\_\_(self, x, pos\=0):
        """Return the label for time x at position pos."""
        try:
            return self.dates\[round(x)\].item().strftime(self.fmt)
        except IndexError:
            pass

[ax2.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
([MyFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
([r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\["date"\], '%a'))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 1.238 seconds)

[`Download Jupyter notebook: date_index_formatter.ipynb`](https://matplotlib.org/stable/_downloads/43f846a2e7762cf70a957ab3d40b7678/date_index_formatter.ipynb)

[`Download Python source code: date_index_formatter.py`](https://matplotlib.org/stable/_downloads/8bed961b9fa5a0bf5184a42332b13e0a/date_index_formatter.py)

[`Download zipped: date_index_formatter.zip`](https://matplotlib.org/stable/_downloads/ce9e70101ecfbed70f0713703f583bf8/date_index_formatter.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)