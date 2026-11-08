[Skip to main content](https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html#sphx-glr-download-gallery-statistics-histogram-multihist-py)
 to download the full example code.

The histogram (hist) function with multiple data sets[#](https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html#the-histogram-hist-function-with-multiple-data-sets "Link to this heading")

===============================================================================================================================================================================================================

Plot histogram with multiple sample sets and demonstrate:

*   Use of legend with multiple sample sets
    
*   Stacked bars
    
*   Step curve with no fill
    
*   Data sets of different sample sizes
    

Selecting different bin counts and sizes can significantly affect the shape of a histogram. The Astropy docs have a great section on how to select these parameters: [http://docs.astropy.org/en/stable/visualization/histogram.html](http://docs.astropy.org/en/stable/visualization/histogram.html)

import matplotlib.pyplot as plt
import numpy as np

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 10
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(1000, 3)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, (([ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
), ([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=2)

[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['red', 'tan', 'lime'\]
[ax0.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
, density\=True, histtype\='bar', color\=[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, label\=[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax0.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(prop\={'size': 10})
[ax0.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('bars with legend')

[ax1.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
, density\=True, histtype\='bar', stacked\=True)
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('stacked bar')

[ax2.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
, histtype\='step', stacked\=True, fill\=False)
[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('stack step (unfilled)')

\# Make a multiple-histogram of data-sets with different length.
[x\_multi](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")\
(n) for n in \[10000, 5000, 2000\]\]
[ax3.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([x\_multi](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
, histtype\='bar')
[ax3.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('different sample sizes')

[fig.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![bars with legend, stacked bar, stack step (unfilled), different sample sizes](https://matplotlib.org/stable/_images/sphx_glr_histogram_multihist_001_2_00x.png)

Setting properties for each dataset[#](https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html#setting-properties-for-each-dataset "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can style the histograms individually by passing a list of values to the following parameters:

*   edgecolor
    
*   facecolor
    
*   hatch
    
*   linewidth
    
*   linestyle
    

### edgecolor[#](https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html#edgecolor "Link to this heading")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[edgecolors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['green', 'red', 'blue'\]

[ax.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
, fill\=False, histtype\="step", stacked\=True,
        edgecolor\=[edgecolors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, label\=[edgecolors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Stacked Steps with Edgecolors')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Stacked Steps with Edgecolors](https://matplotlib.org/stable/_images/sphx_glr_histogram_multihist_002_2_00x.png)

### facecolor[#](https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html#facecolor "Link to this heading")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[facecolors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['green', 'red', 'blue'\]

[ax.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
, histtype\="barstacked", facecolor\=[facecolors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, label\=[facecolors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Bars with different Facecolors")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Bars with different Facecolors](https://matplotlib.org/stable/_images/sphx_glr_histogram_multihist_003_2_00x.png)

### hatch[#](https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html#hatch "Link to this heading")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[hatches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[".", "o", "x"\]

[ax.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
, histtype\="barstacked", hatch\=[hatches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, label\=[hatches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Hatches on Stacked Bars")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Hatches on Stacked Bars](https://matplotlib.org/stable/_images/sphx_glr_histogram_multihist_004_2_00x.png)

### linewidth[#](https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html#linewidth "Link to this heading")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[linewidths](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[1, 2, 3\]
[edgecolors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \["green", "red", "blue"\]

[ax.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
, fill\=False, histtype\="bar", linewidth\=[linewidths](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
,
        edgecolor\=[edgecolors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, label\=[linewidths](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Bars with Linewidths")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Bars with Linewidths](https://matplotlib.org/stable/_images/sphx_glr_histogram_multihist_005_2_00x.png)

### linestyle[#](https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html#linestyle "Link to this heading")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[linestyles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['-', ':', '--'\]

[ax.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
, fill\=False, histtype\='bar', linestyle\=[linestyles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
,
        edgecolor\=[edgecolors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, label\=[linestyles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Bars with Linestyles')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Bars with Linestyles](https://matplotlib.org/stable/_images/sphx_glr_histogram_multihist_006_2_00x.png)

Tags: [plot-type: histogram](https://matplotlib.org/stable/_tags/plot-type-histogram.html)
 [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)
 [purpose: reference](https://matplotlib.org/stable/_tags/purpose-reference.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
     / [`matplotlib.pyplot.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist "matplotlib.pyplot.hist")
    

**Total running time of the script:** (0 minutes 3.845 seconds)

[`Download Jupyter notebook: histogram_multihist.ipynb`](https://matplotlib.org/stable/_downloads/3e6c719f7d1fe721c72d931dc8a96f38/histogram_multihist.ipynb)

[`Download Python source code: histogram_multihist.py`](https://matplotlib.org/stable/_downloads/04f39a3d85a1b2537b2f1fa65e101df4/histogram_multihist.py)

[`Download zipped: histogram_multihist.zip`](https://matplotlib.org/stable/_downloads/62b25e16385d940a71f50643538f9f8d/histogram_multihist.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page