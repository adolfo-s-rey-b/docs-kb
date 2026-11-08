[Skip to main content](https://matplotlib.org/stable/gallery/ticks/major_minor_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/ticks/major_minor_demo.html#sphx-glr-download-gallery-ticks-major-minor-demo-py)
 to download the full example code.

Major and minor ticks[#](https://matplotlib.org/stable/gallery/ticks/major_minor_demo.html#major-and-minor-ticks "Link to this heading")

=========================================================================================================================================

Demonstrate how to use major and minor tickers.

The two relevant classes are [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
s and [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
s. Locators determine where the ticks are, and formatters control the formatting of tick labels.

Minor ticks are off by default (using [`NullLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator "matplotlib.ticker.NullLocator")
 and [`NullFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
). Minor ticks can be turned on without labels by setting the minor locator. Minor tick labels can be turned on by setting the minor formatter.

[`MultipleLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
 places ticks on multiples of some base. [`StrMethodFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "matplotlib.ticker.StrMethodFormatter")
 uses a format string (e.g., `'{x:d}'` or `'{x:1.2f}'` or `'{x:1.1f} cm'`) to format the tick labels (the variable in the format string must be `'x'`). For a [`StrMethodFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "matplotlib.ticker.StrMethodFormatter")
, the string can be passed directly to [`Axis.set_major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
 or [`Axis.set_minor_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_formatter.html#matplotlib.axis.Axis.set_minor_formatter "matplotlib.axis.Axis.set_minor_formatter")
. An appropriate [`StrMethodFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "matplotlib.ticker.StrMethodFormatter")
 will be created and used automatically.

[`pyplot.grid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")
 changes the grid settings of the major ticks of the x- and y-axis together. If you want to control the grid of the minor ticks for a given axis, use for example

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.xaxis.grid(True, which\='minor')

Note that a given locator or formatter instance can only be used on a single axis (because the locator stores references to the axis data and view limits).

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import [AutoMinorLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoMinorLocator "matplotlib.ticker.AutoMinorLocator")
, [MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")

[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 100.0, 0.1)
[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(0.1 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* 0.01)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# Make a plot with major ticks that are multiples of 20 and minor ticks that
\# are multiples of 5.  Label major ticks with '.0f' formatting but don't label
\# minor ticks.  The string is used directly, the \`StrMethodFormatter\` is
\# created automatically.
[ax.xaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(20))
[ax.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
('{x:.0f}')

\# For the minor ticks, use no labels; default NullFormatter.
[ax.xaxis.set\_minor\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html#matplotlib.axis.Axis.set_minor_locator "matplotlib.axis.Axis.set_minor_locator")
([MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(5))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![major minor demo](https://matplotlib.org/stable/_images/sphx_glr_major_minor_demo_001_2_00x.png)

Automatic tick selection for major and minor ticks.

Use interactive pan and zoom to see how the tick intervals change. There will be either 4 or 5 minor tick intervals per major interval, depending on the major interval.

One can supply an argument to [`AutoMinorLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoMinorLocator "matplotlib.ticker.AutoMinorLocator")
 to specify a fixed number of minor intervals per major interval, e.g. `AutoMinorLocator(2)` would lead to a single minor tick between major ticks.

[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 100.0, 0.01)
[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* 0.01)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[ax.xaxis.set\_minor\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html#matplotlib.axis.Axis.set_minor_locator "matplotlib.axis.Axis.set_minor_locator")
([AutoMinorLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoMinorLocator "matplotlib.ticker.AutoMinorLocator")
())

[ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(which\='both', width\=2)
[ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(which\='major', length\=7)
[ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(which\='minor', length\=4, color\='r')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![major minor demo](https://matplotlib.org/stable/_images/sphx_glr_major_minor_demo_002_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
    
*   [`matplotlib.axis.Axis.set_major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
    
*   [`matplotlib.axis.Axis.set_major_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
    
*   [`matplotlib.axis.Axis.set_minor_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html#matplotlib.axis.Axis.set_minor_locator "matplotlib.axis.Axis.set_minor_locator")
    
*   [`matplotlib.ticker.AutoMinorLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoMinorLocator "matplotlib.ticker.AutoMinorLocator")
    
*   [`matplotlib.ticker.MultipleLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
    
*   [`matplotlib.ticker.StrMethodFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "matplotlib.ticker.StrMethodFormatter")
    

**Total running time of the script:** (0 minutes 1.195 seconds)

[`Download Jupyter notebook: major_minor_demo.ipynb`](https://matplotlib.org/stable/_downloads/6eba179f4524ac54b291dcc567164966/major_minor_demo.ipynb)

[`Download Python source code: major_minor_demo.py`](https://matplotlib.org/stable/_downloads/4ad72df52615cfce120da1981d41d969/major_minor_demo.py)

[`Download zipped: major_minor_demo.zip`](https://matplotlib.org/stable/_downloads/a0d5ac71940a842cb069e8dcffc20c0c/major_minor_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)