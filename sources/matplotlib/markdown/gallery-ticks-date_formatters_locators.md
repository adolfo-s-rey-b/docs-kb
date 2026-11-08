[Skip to main content](https://matplotlib.org/stable/gallery/ticks/date_formatters_locators.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/ticks/date_formatters_locators.html#sphx-glr-download-gallery-ticks-date-formatters-locators-py)
 to download the full example code.

Date tick locators and formatters[#](https://matplotlib.org/stable/gallery/ticks/date_formatters_locators.html#date-tick-locators-and-formatters "Link to this heading")

=========================================================================================================================================================================

This example illustrates the usage and effect of the various date locators and formatters.

import matplotlib.pyplot as plt
import numpy as np

\# While these appear unused directly, they are used from eval'd strings.
from matplotlib.dates import (FR, MO, MONTHLY, SA, SU, TH, TU, WE, AutoDateFormatter,
                              AutoDateLocator, ConciseDateFormatter, [DateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
,
                              DayLocator, HourLocator, MicrosecondLocator,
                              MinuteLocator, MonthLocator, RRuleLocator, SecondLocator,
                              WeekdayLocator, YearLocator, rrulewrapper)
import matplotlib.ticker as ticker

def plot\_axis([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [locator](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=None, [xmax](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='2002-02-01', [fmt](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=None, formatter\=None):
    """Set up common parameters for the Axes in the example."""
    [ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[\['left', 'right', 'top'\]\].set\_visible(False)
    [ax.yaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([ticker.NullLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator "matplotlib.ticker.NullLocator")
())
    [ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(which\='major', width\=1.00, length\=5)
    [ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(which\='minor', width\=0.75, length\=2.5)
    [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
([np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
('2000-02-01'), [np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
([xmax](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
))
    if [locator](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
:
        [ax.xaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
(eval([locator](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
))
        [ax.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
([DateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
([fmt](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
))
    else:
        [ax.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
(eval(formatter))
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.0, 0.2, [locator](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 or formatter, transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
,
            fontsize\=14, fontname\='Monospace', color\='tab:blue')

[Date tick locators](https://matplotlib.org/stable/api/dates_api.html#date-locators)
[#](https://matplotlib.org/stable/gallery/ticks/date_formatters_locators.html#date-locators "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[locators](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
    \# locator as str, xmax, fmt\
    ('AutoDateLocator(maxticks=8)', '2003-02-01', '%Y-%m'),\
    ('YearLocator(month=4)', '2003-02-01', '%Y-%m'),\
    ('MonthLocator(bymonth=\[4, 8, 12\])', '2003-02-01', '%Y-%m'),\
    ('DayLocator(interval=180)', '2003-02-01', '%Y-%m-%d'),\
    ('WeekdayLocator(byweekday=SU, interval=4)', '2000-07-01', '%a %Y-%m-%d'),\
    ('HourLocator(byhour=range(0, 24, 6))', '2000-02-04', '%H h'),\
    ('MinuteLocator(interval=15)', '2000-02-01 02:00', '%H:%M'),\
    ('SecondLocator(bysecond=(0, 30))', '2000-02-01 00:02', '%H:%M:%S'),\
    ('MicrosecondLocator(interval=1000)', '2000-02-01 00:00:00.005', '%S.%f'),\
    ('RRuleLocator(rrulewrapper(freq=MONTHLY, \\nbyweekday=(MO, TU, WE, TH, FR), '\
     'bysetpos=-1))', '2000-07-01', '%Y-%m-%d'),\
\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(len([locators](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
), 1, figsize\=(8, len([locators](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
) \* .8),
                        layout\='constrained')
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Date Locators')
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, ([locator](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [xmax](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [fmt](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
) in zip([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [locators](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    plot\_axis([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [locator](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [xmax](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [fmt](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

![Date Locators](https://matplotlib.org/stable/_images/sphx_glr_date_formatters_locators_001_2_00x.png)

[Date formatters](https://matplotlib.org/stable/api/dates_api.html#date-formatters)
[#](https://matplotlib.org/stable/gallery/ticks/date_formatters_locators.html#date-formatters "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[formatters](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
    'AutoDateFormatter(ax.xaxis.get\_major\_locator())',\
    'ConciseDateFormatter(ax.xaxis.get\_major\_locator())',\
    'DateFormatter("%b %Y")',\
\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(len([formatters](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
), 1, figsize\=(8, len([formatters](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
) \* .8),
                        layout\='constrained')
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Date Formatters')
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [fmt](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [formatters](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    plot\_axis([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, formatter\=[fmt](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

![Date Formatters](https://matplotlib.org/stable/_images/sphx_glr_date_formatters_locators_002_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.dates.AutoDateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
    
*   [`matplotlib.dates.YearLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.YearLocator "matplotlib.dates.YearLocator")
    
*   [`matplotlib.dates.MonthLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MonthLocator "matplotlib.dates.MonthLocator")
    
*   [`matplotlib.dates.DayLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DayLocator "matplotlib.dates.DayLocator")
    
*   [`matplotlib.dates.WeekdayLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.WeekdayLocator "matplotlib.dates.WeekdayLocator")
    
*   [`matplotlib.dates.HourLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.HourLocator "matplotlib.dates.HourLocator")
    
*   [`matplotlib.dates.MinuteLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MinuteLocator "matplotlib.dates.MinuteLocator")
    
*   [`matplotlib.dates.SecondLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.SecondLocator "matplotlib.dates.SecondLocator")
    
*   [`matplotlib.dates.MicrosecondLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MicrosecondLocator "matplotlib.dates.MicrosecondLocator")
    
*   [`matplotlib.dates.RRuleLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator "matplotlib.dates.RRuleLocator")
    
*   [`matplotlib.dates.rrulewrapper`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.rrulewrapper "matplotlib.dates.rrulewrapper")
    
*   [`matplotlib.dates.DateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
    
*   [`matplotlib.dates.AutoDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateFormatter "matplotlib.dates.AutoDateFormatter")
    
*   [`matplotlib.dates.ConciseDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")
    

Tags: [component: ticks](https://matplotlib.org/stable/_tags/component-ticks.html)
 [purpose: reference](https://matplotlib.org/stable/_tags/purpose-reference.html)

**Total running time of the script:** (0 minutes 3.695 seconds)

[`Download Jupyter notebook: date_formatters_locators.ipynb`](https://matplotlib.org/stable/_downloads/12f8f756d5696d4888f93d42c5652d18/date_formatters_locators.ipynb)

[`Download Python source code: date_formatters_locators.py`](https://matplotlib.org/stable/_downloads/ab99798b19ac3141cfb6384315e229d8/date_formatters_locators.py)

[`Download zipped: date_formatters_locators.zip`](https://matplotlib.org/stable/_downloads/d8de61d5f109eb88da3831bbfebb821a/date_formatters_locators.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page