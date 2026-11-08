[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stackplot_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stackplot_demo.html#sphx-glr-download-gallery-lines-bars-and-markers-stackplot-demo-py)
 to download the full example code.

Stackplots and streamgraphs[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stackplot_demo.html#stackplots-and-streamgraphs "Link to this heading")

====================================================================================================================================================================

Stackplots[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stackplot_demo.html#stackplots "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

Stackplots draw multiple datasets as vertically stacked areas. This is useful when the individual data values and additionally their cumulative value are of interest.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.ticker as mticker

\# data from United Nations World Population Prospects (Revision 2019)
\# https://population.un.org/wpp/, license: CC BY 3.0 IGO
[year](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[1950, 1960, 1970, 1980, 1990, 2000, 2010, 2018\]
[population\_by\_continent](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    'Africa': \[.228, .284, .365, .477, .631, .814, 1.044, 1.275\],
    'the Americas': \[.340, .425, .519, .619, .727, .840, .943, 1.006\],
    'Asia': \[1.394, 1.686, 2.120, 2.625, 3.202, 3.714, 4.169, 4.560\],
    'Europe': \[.220, .253, .276, .295, .310, .303, .294, .293\],
    'Oceania': \[.012, .015, .019, .022, .026, .031, .036, .039\],
}

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.stackplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stackplot.html#matplotlib.axes.Axes.stackplot "matplotlib.axes.Axes.stackplot")
([year](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [population\_by\_continent](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.values(),
             labels\=[population\_by\_continent](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.keys(), alpha\=0.8)
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(loc\='upper left', reverse\=True)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('World population')
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('Year')
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('Number of people (billions)')
\# add tick at every 200 million people
[ax.yaxis.set\_minor\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html#matplotlib.axis.Axis.set_minor_locator "matplotlib.axis.Axis.set_minor_locator")
([mticker.MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(.2))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![World population](https://matplotlib.org/stable/_images/sphx_glr_stackplot_demo_001_2_00x.png)

Streamgraphs[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stackplot_demo.html#streamgraphs "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

Using the _baseline_ parameter, you can turn an ordinary stacked area plot with baseline 0 into a stream graph.

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

def gaussian\_mixture([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, n\=5):
    """Return a random mixture of \*n\* Gaussians, evaluated at positions \*x\*."""
    def add\_random\_gaussian(a):
        amplitude \= 1 / (.1 + [np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
())
        dx \= [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[\-1\] \- [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\]
        x0 \= (2 \* [np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
() \- .5) \* dx
        z \= 10 / (.1 + [np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
()) / dx
        a += amplitude \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-(z \* ([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- x0))\*\*2)
    a \= [np.zeros\_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    for j in range(n):
        add\_random\_gaussian(a)
    return a

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 100, 101)
[ys](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[gaussian\_mixture([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
) for \_ in range(3)\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.stackplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stackplot.html#matplotlib.axes.Axes.stackplot "matplotlib.axes.Axes.stackplot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ys](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, baseline\='wiggle')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![stackplot demo](https://matplotlib.org/stable/_images/sphx_glr_stackplot_demo_002_2_00x.png)

Tags: [plot-type: stackplot](https://matplotlib.org/stable/_tags/plot-type-stackplot.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

**Total running time of the script:** (0 minutes 1.308 seconds)

[`Download Jupyter notebook: stackplot_demo.ipynb`](https://matplotlib.org/stable/_downloads/7afd487d29d3e4007341ca5784ceb850/stackplot_demo.ipynb)

[`Download Python source code: stackplot_demo.py`](https://matplotlib.org/stable/_downloads/a4ca2d398a778f09d428679d85cdef43/stackplot_demo.py)

[`Download zipped: stackplot_demo.zip`](https://matplotlib.org/stable/_downloads/6301f743b360194a40d4921074be4bdd/stackplot_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page