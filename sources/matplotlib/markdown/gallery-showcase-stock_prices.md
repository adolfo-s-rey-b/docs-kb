[Skip to main content](https://matplotlib.org/stable/gallery/showcase/stock_prices.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/showcase/stock_prices.html#sphx-glr-download-gallery-showcase-stock-prices-py)
 to download the full example code.

Stock prices over 32 years[#](https://matplotlib.org/stable/gallery/showcase/stock_prices.html#stock-prices-over-32-years "Link to this heading")

==================================================================================================================================================

A graph of multiple time series that demonstrates custom styling of plot frame, tick lines, tick labels, and line graph properties. It also uses custom placement of text labels along the right edge as an alternative to a conventional legend.

Note: The third-party mpl style [dufte](https://github.com/nschloe/dufte)
 produces similar-looking plots with less code.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.cbook import [get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
import matplotlib.transforms as mtransforms

with [get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
('Stocks.csv') as file:
    [stock\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.genfromtxt](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt")
(
        file, delimiter\=',', names\=True, dtype\=None,
        converters\={0: lambda x: [np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
(x, 'D')}, skip\_header\=1)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 1, figsize\=(6, 8), layout\='constrained')

\# These are the colors that will be used in the plot
[ax.set\_prop\_cycle](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle")
(color\=\[\
    '#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a',\
    '#d62728', '#ff9896', '#9467bd', '#c5b0d5', '#8c564b', '#c49c94',\
    '#e377c2', '#f7b6d2', '#7f7f7f', '#c7c7c7', '#bcbd22', '#dbdb8d',\
    '#17becf', '#9edae5'\])

[stocks\_name](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['IBM', 'Apple', 'Microsoft', 'Xerox', 'Amazon', 'Dell',\
               'Alphabet', 'Adobe', 'S&P 500', 'NASDAQ'\]
[stocks\_ticker](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['IBM', 'AAPL', 'MSFT', 'XRX', 'AMZN', 'DELL', 'GOOGL',\
                 'ADBE', 'GSPC', 'IXIC'\]

\# Manually adjust the label positions vertically (units are points = 1/72 inch)
[y\_offsets](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict.fromkeys([stocks\_ticker](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, 0)
[y\_offsets](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['IBM'\] \= 5
[y\_offsets](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['AAPL'\] \= \-5
[y\_offsets](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['AMZN'\] \= \-6

for [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [column](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate([stocks\_ticker](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    \# Plot each line separately with its own color.
    \# don't include any data with NaN.
    [good](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= [np.nonzero](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")
([np.isfinite](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([stock\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[column](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\]))
    [line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([stock\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['Date'\]\[[good](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\], [stock\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[column](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\]\[[good](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\], lw\=2.5)

    \# Add a text label to the right end of every line. Most of the code below
    \# is adding specific offsets y position because some labels overlapped.
    [y\_pos](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [stock\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[column](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\]\[\-1\]

    \# Use an offset transform, in points, for any text that needs to be nudged
    \# up or down.
    [offset](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [y\_offsets](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[column](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\] / 72
    [trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 \= [mtransforms.ScaledTranslation](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation "matplotlib.transforms.ScaledTranslation")
(0, [offset](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [fig.dpi\_scale\_trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
)
    [trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 \= [ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 + [trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")

    \# Again, make sure that all labels are large enough to be easily read
    \# by the viewer.
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
('2022-10-01'), [y\_pos](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [stocks\_name](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[nn](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\],
            color\=[line.get\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_color "matplotlib.lines.Line2D.get_color")
(), transform\=[trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
)

[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
([np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
('1989-06-01'), [np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
('2023-01-01'))

[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
("Technology company stocks prices dollars (1990-2022)",
             ha\="center")

\# Remove the plot frame lines. They are unnecessary here.
[ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[:\].set\_visible(False)

\# Ensure that the axis ticks only show up on the bottom and left of the plot.
\# Ticks on the right and top of the plot are generally unnecessary.
[ax.xaxis.tick\_bottom](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.tick_bottom.html#matplotlib.axis.XAxis.tick_bottom "matplotlib.axis.XAxis.tick_bottom")
()
[ax.yaxis.tick\_left](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.YAxis.tick_left.html#matplotlib.axis.YAxis.tick_left "matplotlib.axis.YAxis.tick_left")
()
[ax.set\_yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale")
('log')

\# Provide tick lines across the plot to help your viewers trace along
\# the axis ticks. Make sure that the lines are light and small so they
\# don't obscure the primary data lines.
[ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
(True, 'major', 'both', ls\='--', lw\=.5, c\='k', alpha\=.3)

\# Remove the tick marks; they are unnecessary with the tick lines we just
\# plotted. Make sure your axis ticks are large enough to be easily read.
\# You don't want your viewers squinting to read your plot.
[ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(axis\='both', which\='both', labelsize\='large',
               bottom\=False, top\=False, labelbottom\=True,
               left\=False, right\=False, labelleft\=True)

\# Finally, save the figure as a PNG.
\# You can also save it as a PDF, JPEG, etc.
\# Just change the file extension in this call.
\# fig.savefig('stock-prices.png', bbox\_inches='tight')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Technology company stocks prices dollars (1990-2022)](https://matplotlib.org/stable/_images/sphx_glr_stock_prices_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
    
*   [`matplotlib.axes.Axes.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
    
*   [`matplotlib.axis.XAxis.tick_bottom`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.tick_bottom.html#matplotlib.axis.XAxis.tick_bottom "matplotlib.axis.XAxis.tick_bottom")
    
*   [`matplotlib.axis.YAxis.tick_left`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.YAxis.tick_left.html#matplotlib.axis.YAxis.tick_left "matplotlib.axis.YAxis.tick_left")
    
*   [`matplotlib.artist.Artist.set_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible")
    

**Total running time of the script:** (0 minutes 2.143 seconds)

[`Download Jupyter notebook: stock_prices.ipynb`](https://matplotlib.org/stable/_downloads/f26ac8c8ae5b253bf8f75e0c4dde8be2/stock_prices.ipynb)

[`Download Python source code: stock_prices.py`](https://matplotlib.org/stable/_downloads/f45b7da3bfe46d4737fa57ae1cf81167/stock_prices.py)

[`Download zipped: stock_prices.zip`](https://matplotlib.org/stable/_downloads/1d621d068171caa723900f7292f62fcd/stock_prices.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)