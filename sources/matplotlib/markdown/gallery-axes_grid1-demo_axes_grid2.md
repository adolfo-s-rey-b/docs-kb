[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_grid2.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_grid2.html#sphx-glr-download-gallery-axes-grid1-demo-axes-grid2-py)
 to download the full example code.

Axes Grid2[#](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_grid2.html#axes-grid2 "Link to this heading")

=======================================================================================================================

Grid of images with shared xaxis and yaxis.

![demo axes grid2](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_grid2_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cbook
from mpl\_toolkits.axes\_grid1 import [ImageGrid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")

def add\_inner\_title([ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
, title, loc, \*\*kwargs):
    from matplotlib.offsetbox import [AnchoredText](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredText "matplotlib.offsetbox.AnchoredText")
    from matplotlib.patheffects import [withStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withStroke "matplotlib.patheffects.withStroke")
    prop \= dict(path\_effects\=\[[withStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withStroke "matplotlib.patheffects.withStroke")\
(foreground\='w', linewidth\=3)\],
                size\=[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['legend.fontsize'\])
    at \= [AnchoredText](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredText "matplotlib.offsetbox.AnchoredText")
(title, loc\=loc, prop\=prop,
                      pad\=0., borderpad\=0.5,
                      frameon\=False, \*\*kwargs)
    [ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
(at)
    return at

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(6, 6))

\# Prepare images
[Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
("axes\_grid/bivariate\_normal.npy")
[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (\-3, 4, \-4, 3)
[ZS](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
::3, :\] for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 in range(3)\]
[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= [extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\], [extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[1\]/3., [extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[2\], [extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[3\]

\# \*\*\* Demo 1: colorbar at each Axes \*\*\*
[grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
 \= [ImageGrid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
(
    \# 211 = at the position of fig.add\_subplot(211)
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, 211, nrows\_ncols\=(1, 3), axes\_pad\=0.05, label\_mode\="1", share\_all\=True,
    cbar\_location\="top", cbar\_mode\="each", cbar\_size\="7%", cbar\_pad\="1%")
[grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
\[0\].set(xticks\=\[\-2, 0\], yticks\=\[\-2, 0, 2\])

for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, ([ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) in enumerate(zip([grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
, [ZS](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)):
    [im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, origin\="lower", [extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)
    [cb](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= [ax.cax.colorbar](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.CbarAxesBase.html#mpl_toolkits.axes_grid1.axes_grid.CbarAxesBase.colorbar "mpl_toolkits.axes_grid1.axes_grid.CbarAxesBase.colorbar")
([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
)
    \# Changing the colorbar ticks
    if [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in \[1, 2\]:
        [cb.set\_ticks](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_ticks "matplotlib.colorbar.Colorbar.set_ticks")
(\[\-1, 0, 1\])

for [ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
, [im\_title](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip([grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
, \["Image 1", "Image 2", "Image 3"\]):
    add\_inner\_title([ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
, [im\_title](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, loc\='lower left')

\# \*\*\* Demo 2: shared colorbar \*\*\*
[grid2](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
 \= [ImageGrid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
(
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, 212, nrows\_ncols\=(1, 3), axes\_pad\=0.05, label\_mode\="1", share\_all\=True,
    cbar\_location\="right", cbar\_mode\="single", cbar\_size\="10%", cbar\_pad\=0.05)
[grid2](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
\[0\].set(xlabel\="X", ylabel\="Y", xticks\=\[\-2, 0\], yticks\=\[\-2, 0, 2\])

[clim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= ([np.min](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")
([ZS](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
), [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
([ZS](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
))
for [ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 in zip([grid2](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
, [ZS](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [clim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[clim](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, origin\="lower", [extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)

\# With cbar\_mode="single", cax attribute of all Axes are identical.
[ax.cax.colorbar](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.CbarAxesBase.html#mpl_toolkits.axes_grid1.axes_grid.CbarAxesBase.colorbar "mpl_toolkits.axes_grid1.axes_grid.CbarAxesBase.colorbar")
([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
)

for [ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
, [im\_title](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip([grid2](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
, \["(a)", "(b)", "(c)"\]):
    add\_inner\_title([ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
, [im\_title](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, loc\='upper left')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: demo_axes_grid2.ipynb`](https://matplotlib.org/stable/_downloads/33e9e63a8ae362ca719df5cfd81d735e/demo_axes_grid2.ipynb)

[`Download Python source code: demo_axes_grid2.py`](https://matplotlib.org/stable/_downloads/5fc19bc53f353b5d6f24bdca17a4c140/demo_axes_grid2.py)

[`Download zipped: demo_axes_grid2.zip`](https://matplotlib.org/stable/_downloads/66ee71bdff7c61d7efe599909c728163/demo_axes_grid2.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)