[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/timeline.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/timeline.html#sphx-glr-download-gallery-lines-bars-and-markers-timeline-py)
 to download the full example code.

Timeline with lines, dates, and text[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/timeline.html#timeline-with-lines-dates-and-text "Link to this heading")

==============================================================================================================================================================================

How to create a simple timeline using Matplotlib release dates.

Timelines can be created with a collection of dates and text. In this example, we show how to create a simple timeline using the dates for recent releases of Matplotlib. First, we'll pull the data from GitHub.

from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.dates as mdates

try:
    \# Try to fetch a list of Matplotlib releases and their dates
    \# from https://api.github.com/repos/matplotlib/matplotlib/releases
    import json
    import urllib.request

    [url](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= 'https://api.github.com/repos/matplotlib/matplotlib/releases'
    [url](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 += '?per\_page=100'
    [data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [json.loads](https://docs.python.org/3/library/json.html#json.loads "json.loads")
([urllib.request.urlopen](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen")
([url](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, timeout\=1).read().decode())

    [dates](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= \[\]
    [releases](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= \[\]
    for [item](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 in [data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
:
        if 'rc' not in [item](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['tag\_name'\] and 'b' not in [item](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['tag\_name'\]:
            [dates.append](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
([item](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['published\_at'\].split("T")\[0\])
            [releases.append](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
([item](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['tag\_name'\].lstrip("v"))

except Exception:
    \# In case the above fails, e.g. because of missing internet connection
    \# use the following lists as fallback.
    [releases](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= \['2.2.4', '3.0.3', '3.0.2', '3.0.1', '3.0.0', '2.2.3',\
                '2.2.2', '2.2.1', '2.2.0', '2.1.2', '2.1.1', '2.1.0',\
                '2.0.2', '2.0.1', '2.0.0', '1.5.3', '1.5.2', '1.5.1',\
                '1.5.0', '1.4.3', '1.4.2', '1.4.1', '1.4.0'\]
    [dates](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= \['2019-02-26', '2019-02-26', '2018-11-10', '2018-11-10',\
             '2018-09-18', '2018-08-10', '2018-03-17', '2018-03-16',\
             '2018-03-06', '2018-01-18', '2017-12-10', '2017-10-07',\
             '2017-05-10', '2017-05-02', '2017-01-17', '2016-09-09',\
             '2016-07-03', '2016-01-10', '2015-10-29', '2015-02-16',\
             '2014-10-26', '2014-10-18', '2014-08-26'\]

[dates](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= \[[datetime.strptime](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime")\
(d, "%Y-%m-%d") for d in [dates](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\]  \# Convert strs to dates.
[releases](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= \[tuple([release.split](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
('.')) for [release](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
 in [releases](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\]  \# Split by component.
[dates](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [releases](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= zip(\*sorted(zip([dates](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [releases](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)))  \# Sort by increasing date.

Next, we'll create a stem plot with some variation in levels as to distinguish even close-by events. We add markers on the baseline for visual emphasis on the one-dimensional nature of the timeline.

For each event, we add a text label via [`annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
, which is offset in units of points from the tip of the event line.

Note that Matplotlib will automatically plot datetime inputs.

\# Choose some nice levels: alternate meso releases between top and bottom, and
\# progressively shorten the stems for micro releases.
[levels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
[macro\_meso\_releases](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= sorted({[release](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[:2\] for [release](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 in [releases](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
})
for [release](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 in [releases](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
:
    [macro\_meso](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= [release](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[:2\]
    [micro](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= int([release](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[2\])
    [h](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 1 + 0.8 \* (5 \- [micro](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [level](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [h](https://docs.python.org/3/library/functions.html#float "builtins.float")
 if [macro\_meso\_releases](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.index([macro\_meso](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
) % 2 \== 0 else \-[h](https://docs.python.org/3/library/functions.html#float "builtins.float")
    [levels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append([level](https://docs.python.org/3/library/functions.html#float "builtins.float")
)

def is\_feature([release](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
):
    """Return whether a version (split into components) is a feature release."""
    return [release](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[\-1\] \== '0'

\# The figure and the axes.
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(8.8, 4), layout\="constrained")
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(title\="Matplotlib release dates")

\# The vertical stems.
[ax.vlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.vlines.html#matplotlib.axes.Axes.vlines "matplotlib.axes.Axes.vlines")
([dates](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, 0, [levels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
,
          color\=\[("tab:red", 1 if is\_feature([release](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
) else .5) for [release](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
 in [releases](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\])
\# The baseline.
[ax.axhline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline")
(0, c\="black")
\# The markers on the baseline.
[meso\_dates](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[date](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")\
 for [date](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")\
, [release](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
 in zip([dates](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
, [releases](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
) if is\_feature([release](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
)\]
[micro\_dates](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[date](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")\
 for [date](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")\
, [release](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
 in zip([dates](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
, [releases](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
)\
               if not is\_feature([release](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
)\]
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([micro\_dates](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [np.zeros\_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
([micro\_dates](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
), "ko", mfc\="white")
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([meso\_dates](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [np.zeros\_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
([meso\_dates](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
), "ko", mfc\="tab:red")

\# Annotate the lines.
for [date](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
, [level](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [release](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 in zip([dates](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [levels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [releases](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
):
    [version\_str](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= '.'.join([release](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)
    [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
([version\_str](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, xy\=([date](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
, [level](https://docs.python.org/3/library/functions.html#float "builtins.float")
),
                xytext\=(\-3, [np.sign](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([level](https://docs.python.org/3/library/functions.html#float "builtins.float")
)\*3), textcoords\="offset points",
                verticalalignment\="bottom" if [level](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \> 0 else "top",
                weight\="bold" if is\_feature([release](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
) else "normal",
                bbox\=dict(boxstyle\='square', pad\=0, lw\=0, fc\=(1, 1, 1, 0.7)))

[ax.xaxis.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "matplotlib.artist.Artist.set")
(major\_locator\=[mdates.YearLocator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.YearLocator "matplotlib.dates.YearLocator")
(),
             major\_formatter\=[mdates.DateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
("%Y"))

\# Remove the y-axis and some spines.
[ax.yaxis.set\_visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible")
(False)
[ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[\["left", "top", "right"\]\].set\_visible(False)

[ax.margins](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")
(y\=0.1)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Matplotlib release dates](https://matplotlib.org/stable/_images/sphx_glr_timeline_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
    
*   [`matplotlib.axes.Axes.vlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.vlines.html#matplotlib.axes.Axes.vlines "matplotlib.axes.Axes.vlines")
    
*   [`matplotlib.axis.Axis.set_major_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
    
*   [`matplotlib.axis.Axis.set_major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
    
*   [`matplotlib.dates.MonthLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MonthLocator "matplotlib.dates.MonthLocator")
    
*   [`matplotlib.dates.DateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
    

Tags: [component: annotation](https://matplotlib.org/stable/_tags/component-annotation.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

**Total running time of the script:** (0 minutes 2.806 seconds)

[`Download Jupyter notebook: timeline.ipynb`](https://matplotlib.org/stable/_downloads/8323aa2f43944c2eb345c63483dc9f7f/timeline.ipynb)

[`Download Python source code: timeline.py`](https://matplotlib.org/stable/_downloads/e4e3bbd0b1c82e93b916e64bd632f7a9/timeline.py)

[`Download zipped: timeline.zip`](https://matplotlib.org/stable/_downloads/8f65f61e1ebd23065e631d34762f8fb2/timeline.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)