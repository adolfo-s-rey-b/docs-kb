[Skip to main content](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_title.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_title.html#sphx-glr-download-gallery-subplots-axes-and-figures-figure-title-py)
 to download the full example code.

Figure labels: suptitle, supxlabel, supylabel[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_title.html#figure-labels-suptitle-supxlabel-supylabel "Link to this heading")

======================================================================================================================================================================================================

Each Axes can have a title (or actually three - one each with _loc_ "left", "center", and "right"), but is sometimes desirable to give a whole figure (or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
) an overall title, using [`Figure.suptitle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
.

We can also add figure-level x- and y-labels using [`Figure.supxlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.supxlabel.html#matplotlib.figure.Figure.supxlabel "matplotlib.figure.Figure.supxlabel")
 and [`Figure.supylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.supylabel.html#matplotlib.figure.Figure.supylabel "matplotlib.figure.Figure.supylabel")
.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.cbook import [get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.0, 5.0, 501)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, layout\='constrained', sharey\=True)
[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(6\*[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('damped')
[ax1.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('time (s)')
[ax1.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('amplitude')

[ax2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(6\*[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
[ax2.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('time (s)')
[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('undamped')

[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Different types of oscillations', fontsize\=16)

![Different types of oscillations, damped, undamped](https://matplotlib.org/stable/_images/sphx_glr_figure_title_001_2_00x.png)

A global x- or y-label can be set using the [`Figure.supxlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.supxlabel.html#matplotlib.figure.Figure.supxlabel "matplotlib.figure.Figure.supxlabel")
 and [`Figure.supylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.supylabel.html#matplotlib.figure.Figure.supylabel "matplotlib.figure.Figure.supylabel")
 methods.

with [get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
('Stocks.csv') as file:
    [stocks](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.genfromtxt](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt")
(
        file, delimiter\=',', names\=True, dtype\=None,
        converters\={0: lambda [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
: [np.datetime64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'D')}, skip\_header\=1)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(4, 2, figsize\=(9, 5), layout\='constrained',
                        sharex\=True, sharey\=True)
for [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in enumerate([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
):
    [column\_name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= [stocks.dtype.names](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[1+[nn](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]
    [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [stocks](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[column\_name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\]
    [line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([stocks](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['Date'\], [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 / [np.nanmax](https://numpy.org/doc/stable/reference/generated/numpy.nanmax.html#numpy.nanmax "numpy.nanmax")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), lw\=2.5)
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
([column\_name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, fontsize\='small', loc\='left')
[fig.supxlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.supxlabel.html#matplotlib.figure.Figure.supxlabel "matplotlib.figure.Figure.supxlabel")
('Year')
[fig.supylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.supylabel.html#matplotlib.figure.Figure.supylabel "matplotlib.figure.Figure.supylabel")
('Stock price relative to max')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![IBM, AAPL, MSFT, XRX, AMZN, DELL, GOOGL, ADBE](https://matplotlib.org/stable/_images/sphx_glr_figure_title_002_2_00x.png)

Tags: [component: figure](https://matplotlib.org/stable/_tags/component-figure.html)
 [component: title](https://matplotlib.org/stable/_tags/component-title.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

**Total running time of the script:** (0 minutes 3.927 seconds)

[`Download Jupyter notebook: figure_title.ipynb`](https://matplotlib.org/stable/_downloads/e8f5fb547c55505e758bccbd0583f193/figure_title.ipynb)

[`Download Python source code: figure_title.py`](https://matplotlib.org/stable/_downloads/cbc6cc42af06a4be6b3d6f8c5e33ead1/figure_title.py)

[`Download zipped: figure_title.zip`](https://matplotlib.org/stable/_downloads/24507fc6105fb780dd67ae201816436f/figure_title.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)