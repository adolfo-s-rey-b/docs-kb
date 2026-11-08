[Skip to main content](https://matplotlib.org/stable/gallery/statistics/violinplot.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/statistics/violinplot.html#sphx-glr-download-gallery-statistics-violinplot-py)
 to download the full example code.

Violin plot basics[#](https://matplotlib.org/stable/gallery/statistics/violinplot.html#violin-plot-basics "Link to this heading")

==================================================================================================================================

Violin plots are similar to histograms and box plots in that they show an abstract representation of the probability distribution of the sample. Rather than showing counts of data points that fall into bins or order statistics, violin plots use kernel density estimation (KDE) to compute an empirical distribution of the sample. That computation is controlled by several parameters. This example demonstrates how to modify the number of points at which the KDE is evaluated (`points`) and how to modify the bandwidth of the KDE (`bw_method`).

For more information on violin plots and KDE, the scikit-learn docs have a great section: [https://scikit-learn.org/stable/modules/density.html](https://scikit-learn.org/stable/modules/density.html)

import matplotlib.pyplot as plt
import numpy as np

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

\# fake data
[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 10  \# fontsize
[pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[1, 2, 4, 5, 7, 8\]
[data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")\
(0, std, size\=100) for std in [pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=6, figsize\=(10, 4))

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].violinplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, points\=20, widths\=0.3,
                     showmeans\=True, showextrema\=True, showmedians\=True)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].set\_title('Custom violin 1', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].violinplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, points\=40, widths\=0.5,
                     showmeans\=True, showextrema\=True, showmedians\=True,
                     bw\_method\='silverman')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].set\_title('Custom violin 2', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 2\].violinplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, points\=60, widths\=0.7, showmeans\=True,
                     showextrema\=True, showmedians\=True, bw\_method\=0.5)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 2\].set\_title('Custom violin 3', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 3\].violinplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, points\=60, widths\=0.7, showmeans\=True,
                     showextrema\=True, showmedians\=True, bw\_method\=0.5,
                     quantiles\=\[\[0.1\], \[\], \[\], \[0.175, 0.954\], \[0.75\], \[0.25\]\])
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 3\].set\_title('Custom violin 4', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 4\].violinplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[\-1:\], [pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[\-1:\], points\=60, widths\=0.7,
                     showmeans\=True, showextrema\=True, showmedians\=True,
                     quantiles\=\[0.05, 0.1, 0.8, 0.9\], bw\_method\=0.5)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 4\].set\_title('Custom violin 5', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 5\].violinplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[\-1:\], [pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[\-1:\], points\=60, widths\=0.7,
                     showmeans\=True, showextrema\=True, showmedians\=True,
                     quantiles\=\[0.05, 0.1, 0.8, 0.9\], bw\_method\=0.5, side\='low')

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 5\].violinplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[\-1:\], [pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[\-1:\], points\=60, widths\=0.7,
                     showmeans\=True, showextrema\=True, showmedians\=True,
                     quantiles\=\[0.05, 0.1, 0.8, 0.9\], bw\_method\=0.5, side\='high')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 5\].set\_title('Custom violin 6', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].violinplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, points\=80, orientation\='horizontal', widths\=0.7,
                     showmeans\=True, showextrema\=True, showmedians\=True)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].set\_title('Custom violin 7', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].violinplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, points\=100, orientation\='horizontal', widths\=0.9,
                     showmeans\=True, showextrema\=True, showmedians\=True,
                     bw\_method\='silverman')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].set\_title('Custom violin 8', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 2\].violinplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, points\=200, orientation\='horizontal', widths\=1.1,
                     showmeans\=True, showextrema\=True, showmedians\=True,
                     bw\_method\=0.5)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 2\].set\_title('Custom violin 9', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 3\].violinplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, points\=200, orientation\='horizontal', widths\=1.1,
                     showmeans\=True, showextrema\=True, showmedians\=True,
                     quantiles\=\[\[0.1\], \[\], \[\], \[0.175, 0.954\], \[0.75\], \[0.25\]\],
                     bw\_method\=0.5)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 3\].set\_title('Custom violin 10', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 4\].violinplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[\-1:\], [pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[\-1:\], points\=200, orientation\='horizontal',
                     widths\=1.1, showmeans\=True, showextrema\=True, showmedians\=True,
                     quantiles\=\[0.05, 0.1, 0.8, 0.9\], bw\_method\=0.5)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 4\].set\_title('Custom violin 11', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 5\].violinplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[\-1:\], [pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[\-1:\], points\=200, orientation\='horizontal',
                     widths\=1.1, showmeans\=True, showextrema\=True, showmedians\=True,
                     quantiles\=\[0.05, 0.1, 0.8, 0.9\], bw\_method\=0.5, side\='low')

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 5\].violinplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[\-1:\], [pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[\-1:\], points\=200, orientation\='horizontal',
                     widths\=1.1, showmeans\=True, showextrema\=True, showmedians\=True,
                     quantiles\=\[0.05, 0.1, 0.8, 0.9\], bw\_method\=0.5, side\='high')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 5\].set\_title('Custom violin 12', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    [ax.set\_yticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels")
(\[\])

[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
("Violin Plotting Examples")
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(hspace\=0.4)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Violin Plotting Examples, Custom violin 1, Custom violin 2, Custom violin 3, Custom violin 4, Custom violin 5, Custom violin 6, Custom violin 7, Custom violin 8, Custom violin 9, Custom violin 10, Custom violin 11, Custom violin 12](https://matplotlib.org/stable/_images/sphx_glr_violinplot_001_2_00x.png)

Tags: [plot-type: violin](https://matplotlib.org/stable/_tags/plot-type-violin.html)
 [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.violinplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html#matplotlib.axes.Axes.violinplot "matplotlib.axes.Axes.violinplot")
     / [`matplotlib.pyplot.violinplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.violinplot.html#matplotlib.pyplot.violinplot "matplotlib.pyplot.violinplot")
    

**Total running time of the script:** (0 minutes 1.652 seconds)

[`Download Jupyter notebook: violinplot.ipynb`](https://matplotlib.org/stable/_downloads/604f15717c1743907b81ea19a7a0bb6c/violinplot.ipynb)

[`Download Python source code: violinplot.py`](https://matplotlib.org/stable/_downloads/77f53caf20c3697ea59d377ac3f4ebeb/violinplot.py)

[`Download zipped: violinplot.zip`](https://matplotlib.org/stable/_downloads/1f7038e54249466332a3c93d84e24fd6/violinplot.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)