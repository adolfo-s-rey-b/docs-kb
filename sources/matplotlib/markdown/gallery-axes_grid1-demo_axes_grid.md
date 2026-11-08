[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_grid.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_grid.html#sphx-glr-download-gallery-axes-grid1-demo-axes-grid-py)
 to download the full example code.

Demo Axes Grid[#](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_grid.html#demo-axes-grid "Link to this heading")

==============================================================================================================================

Grid of 2x2 images with a single colorbar or with one colorbar per Axes.

![demo axes grid](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_grid_001_2_00x.png)

import matplotlib.pyplot as plt

from matplotlib import cbook
from mpl\_toolkits.axes\_grid1 import [ImageGrid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10.5, 2.5))
[Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
("axes\_grid/bivariate\_normal.npy")  \# 15x15 array
[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (\-3, 4, \-4, 3)

\# A grid of 2x2 images with 0.05 inch pad between images and only the
\# lower-left Axes is labeled.
[grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
 \= [ImageGrid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
(
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, 141,  \# similar to fig.add\_subplot(141).
     nrows\_ncols\=(2, 2), axes\_pad\=0.05, label\_mode\="1")
for [ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
 in [grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
:
    [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)
\# This only affects Axes in first column and second row as share\_all=False.
[grid.axes\_llc.set](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes.set "mpl_toolkits.axes_grid1.mpl_axes.Axes.set")
(xticks\=\[\-2, 0, 2\], yticks\=\[\-2, 0, 2\])

\# A grid of 2x2 images with a single colorbar.
[grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
 \= [ImageGrid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
(
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, 142,  \# similar to fig.add\_subplot(142).
    nrows\_ncols\=(2, 2), axes\_pad\=0.0, label\_mode\="L", share\_all\=True,
    cbar\_location\="top", cbar\_mode\="single")
for [ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
 in [grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
:
    [im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)
[grid.cbar\_axes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\].colorbar([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
)
for cax in [grid.cbar\_axes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
:
    [cax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(labeltop\=False)
\# This affects all Axes as share\_all = True.
[grid.axes\_llc.set](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes.set "mpl_toolkits.axes_grid1.mpl_axes.Axes.set")
(xticks\=\[\-2, 0, 2\], yticks\=\[\-2, 0, 2\])

\# A grid of 2x2 images. Each image has its own colorbar.
[grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
 \= [ImageGrid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
(
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, 143,  \# similar to fig.add\_subplot(143).
    nrows\_ncols\=(2, 2), axes\_pad\=0.1, label\_mode\="1", share\_all\=True,
    cbar\_location\="top", cbar\_mode\="each", cbar\_size\="7%", cbar\_pad\="2%")
for [ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
, cax in zip([grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
, [grid.cbar\_axes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)
    [cax.colorbar](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.CbarAxesBase.html#mpl_toolkits.axes_grid1.axes_grid.CbarAxesBase.colorbar "mpl_toolkits.axes_grid1.axes_grid.CbarAxesBase.colorbar")
([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
)
    [cax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(labeltop\=False)
\# This affects all Axes as share\_all = True.
[grid.axes\_llc.set](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes.set "mpl_toolkits.axes_grid1.mpl_axes.Axes.set")
(xticks\=\[\-2, 0, 2\], yticks\=\[\-2, 0, 2\])

\# A grid of 2x2 images. Each image has its own colorbar.
[grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
 \= [ImageGrid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
(
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, 144,  \# similar to fig.add\_subplot(144).
    nrows\_ncols\=(2, 2), axes\_pad\=(0.45, 0.15), label\_mode\="1", share\_all\=True,
    cbar\_location\="right", cbar\_mode\="each", cbar\_size\="7%", cbar\_pad\="2%")
\# Use a different colorbar range every time
[limits](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= ((0, 1), (\-2, 2), (\-1.7, 1.4), (\-1.5, 1))
for [ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
, cax, [vlim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 in zip([grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
, [grid.cbar\_axes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [limits](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
):
    [im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, vmin\=[vlim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\], vmax\=[vlim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[1\])
    [cb](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= [cax.colorbar](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.CbarAxesBase.html#mpl_toolkits.axes_grid1.axes_grid.CbarAxesBase.colorbar "mpl_toolkits.axes_grid1.axes_grid.CbarAxesBase.colorbar")
([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
)
    [cb.set\_ticks](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_ticks "matplotlib.colorbar.Colorbar.set_ticks")
(([vlim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\], [vlim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[1\]))
\# This affects all Axes as share\_all = True.
[grid.axes\_llc.set](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes.set "mpl_toolkits.axes_grid1.mpl_axes.Axes.set")
(xticks\=\[\-2, 0, 2\], yticks\=\[\-2, 0, 2\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 1.376 seconds)

[`Download Jupyter notebook: demo_axes_grid.ipynb`](https://matplotlib.org/stable/_downloads/6174472b158bd25cca1b3b86e7439a3c/demo_axes_grid.ipynb)

[`Download Python source code: demo_axes_grid.py`](https://matplotlib.org/stable/_downloads/e59c7fc1ea02b23c213a2688aba898cc/demo_axes_grid.py)

[`Download zipped: demo_axes_grid.zip`](https://matplotlib.org/stable/_downloads/7227629c58305dc576daa5c7d55feb1d/demo_axes_grid.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)