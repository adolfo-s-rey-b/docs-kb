[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html#sphx-glr-download-gallery-lines-bars-and-markers-scatter-with-legend-py)
 to download the full example code.

Scatter plot with a legend[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html#scatter-plot-with-a-legend "Link to this heading")

=======================================================================================================================================================================

To create a scatter plot with a legend one may use a loop and create one [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
 plot per item to appear in the legend and set the `label` accordingly.

The following also demonstrates how transparency of the markers can be adjusted by giving `alpha` a value between 0 and 1.

import matplotlib.pyplot as plt
import numpy as np

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
for [color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in \['tab:blue', 'tab:orange', 'tab:green'\]:
    [n](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 750
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(2, [n](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [scale](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 200.0 \* [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
([n](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [c](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[scale](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, label\=[color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
,
               alpha\=0.3, edgecolors\='none')

[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()
[ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
(True)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![scatter with legend](https://matplotlib.org/stable/_images/sphx_glr_scatter_with_legend_001_2_00x.png)

Automated legend creation[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html#automated-legend-creation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Another option for creating a legend for a scatter is to use the [`PathCollection.legend_elements`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection.legend_elements "matplotlib.collections.PathCollection.legend_elements")
 method. It will automatically try to determine a useful number of legend entries to be shown and return a tuple of handles and labels. Those can be passed to the call to [`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
.

[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 45
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(2, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[c](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")
(1, 5, size\=[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")
(10, 220, size\=[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[scatter](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
 \= [ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [c](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[c](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# produce a legend with the unique colors from the scatter
[legend1](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 \= [ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(\*[scatter.legend\_elements](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection.legend_elements "matplotlib.collections.PathCollection.legend_elements")
(),
                    loc\="lower left", title\="Classes")
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([legend1](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
)

\# produce a legend with a cross-section of sizes from the scatter
[handles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [scatter.legend\_elements](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection.legend_elements "matplotlib.collections.PathCollection.legend_elements")
(prop\="sizes", alpha\=0.6)
[legend2](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 \= [ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
([handles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, loc\="upper right", title\="Sizes")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![scatter with legend](https://matplotlib.org/stable/_images/sphx_glr_scatter_with_legend_002_2_00x.png)

Further arguments to the [`PathCollection.legend_elements`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection.legend_elements "matplotlib.collections.PathCollection.legend_elements")
 method can be used to steer how many legend entries are to be created and how they should be labeled. The following shows how to use some of them.

[volume](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rayleigh](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rayleigh.html#numpy.random.rayleigh "numpy.random.rayleigh")
(27, size\=40)
[amount](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.poisson](https://numpy.org/doc/stable/reference/random/generated/numpy.random.poisson.html#numpy.random.poisson "numpy.random.poisson")
(10, size\=40)
[ranking](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(size\=40)
[price](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(1, 10, size\=40)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

\# Because the price is much too small when being provided as size for \`\`s\`\`,
\# we normalize it to some useful point sizes, s=0.3\*(price\*3)\*\*2
[scatter](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
 \= [ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([volume](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [amount](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [c](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[ranking](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=0.3\*([price](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*3)\*\*2,
                     vmin\=-3, vmax\=3, cmap\="Spectral")

\# Produce a legend for the ranking (colors). Even though there are 40 different
\# rankings, we only want to show 5 of them in the legend.
[legend1](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 \= [ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(\*[scatter.legend\_elements](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection.legend_elements "matplotlib.collections.PathCollection.legend_elements")
(num\=5),
                    loc\="upper left", title\="Ranking")
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([legend1](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
)

\# Produce a legend for the price (sizes). Because we want to show the prices
\# in dollars, we use the \*func\* argument to supply the inverse of the function
\# used to calculate the sizes from above. The \*fmt\* ensures to show the price
\# in dollars. Note how we target at 5 elements here, but obtain only 4 in the
\# created legend due to the automatic round prices that are chosen for us.
[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(prop\="sizes", num\=5, [color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[scatter.cmap](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection.cmap "matplotlib.collections.PathCollection.cmap")
(0.7), fmt\="$ {x:.2f}",
          func\=lambda [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
: [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
/.3)/3)
[legend2](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 \= [ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(\*[scatter.legend\_elements](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection.legend_elements "matplotlib.collections.PathCollection.legend_elements")
(\*\*[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
),
                    loc\="lower right", title\="Price")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![scatter with legend](https://matplotlib.org/stable/_images/sphx_glr_scatter_with_legend_003_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
     / [`matplotlib.pyplot.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
    
*   [`matplotlib.axes.Axes.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
     / [`matplotlib.pyplot.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
    
*   [`matplotlib.collections.PathCollection.legend_elements`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection.legend_elements "matplotlib.collections.PathCollection.legend_elements")
    

Tags: [component: legend](https://matplotlib.org/stable/_tags/component-legend.html)
 [plot-type: scatter](https://matplotlib.org/stable/_tags/plot-type-scatter.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

**Total running time of the script:** (0 minutes 2.158 seconds)

[`Download Jupyter notebook: scatter_with_legend.ipynb`](https://matplotlib.org/stable/_downloads/0683d72347b9f107ec3f791a9f28a1d9/scatter_with_legend.ipynb)

[`Download Python source code: scatter_with_legend.py`](https://matplotlib.org/stable/_downloads/e296fc40ba715311fdebebae0ecf1c71/scatter_with_legend.py)

[`Download zipped: scatter_with_legend.zip`](https://matplotlib.org/stable/_downloads/bbc094b2d06a9747b59fe4939e300463/scatter_with_legend.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page