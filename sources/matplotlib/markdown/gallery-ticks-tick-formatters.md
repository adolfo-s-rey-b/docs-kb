[Skip to main content](https://matplotlib.org/stable/gallery/ticks/tick-formatters.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/ticks/tick-formatters.html#sphx-glr-download-gallery-ticks-tick-formatters-py)
 to download the full example code.

Tick formatters[#](https://matplotlib.org/stable/gallery/ticks/tick-formatters.html#tick-formatters "Link to this heading")

============================================================================================================================

Tick formatters define how the numeric value associated with a tick on an axis is formatted as a string.

This example illustrates the usage and effect of the most common formatters.

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
     for a complete list.
    

import matplotlib.pyplot as plt

from matplotlib import ticker

def setup(ax, title):
    """Set up common parameters for the Axes in the example."""
    \# only show the bottom spine
    ax.yaxis.set\_major\_locator([ticker.NullLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator "matplotlib.ticker.NullLocator")
())
    ax.spines\[\['left', 'right', 'top'\]\].set\_visible(False)

    \# define tick positions
    ax.xaxis.set\_major\_locator([ticker.MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(1.00))
    ax.xaxis.set\_minor\_locator([ticker.MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(0.25))

    ax.xaxis.set\_ticks\_position('bottom')
    ax.tick\_params(which\='major', width\=1.00, length\=5)
    ax.tick\_params(which\='minor', width\=0.75, length\=2.5, labelsize\=10)
    ax.set\_xlim(0, 5)
    ax.set\_ylim(0, 1)
    ax.text(0.0, 0.2, title, transform\=ax.transAxes,
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
('String Formatting', fontsize\=16, x\=0, ha\='left')
[ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig0.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subplots.html#matplotlib.figure.SubFigure.subplots "matplotlib.figure.SubFigure.subplots")
()

setup([ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, title\="'{x} km'")
[ax0.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
('{x} km')

[fig1.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.suptitle.html#matplotlib.figure.SubFigure.suptitle "matplotlib.figure.SubFigure.suptitle")
('Function Formatting', fontsize\=16, x\=0, ha\='left')
[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig1.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subplots.html#matplotlib.figure.SubFigure.subplots "matplotlib.figure.SubFigure.subplots")
()

setup([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, title\="def(x, pos): return str(x-5)")
[ax1.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
(lambda x, pos: str(x\-5))

[fig2.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.suptitle.html#matplotlib.figure.SubFigure.suptitle "matplotlib.figure.SubFigure.suptitle")
('Formatter Object Formatting', fontsize\=16, x\=0, ha\='left')
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

def fmt\_two\_digits(x, pos):
    return f'\[{x:.2f}\]'

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

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![tick formatters](https://matplotlib.org/stable/_images/sphx_glr_tick-formatters_001_2_00x.png)

Tags: [component: ticks](https://matplotlib.org/stable/_tags/component-ticks.html)
 [purpose: reference](https://matplotlib.org/stable/_tags/purpose-reference.html)

**Total running time of the script:** (0 minutes 2.312 seconds)

[`Download Jupyter notebook: tick-formatters.ipynb`](https://matplotlib.org/stable/_downloads/d9e147e69a16616252ca484597c980ea/tick-formatters.ipynb)

[`Download Python source code: tick-formatters.py`](https://matplotlib.org/stable/_downloads/982150f6f72db2a6042ea9a81adacb7e/tick-formatters.py)

[`Download zipped: tick-formatters.zip`](https://matplotlib.org/stable/_downloads/2a624166f18faca4bb9a4e6654047d5e/tick-formatters.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)