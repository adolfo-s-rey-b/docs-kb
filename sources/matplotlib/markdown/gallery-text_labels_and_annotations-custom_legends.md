[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/custom_legends.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/custom_legends.html#sphx-glr-download-gallery-text-labels-and-annotations-custom-legends-py)
 to download the full example code.

Compose custom legends[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/custom_legends.html#compose-custom-legends "Link to this heading")

===============================================================================================================================================================

Composing custom legends piece-by-piece.

Note

For more information on creating and customizing legends, see the following pages:

*   [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
    
*   [Legend Demo](https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend_demo.html)
    

Sometimes you don't want a legend that is explicitly tied to data that you have plotted. For example, say you have plotted 10 lines, but don't want a legend item to show up for each one. If you simply plot the lines and call `ax.legend()`, you will get the following:

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
from matplotlib import cycler

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 10
[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([np.geomspace](https://numpy.org/doc/stable/reference/generated/numpy.geomspace.html#numpy.geomspace "numpy.geomspace")
(1, 10, 100) + [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 100)).T
[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
 \= [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["coolwarm"\]
[mpl.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['axes.prop\_cycle'\] \= cycler(color\=[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)))

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

![custom legends](https://matplotlib.org/stable/_images/sphx_glr_custom_legends_001_2_00x.png)

Since the data does not have any labels, creating a legend requires us to define the icons and labels. In this case, we can compose a legend using Matplotlib objects that aren't explicitly tied to the data that was plotted. For example:

from matplotlib.lines import [Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

[custom\_lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
(\[0\], \[0\], color\=[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")\
(0.), lw\=4),\
                [Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
(\[0\], \[0\], color\=[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")\
(.5), lw\=4),\
                [Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
(\[0\], \[0\], color\=[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")\
(1.), lw\=4)\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
([custom\_lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, \['Cold', 'Medium', 'Hot'\])

![custom legends](https://matplotlib.org/stable/_images/sphx_glr_custom_legends_002_2_00x.png)

There are many other Matplotlib objects that can be used in this way. In the code below we've listed a few common ones.

from matplotlib.lines import [Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
from matplotlib.patches import [Patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")

[legend\_elements](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
(\[0\], \[0\], color\='b', lw\=4, label\='Line'),\
                   [Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
(\[0\], \[0\], marker\='o', color\='w', label\='Scatter',\
                          markerfacecolor\='g', markersize\=15),\
                   [Patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")\
(facecolor\='orange', edgecolor\='r',\
                         label\='Color Patch')\]

\# Create the figure
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(handles\=[legend\_elements](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, loc\='center')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![custom legends](https://matplotlib.org/stable/_images/sphx_glr_custom_legends_003_2_00x.png)

**Total running time of the script:** (0 minutes 1.598 seconds)

[`Download Jupyter notebook: custom_legends.ipynb`](https://matplotlib.org/stable/_downloads/b757a464e6c36d1fb3a78463a8df8511/custom_legends.ipynb)

[`Download Python source code: custom_legends.py`](https://matplotlib.org/stable/_downloads/dcd6af3a3384b030d707536e9a7319f3/custom_legends.py)

[`Download zipped: custom_legends.zip`](https://matplotlib.org/stable/_downloads/0a1a7bdd88420360cf7832cb20733c15/custom_legends.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)