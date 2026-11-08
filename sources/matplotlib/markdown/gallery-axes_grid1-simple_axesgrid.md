[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/simple_axesgrid.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/simple_axesgrid.html#sphx-glr-download-gallery-axes-grid1-simple-axesgrid-py)
 to download the full example code.

Simple ImageGrid[#](https://matplotlib.org/stable/gallery/axes_grid1/simple_axesgrid.html#simple-imagegrid "Link to this heading")

===================================================================================================================================

Align multiple images using [`ImageGrid`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.axes_grid.ImageGrid")
.

![simple axesgrid](https://matplotlib.org/stable/_images/sphx_glr_simple_axesgrid_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from mpl\_toolkits.axes\_grid1 import [ImageGrid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")

[im1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(100).reshape((10, 10))
[im2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [im1.T](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
[im3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.flipud](https://numpy.org/doc/stable/reference/generated/numpy.flipud.html#numpy.flipud "numpy.flipud")
([im1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[im4](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.fliplr](https://numpy.org/doc/stable/reference/generated/numpy.fliplr.html#numpy.fliplr "numpy.fliplr")
([im2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(4., 4.))
[grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
 \= [ImageGrid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, 111,  \# similar to subplot(111)
                 nrows\_ncols\=(2, 2),  \# creates 2x2 grid of Axes
                 axes\_pad\=0.1,  \# pad between Axes in inch.
                 )

for [ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
, [im](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 in zip([grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
, \[[im1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [im2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [im3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [im4](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\]):
    \# Iterating over the grid returns the Axes.
    [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([im](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: simple_axesgrid.ipynb`](https://matplotlib.org/stable/_downloads/62b471e9287f2bde747eca15d2e118c3/simple_axesgrid.ipynb)

[`Download Python source code: simple_axesgrid.py`](https://matplotlib.org/stable/_downloads/c28e31130cca60f0a4ac710f3fbf96c8/simple_axesgrid.py)

[`Download zipped: simple_axesgrid.zip`](https://matplotlib.org/stable/_downloads/a69e0dee607f3a118f80ab8f1eb2c3e7/simple_axesgrid.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)