[Skip to main content](https://matplotlib.org/stable/gallery/statistics/hexbin_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/statistics/hexbin_demo.html#sphx-glr-download-gallery-statistics-hexbin-demo-py)
 to download the full example code.

Hexagonal binned plot[#](https://matplotlib.org/stable/gallery/statistics/hexbin_demo.html#hexagonal-binned-plot "Link to this heading")

=========================================================================================================================================

[`hexbin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin "matplotlib.axes.Axes.hexbin")
 is a 2D histogram plot, in which the bins are hexagons and the color represents the number of data points within each bin.

import matplotlib.pyplot as plt
import numpy as np

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[n](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 100\_000
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.standard\_normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_normal.html#numpy.random.standard_normal "numpy.random.standard_normal")
([n](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 2.0 + 3.0 \* [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + 4.0 \* [np.random.standard\_normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_normal.html#numpy.random.standard_normal "numpy.random.standard_normal")
([n](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[xlim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.min(), [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max()
[ylim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.min(), [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max()

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, sharey\=True, figsize\=(9, 4))

[hb](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 \= [ax0.hexbin](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin "matplotlib.axes.Axes.hexbin")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, gridsize\=50, cmap\='inferno')
[ax0.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
([xlim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[xlim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [ylim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[ylim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)
[ax0.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Hexagon binning")
[cb](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= [fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([hb](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
, ax\=[ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, label\='counts')

[hb](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 \= [ax1.hexbin](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin "matplotlib.axes.Axes.hexbin")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, gridsize\=50, bins\='log', cmap\='inferno')
[ax1.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
([xlim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[xlim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [ylim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[ylim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("With a log color scale")
[cb](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= [fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([hb](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
, ax\=[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, label\='counts')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Hexagon binning, With a log color scale](https://matplotlib.org/stable/_images/sphx_glr_hexbin_demo_001_2_00x.png)

Tags: [plot-type: histogram](https://matplotlib.org/stable/_tags/plot-type-histogram.html)
 [plot-type: hexbin](https://matplotlib.org/stable/_tags/plot-type-hexbin.html)
 [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.hexbin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin "matplotlib.axes.Axes.hexbin")
     / [`matplotlib.pyplot.hexbin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hexbin.html#matplotlib.pyplot.hexbin "matplotlib.pyplot.hexbin")
    

**Total running time of the script:** (0 minutes 1.062 seconds)

[`Download Jupyter notebook: hexbin_demo.ipynb`](https://matplotlib.org/stable/_downloads/9c8c2d65864aea7819fe105e149ec332/hexbin_demo.ipynb)

[`Download Python source code: hexbin_demo.py`](https://matplotlib.org/stable/_downloads/0bc1dcea7f6f63c4a84c92bb99b984da/hexbin_demo.py)

[`Download zipped: hexbin_demo.zip`](https://matplotlib.org/stable/_downloads/4468f120e2c363526b5b691d5e6c13d7/hexbin_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)