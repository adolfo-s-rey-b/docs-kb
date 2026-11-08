[Skip to main content](https://matplotlib.org/stable/gallery/showcase/anatomy.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/showcase/anatomy.html#sphx-glr-download-gallery-showcase-anatomy-py)
 to download the full example code.

Anatomy of a figure[#](https://matplotlib.org/stable/gallery/showcase/anatomy.html#anatomy-of-a-figure "Link to this heading")

===============================================================================================================================

This figure shows the name of several matplotlib elements composing a figure

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
from matplotlib.patheffects import [withStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withStroke "matplotlib.patheffects.withStroke")
from matplotlib.ticker import [AutoMinorLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoMinorLocator "matplotlib.ticker.AutoMinorLocator")
, [MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")

[royal\_blue](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[0, 20/256, 82/256\]

\# make the figure

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.5, 3.5, 100)
[Y1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 3+[np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[Y2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 1+[np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(1+[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
/0.75)/2
[Y3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
([Y1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, len([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(7.5, 7.5))
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0.2, 0.17, 0.68, 0.7), aspect\=1)

[ax.xaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(1.000))
[ax.xaxis.set\_minor\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html#matplotlib.axis.Axis.set_minor_locator "matplotlib.axis.Axis.set_minor_locator")
([AutoMinorLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoMinorLocator "matplotlib.ticker.AutoMinorLocator")
(4))
[ax.yaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(1.000))
[ax.yaxis.set\_minor\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html#matplotlib.axis.Axis.set_minor_locator "matplotlib.axis.Axis.set_minor_locator")
([AutoMinorLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoMinorLocator "matplotlib.ticker.AutoMinorLocator")
(4))
[ax.xaxis.set\_minor\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_formatter.html#matplotlib.axis.Axis.set_minor_formatter "matplotlib.axis.Axis.set_minor_formatter")
("{x:.2f}")

[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0, 4)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(0, 4)

[ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(which\='major', width\=1.0, length\=10, labelsize\=14)
[ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(which\='minor', width\=1.0, length\=5, labelsize\=10,
               labelcolor\='0.25')

[ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
(linestyle\="--", linewidth\=0.5, color\='.25', zorder\=-10)

[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, c\='C0', lw\=2.5, label\="Blue signal", zorder\=10)
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, c\='C1', lw\=2.5, label\="Orange signal")
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[::3\], [Y3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[::3\], linewidth\=0, markersize\=9,
        marker\='s', markerfacecolor\='none', markeredgecolor\='C4',
        markeredgewidth\=2.5)

[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Anatomy of a figure", fontsize\=20, verticalalignment\='bottom')
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
("x Axis label", fontsize\=14)
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
("y Axis label", fontsize\=14)
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(loc\="upper right", fontsize\=14)

\# Annotate the figure

def annotate(x, y, text, code):
    \# Circle marker
    c \= [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
((x, y), radius\=0.15, clip\_on\=False, zorder\=10, linewidth\=2.5,
               edgecolor\=[royal\_blue](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 + \[0.6\], facecolor\='none',
               path\_effects\=\[[withStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withStroke "matplotlib.patheffects.withStroke")\
(linewidth\=7, foreground\='white')\])
    [ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
(c)

    \# use path\_effects as a background for the texts
    \# draw the path\_effects and the colored text separately so that the
    \# path\_effects cannot clip other texts
    for path\_effects in \[\[[withStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withStroke "matplotlib.patheffects.withStroke")\
(linewidth\=7, foreground\='white')\], \[\]\]:
        color \= 'white' if path\_effects else [royal\_blue](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
        [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(x, y\-0.2, text, zorder\=100,
                ha\='center', va\='top', weight\='bold', color\=color,
                style\='italic', fontfamily\='monospace',
                path\_effects\=path\_effects)

        color \= 'white' if path\_effects else 'black'
        [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(x, y\-0.33, code, zorder\=100,
                ha\='center', va\='top', weight\='normal', color\=color,
                fontfamily\='monospace', fontsize\='medium',
                path\_effects\=path\_effects)

annotate(3.5, \-0.13, "Minor tick label", "ax.xaxis.set\_minor\_formatter")
annotate(\-0.03, 1.0, "Major tick", "ax.yaxis.set\_major\_locator")
annotate(0.00, 3.75, "Minor tick", "ax.yaxis.set\_minor\_locator")
annotate(\-0.15, 3.00, "Major tick label", "ax.yaxis.set\_major\_formatter")
annotate(1.68, \-0.39, "xlabel", "ax.set\_xlabel")
annotate(\-0.38, 1.67, "ylabel", "ax.set\_ylabel")
annotate(1.52, 4.15, "Title", "ax.set\_title")
annotate(1.75, 2.80, "Line", "ax.plot")
annotate(2.25, 1.54, "Markers", "ax.scatter")
annotate(3.00, 3.00, "Grid", "ax.grid")
annotate(3.60, 3.58, "Legend", "ax.legend")
annotate(2.5, 0.55, "Axes", "fig.subplots")
annotate(4, 4.5, "Figure", "plt.figure")
annotate(0.65, 0.01, "x Axis", "ax.xaxis")
annotate(0, 0.36, "y Axis", "ax.yaxis")
annotate(4.0, 0.7, "Spine", "ax.spines")

\# frame around figure
[fig.patch.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set "matplotlib.patches.Rectangle.set")
(linewidth\=4, edgecolor\='0.5')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Anatomy of a figure](https://matplotlib.org/stable/_images/sphx_glr_anatomy_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.pyplot.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
    
*   [`matplotlib.axes.Axes.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
    
*   [`matplotlib.axis.Axis.set_minor_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_formatter.html#matplotlib.axis.Axis.set_minor_formatter "matplotlib.axis.Axis.set_minor_formatter")
    
*   [`matplotlib.axis.Axis.set_major_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
    
*   [`matplotlib.axis.Axis.set_minor_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html#matplotlib.axis.Axis.set_minor_locator "matplotlib.axis.Axis.set_minor_locator")
    
*   [`matplotlib.patches.Circle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
    
*   [`matplotlib.patheffects.withStroke`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withStroke "matplotlib.patheffects.withStroke")
    
*   [`matplotlib.ticker.FuncFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
    

**Total running time of the script:** (0 minutes 2.230 seconds)

[`Download Jupyter notebook: anatomy.ipynb`](https://matplotlib.org/stable/_downloads/d2c8b8c6d25d7da97611d120d4eafb12/anatomy.ipynb)

[`Download Python source code: anatomy.py`](https://matplotlib.org/stable/_downloads/3f00827998b6984a744509eca414f222/anatomy.py)

[`Download zipped: anatomy.zip`](https://matplotlib.org/stable/_downloads/91da19ddf8265f5ab587e70a263ccef7/anatomy.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)