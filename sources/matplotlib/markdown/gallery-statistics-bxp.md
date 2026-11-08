[Skip to main content](https://matplotlib.org/stable/gallery/statistics/bxp.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/statistics/bxp.html#sphx-glr-download-gallery-statistics-bxp-py)
 to download the full example code.

Separate calculation and plotting of boxplots[#](https://matplotlib.org/stable/gallery/statistics/bxp.html#separate-calculation-and-plotting-of-boxplots "Link to this heading")

=================================================================================================================================================================================

Drawing a [`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
 for a given data set, consists of two main operations, that can also be used separately:

1.  Calculating the boxplot statistics: [`matplotlib.cbook.boxplot_stats`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.boxplot_stats "matplotlib.cbook.boxplot_stats")
    
2.  Drawing the boxplot: [`matplotlib.axes.Axes.bxp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "matplotlib.axes.Axes.bxp")
    

Thus, `ax.boxplot(data)` is equivalent to

[stats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [cbook.boxplot\_stats](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.boxplot_stats "matplotlib.cbook.boxplot_stats")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.bxp](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "matplotlib.axes.Axes.bxp")
([stats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

All styling keyword arguments are identical between [`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
 and [`bxp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "matplotlib.axes.Axes.bxp")
, and they are passed through from [`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
 to [`bxp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "matplotlib.axes.Axes.bxp")
. However, the _tick\_labels_ parameter of [`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
 translates to a generic _labels_ parameter in [`boxplot_stats`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.boxplot_stats "matplotlib.cbook.boxplot_stats")
, because the labels are data-related and attached to the returned per-dataset dictionaries.

The following code demonstrates the equivalence between the two methods.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cbook

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)
[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(20, 3)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2)

\# single boxplot call
[ax1.boxplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, tick\_labels\=\['A', 'B', 'C'\],
            patch\_artist\=True, boxprops\={'facecolor': 'bisque'})

\# separate calculation of statistics and plotting
[stats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [cbook.boxplot\_stats](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.boxplot_stats "matplotlib.cbook.boxplot_stats")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, labels\=\['A', 'B', 'C'\])
[ax2.bxp](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "matplotlib.axes.Axes.bxp")
([stats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, patch\_artist\=True, boxprops\={'facecolor': 'bisque'})

![bxp](https://matplotlib.org/stable/_images/sphx_glr_bxp_001_2_00x.png)

Using the separate functions allows to pre-calculate statistics, in case you need them explicitly for other purposes, or to reuse the statistics for multiple plots.

Conversely, you can also use the [`bxp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "matplotlib.axes.Axes.bxp")
 function directly, if you already have the statistical parameters:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[stats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
    dict(med\=0, q1\=-1, q3\=1, whislo\=-2, whishi\=2, fliers\=\[\-4, \-3, 3, 4\], label\='A'),\
    dict(med\=0, q1\=-2, q3\=2, whislo\=-3, whishi\=3, fliers\=\[\], label\='B'),\
    dict(med\=0, q1\=-3, q3\=3, whislo\=-4, whishi\=4, fliers\=\[\], label\='C'),\
\]

[ax.bxp](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "matplotlib.axes.Axes.bxp")
([stats](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, patch\_artist\=True, boxprops\={'facecolor': 'bisque'})

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![bxp](https://matplotlib.org/stable/_images/sphx_glr_bxp_002_2_00x.png)

Tags: [plot-type: specialty](https://matplotlib.org/stable/_tags/plot-type-specialty.html)
 [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.bxp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "matplotlib.axes.Axes.bxp")
    
*   [`matplotlib.axes.Axes.boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
    
*   [`matplotlib.cbook.boxplot_stats`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.boxplot_stats "matplotlib.cbook.boxplot_stats")
    

[`Download Jupyter notebook: bxp.ipynb`](https://matplotlib.org/stable/_downloads/f1dc0583b704179f720a3839eff6d57c/bxp.ipynb)

[`Download Python source code: bxp.py`](https://matplotlib.org/stable/_downloads/19e830e3793676dff715e60078f0dd91/bxp.py)

[`Download zipped: bxp.zip`](https://matplotlib.org/stable/_downloads/d61c0a0763c0256ff1e483ed09273d57/bxp.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)