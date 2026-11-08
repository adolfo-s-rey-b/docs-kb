[Skip to main content](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/zoom_inset_axes.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/zoom_inset_axes.html#sphx-glr-download-gallery-subplots-axes-and-figures-zoom-inset-axes-py)
 to download the full example code.

Zoom region inset Axes[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/zoom_inset_axes.html#zoom-region-inset-axes "Link to this heading")

==============================================================================================================================================================

Example of an inset Axes and a rectangle showing where the zoom is located.

import numpy as np

from matplotlib import cbook
from matplotlib import pyplot as plt

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

\# make data
[Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
("axes\_grid/bivariate\_normal.npy")  \# 15x15 array
[Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((150, 150))
[ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= [Z.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
[Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[30:30+[ny](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, 30:30+[nx](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\] \= [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (\-3, 4, \-4, 3)

[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, origin\="lower")

\# inset Axes....
[x1](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [x2](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y1](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y2](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= \-1.5, \-0.9, \-2.5, \-1.9  \# subregion of the original image
[axins](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax.inset\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#matplotlib.axes.Axes.inset_axes "matplotlib.axes.Axes.inset_axes")
(
    \[0.5, 0.5, 0.47, 0.47\],
    xlim\=([x1](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [x2](https://docs.python.org/3/library/functions.html#float "builtins.float")
), ylim\=([y1](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y2](https://docs.python.org/3/library/functions.html#float "builtins.float")
), xticklabels\=\[\], yticklabels\=\[\])
[axins.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, origin\="lower")

[ax.indicate\_inset\_zoom](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset_zoom.html#matplotlib.axes.Axes.indicate_inset_zoom "matplotlib.axes.Axes.indicate_inset_zoom")
([axins](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, edgecolor\="black")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![zoom inset axes](https://matplotlib.org/stable/_images/sphx_glr_zoom_inset_axes_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.inset_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#matplotlib.axes.Axes.inset_axes "matplotlib.axes.Axes.inset_axes")
    
*   [`matplotlib.axes.Axes.indicate_inset_zoom`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset_zoom.html#matplotlib.axes.Axes.indicate_inset_zoom "matplotlib.axes.Axes.indicate_inset_zoom")
    
*   [`matplotlib.axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
    

Tags: [component: axes](https://matplotlib.org/stable/_tags/component-axes.html)
 [plot-type: imshow](https://matplotlib.org/stable/_tags/plot-type-imshow.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

[`Download Jupyter notebook: zoom_inset_axes.ipynb`](https://matplotlib.org/stable/_downloads/8240186cd25536b696d5c0bce0e3d5c9/zoom_inset_axes.ipynb)

[`Download Python source code: zoom_inset_axes.py`](https://matplotlib.org/stable/_downloads/7600459cba10d19716daad4a919e2705/zoom_inset_axes.py)

[`Download zipped: zoom_inset_axes.zip`](https://matplotlib.org/stable/_downloads/284b5e3f39b44c94296fcea0f8a389f5/zoom_inset_axes.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)