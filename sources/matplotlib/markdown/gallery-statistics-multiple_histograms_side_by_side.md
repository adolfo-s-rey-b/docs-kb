[Skip to main content](https://matplotlib.org/stable/gallery/statistics/multiple_histograms_side_by_side.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/statistics/multiple_histograms_side_by_side.html#sphx-glr-download-gallery-statistics-multiple-histograms-side-by-side-py)
 to download the full example code.

Multiple histograms side by side[#](https://matplotlib.org/stable/gallery/statistics/multiple_histograms_side_by_side.html#multiple-histograms-side-by-side "Link to this heading")

====================================================================================================================================================================================

This example plots horizontal histograms of different samples along a categorical x-axis. Additionally, the histograms are plotted to be symmetrical about their x-position, thus making them very similar to violin plots.

To make this highly specialized plot, we can't use the standard `hist` method. Instead, we use `barh` to draw the horizontal bars directly. The vertical positions and lengths of the bars are computed via the `np.histogram` function. The histograms for all the samples are computed using the same range (min and max values) and number of bins, so that the bins for each sample are in the same vertical positions.

Selecting different bin counts and sizes can significantly affect the shape of a histogram. The Astropy docs have a great section on how to select these parameters: [http://docs.astropy.org/en/stable/visualization/histogram.html](http://docs.astropy.org/en/stable/visualization/histogram.html)

import matplotlib.pyplot as plt
import numpy as np

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)
[number\_of\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 20

\# An example of three data sets to compare
[number\_of\_data\_points](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 387
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \["A", "B", "C"\]
[data\_sets](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")\
(0, 1, [number\_of\_data\_points](https://docs.python.org/3/library/functions.html#int "builtins.int")\
),\
             [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")\
(6, 1, [number\_of\_data\_points](https://docs.python.org/3/library/functions.html#int "builtins.int")\
),\
             [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")\
(\-3, 1, [number\_of\_data\_points](https://docs.python.org/3/library/functions.html#int "builtins.int")\
)\]

\# Computed quantities to aid plotting
[hist\_range](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= ([np.min](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")
([data\_sets](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
), [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
([data\_sets](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
))
[binned\_data\_sets](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
    [np.histogram](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "numpy.histogram")\
(d, range\=[hist\_range](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
, bins\=[number\_of\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")\
)\[0\]\
    for d in [data\_sets](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\]
[binned\_maximums](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
([binned\_data\_sets](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, axis\=1)
[x\_locations](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, sum([binned\_maximums](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
([binned\_maximums](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))

\# The bin\_edges are the same for all of the histograms
[bin\_edges](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([hist\_range](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\], [hist\_range](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[1\], [number\_of\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + 1)
[heights](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.diff](https://numpy.org/doc/stable/reference/generated/numpy.diff.html#numpy.diff "numpy.diff")
([bin\_edges](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[centers](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [bin\_edges](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:\-1\] + [heights](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 / 2

\# Cycle through and plot each histogram
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
for [x\_loc](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, [binned\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 in zip([x\_locations](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [binned\_data\_sets](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [lefts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [x\_loc](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
 \- 0.5 \* [binned\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
    [ax.barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
([centers](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [binned\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, height\=[heights](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, left\=[lefts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[ax.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
([x\_locations](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
("Data values")
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
("Data sets")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![multiple histograms side by side](https://matplotlib.org/stable/_images/sphx_glr_multiple_histograms_side_by_side_001_2_00x.png)

Tags: [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)
 [plot-type: barh](https://matplotlib.org/stable/_tags/plot-type-barh.html)
 [plot-type: histogram](https://matplotlib.org/stable/_tags/plot-type-histogram.html)
 [styling: position](https://matplotlib.org/stable/_tags/styling-position.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
     / [`matplotlib.pyplot.barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html#matplotlib.pyplot.barh "matplotlib.pyplot.barh")
    

[`Download Jupyter notebook: multiple_histograms_side_by_side.ipynb`](https://matplotlib.org/stable/_downloads/2018481c7f104b447e00b9df2654b4e0/multiple_histograms_side_by_side.ipynb)

[`Download Python source code: multiple_histograms_side_by_side.py`](https://matplotlib.org/stable/_downloads/a2298827019c2c94b5fc1bf606e6d29b/multiple_histograms_side_by_side.py)

[`Download zipped: multiple_histograms_side_by_side.zip`](https://matplotlib.org/stable/_downloads/d3e3c638b2379402d00163d9480c0669/multiple_histograms_side_by_side.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)