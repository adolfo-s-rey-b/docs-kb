[Skip to main content](https://matplotlib.org/stable/users/explain/axes/axes_units.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/axes/axes_units.html#sphx-glr-download-users-explain-axes-axes-units-py)
 to download the full example code.

Plotting dates and strings[#](https://matplotlib.org/stable/users/explain/axes/axes_units.html#plotting-dates-and-strings "Link to this heading")

==================================================================================================================================================

The most basic way to use Matplotlib plotting methods is to pass coordinates in as numerical numpy arrays. For example, `plot(x, y)` will work if `x` and `y` are numpy arrays of floats (or integers). Plotting methods will also work if [`numpy.asarray`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "(in NumPy v2.5)")
 will convert `x` and `y` to an array of floating point numbers; e.g. `x` could be a python list.

Matplotlib also has the ability to convert other data types if a "unit converter" exists for the data type. Matplotlib has two built-in converters, one for dates and the other for lists of strings. Other downstream libraries have their own converters to handle their data types.

The method to add converters to Matplotlib is described in [`matplotlib.units`](https://matplotlib.org/stable/api/units_api.html#module-matplotlib.units "matplotlib.units")
. Here we briefly overview the built-in date and string converters.

Date conversion[#](https://matplotlib.org/stable/users/explain/axes/axes_units.html#date-conversion "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

If `x` and/or `y` are a list of [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "(in Python v3.14)")
 or an array of [`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")
, Matplotlib has a built-in converter that will convert the datetime to a float, and add tick locators and formatters to the axis that are appropriate for dates. See [`matplotlib.dates`](https://matplotlib.org/stable/api/dates_api.html#module-matplotlib.dates "matplotlib.dates")
.

In the following example, the x-axis gains a converter that converts from [`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")
 to float, and a locator that put ticks at the beginning of the month, and a formatter that label the ticks appropriately:

import numpy as np

import matplotlib.dates as mdates
import matplotlib.units as munits

import matplotlib.pyplot as plt

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(5.4, 2), layout\='constrained')
[time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
('1980-01-01', '1980-06-25', dtype\='datetime64\[D\]')
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len([time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

![axes units](https://matplotlib.org/stable/_images/sphx_glr_axes_units_001_2_00x.png)

Note that if we try to plot a float on the x-axis, it will be plotted in units of days since the "epoch" for the converter, in this case 1970-01-01 (see [Matplotlib date format](https://matplotlib.org/stable/api/dates_api.html#date-format)
). So when we plot the value 0, the ticks start at 1970-01-01. (The locator also now chooses every two years for a tick instead of every month):

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(5.4, 2), layout\='constrained')
[time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
('1980-01-01', '1980-06-25', dtype\='datetime64\[D\]')
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len([time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
\# 0 gets labeled as 1970-01-01
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(0, 0, 'd')
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0, 0, ' Float x=0', rotation\=45)

![axes units](https://matplotlib.org/stable/_images/sphx_glr_axes_units_002_2_00x.png)

We can customize the locator and the formatter; see [Date tick locators](https://matplotlib.org/stable/api/dates_api.html#date-locators)
 and [Date formatters](https://matplotlib.org/stable/api/dates_api.html#date-formatters)
 for a complete list, and [Date tick locators and formatters](https://matplotlib.org/stable/gallery/ticks/date_formatters_locators.html#date-formatters-locators)
 for examples of them in use. Here we locate by every second month, and format just with the month's 3-letter name using `"%b"` (see [`strftime`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "(in Python v3.14)")
 for format codes):

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(5.4, 2), layout\='constrained')
[time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
('1980-01-01', '1980-06-25', dtype\='datetime64\[D\]')
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len([time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.xaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([mdates.MonthLocator](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.MonthLocator "matplotlib.dates.MonthLocator")
(bymonth\=[np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(1, 13, 2)))
[ax.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
([mdates.DateFormatter](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
('%b'))
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('1980')

![axes units](https://matplotlib.org/stable/_images/sphx_glr_axes_units_003_2_00x.png)

The default locator is the [`AutoDateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateLocator "matplotlib.dates.AutoDateLocator")
, and the default Formatter [`AutoDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateFormatter "matplotlib.dates.AutoDateFormatter")
. There are also "concise" formatter and locators that give a more compact labelling, and can be set via rcParams. Note how instead of the redundant "Jan" label at the start of the year, "1980" is used instead. See [Format date ticks using ConciseDateFormatter](https://matplotlib.org/stable/gallery/ticks/date_concise_formatter.html#date-concise-formatter)
 for more examples.

[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['date.converter'\] \= 'concise'

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(5.4, 2), layout\='constrained')
[time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
('1980-01-01', '1980-06-25', dtype\='datetime64\[D\]')
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len([time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

![axes units](https://matplotlib.org/stable/_images/sphx_glr_axes_units_004_2_00x.png)

We can set the limits on the axis either by passing the appropriate dates as limits, or by passing a floating-point value in the proper units of days since the epoch. If we need it, we can get this value from [`date2num`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.date2num "matplotlib.dates.date2num")
.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 1, figsize\=(5.4, 3), layout\='constrained')
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    [time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
('1980-01-01', '1980-06-25', dtype\='datetime64\[D\]')
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len([time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# set xlim using datetime64:
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_xlim([np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
('1980-02-01'), [np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
('1980-04-01'))

\# set xlim using floats:
\# Note can get from mdates.date2num(np.datetime64('1980-02-01'))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_xlim(3683, 3683+60)

![axes units](https://matplotlib.org/stable/_images/sphx_glr_axes_units_005_2_00x.png)

String conversion: categorical plots[#](https://matplotlib.org/stable/users/explain/axes/axes_units.html#string-conversion-categorical-plots "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes we want to label categories on an axis rather than numbers. Matplotlib allows this using a "categorical" converter (see [`category`](https://matplotlib.org/stable/api/category_api.html#module-matplotlib.category "matplotlib.category")
).

[data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
[names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= list([data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.keys())
[values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= list([data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.[values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
())

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 3, figsize\=(7, 3), sharey\=True, layout\='constrained')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].bar([names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].scatter([names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].plot([names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Categorical Plotting')

![Categorical Plotting](https://matplotlib.org/stable/_images/sphx_glr_axes_units_006_2_00x.png)

Note that the "categories" are plotted in the order that they are first specified and that subsequent plotting in a different order will not affect the original order. Further, new additions will be added on the end (see "pear" below):

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(5, 3), layout\='constrained')
[ax.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
([names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

\# plot in a different order:
[ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
(\['lemon', 'apple'\], \[7, 12\])

\# add a new category, "pear", and put the other categories in a different order:
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\['pear', 'orange', 'apple', 'lemon'\], \[13, 10, 7, 12\], color\='C1')

![axes units](https://matplotlib.org/stable/_images/sphx_glr_axes_units_007_2_00x.png)

Note that when using `plot` like in the above, the order of the plotting is mapped onto the original order of the data, so the new line goes in the order specified.

The category converter maps from categories to integers, starting at zero. So data can also be manually added to the axis using a float. Note that if a float is passed in that does not have a "category" associated with it, the data point can still be plotted, but a tick will not be created. In the following, we plot data at 4.0 and 2.5, but no tick is added there because those are not categories.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(5, 3), layout\='constrained')
[ax.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
([names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
\# arguments for styling the labels below:
[args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {'rotation': 70, 'color': 'C1',
        'bbox': {'color': 'white', 'alpha': .7, 'boxstyle': 'round'}}

\# 0 gets labeled as "apple"
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(0, 2, 'd', color\='C1')
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0, 3, 'Float x=0', \*\*[args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# 2 gets labeled as "lemon"
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(2, 2, 'd', color\='C1')
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(2, 3, 'Float x=2', \*\*[args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# 4 doesn't get a label
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(4, 2, 'd', color\='C1')
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(4, 3, 'Float x=4', \*\*[args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# 2.5 doesn't get a label
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(2.5, 2, 'd', color\='C1')
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(2.5, 3, 'Float x=2.5', \*\*[args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![axes units](https://matplotlib.org/stable/_images/sphx_glr_axes_units_008_2_00x.png)

Setting the limits for a category axis can be done by specifying the categories, or by specifying floating point numbers:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 1, figsize\=(5, 5), layout\='constrained')
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\]
[ax.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
([names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
('orange', 'lemon')
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('limits set with categories')
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\]
[ax.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
([names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0.5, 2.5)
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('limits set with floats')

![axes units](https://matplotlib.org/stable/_images/sphx_glr_axes_units_009_2_00x.png)

The category axes are helpful for some plot types, but can lead to confusion if data is read in as a list of strings, even if it is meant to be a list of floats or dates. This sometimes happens when reading comma-separated value (CSV) files. The categorical locator and formatter will put a tick at every string value and label each one as well:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(5.4, 2.5), layout\='constrained')
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \[str(xx) for xx in [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")\
(100)\]  \# list of strings
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(100))
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('x is list of strings')

![axes units](https://matplotlib.org/stable/_images/sphx_glr_axes_units_010_2_00x.png)

If this is not desired, then simply convert the data to floats before plotting:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(5.4, 2.5), layout\='constrained')
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, dtype\='float')  \# array of float.
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(100))
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('x is array of floats')

![axes units](https://matplotlib.org/stable/_images/sphx_glr_axes_units_011_2_00x.png)

Determine converter, formatter, and locator on an axis[#](https://matplotlib.org/stable/users/explain/axes/axes_units.html#determine-converter-formatter-and-locator-on-an-axis "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes it is helpful to be able to debug what Matplotlib is using to convert the incoming data. We can do that by querying the `converter` property on the axis. We can also query the formatters and locators using [`get_major_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_locator.html#matplotlib.axis.Axis.get_major_locator "matplotlib.axis.Axis.get_major_locator")
 and [`get_major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_formatter.html#matplotlib.axis.Axis.get_major_formatter "matplotlib.axis.Axis.get_major_formatter")
.

Note that by default the converter is _None_.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 1, figsize\=(6.4, 7), layout\='constrained')
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(100)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\]
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= f'Converter: {[ax.xaxis.get\_converter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_converter.html#matplotlib.axis.Axis.get_converter "matplotlib.axis.Axis.get_converter")
()}\\n '
[label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 += f'Locator: {[ax.xaxis.get\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_locator.html#matplotlib.axis.Axis.get_major_locator "matplotlib.axis.Axis.get_major_locator")
()}\\n'
[label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 += f'Formatter: {[ax.xaxis.get\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_formatter.html#matplotlib.axis.Axis.get_major_formatter "matplotlib.axis.Axis.get_major_formatter")
()}\\n'
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
([label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\]
[time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
('1980-01-01', '1980-06-25', dtype\='datetime64\[D\]')
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len([time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([time](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= f'Converter: {[ax.xaxis.get\_converter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_converter.html#matplotlib.axis.Axis.get_converter "matplotlib.axis.Axis.get_converter")
()}\\n '
[label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 += f'Locator: {[ax.xaxis.get\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_locator.html#matplotlib.axis.Axis.get_major_locator "matplotlib.axis.Axis.get_major_locator")
()}\\n'
[label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 += f'Formatter: {[ax.xaxis.get\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_formatter.html#matplotlib.axis.Axis.get_major_formatter "matplotlib.axis.Axis.get_major_formatter")
()}\\n'
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
([label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\]
[data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
[names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= list([data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.keys())
[values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= list([data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.[values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
())
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= f'Converter: {[ax.xaxis.get\_converter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_converter.html#matplotlib.axis.Axis.get_converter "matplotlib.axis.Axis.get_converter")
()}\\n '
[label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 += f'Locator: {[ax.xaxis.get\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_locator.html#matplotlib.axis.Axis.get_major_locator "matplotlib.axis.Axis.get_major_locator")
()}\\n'
[label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 += f'Formatter: {[ax.xaxis.get\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_formatter.html#matplotlib.axis.Axis.get_major_formatter "matplotlib.axis.Axis.get_major_formatter")
()}\\n'
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
([label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

![axes units](https://matplotlib.org/stable/_images/sphx_glr_axes_units_012_2_00x.png)

More about "unit" support[#](https://matplotlib.org/stable/users/explain/axes/axes_units.html#more-about-unit-support "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

The support for dates and categories is part of "units" support that is built into Matplotlib. This is described at [`matplotlib.units`](https://matplotlib.org/stable/api/units_api.html#module-matplotlib.units "matplotlib.units")
 and in the [Basic units](https://matplotlib.org/stable/gallery/units/basic_units.html#basic-units)
 example.

Unit support works by querying the type of data passed to the plotting function and dispatching to the first converter in a list that accepts that type of data. So below, if `x` has `datetime` objects in it, the converter will be `_SwitchableDateConverter`; if it has strings in it, it will be sent to the `StrCategoryConverter`.

for [k](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_")
, [v](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.StrCategoryConverter "matplotlib.category.StrCategoryConverter")
 in munits.registry.items():
    print(f"type: {[k](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_")
};\\n    converter: {type([v](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.StrCategoryConverter "matplotlib.category.StrCategoryConverter")
)}")

type: <class 'decimal.Decimal'>;
    converter: <class 'matplotlib.units.DecimalConverter'>
type: <class 'numpy.datetime64'>;
    converter: <class 'matplotlib.dates.\_SwitchableDateConverter'>
type: <class 'datetime.date'>;
    converter: <class 'matplotlib.dates.\_SwitchableDateConverter'>
type: <class 'datetime.datetime'>;
    converter: <class 'matplotlib.dates.\_SwitchableDateConverter'>
type: <class 'str'>;
    converter: <class 'matplotlib.category.StrCategoryConverter'>
type: <class 'numpy.str\_'>;
    converter: <class 'matplotlib.category.StrCategoryConverter'>
type: <class 'bytes'>;
    converter: <class 'matplotlib.category.StrCategoryConverter'>
type: <class 'numpy.bytes\_'>;
    converter: <class 'matplotlib.category.StrCategoryConverter'>

There are a number of downstream libraries that provide their own converters with locators and formatters. Physical unit support is provided by [astropy](https://www.astropy.org/)
, [pint](https://pint.readthedocs.io/)
, and [unyt](https://unyt.readthedocs.io/)
, among others.

High level libraries like [pandas](https://pandas.pydata.org/)
 and [nc-time-axis](https://nc-time-axis.readthedocs.io/)
 (and thus [xarray](https://docs.xarray.dev/)
) provide their own datetime support. This support can sometimes be incompatible with Matplotlib native datetime support, so care should be taken when using Matplotlib locators and formatters if these libraries are being used.

**Total running time of the script:** (0 minutes 7.944 seconds)

[`Download Jupyter notebook: axes_units.ipynb`](https://matplotlib.org/stable/_downloads/0058fbe25cf21cd7c40fb5bd22f92895/axes_units.ipynb)

[`Download Python source code: axes_units.py`](https://matplotlib.org/stable/_downloads/c574b5e3ff9c69fcd37a9af9609c99d1/axes_units.py)

[`Download zipped: axes_units.zip`](https://matplotlib.org/stable/_downloads/366da7a51034486094d192bf35a772b8/axes_units.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page