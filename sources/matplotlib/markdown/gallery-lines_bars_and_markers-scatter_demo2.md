[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_demo2.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_demo2.html#sphx-glr-download-gallery-lines-bars-and-markers-scatter-demo2-py)
 to download the full example code.

Scatter Demo2[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_demo2.html#scatter-demo2 "Link to this heading")

=======================================================================================================================================

Demo of scatter plot with varying marker colors and sizes.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook

\# Load a numpy record array from yahoo csv data with fields date, open, high,
\# low, close, volume, adj\_close from the mpl-data/sample\_data directory. The
\# record array stores the date as an np.datetime64 with a day unit ('D') in
\# the date column.
[price\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
('goog.npz')\['price\_data'\]
[price\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [price\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[\-250:\]  \# get the most recent 250 trading days

[delta1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.diff](https://numpy.org/doc/stable/reference/generated/numpy.diff.html#numpy.diff "numpy.diff")
([price\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\["adj\_close"\]) / [price\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\["adj\_close"\]\[:\-1\]

\# Marker size in units of points^2
[volume](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= (15 \* [price\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\["volume"\]\[:\-2\] / [price\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\["volume"\]\[0\])\*\*2
[close](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 0.003 \* [price\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\["close"\]\[:\-2\] / 0.003 \* [price\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\["open"\]\[:\-2\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([delta1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:\-1\], [delta1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1:\], c\=[close](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, s\=[volume](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, alpha\=0.5)

[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
(r'$\\Delta\_i$', fontsize\=15)
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
(r'$\\Delta\_{i+1}$', fontsize\=15)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Volume and percent change')

[ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
(True)
[fig.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Volume and percent change](https://matplotlib.org/stable/_images/sphx_glr_scatter_demo2_001_2_00x.png)

Tags: [component: marker](https://matplotlib.org/stable/_tags/component-marker.html)
 [styling: color](https://matplotlib.org/stable/_tags/styling-color.html)
 [styling: colormap](https://matplotlib.org/stable/_tags/styling-colormap.html)
 [plot-type: scatter](https://matplotlib.org/stable/_tags/plot-type-scatter.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: scatter_demo2.ipynb`](https://matplotlib.org/stable/_downloads/e907154b844b545d5d44de7aab05fea3/scatter_demo2.ipynb)

[`Download Python source code: scatter_demo2.py`](https://matplotlib.org/stable/_downloads/5b9eb7dec3f843b16e67ad82e4647a08/scatter_demo2.py)

[`Download zipped: scatter_demo2.zip`](https://matplotlib.org/stable/_downloads/d39f5b330ed73751c0d61a7a20d032be/scatter_demo2.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)