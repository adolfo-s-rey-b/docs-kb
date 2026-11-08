[Skip to main content](https://matplotlib.org/stable/gallery/statistics/histogram_histtypes.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/statistics/histogram_histtypes.html#sphx-glr-download-gallery-statistics-histogram-histtypes-py)
 to download the full example code.

Demo of the histogram function's different `histtype` settings[#](https://matplotlib.org/stable/gallery/statistics/histogram_histtypes.html#demo-of-the-histogram-function-s-different-histtype-settings "Link to this heading")

=================================================================================================================================================================================================================================

*   Histogram with step curve that has a color fill.
    
*   Histogram with step curve with no fill.
    
*   Histogram with custom and unequal bin widths.
    
*   Two histograms with stacked bars.
    

Selecting different bin counts and sizes can significantly affect the shape of a histogram. The Astropy docs have a great section on how to select these parameters: [http://docs.astropy.org/en/stable/visualization/histogram.html](http://docs.astropy.org/en/stable/visualization/histogram.html)

import matplotlib.pyplot as plt
import numpy as np

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[mu\_x](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 200
[sigma\_x](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 25
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
([mu\_x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [sigma\_x](https://docs.python.org/3/library/functions.html#int "builtins.int")
, size\=100)

[mu\_w](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 200
[sigma\_w](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 10
[w](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
([mu\_w](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [sigma\_w](https://docs.python.org/3/library/functions.html#int "builtins.int")
, size\=100)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=2)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].hist([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 20, density\=True, histtype\='stepfilled', facecolor\='g',
               alpha\=0.75)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].set\_title('stepfilled')

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].hist([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 20, density\=True, histtype\='step', facecolor\='g',
               alpha\=0.75)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].set\_title('step')

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].hist([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, density\=True, histtype\='barstacked', rwidth\=0.8)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].hist([w](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, density\=True, histtype\='barstacked', rwidth\=0.8)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].set\_title('barstacked')

\# Create a histogram by providing the bin edges (unequally spaced).
[bins](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[100, 150, 180, 195, 205, 220, 250, 300\]
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].hist([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bins](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, density\=True, histtype\='bar', rwidth\=0.8)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].set\_title('bar, unequal bins')

[fig.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![stepfilled, step, barstacked, bar, unequal bins](https://matplotlib.org/stable/_images/sphx_glr_histogram_histtypes_001_2_00x.png)

Tags: [plot-type: histogram](https://matplotlib.org/stable/_tags/plot-type-histogram.html)
 [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)
 [purpose: reference](https://matplotlib.org/stable/_tags/purpose-reference.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
     / [`matplotlib.pyplot.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist "matplotlib.pyplot.hist")
    

**Total running time of the script:** (0 minutes 1.042 seconds)

[`Download Jupyter notebook: histogram_histtypes.ipynb`](https://matplotlib.org/stable/_downloads/37abb4a85ffcd007e8f7cbf2f4d24d67/histogram_histtypes.ipynb)

[`Download Python source code: histogram_histtypes.py`](https://matplotlib.org/stable/_downloads/f8c0358a738de22bc3fd0b333e981c29/histogram_histtypes.py)

[`Download zipped: histogram_histtypes.zip`](https://matplotlib.org/stable/_downloads/e29d8220ef916b83f2d8f046d0d2a0ec/histogram_histtypes.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)