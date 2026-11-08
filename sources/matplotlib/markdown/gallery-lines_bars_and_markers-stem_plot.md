[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stem_plot.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stem_plot.html#sphx-glr-download-gallery-lines-bars-and-markers-stem-plot-py)
 to download the full example code.

Stem plot[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stem_plot.html#stem-plot "Link to this heading")

===========================================================================================================================

[`stem`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stem.html#matplotlib.pyplot.stem "matplotlib.pyplot.stem")
 plots vertical lines from a baseline to the y-coordinate and places a marker at the tip.

import matplotlib.pyplot as plt
import numpy as np

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.1, 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 41)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))

[plt.stem](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stem.html#matplotlib.pyplot.stem "matplotlib.pyplot.stem")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![stem plot](https://matplotlib.org/stable/_images/sphx_glr_stem_plot_001_2_00x.png)

The position of the baseline can be adapted using _bottom_. The parameters _linefmt_, _markerfmt_, and _basefmt_ control basic format properties of the plot. However, in contrast to [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
 not all properties are configurable via keyword arguments. For more advanced control adapt the line objects returned by [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
.

[markerline](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, [stemlines](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
, [baseline](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 \= [plt.stem](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stem.html#matplotlib.pyplot.stem "matplotlib.pyplot.stem")
(
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, linefmt\='grey', markerfmt\='D', bottom\=1.1)
[markerline.set\_markerfacecolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecolor "matplotlib.lines.Line2D.set_markerfacecolor")
('none')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![stem plot](https://matplotlib.org/stable/_images/sphx_glr_stem_plot_002_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.stem`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html#matplotlib.axes.Axes.stem "matplotlib.axes.Axes.stem")
     / [`matplotlib.pyplot.stem`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stem.html#matplotlib.pyplot.stem "matplotlib.pyplot.stem")
    

Tags: [plot-type: stem](https://matplotlib.org/stable/_tags/plot-type-stem.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: stem_plot.ipynb`](https://matplotlib.org/stable/_downloads/a9d7666ecc546aca5a09ec9b65cbb407/stem_plot.ipynb)

[`Download Python source code: stem_plot.py`](https://matplotlib.org/stable/_downloads/605cad767f8ac8bf813bcd4941015322/stem_plot.py)

[`Download zipped: stem_plot.zip`](https://matplotlib.org/stable/_downloads/a13d778c0ea3ee96846869b663ec941a/stem_plot.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)