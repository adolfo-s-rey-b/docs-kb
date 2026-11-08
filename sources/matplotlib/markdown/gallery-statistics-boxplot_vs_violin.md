[Skip to main content](https://matplotlib.org/stable/gallery/statistics/boxplot_vs_violin.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/statistics/boxplot_vs_violin.html#sphx-glr-download-gallery-statistics-boxplot-vs-violin-py)
 to download the full example code.

Box plot vs. violin plot comparison[#](https://matplotlib.org/stable/gallery/statistics/boxplot_vs_violin.html#box-plot-vs-violin-plot-comparison "Link to this heading")

==========================================================================================================================================================================

Note that although violin plots are closely related to Tukey's (1977) box plots, they add useful information such as the distribution of the sample data (density trace).

By default, box plots show data points outside 1.5 \* the inter-quartile range as outliers above or below the whiskers whereas violin plots show the whole range of the data.

A good general reference on boxplots and their history can be found here: [https://vita.had.co.nz/papers/boxplots.pdf](https://vita.had.co.nz/papers/boxplots.pdf)

Violin plots require matplotlib >= 1.4.

Violin plots show the distribution of the data as a rotated kernel density estimate (KDE) along with summary statistics similar to a box plot.

For more information on violin plots, see: [https://en.wikipedia.org/wiki/Violin\_plot](https://en.wikipedia.org/wiki/Violin_plot)

import matplotlib.pyplot as plt
import numpy as np

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=2, figsize\=(9, 4))

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

\# generate some random test data
[all\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")\
(0, std, 100) for std in range(6, 10)\]

\# plot violin plot
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].violinplot([all\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
,
                  showmeans\=False,
                  showmedians\=True)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title('Violin plot')

\# plot box plot
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].boxplot([all\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_title('Box plot')

\# adding horizontal grid lines
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:
    [ax.yaxis.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.grid.html#matplotlib.axis.Axis.grid "matplotlib.axis.Axis.grid")
(True)
    [ax.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
(\[y + 1 for y in range(len([all\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
))\],
                  labels\=\['x1', 'x2', 'x3', 'x4'\])
    [ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('Four separate samples')
    [ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('Observed values')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Violin plot, Box plot](https://matplotlib.org/stable/_images/sphx_glr_boxplot_vs_violin_001_2_00x.png)

Tags: [plot-type: violin](https://matplotlib.org/stable/_tags/plot-type-violin.html)
 [plot-type: boxplot](https://matplotlib.org/stable/_tags/plot-type-boxplot.html)
 [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
     / [`matplotlib.pyplot.boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot "matplotlib.pyplot.boxplot")
    
*   [`matplotlib.axes.Axes.violinplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html#matplotlib.axes.Axes.violinplot "matplotlib.axes.Axes.violinplot")
     / [`matplotlib.pyplot.violinplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.violinplot.html#matplotlib.pyplot.violinplot "matplotlib.pyplot.violinplot")
    

[`Download Jupyter notebook: boxplot_vs_violin.ipynb`](https://matplotlib.org/stable/_downloads/5338ee4cbadb24f31e9dd0465c609cb1/boxplot_vs_violin.ipynb)

[`Download Python source code: boxplot_vs_violin.py`](https://matplotlib.org/stable/_downloads/82c8fa6f7fde224ac82e9fb57e603326/boxplot_vs_violin.py)

[`Download zipped: boxplot_vs_violin.zip`](https://matplotlib.org/stable/_downloads/f42277c229e613fabdf9bb4b76f8c3ef/boxplot_vs_violin.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)