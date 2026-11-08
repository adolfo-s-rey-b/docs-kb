[Skip to main content](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#sphx-glr-download-users-explain-axes-axes-ticks-py)
 to download the full example code.

Axis ticks[#](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#axis-ticks "Link to this heading")

==================================================================================================================

The x and y Axis on each Axes have default tick "locators" and "formatters" that depend on the scale being used (see [Axis scales](https://matplotlib.org/stable/users/explain/axes/axes_scales.html#user-axes-scales)
). It is possible to customize the ticks and tick labels with either high-level methods like [`set_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
 or set the locators and formatters directly on the axis.

Manual location and formats[#](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#manual-location-and-formats "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

The simplest method to customize the tick locations and formats is to use [`set_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
 and [`set_yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
. These can be used on either the major or the minor ticks.

import numpy as np
import matplotlib.pyplot as plt

import matplotlib.ticker as ticker

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 1, figsize\=(5.4, 5.4), layout\='constrained')
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(100)
for [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in enumerate([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    if [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \== 1:
        [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Manual ticks')
        [ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 100.1, 100/3))
        [xticks](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.50, 101, 20)
        [xlabels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[f'\\\\${[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
:1.2f}' for [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
 in [xticks](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\]
        [ax.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
([xticks](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=[xlabels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
    else:
        [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Automatic ticks')

![Automatic ticks, Manual ticks](https://matplotlib.org/stable/_images/sphx_glr_axes_ticks_001_2_00x.png)

Note that the length of the `labels` argument must have the same length as the array used to specify the ticks.

By default [`set_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
 and [`set_yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
 act on the major ticks of an Axis, however it is possible to add minor ticks:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 1, figsize\=(5.4, 5.4), layout\='constrained')
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(100)
for [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in enumerate([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    if [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \== 1:
        [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Manual ticks')
        [ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 100.1, 100/3))
        [ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 100.1, 100/30), minor\=True)
    else:
        [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Automatic ticks')

![Automatic ticks, Manual ticks](https://matplotlib.org/stable/_images/sphx_glr_axes_ticks_002_2_00x.png)

Locators and Formatters[#](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#locators-and-formatters "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

Manually setting the ticks as above works well for specific final plots, but does not adapt as the user interacts with the Axes. At a lower level, Matplotlib has `Locators` that are meant to automatically choose ticks depending on the current view limits of the axis, and `Formatters` that are meant to format the tick labels automatically.

The full list of locators provided by Matplotlib are listed at [Tick locating](https://matplotlib.org/stable/api/ticker_api.html#locators)
, and the formatters at [Tick formatting](https://matplotlib.org/stable/api/ticker_api.html#formatters)
.

def setup([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, title):
    """Set up common parameters for the Axes in the example."""
    \# only show the bottom spine
    [ax.yaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([ticker.NullLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator "matplotlib.ticker.NullLocator")
())
    [ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[\['left', 'right', 'top'\]\].set\_visible(False)

    [ax.xaxis.set\_ticks\_position](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.set_ticks_position.html#matplotlib.axis.XAxis.set_ticks_position "matplotlib.axis.XAxis.set_ticks_position")
('bottom')
    [ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(which\='major', width\=1.00, length\=5)
    [ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(which\='minor', width\=0.75, length\=2.5)
    [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0, 5)
    [ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(0, 1)
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.0, 0.2, title, transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
,
            fontsize\=14, fontname\='Monospace', color\='tab:blue')

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(8, 1, layout\='constrained')

\# Null Locator
setup([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\], title\="NullLocator()")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].xaxis.set\_major\_locator([ticker.NullLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator "matplotlib.ticker.NullLocator")
())
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].xaxis.set\_minor\_locator([ticker.NullLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator "matplotlib.ticker.NullLocator")
())

\# Multiple Locator
setup([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\], title\="MultipleLocator(0.5)")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].xaxis.set\_major\_locator([ticker.MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(0.5))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].xaxis.set\_minor\_locator([ticker.MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(0.1))

\# Fixed Locator
setup([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\], title\="FixedLocator(\[0, 1, 5\])")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].xaxis.set\_major\_locator([ticker.FixedLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
(\[0, 1, 5\]))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].xaxis.set\_minor\_locator([ticker.FixedLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.2, 0.8, 4)))

\# Linear Locator
setup([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3\], title\="LinearLocator(numticks=3)")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3\].xaxis.set\_major\_locator([ticker.LinearLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LinearLocator "matplotlib.ticker.LinearLocator")
(3))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3\].xaxis.set\_minor\_locator([ticker.LinearLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LinearLocator "matplotlib.ticker.LinearLocator")
(31))

\# Index Locator
setup([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[4\], title\="IndexLocator(base=0.5, offset=0.25)")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[4\].plot(range(0, 5), \[0\]\*5, color\='white')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[4\].xaxis.set\_major\_locator([ticker.IndexLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.IndexLocator "matplotlib.ticker.IndexLocator")
(base\=0.5, offset\=0.25))

\# Auto Locator
setup([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[5\], title\="AutoLocator()")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[5\].xaxis.set\_major\_locator([ticker.AutoLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoLocator "matplotlib.ticker.AutoLocator")
())
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[5\].xaxis.set\_minor\_locator([ticker.AutoMinorLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoMinorLocator "matplotlib.ticker.AutoMinorLocator")
())

\# MaxN Locator
setup([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[6\], title\="MaxNLocator(n=4)")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[6\].xaxis.set\_major\_locator([ticker.MaxNLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
(4))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[6\].xaxis.set\_minor\_locator([ticker.MaxNLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
(40))

\# Log Locator
setup([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[7\], title\="LogLocator(base=10, numticks=15)")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[7\].set\_xlim(10\*\*3, 10\*\*10)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[7\].set\_xscale('log')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[7\].xaxis.set\_major\_locator([ticker.LogLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator")
(base\=10, numticks\=15))
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![axes ticks](https://matplotlib.org/stable/_images/sphx_glr_axes_ticks_003_2_00x.png)

Similarly, we can specify "Formatters" for the major and minor ticks on each axis.

The tick format is configured via the function [`set_major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
 or [`set_minor_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_formatter.html#matplotlib.axis.Axis.set_minor_formatter "matplotlib.axis.Axis.set_minor_formatter")
. It accepts:

*   a format string, which implicitly creates a [`StrMethodFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "matplotlib.ticker.StrMethodFormatter")
    .
    
*   a function, implicitly creates a [`FuncFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
    .
    
*   an instance of a [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
     subclass. The most common are
    
    *   [`NullFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
        : No labels on the ticks.
        
    *   [`StrMethodFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "matplotlib.ticker.StrMethodFormatter")
        : Use string [`str.format`](https://docs.python.org/3/library/stdtypes.html#str.format "(in Python v3.14)")
         method.
        
    *   [`FormatStrFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FormatStrFormatter "matplotlib.ticker.FormatStrFormatter")
        : Use %-style formatting.
        
    *   [`FuncFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
        : Define labels through a function.
        
    *   [`FixedFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedFormatter "matplotlib.ticker.FixedFormatter")
        : Set the label strings explicitly.
        
    *   [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
        : Default formatter for scalars: auto-pick the format string.
        
    *   [`PercentFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.PercentFormatter "matplotlib.ticker.PercentFormatter")
        : Format labels as a percentage.
        

See [Tick formatting](https://matplotlib.org/stable/api/ticker_api.html#formatters)
 for the complete list.

def setup([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, title):
    """Set up common parameters for the Axes in the example."""
    \# only show the bottom spine
    [ax.yaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([ticker.NullLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator "matplotlib.ticker.NullLocator")
())
    [ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[\['left', 'right', 'top'\]\].set\_visible(False)

    \# define tick positions
    [ax.xaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([ticker.MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(1.00))
    [ax.xaxis.set\_minor\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html#matplotlib.axis.Axis.set_minor_locator "matplotlib.axis.Axis.set_minor_locator")
([ticker.MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(0.25))

    [ax.xaxis.set\_ticks\_position](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.set_ticks_position.html#matplotlib.axis.XAxis.set_ticks_position "matplotlib.axis.XAxis.set_ticks_position")
('bottom')
    [ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(which\='major', width\=1.00, length\=5)
    [ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(which\='minor', width\=0.75, length\=2.5, labelsize\=10)
    [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0, 5)
    [ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(0, 1)
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.0, 0.2, title, transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
,
            fontsize\=14, fontname\='Monospace', color\='tab:blue')

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 8), layout\='constrained')
[fig0](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
, [fig1](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
, [fig2](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
 \= [fig.subfigures](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
(3, height\_ratios\=\[1.5, 1.5, 7.5\])

[fig0.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.suptitle.html#matplotlib.figure.SubFigure.suptitle "matplotlib.figure.SubFigure.suptitle")
('String Formatting', fontsize\=16, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=0, ha\='left')
[ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig0.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subplots.html#matplotlib.figure.SubFigure.subplots "matplotlib.figure.SubFigure.subplots")
()

setup([ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, title\="'{x} km'")
[ax0.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
('{x} km')

[fig1.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.suptitle.html#matplotlib.figure.SubFigure.suptitle "matplotlib.figure.SubFigure.suptitle")
('Function Formatting', fontsize\=16, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=0, ha\='left')
[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig1.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subplots.html#matplotlib.figure.SubFigure.subplots "matplotlib.figure.SubFigure.subplots")
()

setup([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, title\="def(x, pos): return str(x-5)")
[ax1.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
(lambda [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, pos: str([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\-5))

[fig2.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.suptitle.html#matplotlib.figure.SubFigure.suptitle "matplotlib.figure.SubFigure.suptitle")
('Formatter Object Formatting', fontsize\=16, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=0, ha\='left')
[axs2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [fig2.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subplots.html#matplotlib.figure.SubFigure.subplots "matplotlib.figure.SubFigure.subplots")
(7, 1)

setup([axs2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\], title\="NullFormatter()")
[axs2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].xaxis.set\_major\_formatter([ticker.NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())

setup([axs2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\], title\="StrMethodFormatter('{x:.3f}')")
[axs2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].xaxis.set\_major\_formatter([ticker.StrMethodFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "matplotlib.ticker.StrMethodFormatter")
("{x:.3f}"))

setup([axs2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\], title\="FormatStrFormatter('#%d')")
[axs2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].xaxis.set\_major\_formatter([ticker.FormatStrFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FormatStrFormatter "matplotlib.ticker.FormatStrFormatter")
("#%d"))

def fmt\_two\_digits([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, pos):
    return f'\[{[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
:.2f}\]'

setup([axs2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3\], title\='FuncFormatter("\[{:.2f}\]".format)')
[axs2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3\].xaxis.set\_major\_formatter([ticker.FuncFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
(fmt\_two\_digits))

setup([axs2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[4\], title\="FixedFormatter(\['A', 'B', 'C', 'D', 'E', 'F'\])")
\# FixedFormatter should only be used together with FixedLocator.
\# Otherwise, one cannot be sure where the labels will end up.
[positions](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[0, 1, 2, 3, 4, 5\]
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['A', 'B', 'C', 'D', 'E', 'F'\]
[axs2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[4\].xaxis.set\_major\_locator([ticker.FixedLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
([positions](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
))
[axs2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[4\].xaxis.set\_major\_formatter([ticker.FixedFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedFormatter "matplotlib.ticker.FixedFormatter")
([labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
))

setup([axs2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[5\], title\="ScalarFormatter()")
[axs2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[5\].xaxis.set\_major\_formatter([ticker.ScalarFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
(useMathText\=True))

setup([axs2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[6\], title\="PercentFormatter(xmax=5)")
[axs2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[6\].xaxis.set\_major\_formatter([ticker.PercentFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.PercentFormatter "matplotlib.ticker.PercentFormatter")
(xmax\=5))

![axes ticks](https://matplotlib.org/stable/_images/sphx_glr_axes_ticks_004_2_00x.png)

Styling ticks (tick parameters)[#](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#styling-ticks-tick-parameters "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

The appearance of ticks can be controlled at a low level by finding the individual [`Tick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Tick "matplotlib.axis.Tick")
 on the axis. However, usually it is simplest to use [`tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
 to change all the objects at once.

The `tick_params` method can change the properties of ticks:

*   length
    
*   direction (in or out of the frame)
    
*   colors
    
*   width and length
    
*   and whether the ticks are drawn at the bottom, top, left, or right of the Axes.
    

It also can control the tick labels:

*   labelsize (fontsize)
    
*   labelcolor (color of the label)
    
*   labelrotation
    
*   labelbottom, labeltop, labelleft, labelright
    

In addition there is a _pad_ keyword argument that specifies how far the tick label is from the tick.

Finally, the grid linestyles can be set:

*   grid\_color
    
*   grid\_alpha
    
*   grid\_linewidth
    
*   grid\_linestyle
    

All these properties can be restricted to one axis, and can be applied to just the major or minor ticks

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(6.4, 3.2), layout\='constrained')

for [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in enumerate([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(100))
    if [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \== 1:
        [ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
('on')
        [ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(right\=True, left\=False, axis\='y', color\='r', length\=16,
                       grid\_color\='none')
        [ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(axis\='x', color\='m', length\=4, direction\='in', width\=4,
                       labelcolor\='g', grid\_color\='b')

![axes ticks](https://matplotlib.org/stable/_images/sphx_glr_axes_ticks_005_2_00x.png)

Tick objects[#](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#tick-objects "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

Warning

Ticks are managed through the autoscaling / view limit mechanism, which may create, move and delete ticks as necessary.

Working with tick instances should only be an option of last resort and requires careful handling to not accidentally overwrite any manual changes through this mechanism.

If a tick configuration can be achieved through [`Axes.tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
 (see [Styling ticks (tick parameters)](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#axes-ticks-styling)
), that approach should be preferred.

On the technical level, ticks are realized through [`Tick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Tick "matplotlib.axis.Tick")
 objects. They consist of

*   `tick1line` / `tick2line` for the tick lines on either side of the axis.
    
*   `label1` / `label2` for the tick labels on either side of the axis.
    
*   `gridline` for the grid line.
    

These objects are publicly accessible through [Axes methods](https://matplotlib.org/stable/api/axes_api.html#axes-api-ticks)
 and [Axis methods](https://matplotlib.org/stable/api/axis_api.html#axis-api-ticks)
 and allow extreme customization such as coloring a specific tick line or tick label separately.

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 1.1 \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-3 \* [np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
(500))
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
(500)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'o')
[ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
()
[ticks](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [ax.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
(\[0, 0.2, 0.4, 0.6, 0.8, 1, 1.2\])
[ticks](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[5\].label1.set\_color("red")
[ticks](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[5\].tick1line.set\_markeredgecolor("red")
[ticks](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[5\].gridline.set(visible\=True, linestyle\=':', linewidth\=1.5, color\='red')

![axes ticks](https://matplotlib.org/stable/_images/sphx_glr_axes_ticks_006_2_00x.png)

Because of the managed nature of ticks, such operations only make sense for static output (e.g., when using the jupyter inline backend or saving the figure to a file) or when you are sure that the view limits of the axis will not change (e.g., when using a fixed locator).

In contrast, [`Axes.tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
 configures the default properties so that they are applied to all current and future ticks.

**Total running time of the script:** (0 minutes 7.406 seconds)

[`Download Jupyter notebook: axes_ticks.ipynb`](https://matplotlib.org/stable/_downloads/5eb4aaff231bef8113c11e23f16047b1/axes_ticks.ipynb)

[`Download Python source code: axes_ticks.py`](https://matplotlib.org/stable/_downloads/3b1d962a9ffc6a29aba6432b8a452f4c/axes_ticks.py)

[`Download zipped: axes_ticks.zip`](https://matplotlib.org/stable/_downloads/11fca6d72e33f2b700e99977dae5387d/axes_ticks.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page