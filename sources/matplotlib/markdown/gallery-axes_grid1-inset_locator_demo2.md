[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo2.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo2.html#sphx-glr-download-gallery-axes-grid1-inset-locator-demo2-py)
 to download the full example code.

Inset locator demo 2[#](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo2.html#inset-locator-demo-2 "Link to this heading")

===============================================================================================================================================

This demo shows how to create a zoomed inset via [`zoomed_inset_axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes "mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes")
. In the first subplot an [`AnchoredSizeBar`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar "mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar")
 shows the zoom effect. In the second subplot a connection to the region of interest is created via [`mark_inset`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.mark_inset.html#mpl_toolkits.axes_grid1.inset_locator.mark_inset "mpl_toolkits.axes_grid1.inset_locator.mark_inset")
.

A version of the second subplot, not using the toolkit, is available in [Zoom region inset Axes](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/zoom_inset_axes.html)
.

![inset locator demo2](https://matplotlib.org/stable/_images/sphx_glr_inset_locator_demo2_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cbook
from mpl\_toolkits.axes\_grid1.anchored\_artists import [AnchoredSizeBar](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar "mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar")
from mpl\_toolkits.axes\_grid1.inset\_locator import [mark\_inset](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.mark_inset.html#mpl_toolkits.axes_grid1.inset_locator.mark_inset "mpl_toolkits.axes_grid1.inset_locator.mark_inset")
, [zoomed\_inset\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes "mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=\[6, 3\])

\# First subplot, showing an inset with a size bar.
[ax.set\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
(1)

axins \= [zoomed\_inset\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes "mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, zoom\=0.5, loc\='upper right')
\# fix the number of ticks on the inset Axes
[axins.yaxis.get\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_locator.html#matplotlib.axis.Axis.get_major_locator "matplotlib.axis.Axis.get_major_locator")
().set\_params(nbins\=7)
[axins.xaxis.get\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_locator.html#matplotlib.axis.Axis.get_major_locator "matplotlib.axis.Axis.get_major_locator")
().set\_params(nbins\=7)
[axins.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(labelleft\=False, labelbottom\=False)

def add\_sizebar([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, size):
    asb \= [AnchoredSizeBar](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar "mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar")
([ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
,
                          size,
                          str(size),
                          loc\="lower center",
                          pad\=0.1, borderpad\=0.5, sep\=5,
                          frameon\=False)
    [ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
(asb)

add\_sizebar([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, 0.5)
add\_sizebar(axins, 0.5)

\# Second subplot, showing an image with an inset zoom and a marked inset
[Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
("axes\_grid/bivariate\_normal.npy")  \# 15x15 array
[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (\-3, 4, \-4, 3)
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

[ax2.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, origin\="lower")

axins2 \= [zoomed\_inset\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes "mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes")
([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, zoom\=6, loc\="upper right")
[axins2.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, origin\="lower")

\# subregion of the original image
[x1](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [x2](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y1](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y2](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= \-1.5, \-0.9, \-2.5, \-1.9
[axins2.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
([x1](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [x2](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
[axins2.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
([y1](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y2](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
\# fix the number of ticks on the inset Axes
[axins2.yaxis.get\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_locator.html#matplotlib.axis.Axis.get_major_locator "matplotlib.axis.Axis.get_major_locator")
().set\_params(nbins\=7)
[axins2.xaxis.get\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_locator.html#matplotlib.axis.Axis.get_major_locator "matplotlib.axis.Axis.get_major_locator")
().set\_params(nbins\=7)
[axins2.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(labelleft\=False, labelbottom\=False)

\# draw a bbox of the region of the inset Axes in the parent Axes and
\# connecting lines between the bbox and the inset Axes area
[mark\_inset](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.mark_inset.html#mpl_toolkits.axes_grid1.inset_locator.mark_inset "mpl_toolkits.axes_grid1.inset_locator.mark_inset")
([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, axins2, loc1\=2, loc2\=4, fc\="none", ec\="0.5")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: inset_locator_demo2.ipynb`](https://matplotlib.org/stable/_downloads/197a48d2414aabb049ec6cec4466cb1b/inset_locator_demo2.ipynb)

[`Download Python source code: inset_locator_demo2.py`](https://matplotlib.org/stable/_downloads/ffced02a69365d873f495b7cd6725498/inset_locator_demo2.py)

[`Download zipped: inset_locator_demo2.zip`](https://matplotlib.org/stable/_downloads/b9f2eea303fdccfd62db6062746cff5a/inset_locator_demo2.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)