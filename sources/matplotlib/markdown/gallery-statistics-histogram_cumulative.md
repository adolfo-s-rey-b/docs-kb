[Skip to main content](https://matplotlib.org/stable/gallery/statistics/histogram_cumulative.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/statistics/histogram_cumulative.html#sphx-glr-download-gallery-statistics-histogram-cumulative-py)
 to download the full example code.

Cumulative distributions[#](https://matplotlib.org/stable/gallery/statistics/histogram_cumulative.html#cumulative-distributions "Link to this heading")

========================================================================================================================================================

This example shows how to plot the empirical cumulative distribution function (ECDF) of a sample. We also show the theoretical CDF.

In engineering, ECDFs are sometimes called "non-exceedance" curves: the y-value for a given x-value gives probability that an observation from the sample is below that x-value. For example, the value of 220 on the x-axis corresponds to about 0.80 on the y-axis, so there is an 80% chance that an observation in the sample does not exceed 220. Conversely, the empirical _complementary_ cumulative distribution function (the ECCDF, or "exceedance" curve) shows the probability y that an observation from the sample is above a value x.

A direct method to plot ECDFs is [`Axes.ecdf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ecdf.html#matplotlib.axes.Axes.ecdf "matplotlib.axes.Axes.ecdf")
. Passing `complementary=True` results in an ECCDF instead.

Alternatively, one can use `ax.hist(data, density=True, cumulative=True)` to first bin the data, as if plotting a histogram, and then compute and plot the cumulative sums of the frequencies of entries in each bin. Here, to plot the ECCDF, pass `cumulative=-1`. Note that this approach results in an approximation of the E(C)CDF, whereas [`Axes.ecdf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ecdf.html#matplotlib.axes.Axes.ecdf "matplotlib.axes.Axes.ecdf")
 is exact.

import matplotlib.pyplot as plt
import numpy as np

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[mu](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 200
[sigma](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 25
[n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 25
[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
([mu](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [sigma](https://docs.python.org/3/library/functions.html#int "builtins.int")
, size\=100)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(9, 4), layout\="constrained")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [fig.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
(1, 2, sharex\=True, sharey\=True)

\# Cumulative distributions.
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].ecdf([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, label\="CDF")
[n](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [patches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].hist([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
, density\=True, histtype\="step",
                               cumulative\=True, label\="Cumulative histogram")
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.min(), [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max())
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ((1 / ([np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
) \* [sigma](https://docs.python.org/3/library/functions.html#int "builtins.int")
)) \*
     [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-0.5 \* (1 / [sigma](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* ([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- [mu](https://docs.python.org/3/library/functions.html#int "builtins.int")
))\*\*2))
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.cumsum()
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 /= [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[\-1\]
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, "k--", linewidth\=1.5, label\="Theory")

\# Complementary cumulative distributions.
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].ecdf([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, complementary\=True, label\="CCDF")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].hist([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, density\=True, histtype\="step", cumulative\=-1,
            label\="Reversed cumulative histogram")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 1 \- [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, "k--", linewidth\=1.5, label\="Theory")

\# Label the figure.
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
("Cumulative distributions")
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:
    [ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
(True)
    [ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()
    [ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
("Annual rainfall (mm)")
    [ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
("Probability of occurrence")
    [ax.label\_outer](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.label_outer.html#matplotlib.axes.Axes.label_outer "matplotlib.axes.Axes.label_outer")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Cumulative distributions](https://matplotlib.org/stable/_images/sphx_glr_histogram_cumulative_001_2_00x.png)

Tags: [plot-type: ecdf](https://matplotlib.org/stable/_tags/plot-type-ecdf.html)
 [plot-type: histogram](https://matplotlib.org/stable/_tags/plot-type-histogram.html)
 [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
     / [`matplotlib.pyplot.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist "matplotlib.pyplot.hist")
    
*   [`matplotlib.axes.Axes.ecdf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ecdf.html#matplotlib.axes.Axes.ecdf "matplotlib.axes.Axes.ecdf")
     / [`matplotlib.pyplot.ecdf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ecdf.html#matplotlib.pyplot.ecdf "matplotlib.pyplot.ecdf")
    

**Total running time of the script:** (0 minutes 1.155 seconds)

[`Download Jupyter notebook: histogram_cumulative.ipynb`](https://matplotlib.org/stable/_downloads/a9a1c37825bddcdb3793adbd89b30ed0/histogram_cumulative.ipynb)

[`Download Python source code: histogram_cumulative.py`](https://matplotlib.org/stable/_downloads/58a1dc1dad006bedcf1fe41aa699b676/histogram_cumulative.py)

[`Download zipped: histogram_cumulative.zip`](https://matplotlib.org/stable/_downloads/b6c29cd767f9b279b89da429b77b9b6b/histogram_cumulative.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)