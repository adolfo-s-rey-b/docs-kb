[Skip to main content](https://matplotlib.org/stable/gallery/ticks/date_concise_formatter.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/ticks/date_concise_formatter.html#sphx-glr-download-gallery-ticks-date-concise-formatter-py)
 to download the full example code.

Format date ticks using ConciseDateFormatter[#](https://matplotlib.org/stable/gallery/ticks/date_concise_formatter.html#format-date-ticks-using-concisedateformatter "Link to this heading")

=============================================================================================================================================================================================

Finding good tick values and formatting the ticks for an axis that has date data is often a challenge. [`ConciseDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")
 is meant to improve the strings chosen for the ticklabels, and to minimize the strings used in those tick labels as much as possible.

Note

This formatter is a candidate to become the default date tick formatter in future versions of Matplotlib. Please report any issues or suggestions for improvement to the GitHub repository or mailing list.

import datetime

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.dates as mdates

First, the default formatter.

[base](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
 \= [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
(2005, 2, 1)
[dates](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[base](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")\
 + [datetime.timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta")\
(hours\=(2 \* i)) for i in range(732)\]
[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= len([dates](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.cumsum](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")
([np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
))

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 1, layout\='constrained', figsize\=(6, 6))
[lims](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[([np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")\
('2005-02'), [np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")\
('2005-04')),\
        ([np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")\
('2005-02-03'), [np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")\
('2005-02-15')),\
        ([np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")\
('2005-02-03 11:00'), [np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")\
('2005-02-04 13:20'))\]
for [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in enumerate([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([dates](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
([lims](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[nn](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\])
    [ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(axis\='x', rotation\=40, rotation\_mode\='xtick')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title('Default Date Formatter')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Default Date Formatter](https://matplotlib.org/stable/_images/sphx_glr_date_concise_formatter_001_2_00x.png)

The default date formatter is quite verbose, so we have the option of using [`ConciseDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")
, as shown below. Note that for this example the labels do not need to be rotated as they do for the default formatter because the labels are as small as possible.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 1, layout\='constrained', figsize\=(6, 6))
for [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in enumerate([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [locator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
 \= [mdates.AutoDateLocator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
(minticks\=3, maxticks\=7)
    [formatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")
 \= [mdates.ConciseDateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")
([locator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
)
    [ax.xaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([locator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
)
    [ax.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
([formatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")
)

    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([dates](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
([lims](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[nn](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\])
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title('Concise Date Formatter')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Concise Date Formatter](https://matplotlib.org/stable/_images/sphx_glr_date_concise_formatter_002_2_00x.png)

If all calls to axes that have dates are to be made using this converter, it is probably most convenient to use the units registry where you do imports:

import matplotlib.units as munits

[converter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateConverter "matplotlib.dates.ConciseDateConverter")
 \= [mdates.ConciseDateConverter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateConverter "matplotlib.dates.ConciseDateConverter")
()
[munits.registry](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.Registry "matplotlib.units.Registry")
\[[np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")\
\] \= [converter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateConverter "matplotlib.dates.ConciseDateConverter")
[munits.registry](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.Registry "matplotlib.units.Registry")
\[[datetime.date](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date")\
\] \= [converter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateConverter "matplotlib.dates.ConciseDateConverter")
[munits.registry](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.Registry "matplotlib.units.Registry")
\[[datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")\
\] \= [converter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateConverter "matplotlib.dates.ConciseDateConverter")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 1, figsize\=(6, 6), layout\='constrained')
for [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in enumerate([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([dates](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
([lims](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[nn](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\])
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title('Concise Date Formatter')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Concise Date Formatter](https://matplotlib.org/stable/_images/sphx_glr_date_concise_formatter_003_2_00x.png)

Localization of date formats[#](https://matplotlib.org/stable/gallery/ticks/date_concise_formatter.html#localization-of-date-formats "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

Dates formats can be localized if the default formats are not desirable by manipulating one of three lists of strings.

The `formatter.formats` list of formats is for the normal tick labels, There are six levels: years, months, days, hours, minutes, seconds. The `formatter.offset_formats` is how the "offset" string on the right of the axis is formatted. This is usually much more verbose than the tick labels. Finally, the `formatter.zero_formats` are the formats of the ticks that are "zeros". These are tick values that are either the first of the year, month, or day of month, or the zeroth hour, minute, or second. These are usually the same as the format of the ticks a level above. For example if the axis limits mean the ticks are mostly days, then we label 1 Mar 2005 simply with a "Mar". If the axis limits are mostly hours, we label Feb 4 00:00 as simply "Feb-4".

Note that these format lists can also be passed to [`ConciseDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")
 as optional keyword arguments.

Here we modify the labels to be "day month year", instead of the ISO "year month day":

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 1, layout\='constrained', figsize\=(6, 6))

for [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in enumerate([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [locator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
 \= [mdates.AutoDateLocator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
()
    [formatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")
 \= [mdates.ConciseDateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")
([locator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
)
    [formatter.formats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['%y',  \# ticks are mostly years\
                         '%b',       \# ticks are mostly months\
                         '%d',       \# ticks are mostly days\
                         '%H:%M',    \# hrs\
                         '%H:%M',    \# min\
                         '%S.%f', \]  \# secs
    \# these are mostly just the level above...
    [formatter.zero\_formats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[''\] + [formatter.formats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[:\-1\]
    \# ...except for ticks that are mostly hours, then it is nice to have
    \# month-day:
    [formatter.zero\_formats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[3\] \= '%d\-%b'

    [formatter.offset\_formats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['',\
                                '%Y',\
                                '%b %Y',\
                                '%d %b %Y',\
                                '%d %b %Y',\
                                '%d %b %Y %H:%M', \]
    [ax.xaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([locator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
)
    [ax.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
([formatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")
)

    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([dates](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
([lims](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[nn](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\])
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title('Concise Date Formatter')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Concise Date Formatter](https://matplotlib.org/stable/_images/sphx_glr_date_concise_formatter_004_2_00x.png)

Registering a converter with localization[#](https://matplotlib.org/stable/gallery/ticks/date_concise_formatter.html#registering-a-converter-with-localization "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`ConciseDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")
 doesn't have rcParams entries, but localization can be accomplished by passing keyword arguments to [`ConciseDateConverter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateConverter "matplotlib.dates.ConciseDateConverter")
 and registering the datatypes you will use with the units registry:

import datetime

[formats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['%y',          \# ticks are mostly years\
           '%b',     \# ticks are mostly months\
           '%d',     \# ticks are mostly days\
           '%H:%M',  \# hrs\
           '%H:%M',  \# min\
           '%S.%f', \]  \# secs
\# these can be the same, except offset by one level....
[zero\_formats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[''\] + [formats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[:\-1\]
\# ...except for ticks that are mostly hours, then it's nice to have month-day
[zero\_formats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[3\] \= '%d\-%b'
[offset\_formats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['',\
                  '%Y',\
                  '%b %Y',\
                  '%d %b %Y',\
                  '%d %b %Y',\
                  '%d %b %Y %H:%M', \]

[converter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateConverter "matplotlib.dates.ConciseDateConverter")
 \= [mdates.ConciseDateConverter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateConverter "matplotlib.dates.ConciseDateConverter")
(
    [formats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=[formats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [zero\_formats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=[zero\_formats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [offset\_formats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=[offset\_formats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

[munits.registry](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.Registry "matplotlib.units.Registry")
\[[np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")\
\] \= [converter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateConverter "matplotlib.dates.ConciseDateConverter")
[munits.registry](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.Registry "matplotlib.units.Registry")
\[[datetime.date](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date")\
\] \= [converter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateConverter "matplotlib.dates.ConciseDateConverter")
[munits.registry](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.Registry "matplotlib.units.Registry")
\[[datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")\
\] \= [converter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateConverter "matplotlib.dates.ConciseDateConverter")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 1, layout\='constrained', figsize\=(6, 6))
for [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in enumerate([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([dates](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
([lims](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[nn](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\])
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title('Concise Date Formatter registered non-default')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Concise Date Formatter registered non-default](https://matplotlib.org/stable/_images/sphx_glr_date_concise_formatter_005_2_00x.png)

**Total running time of the script:** (0 minutes 6.165 seconds)

[`Download Jupyter notebook: date_concise_formatter.ipynb`](https://matplotlib.org/stable/_downloads/32fcc8f0d9cbd12eb150eeaa1feaf80a/date_concise_formatter.ipynb)

[`Download Python source code: date_concise_formatter.py`](https://matplotlib.org/stable/_downloads/3786188bae617f8a5f8d7443decb1417/date_concise_formatter.py)

[`Download zipped: date_concise_formatter.zip`](https://matplotlib.org/stable/_downloads/08af4ca29a1b5787997b66f518f08aea/date_concise_formatter.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page